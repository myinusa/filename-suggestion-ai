# Changelog

## [1.4.0](https://github.com/myinusa/filename-suggestion-ai/compare/v1.3.0...v1.4.0) (2024-09-01)


### Features

* **filename_suggestion_ai/utils:** add APIClient class to handle API interactions ([5cdb9eb](https://github.com/myinusa/filename-suggestion-ai/commit/5cdb9eb92b4ad416112605574989f4e603900c38))
* **main:** implement collection and logging of answers in main function ([0635eb0](https://github.com/myinusa/filename-suggestion-ai/commit/0635eb0d2e7624cfa06df943d1fb625dfc96e387))


### Bug Fixes

* **constants:** update model constant to new version ([0635eb0](https://github.com/myinusa/filename-suggestion-ai/commit/0635eb0d2e7624cfa06df943d1fb625dfc96e387))

## [1.3.0](https://github.com/myinusa/filename-suggestion-ai/compare/v1.2.0...v1.3.0) (2024-08-31)


### Features

* **args.py:** add new optional arguments for directory and filter processing ([b819649](https://github.com/myinusa/filename-suggestion-ai/commit/b819649317b2bc6569aad8b85f9872a5719c8bbc))
* **main.py:** implement directory and filter based file processing with progress tracking ([b819649](https://github.com/myinusa/filename-suggestion-ai/commit/b819649317b2bc6569aad8b85f9872a5719c8bbc))
* **poetry.lock:** add tqdm package for progress tracking functionality ([b819649](https://github.com/myinusa/filename-suggestion-ai/commit/b819649317b2bc6569aad8b85f9872a5719c8bbc))
* **pyproject.toml:** include tqdm in project dependencies for progress tracking ([b819649](https://github.com/myinusa/filename-suggestion-ai/commit/b819649317b2bc6569aad8b85f9872a5719c8bbc))

## [1.2.0](https://github.com/myinusa/filename-suggestion-ai/compare/v1.1.0...v1.2.0) (2024-08-31)


### Features

* **config:** add import of args module in __init__.py ([5428fd4](https://github.com/myinusa/filename-suggestion-ai/commit/5428fd4a3a5b574a7fd40debbfa7ac4bc548c96e))
* **config:** add new command line argument for file input in args.py ([5428fd4](https://github.com/myinusa/filename-suggestion-ai/commit/5428fd4a3a5b574a7fd40debbfa7ac4bc548c96e))
* **main:** add new payload creation function for POST requests ([5428fd4](https://github.com/myinusa/filename-suggestion-ai/commit/5428fd4a3a5b574a7fd40debbfa7ac4bc548c96e))
* **main:** integrate argument parsing and dynamic user content handling ([5428fd4](https://github.com/myinusa/filename-suggestion-ai/commit/5428fd4a3a5b574a7fd40debbfa7ac4bc548c96e))
* **models:** add new LMStudioChatResponse data model ([5428fd4](https://github.com/myinusa/filename-suggestion-ai/commit/5428fd4a3a5b574a7fd40debbfa7ac4bc548c96e))
* **utils:** implement utility function to read file content ([5428fd4](https://github.com/myinusa/filename-suggestion-ai/commit/5428fd4a3a5b574a7fd40debbfa7ac4bc548c96e))

## [1.1.0](https://github.com/myinusa/filename-suggestion-ai/compare/v1.0.0...v1.1.0) (2024-08-31)


### Features

* **config:** add initial configuration files for filename_suggestion_ai ([bf2d70c](https://github.com/myinusa/filename-suggestion-ai/commit/bf2d70cf6757b55cc05d349ac6e197c2381cdccb))
* **config:** configure logging with rich handler in setup_logging.py ([bf2d70c](https://github.com/myinusa/filename-suggestion-ai/commit/bf2d70cf6757b55cc05d349ac6e197c2381cdccb))
* **config:** define constants for API interaction in constants.py ([bf2d70c](https://github.com/myinusa/filename-suggestion-ai/commit/bf2d70cf6757b55cc05d349ac6e197c2381cdccb))
* **config:** implement argument parsing in args.py ([bf2d70c](https://github.com/myinusa/filename-suggestion-ai/commit/bf2d70cf6757b55cc05d349ac6e197c2381cdccb))
* **config:** setup environment and logging configurations in enviornment_setup.py ([bf2d70c](https://github.com/myinusa/filename-suggestion-ai/commit/bf2d70cf6757b55cc05d349ac6e197c2381cdccb))
* **main:** add main execution flow and POST request handling in main.py ([bf2d70c](https://github.com/myinusa/filename-suggestion-ai/commit/bf2d70cf6757b55cc05d349ac6e197c2381cdccb))

## 1.0.0 (2024-08-31)


### Features

* add poetry.lock with dependencies and their hashes ([029596f](https://github.com/myinusa/filename-suggestion-ai/commit/029596f57c803770233f0ed34ab4c73f32b463a6))
* update pyproject.toml with new dependencies and configurations for black, ruff, pytest, isort, and vulture ([029596f](https://github.com/myinusa/filename-suggestion-ai/commit/029596f57c803770233f0ed34ab4c73f32b463a6))
