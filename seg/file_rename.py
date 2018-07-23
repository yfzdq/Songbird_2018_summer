import os

filecount = 0

os.chdir(os.getcwd() + "/Crow_train")
print os.getcwd()

print os.listdir(".")

for filename in os.listdir("."):
    print filename, filecount
    old_name = filename
    print old_name
    new_name = "crow_" + str(filecount) + ".wav"
    os.rename(old_name, new_name)
    filecount = filecount + 1
