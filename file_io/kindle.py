# Copy kindle 'My clippings.txt' to windows desktop
# Python runtime environment: 3.6.3
# NOTE: Noly for windows platform.

import os
import string
from win32api import GetVolumeInformation  # Need pypiwin32 module
from ctypes import windll
from shutil import copy

# String comparasion with case-insensive.
def iequal(a, b):
    try:
        return a.upper() == b.upper()
    except AttributeError:
        return a == b

# Get a list of all driver names, such as [ 'C:\\', 'D:\\', 'E:\\' ]
def get_available_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter + ":\\")
        bitmask >>= 1
    return drives

# Get volume label and must specify path, such as C:\\ or D:\\
def get_volume_label(path):
    return GetVolumeInformation(path)[0]

# Passing volume label name and return the driver name
def has_volume_label(name):
    drivers = get_available_drives()
    for driver in drivers:
        if iequal(get_volume_label(driver), name):
            return driver
    return ""

# Get desktop fullpath: C:\users\pingsoli\Desktop
def get_desktop_path():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def copy_kindle_clips_to_desktop():
    kindle_driver = has_volume_label('kindle')
    if not kindle_driver: return

    kindle_clips_path = kindle_driver + "\\documents\\My Clippings.txt"
    if os.path.exists(kindle_clips_path) == False: return

    desktop_path = get_desktop_path()

    # Copy clips to desktop
    copy(kindle_clips_path, desktop_path)

    # Remove kindle clips from the kindle device 
    os.remove(kindle_clips_path)

if __name__ == '__main__':
    copy_kindle_clips_to_desktop()
