import logging

from flask import (
    Blueprint,
    render_template,
    jsonify,
    abort
)

from posts.dao.post import Post
from posts.dao.post_dao import PostDao

from config.development import POSTS_DATA_PATH


api_blueprint = Blueprint(
    'api_blueprint',
    __name__,
    template_folder='templates'
)


# activate api logger
logger = logging.getLogger('api')
# create PostDao instance
post_dao = PostDao(POSTS_DATA_PATH)


@api_blueprint.route('/')
def api():
    """
    Api greetings
    """
    logger.info("Request /api")
    return render_template(
        'api_greetings_page.html',
    ), 200


@api_blueprint.route('/posts')
def get_all_posts():
    """
    Api send all posts from data
    """
    logger.info("Request /api/posts")
    # all posts as dict
    posts: list[dict] = [post.to_dict() for post in post_dao.get_all()]
    return jsonify(posts), 200


@api_blueprint.route('/posts/<int:post_id>')
def get_post_by_post_id(post_id: int):
    """
    Api get post from data by post id
    """
    logger.info(f"Request /api/posts/{post_id}")
    # post as dict
    post: Post | None = post_dao.get_by_pk(post_id).to_dict()

    if post is None:
        abort(404)

    return jsonify(post), 200


@api_blueprint.errorhandler(404)
def api_error_404(error):
    return jsonify({"error": str(error)}), 404
