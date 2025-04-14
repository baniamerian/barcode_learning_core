"""
A simple script to get base64 encode of a png
"""

import base64
from pathlib import Path
import sys

def embed_png_as_html_str(file_name: str, caption: str = "") -> str:
    path = Path(file_name)
    if not path.exists():
        raise FileNotFoundError(f"Image file '{file_name}' not found.")
    
    with path.open("rb") as f:
        img_data = base64.b64encode(f.read()).decode("utf-8")
    
    html = f"""<div style="text-align: center">
  <img src="data:image/png;base64,{img_data}" alt="{path.name}" style="max-width: 80%;">
  <p><em>{caption}</em></p>
</div>"""
    return html



def embed_png_as_md_str(fig_name: str, caption: str = "") -> str:
    """
    Takes a PNG image file path and returns a Markdown string
    that embeds the image using base64 data URI.
    """
    # no use of caption
    caption = ""
    path = Path(fig_name)
    if not path.exists():
        raise FileNotFoundError(f"Image file '{figfig_name_path}' not found.")
    
    with path.open("rb") as f:
        img_data = base64.b64encode(f.read()).decode("utf-8")
    
    return f"![{path.name}](data:image/png;base64,{img_data})"

def main():
    if len(sys.argv) < 2:
        print("Usage: python png2str.py <image.png>")
        sys.exit(1)
    if(len(sys.argv) == 2):
        # generate md_str
        fig_name = sys.argv[1]
        fcn = embed_png_as_md_str
    else:
        # generate md_str
        fig_name = sys.argv[1]
        caption = sys.argv[2]
        fcn = embed_png_as_html_str
    try:
        generated_str = fcn(fig_name, caption)
        print(generated_str)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    
if __name__ == "__main__":
   main()
