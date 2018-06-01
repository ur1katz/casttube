#!/usr//bin/python

import sys
import threading

import pychromecast
from pychromecast.controllers import BaseController
from pychromecast.error import UnsupportedNamespace

TYPE_GET_SCREEN_ID = "getMdxSessionStatus"
TYPE_STATUS = "mdxSessionStatus"
ATTR_SCREEN_ID = "screenId"
MESSAGE_TYPE = "type"


class ScreenIdController(BaseController):
    def __init__(self):
        super(ScreenIdController, self).__init__("urn:x-cast:com.google.youtube.mdx", "233637DE")
        self.status_update_event = threading.Event()

    def update_screen_id(self):
        """
        Sends a getMdxSessionStatus to get the screenId and waits for response.
        This function is blocking
        If connected we should always get a response
        (send message will launch app if it is not running).
        """
        self.status_update_event.clear()
        # This gets the screenId but always throws. Couldn't find a better way.
        try:
            self.send_message({MESSAGE_TYPE: TYPE_GET_SCREEN_ID})
        except UnsupportedNamespace:
            pass
        self.status_update_event.wait()
        self.status_update_event.clear()

    def receive_message(self, message, data):
        """ Called when a media message is received. """
        if data[MESSAGE_TYPE] == TYPE_STATUS:
            self._process_status(data.get("data"))
            return True

        return False

    def _process_status(self, status):
        """ Process latest status update. """
        print(status.get(ATTR_SCREEN_ID))
        self.status_update_event.set()


friendly_name = sys.argv[1]

if __name__ == "__main__":
    chromecasts = pychromecast.get_chromecasts()
    cast = next(cc for cc in chromecasts if cc.device.friendly_name == friendly_name)
    cast.wait()
    controller = ScreenIdController()
    cast.register_handler(controller)
    controller.update_screen_id()
