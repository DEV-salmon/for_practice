import numpy as np
import scipy.io.wavfile 
import matplotlib.pyplot as pli
import random
samplerate = 40000
k = input("계이름 -> ")
k = k.split()
data=np.array([])
amplitude = np.linspace(20000, 32767, 20000)
amplitude = np.append(amplitude, np.linspace(32767, 20000, 20000))
for i in k:
    if i == 'C':
        fs = 262
        t = np.linspace(0 , 1, samplerate)
        tempo=amplitude * np.sin(2. * np.pi * fs *t)
        data = np.append(data,tempo)
        data = np.append(data, [i*0 for i in range(0,50)])

    elif i == 'C#' or i == 'DP':
        fs = 278
        t = np.linspace(0 , 1, samplerate)
        tempo=amplitude * np.sin(2. * np.pi * fs *t)
        data = np.append(data,tempo)
        data = np.append(data, [i*0 for i in range(0,50)])
    elif i == 'D':
        fs = 294
        t = np.linspace(0 , 1, samplerate)
        tempo=amplitude * np.sin(2. * np.pi * fs *t)
        data = np.append(data,tempo)
        data = np.append(data, [i*0 for i in range(0,50)])
    elif i == 'D#' or i == 'DP':
        fs = 311
        t = np.linspace(0 , 1, samplerate)
        tempo=amplitude * np.sin(2. * np.pi * fs *t)
        data = np.append(data,tempo)
        data = np.append(data, [i*0 for i in range(0,50)])
    elif i == 'E':
        fs = 330
        t = np.linspace(0 , 1, samplerate)
        tempo=amplitude * np.sin(2. * np.pi * fs *t)
        data = np.append(data,tempo)
        data = np.append(data, [i*0 for i in range(0,50)])
    elif i == 'F':
        fs = 349
        t = np.linspace(0 , 1, samplerate)
        tempo=amplitude * np.sin(2. * np.pi * fs *t)
        data = np.append(data,tempo)
        data = np.append(data, [i*0 for i in range(0,50)])
    elif i == 'F#' or i == 'FP':
        fs = 370
        t = np.linspace(0 , 1, samplerate)
        tempo=amplitude * np.sin(2. * np.pi * fs *t)
        data = np.append(data,tempo)
        data = np.append(data, [i*0 for i in range(0,50)])
    elif i == 'G':
        fs = 392
        t = np.linspace(0 , 1, samplerate)
        tempo=amplitude * np.sin(2. * np.pi * fs *t)
        data = np.append(data,tempo)
        data = np.append(data, [i*0 for i in range(0,50)])
    elif i == 'G#'or i == 'AP':
        fs = 415
        t = np.linspace(0 , 1, samplerate)
        tempo=amplitude * np.sin(2. * np.pi * fs *t)
        data = np.append(data,tempo)
        data = np.append(data, [i*0 for i in range(0,50)])
    elif i == 'A':
        fs = 440
        t = np.linspace(0 , 1, samplerate)
        tempo=amplitude * np.sin(2. * np.pi * fs *t)
        data = np.append(data,tempo)
        data = np.append(data, [i*0 for i in range(0,50)])
    elif i == 'A#' or i == 'BP':
        fs = 466
        t = np.linspace(0 , 1, samplerate)
        tempo=amplitude * np.sin(2. * np.pi * fs *t)
        data = np.append(data,tempo)
        data = np.append(data, [i*0 for i in range(0,50)])
    elif i == 'B':
        fs = 494
        t = np.linspace(0 , 1, samplerate)
        tempo=amplitude * np.sin(2. * np.pi * fs *t)
        data = np.append(data,tempo)
        data = np.append(data, [i*0 for i in range(0,50)])
    elif i == 'C5':
        fs = 523
        t = np.linspace(0 , 1, samplerate)
        tempo=amplitude * np.sin(2. * np.pi * fs *t)
        data = np.append(data,tempo)
        data = np.append(data, [i*0 for i in range(0,50)])


scipy.io.wavfile.write("mathproject.wav", samplerate, data.astype(np.int16))