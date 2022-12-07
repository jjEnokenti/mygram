import pytest

from posts.dao.post import Post
from posts.dao.post_dao import PostDao
from config.development import MOCK_POSTS_DATA_PATH


def check_fields(post):
    """
    Testing fields in post
    """
    correct_fields = {
        'poster_name',
        'poster_avatar',
        'pic',
        'content',
        'views_count',
        'likes_count',
        'pk',
    }

    for field in correct_fields:
        # checking correct fields in post
        assert hasattr(post, field), f"No field {field}"


class TestPostDao:

    @pytest.fixture
    def post_dao(self) -> PostDao:
        """
        PostDao instance for testing
        """
        post_dao_instance = PostDao(MOCK_POSTS_DATA_PATH)
        return post_dao_instance

    def test_get_all_types(self, post_dao: PostDao):
        """
        Test posts types
        """
        # all posts
        posts: list[Post] = post_dao.get_all()
        # first post in posts
        post: Post = posts[0]
        assert isinstance(posts, list), "Incorrect type for data posts"
        assert isinstance(post, Post), "incorrect type for data single post"

    def test_get_all_fields(self, post_dao):
        """
        Test post fields
        """
        # first post in posts
        post: Post = post_dao.get_all()[0]
        # checking correct fields
        check_fields(post)

    def test_get_all_correct_ids(self, post_dao):
        """
        Test post id
        """
        posts = post_dao.get_all()
        # guaranteed pks that are in the mock data
        correct_ids = {1, 2, 3, 4}

        # pks from mock posts data
        ids = {post.pk for post in posts}
        assert ids == correct_ids, 'Incorrect ids for post'

    def test_get_by_user_types(self, post_dao):
        """
        Test founded posts type by user
        """
        # posts by user
        posts = post_dao.get_by_user('LeO')
        # first post by user
        post = posts[0]
        assert isinstance(posts, list)
        assert isinstance(post, Post)

    def test_get_by_user_quantity(self, post_dao):
        """
        Test correct quantity post by user
        """
        # posts by user
        posts = post_dao.get_by_user('LarRy')
        assert len(posts) == 3, 'Incorrect quantity posts'

    def test_get_by_user_fields(self, post_dao):
        """
        Test correct post fields by user
        """
        # first post by user
        post = post_dao.get_by_user('LarRy')[0]
        # checking correct fields
        check_fields(post)

    def test_get_by_user_exception(self, post_dao):
        """
        Test for correct raise
        """
        with pytest.raises(TypeError):
            assert post_dao.get_by_user(2), 'Incorrect exception'

    def test_get_by_pk_types(self, post_dao):
        """
        Test post type founded by pk
        """
        # post by pk 1
        post = post_dao.get_by_pk(1)
        assert isinstance(post, Post), 'Incorrect founded post type by pk'

    def test_get_by_pk_correct_id(self, post_dao):
        """
        Test matching post pk founded by pk
        """
        # post by pk 2
        post = post_dao.get_by_pk(2)
        assert post.pk == 2, 'Not matching founded pk post by pk'

    def test_get_by_pk_fields(self, post_dao):
        """
        Test correct post fields by pk
        """
        # post by pk 3
        post = post_dao.get_by_pk(3)
        # checking correct fields
        check_fields(post)

    def test_get_by_pk_exception(self, post_dao):
        """
        Test for correct raise
        """
        with pytest.raises(TypeError):
            assert post_dao.get_by_pk('2'), 'Incorrect exception'

    def test_get_by_query_types(self, post_dao):
        """
        Test founded posts type by query
        """
        # posts founded by query
        posts = post_dao.get_by_query('Ага')
        # first founded post by query
        post = posts[0]
        assert isinstance(posts, list)
        assert isinstance(post, Post)

    def test_get_by_query_quantity(self, post_dao):
        """
        Test correct quantity post by user
        """
        # posts founded by query
        posts = post_dao.get_by_query('аГа')
        assert len(posts) == 1, 'Incorrect quantity posts'

    def test_get_by_query_fields(self, post_dao):
        """
        Test correct post fields by query
        """
        # first founded post by query
        post = post_dao.get_by_query('АГА')[0]
        # checking correct fields
        check_fields(post)

    def test_get_by_query_exceptions(self, post_dao):
        """
        Test for correct raise
        """
        with pytest.raises(TypeError):
            assert post_dao.get_by_query([1,2,3]), 'Incorrect exception'
