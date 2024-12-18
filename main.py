# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='diabetes', version=1, as_frame=True)
print(data.DESCR)
df = data.frame
df.sample(5)

features = df.columns
selected_features = [features[1], features[2], features[4], features[6], features[7]]

features = list(df.columns)
print("Available features:", features)
selected_features = [features[1], features[2], features[4], features[6], features[7]]
print("Selected features: ", selected_features)

reference_feature = selected_features[0]  # The reference feature
comparison_feature = selected_features[2]  # A feature to compare to

# Create a scatter plot for the selected pair
plt.figure(figsize=(8, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.8, c='yellow')
plt.xlabel(reference_feature)
plt.ylabel(comparison_feature)

# Save the plot as an image file
plt.savefig('correlation_plot.png')

plt.show()
