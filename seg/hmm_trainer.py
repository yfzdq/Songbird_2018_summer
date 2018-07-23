from pyAudioAnalysis import audioSegmentation as aS
import sys

'''
ARGUMENTS:
     - dirPath:        the path of the data diretory
     - hmmModelName:    the name of the HMM model to be stored
     - mtWin:        mid-term window size
     - mtStep:        mid-term window step
'''

def train(file_path, model_name):
    print ("training " + model_name)
    aS.trainHMM_fromDir(file_path, model_name, 1.0, 1.0)
    print("trained")

def main():
    print ("starting")

def hmm_classify(file_path, model_name, do_plot):
    train(file, sys.argv[2])
    print("start classifying")
    # aS.hmmSegmentation('data/field_4.wav','Field_model',True)
    aS.hmmSegmentation(file_path, model_name, do_plot)
    print("HMM Classification using " + model_name + " is done")