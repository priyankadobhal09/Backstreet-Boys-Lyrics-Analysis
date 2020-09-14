import json
import requests
import pandas as pd
from pandas import ExcelWriter
import xlsxwriter
import numpy as np

excel_file = 'Backstreet_Boys_Lyrics.xlsx'
xls_file = pd.ExcelFile(excel_file)
df = xls_file.parse('Lyrics')
print(type(df))
rows = df.shape[0]
print(rows)
artist = "Backstreet Boys"
lyrics_list = []


df['Lyrics'] = df['Lyrics'].str.replace("\n", " ")

print(df)
new_df = pd.DataFrame(df.Lyrics.str.split(' ').tolist(), index=df.Title).stack()

print(new_df)

new_df = new_df.reset_index([0, 'Title'])
print(new_df)

new_df.columns = ['Title', 'Words']

print(new_df)

df_songs = pd.merge(df, new_df, on='Title', how='inner')

print(df_songs)

list = ['.', ',', '"', '?', "!", '(', ')', '2x', '<', '*']

for i in list:

    df_songs['Words'] = df_songs['Words'].str.replace(i, "")
    print(df_songs)

df_songs.dropna()

print(df_songs)

writer = ExcelWriter('Backstreet_Boys_Lyrics_words.xlsx',engine='xlsxwriter')
df_songs.to_excel(writer,sheet_name='Lyrics')
writer.save()

print("Saved to file")
