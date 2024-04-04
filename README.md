# FastAPI User Management

[![Packaged with Poetry][poetry-badge]](https://python-poetry.org/)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v1.json)](https://docs.pydantic.dev/latest/contributing/#badges)

[poetry-badge]: https://img.shields.io/badge/packaging-poetry-cyan.svg

This project is the most secure BackEnd out there 😂, also it has the cleanest code that ever written. With proper tests that give us 100% coverage of our code. 

---

### Image

![](ui.png)

![run app](image.png)


### Development

```bash
poetry install --with test,lint

# Run Test
poetry run pytest

# Lint
poetry run pre-commit install
poetry run pre-commit run

# Run Service
poetry run uvicorn fastapi_user_management.app:app --host 0.0.0.0 --port 8000 --reload
```
