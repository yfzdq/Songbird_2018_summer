# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
from pydub import AudioSegment as seg
import matplotlib.pyplot as plt

def large_file_split(file_size, audio_file)
    
    
#global cpnstants
SIZE_LIMIT = 80000000

    
#read file
print sys.argv[1]
sound = seg.from_file(sys.argv[1])
#loudness = sound.dBFS



file_size = os.path.getsize(sys.argv[1])
#print(str(float(("%0.2f"%(file_size / 1000000)))) + " mb")
if (file_size > SIZE_LIMIT):
    print("file is too big for a single graph")
    
    #exit(1)

#get wavfile info
frame_count = np.floor(sound.frame_count())
frame_rate = sound.frame_rate
print(frame_count, frame_rate)
duration = np.floor(frame_count / frame_rate)

#prepare for plotting
plot_unit = round((duration / 30),2)
x_label = np.linspace(0, duration, frame_count)

raw = sound.get_array_of_samples()
#print(raw)
plt.figure(1, (16,10))
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.plot(x_label, raw)
file_name = sys.argv[1][:-3] + ".png"
plt.savefig(file_name)


    