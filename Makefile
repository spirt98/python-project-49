install: lint build package-install publish # install and publish application

start: # run applicaion
	poetry run brain-games

lint:
	poetry run flake8 brain_games

build: # build application
	poetry build

publish: # test publish application
	poetry publish --dry-run

package-install: # install aplication in environment
	pip install --user --force-reinstall dist\hexlet_code-0.1.0-py3-none-any.whl