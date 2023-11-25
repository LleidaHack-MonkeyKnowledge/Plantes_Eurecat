import pandas as pd
from matplotlib import pyplot as plt
import csv

str_fileName = '1.Margarida/data/data.csv'

fh = open(str_fileName)
csv_reader = csv.reader(fh)

csv_header = next(csv_reader)
csv_header

['id', 'light', 'soil_humidity', 'air_humidity', 'temperature']