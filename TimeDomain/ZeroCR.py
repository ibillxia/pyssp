'''
Created on May 15, 2013
@author: Bill Xia

Audio signal processing in time domain: Zero-Crossing Rate calculation.

References: 
    Audio Signal Processing and Recognition lecture by Roger Jang:
     http://neural.cs.nthu.edu.tw/jang/books/audiosignalprocessing/
     basicFeatureZeroCrossingRate.asp?title=5-3%20Zero%20Crossing%20Rate
'''

import math
import numpy as np

def ZeroCR(waveData,frameSize,overLap):
    wlen = len(waveData)
    step = frameSize - overLap
    frameNum = int(math.ceil(wlen*1.0/step))
    zcr = np.zeros((frameNum,1))
    for i in range(frameNum):
        curFrame = waveData[np.arange(i*step,min(i*step+frameSize,wlen))]
        #To avoid DC bias, usually we need to perform mean subtraction on each frame
        curFrame = curFrame - np.mean(curFrame) # zero-justified
        zcr[i] = sum(curFrame[0:-1]*curFrame[1::]<=0)
    return zcr
