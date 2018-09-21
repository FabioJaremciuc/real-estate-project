# Importing the dataset using Python (SQLite 3)

import pandas as pd
import numpy as np
import csv
import sqlite3

db = sqlite3.connect('database.db') # connects to the database
print("Opened database successfully!")

def create_table():
  ''' Creates the Casafari table '''
  c = db.cursor()
  c.execute("CREATE TABLE Casafari (id,title,features,living_area,total_area,plot_area,price);")
  print("Table created successfully")
    
def data_entry():
  ''' Inserts the data into the database '''
  with open('/home/jaremciuc/data_analysis_test/assignment_data.csv') as fin: # it is necessary to change the file path
    c = db.cursor()
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['title'], i['features'], i['living_area'], i['total_area'], i['plot_area'], i['price']) for i in dr]
    c.executemany("INSERT INTO Casafari (id,title,features,living_area,total_area,plot_area,price) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
    db.commit()
    c.close()
    print('Data entered successfully')
    
create_table()
data_entry()

# To print the table
df = pd.read_sql_query("SELECT * FROM Casafari;", db)
df
