# CastTube

casttube provides a way to interact with the Youtube Chromecast api.

**Install:**

```
pip install casttube
```

**Features**
* Play video
* Play a playlist
* Add video to the end of the play queue
* Play next
* Remove video
* Clear the entire queue

```
from casttube import YouTubeSession
session = YouTubeSession(screen_id)

# YouTube video id is http://youtube.com/watch?v=video_id
session.play_video(video_id)
```

The library requires 2 things:
1. screen id
2. The Chromecast youtube app needs to be open

There is a small script in https://github.com/ur1katz/CastTube-Scripts to print the screen id and launch the app.


