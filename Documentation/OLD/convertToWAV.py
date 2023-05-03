# -=-=-=-=-=-=-=-=-=-=-=-=
# Imports
# -=-=-=-=-=-=-=-=-=-=-=-=
import os
from moviepy.editor import *

import soundfile
import wave

# -=-=-=-=-=-=-=-=-=-=-=-=
# Variables
# -=-=-=-=-=-=-=-=-=-=-=-=

# allowed extensions for conversion
ALLOWED_EXTENSIONS = set(['mp4'])

# Target Folder to open
folderPath = '.\FilesToConvert'

# Extracting all the contents in the directory corresponding to path
l_files = os.listdir(folderPath)

# Make output Folder name
convertedFolderUser = input("Enter name of output folder: ")
convertedFolderPath = f".\{convertedFolderUser}"
# Create the directory
os.mkdir(convertedFolderPath)
print("Directory '% s' created" % convertedFolderPath)


# -=-=-=-=-=-=-=-=-=-=-=-=
# Functions
# -=-=-=-=-=-=-=-=-=-=-=-=

# used to find ending type for file AND checking to make sure that it is an allowed type
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# convert mp4 to mp3
def mp4_to_mp3(mp4, mp3):     
	mp4_without_frames = AudioFileClip(mp4)    
	mp4_without_frames.write_audiofile(mp3)     
	mp4_without_frames.close() 
	# function call mp4_to_mp3("my_mp4_path.mp4", "audio.mp3")

# # -=-=-=-=-=-=-=-=-=-=-=-=
# # Main
# # -=-=-=-=-=-=-=-=-=-=-=-=


# Iterating over all the files
for file in l_files:
    # Generate output files and path
    convertedName = f'converted_{file}.wav'
    convertedOutputPath = f'{convertedFolderPath}\{convertedName}'

    # get input path
    fullPath = f"{folderPath}\{file}"

    # printing out values
    print(f"Incoming fullpath: {fullPath}")
    print(f"Outgoing converted file name: {convertedName}")
    print(f"Outgoing file path: {convertedOutputPath}")

    # if this is an allowed mp4, allow convert
    if allowed_file(file):

        # soundfile convert
        # Read and rewrite the file with soundfile
        data, samplerate = soundfile.read(fullPath)
        soundfile.write(convertedOutputPath, data, samplerate)


        # converting!
        # mp4_to_mp3(fullPath, convertedOutputPath)

        # # Opening video of file
        # video = VideoFileClip(fullPath)

        # # Outputing audio of file
        # video.audio.write_audiofile(convertedOutputPath)

    else:
        print(f"The file {file} was not an MP4")
# video = VideoFileClip(os.path.join("path","to","movie.mp4"))
# video.audio.write_audiofile(os.path.join("path","to","movie_sound.mp3"))
