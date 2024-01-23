import cv2
import sys
import time
import playsound
import threading

path = 'datafile/bad_apple.mp4'
frame_interval = 1.0 / 30.75 # second / frame

class AudioThread(threading.Thread):
    def run(self):
        playsound.playsound("datafile/bad-apple-audio.mp3")

class VideoThread(threading.Thread):
    def run(self):
        anime_str = []

        cap = cv2.VideoCapture(path)
        if not cap.isOpened(): # determine whether video is read
            print(f'Error: Cannot open the video from: {path}')
            exit()

        cnt = 0
        print('\033[2J') # clear terminal
        while True:
            # if video cannot be captured, loop break
            ret, frame = cap.read()
            if not ret:
                print(f'Error: Cannot recieve frame from: {path}')
                break

            frame = cv2.resize(frame, (90, 30)) # resize the frame
            img = ANSI_generator(frame) # convert each to frame strings from a list
            anime_str.append(img) # put every string in a list

            print(f'\033[HProcessing: {round(cnt / 6571 * 100, 1)}%') # display processing percentage
            cnt += 1

        cap.release() # release resources from memory

        audio_thread.start() # start music when video is full processed
        print('\033[2JPlaying bad_apple_ANSIVer.py')
        for frame in anime_str:
            # because print() and sys.stdout.write() may cause delay
            # it's necessary to compute delay time
            start_time = time.time()

            print('\033[H') # move the cursor to the upper-left corner of the screen
            sys.stdout.write(''.join(frame))

            compute_delay = float(time.time() - start_time)
            delay_duration = frame_interval - compute_delay # compute delay duration
            if delay_duration < 0:
                delay_duration = 0
            time.sleep(delay_duration) # make it sleep in order to maintain fps

def ANSI_generator(image_frame):
    height, width, chennels = image_frame.shape # get the frame shape
    str = []
    for y in range(0, height):
        pre_r, pre_g, pre_b = image_frame[y][0]
        str.append(f'\033[48;2;{pre_r};{pre_g};{pre_b}m')
        for x in range(0, width):
            r, g, b = image_frame[y][x] # get r, g, b from every frame
            str.append(f'\033[48;2;{r};{g};{b}m ' if r != pre_r or g != pre_g or b != pre_b else ' ')
            pre_r, pre_g, pre_b = r, g, b
        str.append('\033[0m\n')
    return str

audio_thread = AudioThread(name = "Audio Thread")
video_thread = VideoThread(name = "Video Thread")
video_thread.start()