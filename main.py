# Main video: https://youtu.be/EMlM6QTzJo0
# Demo code: https://replit.com/@tiffintech/Youtubedownloader#main.py
# Fix by moken: https://stackoverflow.com/questions/76129007/pytube-keyerror-streamdata-while-downloading-a-video

import pip
from pytube import YouTube

# Function to check for and update pytube
def update_pytube():
    try:
        from pytube import __version__ as pytube_version
        installed_version = pip.get_installed_distributions(local_only=True)["pytube"].version
        if pytube_version != installed_version:
            print(f"Updating pytube from {pytube_version} to {installed_version}")
            pip.main(['install', '--upgrade', 'pytube'])
    except Exception as e:
        print("Error checking/updating pytube:", e)

# Call the update function before anything else
update_pytube()

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
        print("This download has completed! Yahooooo!")
    except:
        print("There has been an error in downloading your youtube video")

link = input("Put your youtube link here!! URL: ")
Download(link)
