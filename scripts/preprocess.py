"""
Python script to transform some elements in the notebooks into appropriate MyST markdown notation,
as supported by the Jupyter Book tool.

As of now, this preprocessing step:
 - transforms image links into MyST figures
 - transforms especially marked-up sections into admonitions
 - generates labels for all headers
 - converts relative links into references to the respective headers
"""

import json
import os
import re
import sys
from pathlib import Path
from ruamel import yaml


BOOK_FOLDER = "book"
SOURCE_FOLDER = "docs"

CUSTOM_ADMONITION_STYLES = {
    "advice": "tip",
    "example": "tip",
    "exercise": "hint",
    "remark": "tip",
    "rule": "tip",
    "rules": "tip",
}

def safe_hyphenate(string):
    """Hyphenate a string and remove all non-alphanumeric chars."""
    return re.sub(r"[^\w-]", "", string.replace(" ", "-"))

def generate_header_labels(filename, lines):
    """Creates labels for all sections at all depths.

    Looks for lines that start with any number of # and precedes the line
    with the MyST annotation for a label, where the label name is the safely
    hyphenated version of the header name.
    Prefixes each label with the safely hyphenated version of the file name
    to help prevent duplicate labels.
    E.g. the header "What is this?" in the file "Oh yeah" gets the label
    "Oh-yeah-What-is-this"
    """

    i = 0
    label_prefix = safe_hyphenate(filename)
    while i < len(lines):
        m = re.match(r"^(#)+ (.*)\n$", lines[i])
        if m:
            header_name = m.group(2)
            label_name = safe_hyphenate(header_name)
            new_lines = [
                f"({label_prefix}-{label_name})=\n",
            ]
            lines = lines[:i] + new_lines + lines[i:]
            i += 2
        else:
            i += 1

    return lines

cross_ref_pattern = re.compile(r" \[.*?\]\((\.(.*?)\.ipynb)?#(.*?)\)")
def generate_cross_references(filename, lines):
    """Generates MyST cross-references for (sub-)sections.

    Links that have relative paths are assumed to be cross-references.
    The relative path is assumed to have a first part pointing to the file name
    and the second part to the Jupyter-compatible header href.
    """

    label_prefix = safe_hyphenate(filename)
    # Define a helper function.
    sh = safe_hyphenate
    def replacer_function(match):
        """cf. https://docs.python.org/3/library/re.html#re.sub"""
        if match.group(1):
            return f" {{numref}}`{sh(match.group(2))}-{sh(match.group(3))}`"
        else:
            return f" {{numref}}`{label_prefix}-{sh(match.group(3))}`"

    for i, line in enumerate(lines):
        lines[i] = re.sub(
            cross_ref_pattern,
            replacer_function,
            line,
        )

    return lines

def image_to_figure(lines):
    """Convert an image link to a MyST figure with a label.

    This looks for lines that only contain an image link and format said image
    as a MyST figure. The alt text is used as the figure caption and no other
    figure customization is done.
    The image name is used as the figure label.
    """

    i = 0
    while i < len(lines):
        # Does this line have a ![caption](path.ext) figure?
        m = re.match(r"!\[(.*)\]\((res/(.*?)\.(.*?))\)", lines[i])
        if m:
            caption, path, name = m.group(1), m.group(2), m.group(3)
            new_lines = [
                f"(fig-{name})=\n",
                f"```{{figure}} {path}\n",
                f"---\n",
                f"name: {name}\n",
                f"---\n",
                f"{caption}\n",
                f"```\n",
            ]
            lines = lines[:i] + new_lines + lines[i+1:]
            i += len(new_lines)
        else:
            i += 1

    return lines

figure_ref_pattern = re.compile(r"<!--figure-->.*?<!--(.*?)-->")
def generate_figure_references(lines):
    """Generates MyST numbered references for figures.

    References to figures are marked up with <!--figure-->.*<!--names-->
    where the text between the two HTML comments is to be ignored.
    `names` is a comma-separated list of figure labels to be inserted.
    """

    def replacer_function(match):
        names = list(map(
            lambda f: f"{{numref}}`fig-{f}`",
            match.group(1).split(",")
        ))
        if len(names) == 1:
            return names[0]
        elif len(names) == 2:
            return " and ".join(names)
        else:
            return ", ".join(names[:-1]) + ", and " + names[-1]
    for i, line in enumerate(lines):
        lines[i] = re.sub(
            figure_ref_pattern,
            replacer_function,
            line,
        )

    return lines


def create_exercises(filename, lines):
    """Convert an exercise section to the sphinx-exercise syntax."""

    i = 0
    while i < len(lines):
        m = re.match(r"<!-- ?exercise (.+?) ?-->", lines[i])
        if m:
            label = m.group(1)
            end_match = "<!-- end -->\n"
            try:
                matching_line = lines.index(end_match)
            except ValueError:
                if lines[-1] == end_match[:-1]:
                    matching_line = len(lines) - 1
                else:
                    print(f"Exercise has no closing 'end' in file {filename}, line {i}.")
                    sys.exit(1)
            content_lines = lines[i+3:matching_line]
            # How deep must the admonition nesting be?
            backtick_nesting = max(
                map(len, re.findall(r"`+", "\n".join(content_lines))),
                default=0,
            )
            backticks = "`" * max(3, 1 + backtick_nesting)
            lines[i:matching_line + 1] = (
                [f"{backticks}{{exercise}}\n", f":label: {label}\n"] +
                content_lines +
                [f"{backticks}\n"]
            )
            # after doing the maths, this is exactly where we want to resume processing:
            i = matching_line
        else:
            i += 1

    return lines


def create_solutions(lines):
    """ Convert a solution section to the sphinx-exercise syntax."""

    i = 0
    while i < len(lines):
        m = re.match(r"<!-- ?solution (.+) ?-->", lines[i])
        if m:
            label = m.group(1)
            lines[i:i+2] = [f"```{{solution}} {label}\n", "```\n"]
            i += 2
        else:
            i += 1

    return lines


def create_admonitions(filename, lines):
    """Convert an admonition section into a MyST admonition.

    This function looks for sections that have been marked-up with HTML comments
    that delimit an admonition. These sections are then extracted and converted
    into a proper MyST admonition.

    These sections are started with <!-- begin `name` `style=stylename` -->
    and end with <!-- end -->. The sections can optionally be completely offset
    with " > " to produce a blockquote that gives a visual cue for readers of
    the plain notebooks.

    Inside those sections, we look for code blocks or other formatting done with
    backticks (`), to ensure that the outer admonition is nested correctly.

    Here, `name` is the name of the admonition and an optional `style=stylename`
    can be used to style the admonition as described in
    https://sphinx-book-theme.readthedocs.io/en/latest/reference/demo.html#admonitions
    """

    i = 0
    while i < len(lines):
        # Does this line start an admonition comment?
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
                    print(f"{text!r} has no closing 'end' in file {filename}.")
                    sys.exit(1)
            # check if the lines are in a blockquote
            intermediate_lines = lines[i+3:matching_line]
            bq_matches = [re.match(r"^ >( |\n)(.*)$", line) for line in intermediate_lines]
            if all(bq_matches):
                content_lines = [match.group(2) + "\n" for match in bq_matches]
            else:
                content_lines = intermediate_lines
            # How deep must the admonition nesting be?
            backtick_nesting = max(map(len, re.findall(r"`+", "\n".join(content_lines))), default=0)
            backticks = "`" * max(3, 1 + backtick_nesting)
            lines = (
                lines[:i] +
                [f"{backticks}{{admonition}} {text} \n", f":class: {style}\n"] +
                content_lines +
                [f"{backticks}\n"] +
                lines[matching_line+1:]
            )
            # after doing the maths, this is exactly where we want to resume processing:
            i = matching_line
        else:
            i += 1

    return lines

def parse_md(filename):
    """Tries to copy a Markdown file to the book folder and parse its lines.
    
    This function assumes the filename refers to a .md file.
    Returns False if the file is not found, True otherwise.
    """

    source = f"{filename}.md"
    try:
        with open(source, "r", encoding="utf8") as f:
            contents = f.readlines()
    except FileNotFoundError:
        return False
    
    lines = parse_lines(filename, list(contents))
    destination = os.path.join(BOOK_FOLDER, source)
    with open(destination, "w", encoding="utf8") as f:
        f.writelines(lines)
    return True
        
def parse_lines(filename, lines):
    """Apply all parsing functions to the list of lines."""
    
    lines = generate_header_labels(filename, lines)
    lines = generate_cross_references(filename, lines)
    lines = generate_figure_references(lines)
    lines = image_to_figure(lines)
    lines = create_admonitions(filename, lines)
    lines = create_exercises(filename, lines)
    lines = create_solutions(lines)
    return lines

if __name__ == "__main__":

    # Ensure the book folder exists.
    if not os.path.exists(BOOK_FOLDER):
        os.makedirs(BOOK_FOLDER)

    try:
        with open(f"{BOOK_FOLDER}/_toc.yml", "r") as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print("Could not open ToC.")
        sys.exit()

    for dic in data.get("sections", []):
        try:
            filename = Path(dic["file"]).name
        except KeyError:
            continue

        try:
            with open(f"{SOURCE_FOLDER}/{filename}.ipynb", "r", encoding="utf8") as f:
                contents = json.load(f)
        except FileNotFoundError:
            parse_md(filename)
            continue

        for cell in contents["cells"]:
            lines = cell["source"]
            cell["source"] = parse_lines(filename, lines)

        with open(f"{BOOK_FOLDER}/{filename}.ipynb", "w", encoding="utf8") as f:
            json.dump(contents, f, indent=2)
