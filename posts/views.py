import logging

from flask import (
    Blueprint,
    render_template,
    request,
    abort
)

from posts.dao.post import Post
from posts.dao.post_dao import PostDao
from posts.dao.comment import Comment
from posts.dao.comment_dao import CommentDao

from config.development import POSTS_DATA_PATH, COMMENTS_DATA_PATH

from my_exceptions.data_exception import DataSourceError


#
logger = logging.getLogger('posts')
#
post_dao = PostDao(POSTS_DATA_PATH)
comment_dao = CommentDao(COMMENTS_DATA_PATH)

posts_blueprint = Blueprint(
    'posts_blueprint',
    __name__,
    template_folder='templates'
)


@posts_blueprint.route('/')
def index_page():
    """
    View index page
    """
    try:
        posts: list[Post] = post_dao.get_all()

        return render_template(
            'posts_index.html',
            posts=posts
        )
    except DataSourceError as message:
        logger.info(message)
        return render_template(
            'error_info_page.html',
            message=message,
        )


@posts_blueprint.route('/posts/<int:pk>')
def single_post(pk: int):
    """
    View single post by pk
    """
    try:
        post: Post | None = post_dao.get_by_pk(pk)
        comments: list[Comment] = comment_dao.get_by_post_id(pk)
        if post is None:
            abort(404, f"Post with this {pk} non exists")

        return render_template(
            'posts_single_post.html',
            post=post,
            comments=comments
        )
    except (TypeError, DataSourceError) as message:
        logger.info(message)
        return render_template(
            'error_info_page.html',
            message=message,
        )


@posts_blueprint.route('/search/')
def search_view():
    """
    View search result by query
    """
    try:
        query: str = request.args.get('search')
        # posts by query
        posts: list[Post] = post_dao.get_by_query(query)[:10]

        return render_template(
            'posts_search.html',
            posts=posts,
        )
    except (TypeError, DataSourceError) as message:
        # write log about of problem
        logger.info(message)
        return render_template(
            'error_info_page.html',
            message=message,
        )


@posts_blueprint.route('/users/<username>')
def get_by_username(username):
    """
    View user feed posts by username
    """
    try:
        username = str(username)
        # poster posts by name
        posts: list[Post] = post_dao.get_by_user(username)
        # if user posts not found
        if not posts:
            abort(404, f"User with name {username} not found")

        return render_template(
            'posts_user-feed.html',
            posts=posts,
            username=username
        )
    except (TypeError, DataSourceError) as message:
        # write log about of problem
        logger.info(message)
        return render_template(
            'error_info_page.html',
            message=message,
        )
