from pytube import YouTube
import os
import requests
import sys

# Test if given path is valid
def test_for_valid_path(path):
    if(os.path.exists(path) == True):
        return True
    else:
        return False

# Test if given resolution is valid
def test_for_valid_res(res, resolutions):
    if(resolutions.count(res) < 1):
        return False
    else:
        return True

# Test if given url is valid
def test_for_valid_url(url):
    request = requests.get(url)
    if(request.status_code == 200):
        return True
    else:
        return False

# Download progress bar
def progress_function(chunk, file_handle, bytes_remaining):
    global filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()

# test filename format, if incorrect add correct filetype to the end of the name
def test_for_filename_format(filename):
    filetype_check = filename[-4:]
    if(filetype_check != ".mp4"):
        filename += ".mp4"
        return filename
    else:
        return filename

# Ask for video url
while True:
    video_link = input("Enter youtube video url: ")
    if(test_for_valid_url(video_link) == True):
        break
    else:
        pass

# Create youtube object
yt = YouTube(video_link, on_progress_callback=progress_function)

# Filter for progressive and mp4 format videos
resolutions = [stream.resolution for stream in yt.streams.filter(progressive=True, file_extension='mp4')]

# List available resolutions
print("Available resolutions:\n")
print("----------------------")
for res in resolutions:
    print(res)
print("----------------------")

# Ask for wanted resolution
while True:
    userinput_resolution = input("\nInput wanted resolution: ")
    if(test_for_valid_res(userinput_resolution, resolutions) == True):
        break
    else:
        print("\nError: Resolution input was not valid")

# Ask for download path
while True:
    userinput_path = input("\n" + r"Enter download path in format C:\Users\User\Downloads" + "\n")
    if(test_for_valid_path(userinput_path) == True):
        break
    else:
        print("\nError: Path input was not valid")
        pass

# Ask what name the video will be saved as
userinput_filename = input("\nEnter Filename in format Example.mp4:\n")
userinput_filename = test_for_filename_format(userinput_filename)

# filesize for progress bar use
filesize = yt.streams.filter(progressive=True, file_extension='mp4', resolution=userinput_resolution).first().filesize

# Filter for inputted resolution and download
print("\nStarting download\n")

# Inititate download
yt.streams.filter(progressive=True, file_extension='mp4', resolution=userinput_resolution).first().download(output_path=userinput_path, filename=userinput_filename)

print("\n\nDownload complete\n")
os.system("pause")