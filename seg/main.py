import hmm_trainer
import sys
import os

dir_name = sys.argv[1]
model_name = sys.argv[2]

train_folder = os.path.join(os.getcwd(), dir_name)
print(train_folder)

hmm_trainer.train(train_folder, model_name)