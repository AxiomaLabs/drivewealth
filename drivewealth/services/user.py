from ..schemas import create_object_from_json_response


class UserApiMixin:
    """
    Details specific user
    """

    def get_user(self, user_id):
        """
        Get user's information
        @Params
            user_id: User id String
        @Return
            User Object
        """
        response = self.drive_wealth.users(self.user_id).GET()
        return create_object_from_json_response('User', response)
