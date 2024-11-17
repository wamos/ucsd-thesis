import matplotlib.pyplot as plt
import numpy as np

# Data for the bar plot
values = [2.04, 1.82, 1.68, 2.61]
values = np.array(values)
improvement_ratio = np.abs(1/(1-values))
print(f"{improvement_ratio}")

# Updated labels for the x-axis
labels = ['A', 'B', 'C', 'F']

# Create the bar plot with thinner bars and teal green color
plt.figure(figsize=(8, 5))
plt.bar(labels, values, color='teal', width=0.3)

# Add title and labels
#plt.title('Bar Plot Example')
plt.xlabel('YCSB Benchmarks')
plt.ylabel(r'99th Percentile Latenecy Reduction ($\times$)')

# Display the plot
name = "ycsb"
plt.savefig(f'{name}.pdf', bbox_inches='tight', dpi=600)
plt.show()