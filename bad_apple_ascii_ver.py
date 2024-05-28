import cv2
import sys
import time
import playsound
import threading

path = 'datafile/bad_apple_seikai.mp4'
frame_interval = 1.0 / 24.143 # second / frame
ascii_chars = ['@', '#', '$', '%', '&', '~', '!', '?']

class AudioThread(threading.Thread):
    def run(self):
        playsound.playsound("datafile/bad_apple_seikai_audio.m4a")

class VideoThread(threading.Thread):
    def run(self):

        cap = cv2.VideoCapture(path)
        if not cap.isOpened(): # determine whether video is read
            print(f'Error: Cannot open the video from: {path}')
            exit()

        print('\033[2JPlaying bad_apple.py: ')
        
        while True:
            # because print(), sys.stdout.write() and other functions may cause delay
            # it's necessary to compute delay time
            start_time = time.time()

            # if video cannot be captured, loop break
            ret, frame = cap.read()
            if not ret:
                print(f'Error: Cannot recieve frame from: {path}')
                break

            frame = cv2.resize(frame, (200, 65)) # resize the frame
            img = binary_generator(frame) # convert each to frame strings from a list

            print('\033[H') # move the cursor to the upper-left corner of the screen
            sys.stdout.write(img)
            
            compute_delay = float(time.time() - start_time)
            delay_duration = frame_interval - compute_delay # compute delay duration
            if delay_duration < 0:
                delay_duration = 0
            time.sleep(delay_duration) # make it sleep in order to maintain fps

        cap.release()

def binary_generator(image_frame):
    image_frame = cv2.cvtColor(image_frame, cv2.COLOR_RGB2GRAY) # convert to grayscale
    height, width = image_frame.shape
    str = "               "
    
    for y in range(0, height):
        for x in range(0, width):
            str += ascii_chars[image_frame[y, x] // 32]
        str += '\n               '
    return str

audio_thread = AudioThread(name = "Audio Thread")
video_thread = VideoThread(name = "Video Thread")
audio_thread.start()
video_thread.start()