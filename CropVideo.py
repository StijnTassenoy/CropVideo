import os
import subprocess
from cv2 import cv2

def getAllVideos(extension):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        if not file.endswith(extension):
            files.remove(file)
    return files        


extension_type = input("Enter extension type: ")
cut_from_top = input("How much from top?: ")
cut_from_bottom = input("How much from bottom?: ")
cut_from_left = input("How much from left?: ")
cut_from_right = input("How much from right?: ")
allvids = getAllVideos(extension_type)

try:
    for i in range(0, len(allvids)):
        print(allvids[i])
        vid = cv2.VideoCapture(allvids[i])
        height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        width -= int(cut_from_left)
        width -= int(cut_from_right)
        episode = allvids[i][:-len(extension_type)-1]+"_cropped."+extension_type
        downside = str(float(height)-float(cut_from_bottom)-float(cut_from_top))[:-2]
        #? input(f"w={str(width)[:-2]} h={downside} x={cut_from_left} y={cut_from_top}")
        subprocess.call(["ffmpeg", "-i", allvids[i], "-vf", "crop="+str(width)[:-2]+":"+downside+":" + cut_from_left + ":"+cut_from_top, "-c:v", "libx264", "-crf", "0", "-c:a", "copy", episode])
except:
    print("Couldn't find")
