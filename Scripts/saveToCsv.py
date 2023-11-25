import csv
import numpy as np
import pandas as pd
import json

#tabla = np.random.random((3000,14))

# Reading JSON data from a file
with open("data/data.json") as f:
    json_data = json.load(f)

# Converting JSON data to a pandas DataFrame
df = pd.read_json(json_data)

# Writing DataFrame to a CSV file
df.to_csv("data/data.csv", index=False)

#with open('data/data.csv', 'w', newline='', encoding='utf-8') as csvfile:
 #   writer = csv.writer(csvfile)
  #  writer.writerows(tabla)