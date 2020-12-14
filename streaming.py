# Carlos Hortensius U150010

# Seminar 3  Video Encoding

import os
from class_definition import *



print('Welcome to Practice 2: Introduce the path where your file is located:\n')
path = input()
os.chdir(path)

print('Introduce the name of your video:')
video_to_stream = input()

# I tried to have the two commands executed at the same time in two different terminals,
# but I did not succeed

video = Seminar3(video_to_stream)
video.streaming()