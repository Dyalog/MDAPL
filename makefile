html: preprocess build_html publish_html

latex: preprocess build_latex

preprocess:
	python scripts/migrate_resources.py
	python scripts/preprocess.py

build_html:
	jb build book

build_latex:
	jb build book --builder latex

publish_html:
	ghp-import -npf book/_build/html
