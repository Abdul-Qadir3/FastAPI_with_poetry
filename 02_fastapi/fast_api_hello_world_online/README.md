# API	
API stands for `Application Programming Interface`. It is a set of rules, protocols, and tools that allows different software applications to communicate with each other 
## FastAPI
FastAPI is a `modern, fast (high-performance), web framework` for building APIs with Python 3.7+ based on standard Python type hints.<br>
It's designed to be easy to use, efficient, and intuitive, with built-in support for modern features like `asynchronous programming`.

## Poetry
Poetry is a `dependency management` and `packaging tool` for Python. It simplifies the process of managing dependencies and packaging Python projects by providing a consistent and reliable workflow.<br>
`Package management using poetry`

# `HELLO WORLD WITH FAST API`
`STEPS`
1. poetry new `fastapi_hello_world_online`
2. cd fastapi_hello_world_online
3. Select project with `VsCode`
4. Open toml file `pyprojec.toml`
    - Contains three sections (section is identified using []) 
      - Section 1. Project Meta Data
      - Section 2. Dependencies
      - Section 3. 
```
[tool.poetry]
name = "fastapi-hello-world-online"
version = "0.1.0"
description = ""
authors = ["Abdul-Qadir3 <aqadirsamdani@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
5. install new pakages to the poetry project<br>
    STNTAX:    `poetry add pakage_name`
6. Create a `main.py` file at location `fastapi_hello_world_online\fastapi_hello_world_online\main.py`
    ```
    [tool.poetry.dependencies]
    python = "^3.12"
    fastapi = "^0.111.0"
    uvicorn = {extras = ["standard"], version = "^0.29.0"}
    ```
7. poetry add `fastapi "uvicorn[standard]"` 
(two packages have been added pakages can be added by simply giving spacing)
8. `.lock` file locks all the `dependencies` and `pakages` of project that can be used later on
9. `poetry shell` 

#### Run surver
10. `poetry run uvicorn fastapi_hello_world_online.main:app --reload`
    <b>
    ```
    "poetry run": This part of the command is used to execute a command within the Poetry-managed virtual environment. It ensures that the dependencies installed via Poetry are available for the command.

    "uvicorn": This is the command to run the Uvicorn ASGI server, which is a lightning-fast ASGI server implementation, ideal for running FastAPI applications.

    "fastapi_hello_world_online.main:app": This part specifies the module and object to be served by Uvicorn. Here, fastapi_hello_world_online.main refers to the Python module (main.py) containing the FastAPI application, and app refers to the instance of the FastAPI application within that module.

    "--reload": This option enables automatic reloading of the server whenever changes are detected in the code. It's helpful during development as it eliminates the need to manually restart the server after making code changes.
    ```
11. `http://127.0.0.1:8000/`
    `http://127.0.0.1:8000/piaic/`
    
12. `http://127.0.0.1:8000/docs`
13. Write your own test
    - `test/test_main.py`
14. To run Test
    - `poetry run pytest`

### Summarizing the steps
- `poetry --version`
- `poetry new project_youtube`
- `cd project_youtube`
- `poetry run python --version`
- `poetry add requests`
- `poetry run python ./project_youtube/main.py`
- `poetry add pytest`
- `poetry run pytest`

