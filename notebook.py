# %%
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D  # Import 3D plotting toolkit

# Load the Iris dataset
iris = load_iris()

# Convert to pandas DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Display the first few rows
print(df.head())

# %%
# Plot the data
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['species'], cmap='viridis')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Dataset')
plt.show()

# %%
# Create 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each species with a different color
scatter = ax.scatter(df['sepal length (cm)'], 
                    df['sepal width (cm)'], 
                    df['petal length (cm)'],
                    c=df['species'],
                    cmap='viridis')

# Add labels and title
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Sepal Width (cm)')
ax.set_zlabel('Petal Length (cm)')
ax.set_title('3D Scatter Plot of Iris Dataset')

# Add a color bar
plt.colorbar(scatter, label='Species')

# Add legend
legend_labels = ['Setosa', 'Versicolor', 'Virginica']
handles = [plt.Line2D([0], [0], marker='o', color='w', 
                     markerfacecolor=plt.cm.viridis(i/2.), 
                     markersize=10, label=label)
          for i, label in enumerate(legend_labels)]
ax.legend(handles=handles)

plt.show()
# %%
