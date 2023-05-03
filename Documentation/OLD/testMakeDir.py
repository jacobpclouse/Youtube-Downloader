import os


# Make output Folder name
convertedFolderUser = input("Enter name of output folder: ")
convertedFolderPath = f".\{convertedFolderUser}"
# Create the directory
os.mkdir(convertedFolderPath)
print("Directory '% s' created" % convertedFolderPath)