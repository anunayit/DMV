import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create random data
x = np.random.rand(50)

# Step 2: Create negative correlation
y = -x + np.random.normal(0, 0.1, 50)

# Step 3: Add an outlier
x = np.append(x, 0.2)
y = np.append(y, 2)

# Step 4: Plot scatter graph
plt.scatter(x, y)

# Labels and title
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Negative correlation with outlier")

# Show graph
plt.show()
