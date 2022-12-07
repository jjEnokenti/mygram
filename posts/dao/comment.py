class Comment:
    """
    Class comment
    """

    def __init__(
            self,
            post_id=0,
            commenter_name='',
            comment='',
            pk=0
    ):

        self.post_id = post_id
        self.commenter_name = commenter_name
        self.comment = comment
        self.pk = pk

    def to_dict(self):
        """
        Return comment as dict
        """
        return {
            'post_id': self.post_id,
            'commenter_name': self.commenter_name,
            'comment': self.comment,
            'pk': self.pk
        }

    def __repr__(self):

        return f"Comment(" \
               f"{self.post_id}, " \
               f"{self.commenter_name}, " \
               f"{self.comment}, " \
               f"{self.pk}" \
               f")"
