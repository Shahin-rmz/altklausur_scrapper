##
import pandas as pd
import numpy as np
import glob
##



##
path = input('insert a path to ETL the files: ')
files = glob.glob(path + "/*.csv")
for csvfile in files:
    #read the csv
    df = pd.read_csv(csvfile)
    #delete the id column
    df = df.drop(df.columns[0],axis = 1)
    #bring number to the first column
    first_column = df.pop('number')
    df.insert(0, 'number', first_column)
    #merge the number of question with the question
    df["question"]= df['number'].astype(str)+ '. ' + df['frage']
    #delete the number and frage
    del df['number']
    del df['frage']
    #bring question to the first column
    first_column = df.pop('question')
    df.insert(0, 'question', first_column)
    #write the question type
    df['type'] = pd.Series([1 for x in range(len(df.index))])
    #bring type to second column
    second_column = df.pop('type')
    df.insert(1, 'type', second_column)
    #bring option5 to the 6th column
    sixth_column = df.pop('option5')
    df.insert(6, 'option5', sixth_column)
    #clean the ans column
    df['ans']=df['ans'].str.replace('Lösung: ', "")
    #set type of each question depending on j n or type A
    df['type'] = np.where(df['ans'].str.contains(r'j|n'),0,1)
    #write the answers
    df['ans']=df['ans'].str.replace('A', "1 0 0 0 0")
    df['ans']=df['ans'].str.replace('B', "0 1 0 0 0")
    df['ans']=df['ans'].str.replace('C', "0 0 1 0 0")
    df['ans']=df['ans'].str.replace('D', "0 0 0 1 0")
    df['ans']=df['ans'].str.replace('E', "0 0 0 0 1")
    df['ans']=df['ans'].str.replace('n', "0")
    df['ans']=df['ans'].str.replace('j', "1")
    df.to_csv(csvfile,encoding= 'utf-8-sig',index = False)
##
