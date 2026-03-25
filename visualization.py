import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load matrix
matrix = pd.read_csv("interaction_matrix.csv", index_col=0)

# Plot heatmap
sns.heatmap(matrix, annot=True, cmap="coolwarm")
plt.title("User-Item Interaction Matrix Heatmap")
plt.show()