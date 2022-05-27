import csv
import os
import tensorflow as tf
import pandas as pd
from tensorflow import keras
from keras import layers

#create a file and opens it
path = "images/"
dir_list = os.listdir(path)

with open('images/imgdata.csv', 'w') as file:
    columnnames = ['file_name', 'spoon','knife','fork']
    writer = csv.DictWriter(file, fieldnames=columnnames)
    writer.writeheader()
    for x in dir_list:
        writer.writerow({'file_name':x})

#print(dir_list)