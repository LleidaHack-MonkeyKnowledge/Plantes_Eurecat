import csv
import numpy as np

tabla = np.random.random((3000,14))

with open('data/data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(tabla)