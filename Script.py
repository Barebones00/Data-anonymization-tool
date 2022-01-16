import pandas
import json
import csv
import functions

#open MOCK_DATA.csv file read it and store it in a variable
df = pandas.read_csv('MOCK_DATA.csv')

#create a dictionary for censored values
censored_values = {}

#create a dictionary for switch case
switcher = {1 : "censor",
            2 : "pseudonymization"}

#class for function calls
class calls:
    def censor(column):
        censored_values[column] = functions.functions.censor(df[column].tolist())

    def pseudonymization(column):
        censored_values[column] = functions.functions.pseudonymization(df[column].tolist(), column)

#switch case for calling functions
def switch(arg, column):
    getattr(calls , switcher.get(arg))(column) #gets the function name from dictionary based on arg and calls it

#create a json reader to read test.json file
with open('test.json') as json_file:
    json_data = json.load(json_file)
   
#code block to check if any function applies to column
for column in df.columns:
    if column in json_data.keys():
        switch(json_data.get(column),column)
    else:
        censored_values[column] = df[column].tolist()

#write the censored values to a csv file
file = open('censored_values.csv', 'w')
writefile = csv.writer(file)
df_censored = pandas.DataFrame.from_dict(censored_values)
df_censored.to_csv('censored_values.csv')
file.close()

