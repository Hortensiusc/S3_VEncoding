# Carlos Hortensius U150010

# Seminar 3 Video Encoding Systems

from class_definition import *

print('Welcome to practice 3, which video do you want to prove with different codecs?')
print('1- 720p')
print('2- 480p')
print('3- 360x240')
print('4- 160x120')


while True:
    option = int(input())

    if option == 1:
        video = 'BBB720p.mp4'
        break
    elif option == 2:
        video = 'BBB480p.mp4'
        break
    elif option == 3:
        video = 'BBB360x240.mp4'
        break
    elif option == 4:
        video = 'BBB160x120.mp4'
        break
    else:
        print('Invalid option')


video = Seminar3(video)

#video.convert_vp8()
#video.convert_vp9()
#video.convert_h265()
#video.convert_av1()

video.mosaico()

