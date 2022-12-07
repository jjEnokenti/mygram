from json import load, JSONDecodeError

from posts.dao.post import Post
from my_exceptions.data_exception import DataSourceError


class PostDao:
    """
    Post manager
    """
    def __init__(self, path: str):
        self.path = path

    def _load_raw_data(self) -> list[dict]:
        """
        Upload data from json data
        """
        try:
            with open(self.path, encoding='utf-8') as file:
                return load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError("Data processing problem...")

    def _posts_data(self) -> list[Post]:
        """
        Returns list with an instance class Post
        """
        # upload list data with dicts
        data: list = self._load_raw_data()
        # converting list data with dicts
        # to list data with Post instance
        posts: list[Post] = [Post(**post) for post in data]

        return posts

    def get_all(self) -> list[Post]:
        """
        Returns all posts
        """
        # all posts list data with Post instance
        posts: list[Post] = self._posts_data()

        return posts

    def get_by_pk(self, pk: int) -> Post or None:
        """
        Returns a post by its primary key
        """
        if not isinstance(pk, int):
            raise TypeError("pk must be an int")

        posts: list[Post] = self._posts_data()

        # cycle for searching post in posts by the desired pk
        for post in posts:
            if pk == post.pk:
                return post

    def get_by_user(self, user_name: str) -> list[Post] or []:
        """
        Returns all user posts by username
        """
        # raise an error if invalid data is given
        if not isinstance(user_name, str):
            raise TypeError("User name should be a str")

        # lowercase for correct search
        user_name: str = user_name.lower()

        posts: list[Post] = self._posts_data()
        # filling the list with Post instances
        # if these posts are username
        user_posts: list[Post] = [post for post in posts if post.poster_name.lower() == user_name]

        return user_posts

    def get_by_query(self, query: str) -> list[Post] or []:
        """
        Returns all posts with query in content
        """
        # raise an error if invalid data is given
        if not isinstance(query, str):
            raise TypeError("Query should be a str")

        # lowercase for correct search
        query: str = query.lower()

        posts: list[Post] = self._posts_data()
        # filling the list with Post instances
        # if there is a search word in their content
        matching_post: list[Post] = [post for post in posts if query in post.content.lower()]

        return matching_post
