import cv2
import sys
import time
import playsound
import threading

path = 'datafile/bad_apple.mp4'
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
        print('\033[2J')
        while True:
            
            ret, frame = cap.read()
            if not ret:
                print(f'Error: Cannot recieve frame from: {path}')
                break
            frame = cv2.resize(frame, (90, 30))
            img = ANSI_generator(frame)
            anime_str.append(img)
            print(f'\033[HProcessing: {round(cnt / 6571 * 100, 1)}%')
            cnt += 1
        cap.release()

        audio_thread.start()
        print('\033[2JPlaying bad_apple_ANSIVer.py')
        for frame in anime_str:
            start_time = time.time()
            print('\033[H')
            sys.stdout.write(''.join(frame))
            compute_delay = float(time.time() - start_time)
            delay_duration = frame_interval - compute_delay
            if delay_duration < 0:
                delay_duration = 0
            time.sleep(delay_duration)

def ANSI_generator(image_frame):
    height, width, chennels = image_frame.shape
    str = []
    for y in range(0, height):
        pre_r, pre_g, pre_b = image_frame[y][0]
        str.append(f'\033[48;2;{pre_r};{pre_g};{pre_b}m')
        for x in range(0, width):
            r, g, b = image_frame[y][x]
            str.append(f'\033[48;2;{r};{g};{b}m ' if r != pre_r or g != pre_g or b != pre_b else ' ')
            pre_r, pre_g, pre_b = r, g, b
        str.append('\033[0m\n')
    return str

audio_thread = AudioThread(name = "Audio Thread")
video_thread = VideoThread(name = "Video Thread")
video_thread.start()