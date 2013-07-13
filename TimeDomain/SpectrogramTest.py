'''
Created on May 18, 2013
@author: Bill Xia

Audio signal processing in time domain: Drawing Spectrogram.

References: 
    Audio Signal Processing and Recognition lecture by Roger Jang:
     http://neural.cs.nthu.edu.tw/jang/books/audiosignalprocessing/
     basicFeatureTimber.asp?title=5-5%20Timbre
'''

import wave
import numpy as np
import matplotlib.pyplot as plt

fw = wave.open('aeiou.wav','r')
soundInfo = fw.readframes(-1)
soundInfo = np.fromstring(soundInfo,np.int16)
f = fw.getframerate()
fw.close()

plt.subplot(211)
plt.plot(soundInfo)
plt.ylabel('Amplitude')
plt.title('Wave from and spectrogram of aeiou.wav')

plt.subplot(212)
plt.specgram(soundInfo,Fs = f, scale_by_freq = True, sides = 'default')
plt.ylabel('Frequency')
plt.xlabel('time(seconds)')
plt.show()