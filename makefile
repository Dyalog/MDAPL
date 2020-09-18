html: preprocess_html build_html publish_html

preprocess_html:
	python migrate_resources.py
	python scripts/preprocess_html.py

build_html:
	jb build book

publish_html:
	ghp-import -npf book/_build/html
