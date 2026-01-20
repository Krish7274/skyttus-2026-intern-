# Use os module to list files in a directory.
	
import os

path = "."

files = os.listdir(path)

print("Files and folders in directory:")
for file in files:
    print(file)
