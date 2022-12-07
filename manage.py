import os

import dotenv
from flask import Flask

from api.views import api_blueprint
from posts.views import posts_blueprint

from loggers import api_logger, posts_logger

from my_exceptions.data_exception import DataSourceError


dotenv.load_dotenv()


def configurate_flask_app(path):
    """
    Create and configurate flask application
    """
    # create flask application
    conf_app = Flask(__name__)
    # configuration flask app
    conf_app.config.from_pyfile(path)
    # register blueprints
    conf_app.register_blueprint(posts_blueprint)
    conf_app.register_blueprint(api_blueprint, url_prefix='/api')

    # create loggers
    api_logger(conf_app)
    posts_logger(conf_app)

    return conf_app


def config_path():
    """
    Choice config file development or production
    """
    if os.environ.get("APP_CONFIG") == 'development':
        path = 'config/development.py'
    else:
        path = 'config/production.py'

    return path


# Created and configured flask app
app = configurate_flask_app(config_path())


# error handlers
@app.errorhandler(404)
def page_error_404(error):
    """
    404 error handler
    """
    return f"page not found {error}", 404


@app.errorhandler(500)
def page_error_500(error):
    """
    500 error handler
    """
    return f"Something is wrong on the server side.. {error}", 500


@app.errorhandler(DataSourceError)
def page_data_source_error(error):
    """
    data source error handler
    """
    return f"Something is wrong with database - {error}", 500


if __name__ == '__main__':
    app.run(
        port=8888
    )
