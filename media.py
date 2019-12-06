import vlc
import time

import config

# Instance and player
Instance = vlc.Instance(['--video-on-top', '--input-repeat=999999'])
player = Instance.media_player_new()
vid_name = "media/video.mp4"
Media = Instance.media_new(vid_name)
Media.get_mrl()
player.set_media(Media)
player.set_fullscreen(True)
player.play()
time.sleep(10)
exit()
