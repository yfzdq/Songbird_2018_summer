from pydub import AudioSegment as seg
import os


def slice_audio(file_name, marker_arr):
    pair_arr = []
    
    for i in range(len(marker_arr) - 1):
        # check if even
        if i % 2 == 0:
            pair_arr.append([marker_arr[i], marker_arr[i + 1]])
    
    # for debug
    #for ele in pair_arr:
    #    print ele
    
    # open the wav file
    full = seg.from_wav(file_name)
    # counter for new file name
    file_counter = 0
    
    directory = "/slices"
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print("directory already exists")
    #shutil.rmtree("slices")
    # parse the start/stop time marker pairs, slice the original file using
    # these as guidelines
    for ele in pair_arr:
        new_file_name = "slices/" + str(file_counter) + "_sub_" + file_name[:-4] + '.wav'
        new_path = os.path.join(os.getcwd(), new_file_name)
        t1 = ele[0] * 1000 / 44100
        t2 = ele[1] * 1000 / 44100
        print t1, t2
        print "this piece is " + str((t2 - t1) / 1000) + "s"
        newAudio = full[t1:t2]
        newAudio.export(new_path, format="wav")
        file_counter += 1

