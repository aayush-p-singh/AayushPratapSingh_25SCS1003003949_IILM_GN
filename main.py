import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("data.csv")

# Create interaction matrix (Species vs Habitat)
matrix = data.pivot_table(index='species', columns='habitat', values='interaction', fill_value=0)

print("Species-Habitat Interaction Matrix:\n")
print(matrix)

# Compute similarity between species
similarity = cosine_similarity(matrix)
similarity_df = pd.DataFrame(similarity, index=matrix.index, columns=matrix.index)

print("\nSpecies Similarity Matrix:\n")
print(similarity_df)

# Recommendation (habitat suggestion based on similar species)
def recommend(species):
    similar_species = similarity_df[species].sort_values(ascending=False)[1:]

    print(f"\nSimilar species ranking:\n{similar_species}\n")

    for sim_sp in similar_species.index:
        for habitat in matrix.columns:
            if matrix.loc[species][habitat] == 0 and matrix.loc[sim_sp][habitat] > 0:
                print(f"Suggested Habitat: {habitat} (based on {sim_sp})")
                return

    print("No new habitat to recommend")
# Run example
recommend("Tiger")

# Save outputs
matrix.to_csv("interaction_matrix.csv")
similarity_df.to_csv("similarity_matrix.csv")