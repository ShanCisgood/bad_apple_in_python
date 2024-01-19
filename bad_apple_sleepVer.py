import cv2
import sys
import time
import playsound
import threading
from PIL import Image
import os
import fpstimer

path = 'datafile/bad_apple.mp4'
frame_size = 100
frame_interval = 1.0 / 30.75

class AudioThread(threading.Thread):
    def run(self):
        playsound.playsound("datafile/bad-apple-audio.mp3")

class VideoThread(threading.Thread):
    def run(self):
        anime_str = []
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            print(f'Error: Cannot open the video from: {path}')
            exit()

        cnt = 0
        while True:
            
            ret, frame = cap.read()
            if not ret:
                print(f'Error: Cannot recieve frame from: {path}')
                break
            frame = cv2.resize(frame, (125, 45))
            img = binary_generator(frame)
            anime_str.append(img)
            os.system("cls")
            print(f'Processing: {round(cnt / 6571 * 100, 1)}%')
            cnt += 1
            
        cap.release()

        timer = fpstimer.FPSTimer(30)
        audio_thread.start()
        for frame in anime_str:
            start_time = time.time()
            os.system("cls")
            sys.stdout.write('\r' + frame)
            compute_delay = float(time.time() - start_time)
            delay_duration = frame_interval - compute_delay
            if delay_duration < 0:
                delay_duration = 0
            timer.sleep()
        # f = open('output.txt', 'w')
        # print(anime_str, file = f)
        # f.close


def pixels_to_binary(image_frame):
    height, width = image_frame.shape
    str = "               "
    
    for y in range(0, height):
        for x in range(0, width):
            if image_frame[y, x] == 0:
                str += '0'
            else:
                str += ' '
        str += '\n               '
    return str

def binary_generator(image_frame):
    image_frame = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY) # convert to grayscale
    binary_str = pixels_to_binary(image_frame)
    return binary_str

audio_thread = AudioThread(name = "Audio Thread")
video_thread = VideoThread(name = "Video Thread")

video_thread.start()