import pandas as pd

# Try this first
df = pd.read_csv("taxomany.tsv", sep="\t", skiprows=1)

print(df.shape)
print(df.head())
print(df.columns.tolist())
print(df.dtypes)