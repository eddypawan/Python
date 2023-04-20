import pandas as pd
import matplotlib.pyplot as plt

# Load data into a pandas DataFrame
#data = pd.read_csv('G:\Python\pythonRepo\Python\Files\pandaVisual.xlsx')
data = pd.read_csv('G:\Python\pythonRepo\Python\Files\pandaVisual.csv', encoding='iso-8859-1')

# Create a line plot of the data
#plt.plot(data['x'], data['y'])

# Create a DataFrame
#data = {'col1': [1, 2, 3, 4, 5], 'col2': [2, 4, 6, 8, 10], 'col3': [1, 3, 5, 7, 9], 'col4': [10, 9, 8, 7, 6], 'col5': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# Plot the DataFrame using pandas plot() function
df.plot()

# Set the axis labels and title
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Title of the plot')

# Display the plot
plt.show()
