install: build package-install # install and publish the application

dev: lint build package-install publish # build and publish the application

start: # run the application
	poetry run brain-games

lint:
	poetry run flake8 brain_games

build: # build the application
	poetry build

publish: # test publish the application
	poetry publish --dry-run

package-install: # install the aplication in environment
	pip install --user --force-reinstall dist\hexlet_code-0.1.0-py3-none-any.whl