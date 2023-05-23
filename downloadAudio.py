import yt_dlp

# Set the URL of the video you want to download
url = input("Give me a URL: ")

# Set options for the yt_dlp downloader
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3'
    }],
    'outtmpl': '%(title)s.%(ext)s',
}

# Create a YTDL object with the options specified
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    # Download the audio
    ydl.download([url])