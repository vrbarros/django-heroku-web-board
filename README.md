# django-heroku-web-board
🔬 Study project with Django and Heroku

The project is deploy at [Heroku](https://django-heroku-web-board.herokuapp.com/).


## Features

- Django
- Multiple settings
- Custom project folder structure with apps folder
- Black, isort and flake8 support with VSCode
- .editorconfig and Makefile
- Docker support for local development
- Heroku ready deployment

## Quick Start with virtualenv

1. Create a virtualenv with Python 3.8

```bash
virtualenv venv -p python3.8
```

2. Activate the virtualenv

```bash
source venv/bin/activate
```

3. Install requirements.txt

```bash
pip install -r requirements.txt
```

4. Run the server locally

```bash
python manage.py runserver
```

5. Open browser at `http://localhost:8000/`


## Quick Start with Docker

1. Build the new Docker

```bash
docker-compose up ---build
```

2. Open browser at `http://localhost:8001/`


## References

* [Heroku Python: Getting Started](https://github.com/heroku/python-getting-started)
