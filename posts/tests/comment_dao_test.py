import pytest

from posts.dao.comment import Comment
from posts.dao.comment_dao import CommentDao
from config.development import MOCK_COMMENTS_DATA_PATH


def check_fields(comment):
    """
    Testing fields in post
    """
    correct_fields = {
        'post_id',
        'commenter_name',
        'comment',
        'pk'
    }

    for field in correct_fields:
        # checking correct fields in comment
        assert hasattr(comment, field), f"No field {field}"


class TestCommentDao:
    """
    Test CommentDao
    """
    @pytest.fixture
    def comment_dao(self):
        comment_dao_instance = CommentDao(MOCK_COMMENTS_DATA_PATH)
        return comment_dao_instance

    def test_get_all_type(self, comment_dao):
        """
        Test type sequence all comments
        """
        comments = comment_dao.get_all()
        comment = comments[0]
        assert isinstance(comments, list), 'Incorrect type sequence comments'
        assert isinstance(comment, Comment), 'Incorrect comment type'

    def test_get_all_fields(self, comment_dao):
        """
        Check comment fields all comments
        """
        # first comment from all comments
        comment = comment_dao.get_all()[0]
        check_fields(comment)

    def test_get_all_correct_pks(self, comment_dao):
        """
        Test correct pks all comments
        """
        correct_pks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        # all comments
        comments = comment_dao.get_all()
        comments_pks = {comment.pk for comment in comments}
        assert comments_pks == correct_pks, 'Incorrect pk'

    def test_get_by_post_id_fields(self, comment_dao):
        """
        Check comment fields by post_id
        """
        # first comment from comments by post id
        comment = comment_dao.get_by_post_id(3)[0]
        check_fields(comment)

    def test_get_by_post_id_types(self, comment_dao: CommentDao):
        """
        Test type comment by post_id
        """
        # comments by post id
        comments: list[Comment] = comment_dao.get_by_post_id(2)
        comment = comments[0]
        assert isinstance(comments, list), 'Incorrect type sequence comments'
        assert isinstance(comment, Comment), 'Incorrect comment type'
