# Carlos Hortensius U150010

# Practice 2  Video Encoding

import os
from class_definition import *



print('Welcome to Practice 2: Introduce the path where your file is located:\n')
path = input()
os.chdir(path)

print('Introduce the name of your video:')
video_to_stream = input()

video = Seminar3(video_to_stream)
video.streaming()