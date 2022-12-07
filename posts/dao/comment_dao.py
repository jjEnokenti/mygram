from json import load, JSONDecodeError

from posts.dao.comment import Comment
from my_exceptions.data_exception import DataSourceError


class CommentDao:
    """
    Comments manager
    """

    def __init__(self, path):
        self.path = path

    def _load_raw_data(self) -> list[dict]:
        """
        Load data from json
        """
        try:
            with open(self.path, encoding='utf-8') as file:
                return load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError("Data processing problem...")

    def _comments_data(self) -> list[Comment]:
        """
        Returns list Comment instance
        """
        # load raw data
        comments_data: list[dict] = self._load_raw_data()
        # format from raw data to list Comment instance
        comments: list[Comment] = [Comment(**comment) for comment in comments_data]

        return comments

    def get_all(self):
        """
        Get all comments
        """
        return self._comments_data()

    def get_by_post_id(self, post_id: int) -> list[Comment]:
        """
        Returns all post comments by post_id
        """
        if not isinstance(post_id, int):
            raise TypeError("pk must be an int")
        # list post comments
        post_comments: list[Comment] = [
            comment for comment in self._comments_data()
            if comment.post_id == post_id
        ]

        return post_comments
