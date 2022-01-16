import pandas
import json
import csv
#open MOCK_DATA.csv file and read first row into list header
df = pandas.read_csv('MOCK_DATA.csv', header=0)
#create a dictionary of df.columns as keys and values as empty lists
censored_values = {}
#create a json reader to read test.json file
with open('test.json') as json_file:
    json_data = json.load(json_file)
   
class functions:    
    def censor(col):
        #read values from column and store in list
        values = df[col].tolist()
        #replace values with '*'
        for i in range(len(values)):
            values[i] = '*'
        censored_values[col] = values

for column in df.columns:
    if column in json_data.keys():
        call = getattr(functions, json_data.get(column))
        call(column)
    else:
        censored_values[column] = df[column].tolist()


file = open('censored_values.csv', 'w')
writefile = csv.writer(file)
#convert censored_values dictionary to dataframe and write to csv
df_censored = pandas.DataFrame.from_dict(censored_values)
df_censored.to_csv('censored_values.csv')
file.close()


