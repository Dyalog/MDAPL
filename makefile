html: preprocess_html build_html publish_html

preprocess_html:
	python scripts/preprocesshtml.py

build_html:
	jb build book

publish_html:
	ghp-import -npf book/_build/html
