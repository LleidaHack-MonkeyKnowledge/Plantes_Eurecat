import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('3.Bambu/train.csv')

# Extract the data for the x and y axes
x = df['date']
y = df['temperature']

# Create the graph
plt.bar(x, y)

# Add labels and title to the graph
plt.xlabel('Date')
plt.ylabel('Y Label')
plt.title('Bar Graph Title')

# Show the graph
plt.show()