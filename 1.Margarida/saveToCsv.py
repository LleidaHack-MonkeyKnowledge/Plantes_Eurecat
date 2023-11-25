import csv
import numpy as np
import pandas as pd
import json

csvfile = None
writer = None

def MessageToCsv(msg: str):
    # Converting JSON data to a pandas DataFrame
    df = pd.json_normalize(json.loads(msg))
    
    # Writing DataFrame to a CSV file
    #df.to_csv("1.Margarida/data.csv", index=False)

    #global writer
    #writer.writerows(df.to_csv())


def init():
    #Open file
    global csvfile
    csvfile = open('1.Margarida/data/data.csv', 'w', newline='', encoding='utf-8')

    #Setup writer
    global writer
    writer = csv.writer(csvfile)

def close():
    csvfile.close()