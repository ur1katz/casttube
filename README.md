# CastTube

casttube provides a way to interact with the Youtube Chromecast api.

The current avilable options are:
* Play video
* Add video to the end of the play queue
* Play next
* Remove video

```
from casttube import YouTubeSession
session = YouTubeSession(screen_id)

# YouTube video id is http://youtube.com/watch?v=**video_id
session.play_video(video_id)
