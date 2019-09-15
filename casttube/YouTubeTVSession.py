from . import YouTubeSession

YOUTUBE_BASE_URL = "https://tv.youtube.com/"

BIND_DATA = {"device": "REMOTE_CONTROL", "id": "aaaaaaaaaaaaaaaaaaaaaaaaaa", "name": "Python",
             "mdx-version": 3, "pairing_type": "cast", "app": "android-phone-13.14.55", "theme": "up"}

class YouTubeTVSession(YouTubeSession):
    """ The main logic to interact with YouTube cast api."""

    def __init__(self, screen_id, cookies=None):
        super(YouTubeTVSession, self).__init__(screen_id, cookies)
        self._bind_data = BIND_DATA