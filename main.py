# Main video: https://youtu.be/EMlM6QTzJo0
# Demo code: https://replit.com/@tiffintech/Youtubedownloader#main.py

from pytube import YouTube

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