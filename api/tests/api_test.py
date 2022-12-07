class TestApi:
    """
    Test class for api
    """
    # correct comment fields for matching
    correct_fields = {
        'poster_name',
        'poster_avatar',
        'pic',
        'content',
        'views_count',
        'likes_count',
        'pk',
    }

    # Tests all posts

    def test_get_all_status_code(self, test_client):
        """
        Test status code by request /api/posts
        """
        response = test_client.get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, 'Incorrect status code'

    def test_get_all_types(self, test_client):
        """
        Test types by request /api/posts
        """
        response = test_client.get('/api/posts', follow_redirects=True)
        data = response.get_json()
        assert isinstance(data, list), 'Incorrect data type'

        post = data[0]
        assert isinstance(post, dict), 'Incorrect post type'

    def test_get_all_fields(self, test_client):
        """
        Test fields by request /api/posts
        """
        response = test_client.get('/api/posts', follow_redirects=True)
        data = response.get_json()

        for post in data:
            assert set(post.keys()) == self.correct_fields, 'Incorrect post fields'

    # Tests single post

    def test_get_single_status(self, test_client):
        """
        Test status code by request /api/posts/<post_id>
        """
        response = test_client.get('/api/posts/2', follow_redirects=True)
        assert response.status_code == 200, 'Incorrect status code'

    def test_get_single_type(self, test_client):
        """
        Test type by request /api/posts/<post_id>
        """
        response = test_client.get('/api/posts/3', follow_redirects=True)
        assert isinstance(response.get_json(), dict), 'Incorrect post type'

    def test_get_single_fields(self, test_client):
        """
        Test fields by request /api/posts/<post_id>
        """
        response = test_client.get('/api/posts/1', follow_redirects=True)
        assert set(response.get_json().keys()) == self.correct_fields, 'Incorrect post fields'

    def test_get_single_404(self, test_client):
        """
        Test error 404 by request /api/posts/<non existent post_id>
        """
        response = test_client.get('/api/posts/-1')
        assert response.status_code == 404, 'Incorrect status'
