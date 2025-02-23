SHELL=/bin/bash -euo pipefail

DOC_ROOT := https://caseutil.readthedocs.io/en/latest


.PHONY:
badges: \
	docs/badge/coverage.svg \
	docs/badge/tests.svg

docs/badge/coverage.svg: .tmp/coverage.xml
	uv run genbadge coverage --local -i $< -o $@

docs/badge/tests.svg: .tmp/junit.xml
	uv run genbadge tests --local -i $< -o $@


.PHONY: build
build: dist/%.whl

dist/%.whl: src/**/* pyproject.toml dist/README.md uv.lock
	uv lock
	mkdir -p $(@D)
	rm -rf $(@D)/*.{tar.gz,whl}
	uv build

dist/README.md: README.md
	mkdir -p $(@D)
	sed -e '/#gh-dark-mode-only/ d; s|(docs/\(img/.*\)#gh-light-mode-only|(${DOC_ROOT}/\1|' $< > $@


.PHONY: docs
docs: mkdocs README.md


.PHONY: mkdocs
mkdocs: \
	docs/requirements.txt \
	docs/index.md \
	docs/tokenize.md \
	images

docs/requirements.txt: pyproject.toml uv.lock
	uv export --only-group docs --no-emit-project > $@

docs/index.md: FORCE
	uv run docsub sync -i docs/part/cli.md docs/part/usage.md $@

docs/tokenize.md: FORCE
	uv run docsub sync -i $@


.PHONY: images
images: \
	docs/img/classification-dark.svg \
	docs/img/classification-default.svg \

docs/img/classification-%.svg: docs/classification.md
	mkdir -p .tmp
	sed -ne '/^```mermaid/,/^```/{/^```mermaid/d; s/^```//; p;}' docs/classification.md > .tmp/classification.mmd
	docker compose run --rm mermaid-cli -i /work/.tmp/classification.mmd -o $@ -I classification-$* -t $* -b transparent &>/dev/null


README.md: FORCE
	uv run docsub sync -i docs/part/cli.md docs/part/usage.md $@


FORCE:
