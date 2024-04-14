# filename: scatter.py 
import numpy as np
import matplotlib.pyplot as plt

# generate random data
x = np.random.randn(100)
y = np.random.randn(100)

# create the scatter plot
fig, ax = plt.subplots()
ax.scatter(x, y)

# save the figure as scatter.png
plt.savefig('scatter.png')