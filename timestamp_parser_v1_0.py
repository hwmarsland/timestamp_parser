import pandas as pd
import numpy as np
import sys

data = pd.read_excel(sys.argv[1], header=0)
df = data.copy()

df['temp'] = df['Original']
df['last_access_date'] = np.nan
df['last_access_time'] = np.nan
df['filepath_folder'] = np.nan
df['filepath_file'] = np.nan

path = ''
counter = 0
for i in df['temp']:
    if 'Directory' in str(i):
        if df.at[counter+1, 'temp'] is np.nan:
            path = str(i)
        else:
            path = str(i) + str(df.at[counter+1, 'temp'])
    elif i is np.nan or str(i).startswith('Mode') or '-------------' in str(i):
        pass
    else:
        df.at[counter, 'filepath_folder'] = path
    counter = counter + 1

counter = 0
for i in df['temp']:
    if 'Directory:' in str(i) and '152.2.156.60' in str(i):
        df.at[counter, 'temp'] = np.nan
        df.at[counter+1, 'temp'] = np.nan
    elif 'Mode' in str(i) and 'LastWriteTime' in str(i) and 'Length' in str(i) and 'Name' in str(i):
        df.at[counter, 'temp'] = np.nan
    elif '------------' in str(i):
        df.at[counter, 'temp'] = np.nan
    counter = counter + 1

counter = 0
for i in df['temp']:
    if str(i) == 'nan':
        pass
    else:
        if counter < (len(df['temp']) - 1) and 'AM' not in str(df.at[counter+1, 'temp']) and 'PM' not in str(df.at[counter+1, 'temp']) and df.at[counter+1, 'temp'] is not np.nan:
            df.at[counter, 'temp'] = str(i)[14:] + ' ' + str(df.at[counter+1, 'temp'])
            df.at[counter+1, 'temp'] = np.nan
        else:
            df.at[counter, 'temp'] = str(i)[14:]
    counter = counter + 1

counter = 0
for i in df['temp']:
    if str(i) == 'nan':
        pass
    else:
        df.at[counter, 'last_access_date'] = str(i)[0:10]
        df.at[counter, 'temp'] = str(i)[10:]
    counter = counter + 1

df['last_access_date'] = df['last_access_date'].replace(' ', '', regex=True)

counter = 0
for i in df['temp']:
    if str(i) == 'nan':
        pass
    else:
        df.at[counter, 'last_access_time'] = str(i)[2:10]
        df.at[counter, 'temp'] = str(i)[26:]
    counter = counter + 1

df['last_access_time'] = df['last_access_time'].replace(' ', '', regex=True)
df['last_access_time'] = df['last_access_time'].replace('PM', ' PM', regex=True)
df['last_access_time'] = df['last_access_time'].replace('AM', ' AM', regex=True)

counter = 0
for i in df['temp']:
    if str(i) == 'nan':
        pass
    else:
        df.at[counter, 'filepath_file'] = str(df.at[counter, 'filepath_folder']) + '\\' + str(df.at[counter, 'temp'])
    counter = counter + 1

df['filepath_file'] = df['filepath_file'].replace('  ', ' ', regex=True)
df['filepath_file'] = df['filepath_file'].replace('  ', ' ', regex=True)
df['filepath_file'] = df['filepath_file'].replace('  ', ' ', regex=True)
df['filepath_file'] = df['filepath_file'].replace('  ', ' ', regex=True)
df['filepath_file'] = df['filepath_file'].replace('  ', ' ', regex=True)
df['filepath_file'] = df['filepath_file'].replace('  ', ' ', regex=True)
df['filepath_file'] = df['filepath_file'].replace('  ', ' ', regex=True)
df['filepath_file'] = df['filepath_file'].replace('  ', ' ', regex=True)

counter = 0
for i in df['filepath_file']:
    if str(i) == 'nan':
        pass
    else:
        df.at[counter, 'filepath_file'] = str(i)[1:]
    counter = counter + 1

counter = 0
for i in df['filepath_file']:
    if str(i) == 'nan':
        df.at[counter, 'filepath_folder'] = np.nan
    counter = counter + 1

df['filepath_folder'] = df['filepath_folder'].replace('  ', ' ', regex=True)
df['filepath_folder'] = df['filepath_folder'].replace('  ', ' ', regex=True)
df['filepath_folder'] = df['filepath_folder'].replace('  ', ' ', regex=True)
df['filepath_folder'] = df['filepath_folder'].replace('  ', ' ', regex=True)
df['filepath_folder'] = df['filepath_folder'].replace('  ', ' ', regex=True)
df['filepath_folder'] = df['filepath_folder'].replace('  ', ' ', regex=True)
df['filepath_folder'] = df['filepath_folder'].replace('  ', ' ', regex=True)
df['filepath_folder'] = df['filepath_folder'].replace('  ', ' ', regex=True)

counter = 0
for i in df['filepath_folder']:
    if str(i) == 'nan':
        pass
    else:
        df.at[counter, 'filepath_folder'] = str(i)[1:]
    counter = counter + 1

df = df.drop(columns=['temp'])

writer = pd.ExcelWriter(str(sys.argv[1])+' edited-data.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python timestamp_parser_v1_0.py <filename>')