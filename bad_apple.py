import cv2
import sys
import time
import playsound
import threading
from PIL import Image
import os

path = 'datafile/bad_apple.mp4'
frame_size = 100

class AudioThread(threading.Thread):
    def run(self):
        playsound.playsound("datafile/bad-apple-audio.mp3")

class VideoThread(threading.Thread):
    def run(self):
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            print(f'Error: Cannot open the video from: {path}')
            exit()

        #cnt = 0
        while True:
            #os.system("cls")
            ret, frame = cap.read()
            if not ret:
                print(f'Error: Cannot recieve frame from: {path}')
                break
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #/////////////
            #cv2.imshow('frame', frame)
            frame = cv2.resize(frame, (125, 45))
            img = binary_generator(frame)
            sys.stdout.write('\r' + img)
            
            sys.stdout.flush()
            #cnt += 1
            #delay = 0.001 / 6571 * cnt + 0.03
            #time.sleep(delay)

            if cv2.waitKey(20) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


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
audio_thread.start()
video_thread.start()