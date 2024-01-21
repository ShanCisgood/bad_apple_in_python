import cv2
import sys
import time
import playsound
import threading
import os

path = 'datafile/bad_apple.mp4'
frame_interval = 1.0 / 30.75

class AudioThread(threading.Thread):
    def run(self):
        playsound.playsound("datafile/bad-apple-audio.mp3")

class VideoThread(threading.Thread):
    def run(self):
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            print(f'Error: Cannot open the video from: {path}')
            exit()

        os.system("cls")
        print('Playing bad_apple.py: ')
        #cnt = 0
        while True:
            start_time = time.time()
            ret, frame = cap.read()
            if not ret:
                print(f'Error: Cannot recieve frame from: {path}')
                break
            frame = cv2.resize(frame, (125, 40))
            img = binary_generator(frame)
            print('\033[H')
            sys.stdout.write(img)
            
            compute_delay = float(time.time() - start_time)
            delay_duration = frame_interval - compute_delay
            if delay_duration < 0:
                delay_duration = 0
            time.sleep(delay_duration)

        cap.release()

def binary_generator(image_frame):
    image_frame = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY) # convert to grayscale
    height, width = image_frame.shape
    str = "               "
    
    for y in range(0, height):
        for x in range(0, width):
            str += '0' if image_frame[y, x] == 0 else ' '
        str += '\n               '
    return str

audio_thread = AudioThread(name = "Audio Thread")
video_thread = VideoThread(name = "Video Thread")
audio_thread.start()
video_thread.start()