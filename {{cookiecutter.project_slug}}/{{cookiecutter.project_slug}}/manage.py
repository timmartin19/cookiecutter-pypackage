from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
from logging import config as logging_config

from flask import Flask
from flask_appconfig import AppConfig
from flask_ripozo import FlaskDispatcher
from ripozo.adapters import SirenAdapter, JSONAPIAdapter

from {{ cookiecutter.project_slug }}.views import VIEWS_BLUEPRINT


def create_app(config_dict=None):
    app = Flask('{{cookiecutter.project_slug}}')
    initialize_config(app, config_dict=config_dict)
    initialize_logging(app.config)
    initialize_ripozo(app)
    initialize_extra_views(app)
    return app


def initialize_config(app, config_dict=None):
    config_dict = config_dict or {}
    app_config = AppConfig(app)
    for key, value in config_dict.items():
        app.config[key] = value
    return app_config


def initialize_ripozo(app):
    dispatcher = FlaskDispatcher(app)
    dispatcher.register_adapters(SirenAdapter, JSONAPIAdapter)
    # dispatcher.register_resources()  Simply pass in your resource classes here
    return dispatcher


def initialize_logging(config):
    logging_config.dictConfig(config['LOGGING'])


def initialize_extra_views(app):
    app.register_blueprint(VIEWS_BLUEPRINT)
    return app

