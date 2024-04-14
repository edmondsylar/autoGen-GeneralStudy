# filename: scatter_plot.py
import numpy as np
import matplotlib.pyplot as plt

# Generate random data for the plot
x = np.random.rand(50)
y = np.random.rand(50)

# Create the scatter plot
plt.scatter(x, y)

# Add labels to the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Random Scatter Plot')

# Save the plot as PNG file
plt.savefig('scatter_rand.png')