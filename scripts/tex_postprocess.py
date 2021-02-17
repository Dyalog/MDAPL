"""
Python script to perform necessary adjustments to the TeX build.

Jupyter Book is used to produce a .tex file, which is then amended and compiled
with XeLaTeX.
"""

import os, shutil

BUILD_FOLDER = "book/_build/latex"
SOURCE_TEX_FILE = "python.tex"
DEST_TEX_FILE = "MDAPL.tex"

SOURCE_FILE_PATH = os.path.join(BUILD_FOLDER, SOURCE_TEX_FILE)
DEST_FILE_PATH = os.path.join(BUILD_FOLDER, DEST_TEX_FILE)

def set_APL_font():
    """Set the mono font of the .tex file to APL385 Unicode."""

    # cf. https://aplwiki.com/wiki/Typing_glyphs#LaTeX
    new_lines = [
        "\n",
        "%%% --- Inserted by tex_postprocess.py\n",
        "\\usepackage{fontspec}\n",
        "\\setmonofont{APL385 Unicode}[Scale=MatchLowercase]\n",
        "%%% ---\n",
        "\n",
    ]

    with open(DEST_FILE_PATH, "r", encoding="utf8") as f:
        lines = f.readlines()

    # Look for \begin{document} to set the font right before that.
    i = 0
    while i < len(lines):
        if lines[i].startswith("\\begin{document}"):
            break
        i += 1
    
    if i > len(lines):
        raise Exception("Could not locate document beginning to set APL font before.")

    with open(DEST_FILE_PATH, "w", encoding="utf8") as f:
        f.write("".join(lines[:i]))
        f.write("".join(new_lines))
        f.write("".join(lines[i:]))

if __name__ == "__main__":
    shutil.move(SOURCE_FILE_PATH, DEST_FILE_PATH)
    set_APL_font()
