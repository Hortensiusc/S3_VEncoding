# Carlos Hortensius U150010

# Seminar 3 Video Encoding Systems

import subprocess


class Seminar3:
    def __init__(self, video):
        self.video = video

    def convert_vp8(self):
        cmd = 'ffmpeg -i %s -c:v libvpx -b:v 1M -c:a libvorbis codecvp8.webm' % self.video
        subprocess.call(cmd, shell=True)

    def convert_vp9(self):
        cmd = 'ffmpeg -i %s -c:v libvpx-vp9 codecvp9.mp4' % self.video
        subprocess.call(cmd, shell=True)

    def convert_h265(self):
        cmd = 'ffmpeg -i %s -c:v libx265 codech265.mp4' % self.video
        subprocess.call(cmd, shell=True)

    def convert_av1(self):
        cmd = 'ffmpeg -i %s -c:v libaom-av1 codecav1.mp4' % self.video
        subprocess.call(cmd, shell=True)

    def mosaico(self):
        cmd = 'ffmpeg -i codecvp8.webm -i codecvp9.mp4 -i  codech265.mp4 -i codecav1.mp4 -filter_complex '
        subprocess.call(cmd, shell=True)
