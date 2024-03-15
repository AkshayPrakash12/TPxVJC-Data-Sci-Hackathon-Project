import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('../Datasets/spotify-2023.csv', encoding='latin')
df['key'] = df['key'].fillna('C')
print(df['key'][12]) #empty cell 13
df['key'].info()
