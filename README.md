# CastTube

casttube provides a way to interact with the Youtube and Youtube TV Chromecast api.

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

Example usage:
```
from casttube import YouTubeSession
session = YouTubeSession(screen_id)

# YouTube video id is http://youtube.com/watch?v=video_id
session.play_video(video_id)
```

or for Youtube TV

```
from casttube import YouTubeTVSession
# Add the required Authentication Cookies. These can be found by browsing to YouTube TV,
# logging in, opening the element inspector and browsing to
# Application > Storage > Cookies > https://tv.youtube.com
# and filling in the matching cookie values below.
cookies = {
    "APISID": "",
    "HSID": "",
    "SAPISID": "",
    "SID": "",
    "SSID": "",
}
session = YouTubeTVSession(screen_id, cookies)

# YouTube TV video id is https://tv.youtube.com/watch/video_id
session.play_video(video_id)
```

The library requires 2 things:
1. screen id
2. The Chromecast Youtube or Youtube TV app needs to be open

There is a small script in https://github.com/ur1katz/CastTube-Scripts to print the screen id and launch the app.

**Youtube TV:**

The Youtube TV Casting API is extremely similar to the Youtube one. The only major difference is Youtube TV requires authentication cookies to be passed in as part of your session, which means a Youtube TV subscription is required.

The channels for Youtube TV are different for each area so extracting them is left as an exercise for the implementer. It is very easy to get a list of channels, just go to the `Live` tab in YouTube TV and click on a currently playing show. You will then get a URL that is extremely similar to a YouTube URL. Simply copy the video_id from there.
