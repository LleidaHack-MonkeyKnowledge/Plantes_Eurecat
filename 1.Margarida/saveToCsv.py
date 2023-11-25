import csv
import numpy as np
import pandas as pd
import json

csvfile = None
writer = None

def MessageToCsv(msg):
    # Convert string into json
    msg = json.loads(msg)

    # Write values manually
    line = ""
    line += msg["id"] 
    line += ","
    line += str(msg["light"])
    line += ","
    line += str(msg["soil_humidity"])
    line += ","
    line += str(msg["air_humidity"])
    line += ","
    line += str(msg["temperature"])
    line += "\n"

    # Write into CSV
    csvfile.write(line)

def init():
    # Open file
    global csvfile
    csvfile = open('1.Margarida/data/data.csv', 'w', newline='', encoding='utf-8')

    # Write first line
    csvfile.write("id, light, soil_humidity, air_humidity, temperature,\n")

def close():
    csvfile.close()