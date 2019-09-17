from . import YouTubeSession

from .YouTubeSession import BIND_DATA

YOUTUBE_BASE_URL = "https://tv.youtube.com/"

BIND_DATA.update({"theme": "up"})

class YouTubeTVSession(YouTubeSession):
    """ The main logic to interact with YouTube cast api."""

    def __init__(self, screen_id, cookies=None):
        super(YouTubeTVSession, self).__init__(screen_id, cookies)
        self._bind_data = BIND_DATA
