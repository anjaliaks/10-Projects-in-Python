# install pytube3 and git+http://github.com/pytube/pytube


! pip install pytube3 
! pip install git+http://github.com/pytube/pytube

# import YouTube from pytube
from pytube import YouTube

# provide proper url of video
YouTube('https://www.youtube.com/watch?v=07d2dXHYb94').streams.first().download()

url = "https://www.youtube.com/watch?v=07d2dXHYb94"

yt = YouTube(url)

# check file to download video
yt.streams.first().download()
