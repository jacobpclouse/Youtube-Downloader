import yt_dlp
# NOTE: You need to have ffmpeg downloaded and added to the path variable for this to work, get it here: https://ffmpeg.org/download.html#build-windows
# You also need to 'pip install yt-dlp'

# Set the URL of the YouTube video you want to download
url = input("Give me a URL: ")

# Set options for the downloader
ydl_opts = {
    'format': 'bestvideo+bestaudio',
    'outtmpl': '%(title)s.%(ext)s',
}

# Create the downloader and pass in the options and URL
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
