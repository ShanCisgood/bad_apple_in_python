# Bad Apple in Python
The summer of 2023 was quite boring. Occasionally, I stumbled upon an interesting project, Bad Apple! Actually, I had seen various versions of Bad Apple videos on my YouTube again and again, and they interested me for a while. So, for my summer project, I decided to play Bad Apple on my PC, but in the console!

[Watch the viedo](https://www.youtube.com/watch?v=GkBC2aJ_PUQ)
[![Watch the viedo](https://github.com/ShanCisgood/bad_apple_in_python/blob/main/datafile/badapplepic.png)](https://www.youtube.com/watch?v=GkBC2aJ_PUQ)

## Prerequisites
- opencv-python
- playsound
- threading

## Files on this repository
- `bad_apple.py`: the original version, only '0', '1' and ' '
- `bad_apple_ascii_ver.py`: print pixels in ASCII chars
- `bad_apple_ANSIVer.py`: using ANSI escape codes to print black and white
- `lazy_text.txt`: every frames in Bad Apple, use it if your PC is too lazy to process these videos

## How to run these code?
1. Download this repo in ZIP and unzip it in your PC.
2. Open your console and resize your console frame.
3. Run either `bad_apple.py` or `bad_apple_ascii_ver.py` or `bad_apple_ANSIVer.py`.
4. Enjoy.

~~If you want to stop, just close your console brutally.~~

## Print other videos
You can change to print other videos by changing dir in the code:
```py
path = 'datafile/bad_apple_seikai.mp4'
```
But remember to change frame size if the video has different size:
```py
frame = cv2.resize(frame, (200, 65)) # resize the frame
img = binary_generator(frame) # convert each to frame strings from a list
```

## Some discoveries
- ANSI escape codes are so cool!!
- Bad Apple video is not made by only two colors, actually it is gradient.

## License
[MIT LICENSE](https://github.com/ShanCisgood/bad_apple_in_python/blob/main/LICENSE)

## About this repository

- The arthur of this repo: [ShanC](https://github.com/ShanCisgood)
- The original videos: [Bad Apple!!](https://www.nicovideo.jp/watch/sm8628149), [Bad Apple!! feat.SEKAI / 25時、ナイトコードで。 × 初音ミク](https://www.youtube.com/watch?v=v-fc1zv31zE)

