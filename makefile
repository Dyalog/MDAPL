book = book
build_folder = $(book)/_build
html_build_folder = $(build_folder)/html
latex_build_folder = $(build_folder)/latex

html: preprocess build_html publish_html

latex: preprocess build_latex

preprocess:
	python scripts/migrate_resources.py
	python scripts/preprocess.py

build_html:
	jb build $(book)

build_latex:
	jb build $(book) --builder latex
	python scripts/tex_postprocess.py
	"NOTICE: The tex file needs to be compiled!"

publish_html:
	ghp-import -npf $(html_build_folder)
