document$.subscribe(function () {
  if (typeof mermaid === "undefined") {
    return;
  }

  mermaid.initialize({
    startOnLoad: false,
    securityLevel: "loose",
  });

  const blocks = document.querySelectorAll("pre.mermaid");
  blocks.forEach((block, index) => {
    if (block.dataset.mermaidProcessed === "true") {
      return;
    }

    const wrapper = document.createElement("div");
    wrapper.className = "mermaid";
    wrapper.textContent = block.textContent || "";
    wrapper.id = "mermaid-" + index;

    block.replaceWith(wrapper);
    mermaid.run({ nodes: [wrapper] });
    wrapper.dataset.mermaidProcessed = "true";
  });
});
