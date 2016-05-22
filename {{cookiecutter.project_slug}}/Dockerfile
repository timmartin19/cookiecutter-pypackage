FROM python:latest

ENV APP_ROOT /app

RUN mkdir $APP_ROOT
WORKDIR $APP_ROOT

RUN pip install uwsgi

ADD AUTHORS.rst CONTRIBUTING.rst HISTORY.rst README.rst ./
ADD setup.py setup.py
RUN pip install -e .

ADD image image

ADD docs docs
ADD {{cookiecutter.project_slug}} {{cookiecutter.project_slug}}
ADD {{cookiecutter.project_slug}}_tests {{cookiecutter.project_slug}}_tests

CMD $APP_ROOT/image/run-uwsgi
