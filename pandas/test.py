import pandas as pd 
reviews = pd.read_csv('.\data\wine.csv', index_col=0)
print(reviews.head())