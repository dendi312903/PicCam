from tkinter import *
from tkinter import filedialog
import sounddevice as sd
import numpy as np
import os

SAMPLE_RATE = 44100
THRESHOLD = 0.5
# Само окно
root = Tk()
root.title('PicCam by dendi31')
root.geometry('700x600')
root.resizable(0, 0)
def change(xc):
    global THRESHOLD
    THRESHOLD = float(xc)


# Фото в проге
bp = os.path.dirname(os.path.abspath(__file__))
img_silence = os.path.join(bp, 'pictures', '1.png')
img_loud = os.path.join(bp, 'pictures', '2.png')
image1 = PhotoImage(file = img_silence)
image = PhotoImage(file = img_loud)
label = Label(image=image1)
label.place(x=-3, y=-5)

# Реакция на звук
def audio_callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata)
    if volume_norm > THRESHOLD:
        label.config(image=image)
    else:
        label.config(image=image1)

slider = Scale(root, length=100 ,command=change, orient=VERTICAL, from_=0.0, to=2.0, resolution=0.05)
slider.set(THRESHOLD)
slider.place(x=0, y=500)

stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLE_RATE)
stream.start()

root.mainloop()
