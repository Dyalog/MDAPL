book = book
build_folder = $(book)/_build
html_build_folder = $(build_folder)/html
latex_build_folder = $(build_folder)/latex
cname_url = mastering.dyalog.com

html: preprocess build_html

latex: preprocess build_latex

preprocess:
	python scripts/preprocess.py

build_html:
	jb build $(book)

build_latex:
	jb build $(book) --builder latex
	python scripts/tex_postprocess.py
	echo "NOTICE: The tex file needs to be compiled!"

publish_html:
	ghp-import -npf $(html_build_folder) --cname=$(cname_url)
