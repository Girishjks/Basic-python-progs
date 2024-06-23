# Write a python program to create a ZIP file of a particular folder which contains several files inside it. 
import os
import sys
import pathlib
import zipfile
dirName = input("Enter Directory name that you want to backup : ")
if not os.path.isdir(dirName):
    print("Directory", dirName, "doesn't exists")
    sys.exit(0)
curDirectory = pathlib.Path(dirName)
with zipfile.ZipFile("C:\\Users\\sindh\\OneDrive\\Desktop\\ex.zip", mode="w") as f:
    for file_path in curDirectory.rglob("*"):
        f.write(file_path, arcname=file_path.relative_to(curDirectory))
    print(file_path)
    if os.path.isfile("C:\\Users\\sindh\\OneDrive\\Desktop\\ex.zip"):
        print("Archive", "myZip.zip", "created successfully")
    else:
        print("Error in creating zip archive")
