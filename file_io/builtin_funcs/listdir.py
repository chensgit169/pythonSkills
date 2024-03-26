import os

data_dir = os.getcwd()

for filename in os.listdir(data_dir):
    print(filename)
