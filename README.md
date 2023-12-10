# PythonYoutubeMusicDownloader
Simple scripts in Python to automate downloading music from Youtube Music using yt-dlp

These script were made in order for me to automate downloading all albums of Artists I like from Youtube Music in order to stream them on my local Navidrome instance
# Dependencies
The only dependencies of these scripts are: python3 and yt-dlp - if on Windows yt-dlp MUST be added on PATH in order to work

To start run the script YoutubeMusicDownloader.py via 
```
python3 YoutubeMusicDownloader.py
```
After specifying the dir we want to download our music to and adding artist playlists or entire artists 'Songs' links we can automate the download process for example via Cron to check once a week/however often we want for new realeases in case we added entire links of artists 'Songs' playlist.

When using Cron use only the Download.py script - YoutubeMusicDownloader.py is only a front end for adding artist links into artists.txt and changing the default download dir that Download.py uses.
