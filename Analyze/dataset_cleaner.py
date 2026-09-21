import pandas as pd

# Try this first
df = pd.read_csv("./raw_dataset/Bacteria Taxonomy dataset/data/taxonomy.tsv", sep="\t", names=["Feature_ID", "Taxon", "Confidence"], header=0)


ranks = ["Domain","Phylum","Class","Order","Family","Genus","Species"]
df[ranks] = df["Taxon"].str.split(";", expand=True)

print(df["Phylum"].value_counts().head(15))

print(df["Species"].isna().sum(), "ASVs unresolved to species")

print(df["Confidence"].describe())