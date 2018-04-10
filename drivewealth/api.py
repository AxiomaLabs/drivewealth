from hammock import Hammock as DriveWealth

from services.user import UserApiMixin
from services.session import SessionApiMixin


class Api(SessionApiMixin, UserApiMixin):
    API_BASE_URL = 'https://api.drivewealth.io/v1'

    def __init__(self, username, password, api_base_url=API_BASE_URL):
        self.username = username
        self.password = password
        self.api_base_url = api_base_url

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        self.drive_wealth = DriveWealth(self.api_base_url, headers=headers)

        self.create_session(username, password)

        # Create api with the generated session
        headers['x-mysolomeo-session-key'] = self.session_key
        self.drive_wealth = DriveWealth(self.api_base_url, headers=headers)
