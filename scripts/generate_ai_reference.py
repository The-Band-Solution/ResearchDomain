import ast
import os
from pathlib import Path

def get_docstring(node):
    """Extracts and formats docstring from an AST node."""
    doc = ast.get_docstring(node)
    if doc:
        return f"\n  > {doc.strip().replace(chr(10), chr(10) + '  > ')}\n"
    return ""

def get_args(args):
    """Formats function arguments."""
    arg_list = []
    for arg in args.args:
        arg_str = arg.arg
        if arg.annotation:
            ann = ast.unparse(arg.annotation)
            arg_str += f": {ann}"
        arg_list.append(arg_str)
    
    if args.vararg:
        arg_list.append(f"*{args.vararg.arg}")
    if args.kwarg:
        arg_list.append(f"**{args.kwarg.arg}")
        
    return ", ".join(arg_list)

def get_returns(node):
    """Formats return type annotation."""
    if node.returns:
        return f" -> {ast.unparse(node.returns)}"
    return ""

def process_file(filepath, root_dir):
    """Parses a Python file and extracts classes and functions."""
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            tree = ast.parse(f.read())
        except SyntaxError:
            return ""

    rel_path = filepath.relative_to(root_dir)
    content = [f"## File: `{rel_path}`\n"]

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            content.append(f"### Class `{node.name}`")
            content.append(get_docstring(node))
            
            # Bases
            bases = [ast.unparse(b) for b in node.bases]
            if bases:
                content.append(f"*Inherits from:* `{', '.join(bases)}`\n")

            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    args = get_args(item.args)
                    ret = get_returns(item)
                    content.append(f"- **Method** `{item.name}({args}){ret}`")
                    content.append(get_docstring(item))
            content.append("\n---\n")

        elif isinstance(node, ast.FunctionDef):
            args = get_args(node.args)
            ret = get_returns(node)
            content.append(f"### Function `{node.name}({args}){ret}`")
            content.append(get_docstring(node))
            content.append("\n---\n")

    return "\n".join(content)

def main():
    root_dir = Path(__file__).parent.parent / "src" / "research_domain"
    output_file = root_dir / "AI_REFERENCE.md"
    
    all_content = ["# ResearchDomain API Reference\n\nAutomated documentation for LLM ingestion.\n\n"]
    
    # Ensure directory exists
    if not root_dir.exists():
        print(f"Error: Directory {root_dir} does not exist.")
        return

    files = sorted(list(root_dir.rglob("*.py")))
    
    for filepath in files:
        if filepath.name == "__init__.py":
            continue
        all_content.append(process_file(filepath, root_dir))
        
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(all_content))
    
    print(f"Generated {output_file} with {len(all_content)} sections.")

if __name__ == "__main__":
    main()
