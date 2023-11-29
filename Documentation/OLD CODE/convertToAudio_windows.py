# WINDOWS ONLY
# -=-=-=-=-=-=-=-=-=-=-=-=
# Imports
# -=-=-=-=-=-=-=-=-=-=-=-=
import os
from moviepy.editor import *


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

# used to find file name only (before the extension)
def getFileName(inputFile):
    return '.' and inputFile.rsplit(".",1)[0]

# used to find ending type for file AND checking to make sure that it is an allowed type
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# convert mp4 to mp3 
def convert_video_to_audio_moviepy(video_file, outputFileName,output_ext="mp3"):
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""
    # filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{outputFileName}.{output_ext}")

# # -=-=-=-=-=-=-=-=-=-=-=-=
# # Main
# # -=-=-=-=-=-=-=-=-=-=-=-=


# Iterating over all the files
for file in l_files:
    # get input path
    fullPath = f"{folderPath}\{file}"

    # printing out values
    print(f"Incoming fullpath: {fullPath}")

    # if this is an allowed mp4, allow convert
    if allowed_file(file):

        # removing Extension
        removedExtensionFromFile = getFileName(file)
        
        # Generate output files and path
        convertedName = f'converted_{removedExtensionFromFile}'
        convertedOutputPath = f'{convertedFolderPath}\{convertedName}'

        print(f"Outgoing converted file name: {convertedName}.mp3")
        print(f"Outgoing file path: {convertedOutputPath}.mp3")

        # Converting!
        convert_video_to_audio_moviepy(fullPath,convertedOutputPath,'mp3')



    else:
        print(f"The file {file} was not an MP4")

