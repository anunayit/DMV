import matplotlib.pyplot as plt

# Given dataset
weights = [25, 28, 29, 29, 30, 34, 35, 35, 37, 38]

# Create boxplot
plt.boxplot(weights)

# Add labels and title
plt.xlabel("Weights (grams)")
plt.title("Box plot of box weights")

# Display the plot
plt.show()
