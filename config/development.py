import os

MY_VALUE = 'development_value'

JSON_AS_ASCII = False

# data path config
POSTS_DATA_PATH = os.path.join('data', 'posts.json')
MOCK_POSTS_DATA_PATH = os.path.join('mocks', 'posts_mock.json')
COMMENTS_DATA_PATH = os.path.join('data', 'comments.json')
MOCK_COMMENTS_DATA_PATH = os.path.join('mocks', 'comments_mock.json')

# logger config
API_LOGGER_PATH = os.path.join('logs', 'api.log')
POSTS_LOGGER_PATH = os.path.join('logs', 'posts.log')
LOGGER_FORMAT = "[%(levelname)s]: [%(name)s] %(asctime)s: " \
                "Full path to file [%(pathname)s] - function name %(funcName)s(%(lineno)d) - %(message)s"
DATE_FORMAT = "%d-%m-%y %H:%M:%S"
