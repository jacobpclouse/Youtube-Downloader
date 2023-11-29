## Download Youtube videos & Convert to MP3
- This code allows you to download videos from Youtube (via code from Tech with Tiff and pytube) AND convert MP4 files to MP3 audio files (done via moviepy)
- Alternate version downloads videos using yt-dlp in either .mp4 and .mp3
- Documentation directory has instructions to setup virtual env 
- UPDATE: As of Nov. 2023, you can use the convertToAudio.py to convert .mp4 files to .mp3 files on BOTH windows and linux! (haven't tested MacOS)

### How to use Pytube download code (just youtube, no external programs needed):
1) clone this repo with git and cd into it
2) use the activateVirEnv.txt to setup a virtual environment and activate it
3) use the command pip install requirements.txt to install the requirements for the code (pip install -r requirements.txt)
4) cd into the pytube Code directory, run the downloader with the command: python pytubeDownload.py (if you have python2 and python3 installed, you will need to run it with python3 pytubeDownload.py)
5) provide the url for the youtube video you want to download and hit enter
6) You can convert the video to .mp3 usign the convertToAudio.py file, otherwise you should be all set
(NOTE: you may need to update your version of pytube if your version throws an error using: pip install --upgrade pytube) 

### How to use Yt-dlp download code VIDEO (multiple sites beside youtube, need ffmpeg installed):
1) you will need to have ffmpeg downloaded and installed for this to work, use this link: https://youtu.be/IECI72XEox0
1) clone this repo with git and cd into it
2) use the activateVirEnv.txt to setup a virtual environment and activate it
3) use the command pip install requirements.txt to install the requirements for the code (pip install -r requirements.txt)
4) *cd into the yt-dlp Code directory, run the downloader with the command: python mp4Download.py (if you have python2 and python3 installed, you will need to run it with python3 mp4Download.py)
5) provide the url for the youtube video you want to download and hit enter
6) A video will be downloaded 
(NOTE: you may need to update your version of yt-dlp if your version throws an error using: pip install --upgrade yt-dlp) 

### How to use Yt-dlp download code AUDIO (multiple sites beside youtube, need ffmpeg installed):
- Same steps as the video section, but run the downloadAudio.py file instead of the mp4Download.py
- You can also use the convertToAudio.py in pytube Code to convert an .mp4 to an .mp3


### Sources:
- https://stackoverflow.com/questions/55081352/how-to-convert-mp4-to-mp3-using-python
- MoviePy Install: https://zulko.github.io/moviepy/install.html
- How to print all files within a directory using Python?: https://www.geeksforgeeks.org/how-to-print-all-files-within-a-directory-using-python/
- Moviepy is unable to find ffmpeg libx264 codec #696: https://github.com/Zulko/moviepy/issues/696
- How to Extract Audio from Video in Python: https://www.thepythoncode.com/article/extract-audio-from-video-in-python
