import numpy as np
import matplotlib.pyplot as plt

# Create empty 2D numpy array
arr = np.array([]).reshape(0,2)  

# Bivariate data  
x_data = [2, 4, 6, 8, 10]   
y_data = [100, 250, 400, 550, 700]

# Append data to array
for i in range(len(x_data)):
  arr = np.append(arr, [[x_data[i], y_data[i]]], axis=0)

# Plot scatter plot
plt.style.use('ggplot')  
fig, ax = plt.subplots()
ax.scatter(arr[:,0], arr[:,1])

# Add legend 
labels = ['Bivariate Data']
ax.legend(labels)

ax.set_title("X vs Y")
ax.set_xlabel("X Data")
ax.set_ylabel("Y Data")

plt.show()