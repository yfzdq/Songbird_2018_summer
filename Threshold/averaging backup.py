import numpy as np
from pydub import AudioSegment as seg
from scipy.io import wavfile
import matplotlib.pyplot as plt

'''
plot the compressing and thresholding results and save the output to .png 
'''
def plot_results(compression, threshold, duration, file_name):
    # x_axis labels for sub graph 1 and 2
    x_label = np.linspace(0, duration, len(compression))
    x2_label = np.linspace(0, duration, len(threshold))
    
    negative_compression = np.negative(compression)
    
    plt.rc('font', size=24)  
    plt.figure(figsize=(32,20))
    plt.plot([1,2,3])

    # 1st subplot, averaged amplitude
    plt.subplot(211)
    #fig, ax = plt.subplots(
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.plot(x_label, compression,'b|', x_label, negative_compression,'b|')
    # threshold line
    plt.hlines(y=6000, xmin=0, xmax=duration, linewidth=2, color='r')

    # 2nd subplot, thresholded
    plt.subplot(212)
    plt.ylim(-0.2, 1.2)
    plt.ylabel("Activity")
    plt.xlabel("Time")
    plt.plot(x2_label, threshold,'b')
    
    new_file_name = file_name[:-3] + "png"
    plt.savefig(new_file_name)

''' 
parsing the .wav file and output three arrays containing thresholding & compressing
results
# window time is in seconds,
# sample_rate = number of sameples in 1 second
# sampling_accuracy is number of samples
# threshold unit unknown
'''
def wav_parse(sampling_accuracy, raw_data, threshold, window_time, sample_rate):
    
    #starting helper var
    counter = 0
    maximum = 0
    # if inactivity_marker = 0, it means a window is open
    window_size = sample_rate * window_time
    inactivity_marker = window_size
    
    # return array
    compressed_arr = np.arange(len(raw_data) / sampling_accuracy)
    threshold_arr = np.arange(len(raw_data))
    marker_arr = []
    
    # initiate array counters
    # threshold array counter
    t_counter = 0
    # compression array counter
    c_counter = 0
    
    for element in raw_data:    
        # parse and find the maximum in a suite
        if counter < sampling_accuracy:
            counter += 1
            
            if element > maximum:
                maximum = element
            
            # active (above threshold)
            if element > threshold:
                # add an activity to the output
                # start a window
                #print(t_counter)
                threshold_arr[t_counter] = 1
                if t_counter > 0:
                    if threshold_arr[t_counter - 1] == 0:
                        marker_arr.append(t_counter)
                inactivity_marker = 0
                t_counter += 1
                
                
            # inactive (below threshold)
            else:
                inactivity_marker += 1
                # if inactive for more than window_size time, start marking 
                # inactivity 
                if inactivity_marker >= window_size:
                    threshold_arr[t_counter] = 0
                    if t_counter > 0:
                        if threshold_arr[t_counter - 1] == 1:
                            marker_arr.append(t_counter)
                    t_counter += 1
                # if inactive not long enough, maintain active status 
                else:
                    threshold_arr[t_counter] = 1
                    t_counter += 1
        # resetting the maximum every suite, record the maximum in the
        # output compressed array
        else:
            #print(counter)
            compressed_arr[c_counter] = maximum
            c_counter += 1
            maximum = 0
            counter = 0

    return compressed_arr, threshold_arr, marker_arr





