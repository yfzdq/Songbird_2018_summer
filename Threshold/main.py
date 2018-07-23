import averaging
from pydub import AudioSegment as seg
from scipy.io import wavfile
import sys
import numpy as np
import audio_split as sli
import hmm_trainer
import os
import re


# used to sort the slice files
def sorted_aphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

if __name__ == "__main__":
    
    # get the name of file that needs to be analyzed
    file_name = sys.argv[1]
    
    # read the .wav file 
    sample_rate, raw_data = wavfile.read(sys.argv[1])
    print(sample_rate)
        
    # parameters 
    # (sampling accuracy: how many samples we use to find a local max,
    # raw_data,
    # threshold: user customizable,
    # active window time: the time of silence takes to turn off active,
    # sample rate)
    # sampling accuracy affects plot 1, active window time and threshold
    # affect plot 2
    compression, threshold, marker = averaging.wav_parse(441, raw_data, 6000, 1.5, sample_rate)
   
    # write the activity markers to a txt file
    f = open('markers.txt', 'w')
    for ele in marker:
        f.write(str(ele) + '\n')
    f.close()
    
    # get wavfile info
    sound = seg.from_file(sys.argv[1])
    frame_count = sound.frame_count()
    frame_rate = sound.frame_rate
    duration = np.floor(frame_count / frame_rate)
    print(duration,len(raw_data),len(compression), len(threshold))
    
    averaging.plot_results(compression, threshold, duration, 7000, file_name)
    
    sli.slice_audio(file_name, marker)    
    # print("you got here")    
    sub_path = os.path.join(os.getcwd(), 'slices')
    print(sub_path)
    f = open('result.txt', 'w')
    f_list = sorted_aphanumeric(os.listdir(sub_path))
    print f_list
    for file_name in f_list:
        file_name = 'slices/' + file_name
        sub_path = os.path.join(os.getcwd(), file_name)
        result = hmm_trainer.hmm_classify(sub_path, 'birdx_model', False)
        f.write(file_name + '[')
        
        for ele in result[0]:
            f.write(str(ele) + ' ')
        #if 0 in result[0]:
            #f.write("has birdx")
        #else:
            #f.write("has no birdx")
        f.write('] \n')
       
    f.close()

'''
    import cPickle
    fo = open("Crow_model", "rb")
    hmm = cPickle.load(fo)
    classesAll = cPickle.load(fo)
    mtWin = cPickle.load(fo)
    mtStep = cPickle.load(fo)
    print (classesAll)
    print(hmm)
'''