import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('../Datasets/spotify-2023.csv', encoding='latin')
df['in_shazam_charts'] = pd.to_numeric(df['in_shazam_charts'], errors='coerce')
df['in_shazam_charts'].fillna(-1, inplace=True) #fill to change later
mask = df['in_shazam_charts'] != 0 #excludes 0 to find median
mask = df[mask] != -1 #excludes -1 to find median
filtered_df = df[mask] # initialise masked df to filtered df var
median_value = filtered_df['in_shazam_charts'].median(numeric_only=True)
df['in_shazam_charts'] = df['in_shazam_charts'].replace(-1,median_value)

print(df['in_shazam_charts'][14]) #empty cell for testing
print(df['in_shazam_charts'][54]) #empty cell for testing
print(median_value)
df['in_shazam_charts'].info()


# in_shazam_charts


#0   track_name            952 non-null    object
# 1   artist(s)_name        952 non-null    object
# 2   artist_count          952 non-null    int64
# 3   released_year         952 non-null    int64
# 4   released_month        952 non-null    int64
# 5   released_day          952 non-null    int64
# 6   in_spotify_playlists  952 non-null    int64
# 7   in_spotify_charts     952 non-null    int64
# 8   streams               952 non-null    int64
# 9   in_apple_playlists    952 non-null    int64
# 10  in_apple_charts       952 non-null    int64
# 11  in_deezer_playlists   952 non-null    object
# 12  in_deezer_charts      952 non-null    int64
# 13  in_shazam_charts      902 non-null    object
# 14  bpm                   952 non-null    int64
# 15  key                   857 non-null    object
# 16  mode                  952 non-null    object
# 17  danceability_%        952 non-null    int64
# 18  valence_%             952 non-null    int64
# 19  energy_%              952 non-null    int64
# 20  acousticness_%        952 non-null    int64
# 21  instrumentalness_%    952 non-null    int64
# 22  liveness_%            952 non-null    int64
# 23  speechiness_%         952 non-null    int64