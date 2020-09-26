"""
Python script to transform some elements in the notebooks into appropriate MyST markdown notation,
as supported by the Jupyter Book tool.

As of now, this preprocessing step:
 - transforms image links into MyST figures
 - transforms especially marked-up sections into admonitions
"""

import json
import re
import sys
from pathlib import Path
from ruamel import yaml

try:
    with open("book/_toc.yml", "r") as f:
        data = yaml.safe_load(f)
except FileNotFoundError:
    print("Could not open ToC.")
    sys.exit()

CUSTOM_ADMONITION_STYLES = {
    "example": "tip",
    "rule": "tip",
    "exercise": "hint",
    "remark": "tip",
}

for dic in data:
    try:
        filename = Path(dic["file"]).name
    except KeyError:
        continue

    with open(f"{filename}.ipynb", "r", encoding="utf8") as f:
        #contents = f.read()
        conts = json.load(f)

    for cellid, cell in enumerate(conts["cells"]):
        lines = cell["source"]
        i = 0
        while i < len(lines):

            # does this line have a ![caption](path.ext) figure?
            m = re.match(r"!\[(.*)\]\((res/(.*?)\.(.*?))\)", lines[i])
            if m:
                caption = m.group(1)
                path = f"../{m.group(2)}"
                name = m.group(3)
                new_lines = [
                    f"```{{figure}} {path}\n",
                    f"---\n",
                    f"name: {name}\n",
                    f"---\n",
                    f"{caption}\n",
                    f"```\n",
                ]
                lines = lines[:i] + new_lines + lines[i+1:]
                i += len(new_lines)
                continue

            # does this line start an admonition comment?
            m = re.match(r"<!-- begin (.+?) (style=(\w+) )?-->", lines[i])
            if m:
                adm_header = m.group(1)
                if m.group(3):
                    style = m.group(3)
                else:
                    style = CUSTOM_ADMONITION_STYLES.get(adm_header, adm_header)
                text = adm_header.capitalize() if " " not in adm_header else adm_header
                end_match = f"<!-- end -->\n"
                try:
                    matching_line = lines.index(end_match)
                except ValueError:
                    # the matching line is the final line of the markdown cell
                    if lines[-1] == end_match[:-1]:
                        matching_line = len(lines) - 1
                    else:
                        print(f"{text} has no closing 'end' in cell {cellid} in file {filename}")
                        sys.exit(1)
                # check if the lines are in a blockquote
                intermediate_lines = lines[i+3:matching_line]
                bq_matches = [re.match(r"^ >( |\n)(.*)$", line) for line in intermediate_lines]
                if all(bq_matches):
                    content_lines = [match.group(2) + "\n" for match in bq_matches]
                else:
                    content_lines = intermediate_lines
                lines = (
                    lines[:i] +
                    [f"```{{admonition}} {text} \n", f":class: {style}\n"] +
                    content_lines +
                    ["```\n"] +
                    lines[matching_line+1:]
                )
                # after doing the maths, this is exactly where we want to resume processing:
                i = matching_line
                continue

            i += 1
        cell["source"] = lines

    with open(f"book/{filename}.ipynb", "w", encoding="utf8") as f:
        json.dump(conts, f, indent=2)
