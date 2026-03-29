document$.subscribe(function () {
  if (typeof mermaid === "undefined") {
    return;
  }

  mermaid.initialize({
    startOnLoad: false,
    securityLevel: "loose",
  });

  const blocks = document.querySelectorAll("pre code.mermaid");
  blocks.forEach((block, index) => {
    const parent = block.parentElement;
    if (!parent || parent.dataset.mermaidProcessed === "true") {
      return;
    }

    const wrapper = document.createElement("div");
    wrapper.className = "mermaid";
    wrapper.textContent = block.textContent || "";
    wrapper.id = "mermaid-" + index;

    parent.replaceWith(wrapper);
    mermaid.run({ nodes: [wrapper] });
    wrapper.dataset.mermaidProcessed = "true";
  });
});
