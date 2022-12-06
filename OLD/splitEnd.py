import os

# used to find file name only
def getFileName(inputFile):
    return '.' and inputFile.rsplit(".",1)[0]

# main
# Target Folder to open
# folderPath = '.\OLD'
folderPath = input("Give folder path that you want to list out files in: ")

# Extracting all the contents in the directory corresponding to path
l_files = os.listdir(folderPath)

# Iterating over all the files
for file in l_files:
    print(getFileName(file))