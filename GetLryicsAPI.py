import json
import requests
import pandas as pd
from pandas import ExcelWriter
import xlsxwriter

excel_file = "Backstreet_Boys.xlsx'
xls_file = pd.ExcelFile(excel_file)
df = xls_file.parse('List')
print(type(df))
rows = df.shape[0]
print(rows)
artist = "Backstreet Boys"
lyrics_list = []
for i in range(0, rows):
    song_title = ""
    song_title = df.iloc[i]['Title']
    print(i)
    url = 'https://api.lyrics.ovh/v1/' + artist + '/' + song_title
    print('https://api.lyrics.ovh/v1/' + artist + '/' + song_title)
    response = requests.get(url)
    json_data = json.loads(response.content)
    lyric = json_data['lyrics']
    lyrics_list.append(lyric)
    print('lyrics appended')
df["Lyrics"] = lyrics_list
writer = ExcelWriter('Backstreet_Boys_Lyrics.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='Lyrics')
writer.save()

