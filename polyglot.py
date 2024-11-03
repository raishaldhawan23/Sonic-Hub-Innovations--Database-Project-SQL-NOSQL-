import matplotlib.pyplot as plt
import numpy as np

# creating a dataset for polygot persistance ,
np.random.seed(0)  # Seed for reproducibility
x = np.random.normal(50, 15, 100)  # Mean of 50, standard deviation of 15
y = 2 * x + np.random.normal(0, 10, 100)  # Roughly linear with some random noise

# Scatter plot
plt.figure(figsize=(10, 6))  # Size to mimic the one provided
plt.scatter(x, y, alpha=0.6, edgecolors='w', s=40)  # Alpha for slight transparency, s for size of markers
plt.title('Engagement Metrics vs. Revenue Earned')
plt.xlabel('Total Engagement')
plt.ylabel('Revenue Earned')
plt.xlim(0, 100)
plt.ylim(0, 200)  # Adjusted y-axis limit to match the distribution in the image
plt.grid(True)  # Add grid for better readability
plt.show()

