import csv
import numpy as np
import pandas as pd
import json

#tabla = np.random.random((3000,14))

# Reading JSON data from a file

def MessageToCsv(msg):
    # Converting JSON data to a pandas DataFrame
    df = pd.read_json(msg)

    # Writing DataFrame to a CSV file
    df.to_csv("data/data.csv")
'''
with open('data/data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(tabla)'''