import logging


def create_logger(app, name):
    # get logger
    logger = logging.getLogger(name)
    # set level
    logger.setLevel(logging.INFO)

    # configurate file handler
    file_handler = logging.FileHandler(app.config[f"{name.upper()}_LOGGER_PATH"], encoding='utf-8')
    # configurate formatter for file handler
    formatter_file = logging.Formatter(
        app.config["LOGGER_FORMAT"],
        datefmt=app.config["DATE_FORMAT"]
    )
    # set formatter to file handler
    file_handler.setFormatter(formatter_file)

    # add file handler to logger
    logger.addHandler(file_handler)


def api_logger(app):
    create_logger(app, 'api')


def posts_logger(app):
    create_logger(app, 'posts')
