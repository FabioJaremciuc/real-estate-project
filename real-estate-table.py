import pandas as pd
import numpy as np

# it is necessary to change the file path
df = pd.read_csv('/home/jaremciuc/data_analysis_test/assignment_data.csv')

def remove_nan():
    '''Removes the NaN elements from the dataset'''
    #replaces NaN elements by 0
    df['plot_area'].fillna(0.0, inplace=True)
    df['total_area'].fillna(0.0, inplace=True)
    df['living_area'].fillna(0.0, inplace=True)
    
    #replaces NaN elements by ''
    df['features'].fillna('', inplace=True)
    df['title'].fillna('', inplace=True)

def create_plot():
    '''Creates the plot column'''
    df['plot'] = np.logical_and(df['plot_area']>0.0, df['living_area']==0.0, dtype=bool) # compares two columns and brings a Boolean result
    df['plot'] = (df['plot'] == True).astype(int) # transforms a Boolean result into 0 or 1
    df['plot'] = np.logical_and(df['total_area']==0.0, df['plot']==1, dtype=bool)
    df['plot'] = (df['plot'] == True).astype(int)
    
    # replaces the logical output per 'plot' or ''
    df['plot']=df['plot'].replace(to_replace=1,value='plot')
    df['plot']=df['plot'].replace(to_replace=0,value='')
    
def create_apartment():
    '''Creates the apartment column'''
    # apartment type check
    df['apartamento'] = np.logical_and(df['plot']=='', df['title'].str.contains('partment', case=True).astype(int))
    df['apartamento']=df['apartamento'].replace(to_replace=True,value='apartment')
    df['apartamento']=df['apartamento'].replace(to_replace=False,value='')
    
    # penthouse type check
    df['apartamento'] = np.logical_or(df['apartamento']=='apartment', df['title'].str.contains('enthouse', case=True).astype(int))
    df['apartamento']=df['apartamento'].replace(to_replace=True,value='apartment') 
    df['apartamento']=df['apartamento'].replace(to_replace=False,value='')
    
    # duplex type check
    df['apartamento'] = np.logical_or(df['apartamento']=='apartment', df['title'].str.contains('uplex', case=True).astype(int))
    df['apartamento']=df['apartamento'].replace(to_replace=True,value='apartment')
    df['apartamento']=df['apartamento'].replace(to_replace=False,value='')
  
def create_house():
      '''Creates the house column'''
      # house type check  
      df['house'] = np.logical_and(df['plot']=='', df['apartamento']=='')
      df['house']=df['house'].replace(to_replace=True,value='house')
      df['house']=df['house'].replace(to_replace=False,value='')
      
def types_clean():
    '''Concatenates and erases the auxiliary columns used for creating the column types'''
    df['type'] = df['plot'] + df['apartamento'] + df['house']
    del df['plot']
    del df['apartamento']
    del df['house']
    
def create_locations():
    '''Creates the locations column'''
    # Alenquer locations check
    df['Alenquer'] = np.logical_or(df['title'].str.contains('Alenquer', case=True).astype(int), df['features'].str.contains('Alenquer', case=True).astype(int)) 
    df['Alenquer'] = df['Alenquer'].replace(to_replace=True,value='Alenquer')
    df['Alenquer'] = df['Alenquer'].replace(to_replace=False,value='')
    
    # Quinta da Marinha locations check
    df['Quinta'] = np.logical_or(df['title'].str.contains('Quinta', case=True).astype(int), df['features'].str.contains('Quinta', case=True).astype(int)) 
    df['Quinta'] = df['Quinta'].replace(to_replace=True,value='Quinta')
    df['Quinta'] = df['Quinta'].replace(to_replace=False,value='')
    
    # Golden Mile locations check
    df['Golden'] = np.logical_or(df['title'].str.contains('Golden', case=True).astype(int), df['features'].str.contains('Golden', case=True).astype(int)) 
    df['Golden'] = df['Golden'].replace(to_replace=True,value='Golden Mile')
    df['Golden'] = df['Golden'].replace(to_replace=False,value='')
    
    # Nagüeles locations check
    df['teste'] = np.logical_and(df['Alenquer']=='', df['Quinta']=='')
    df['teste']=df['teste'].replace(to_replace=True,value='Nagüeles')
    df['teste']=df['teste'].replace(to_replace=False,value='')

    df['Nagüeles'] = np.logical_and(df['teste']=='Nagüeles', df['Golden']=='')
    df['Nagüeles']=df['Nagüeles'].replace(to_replace=True,value='Nagüeles')
    df['Nagüeles']=df['Nagüeles'].replace(to_replace=False,value='')

    del df['teste']
    
    df['locations'] = df['Nagüeles'] + df['Alenquer'] + df['Quinta'] + df['Golden']

def concat_clean():
    '''Concat and erases the auxiliary columns used for creating the column locations'''
    del df['Golden']
    del df['Nagüeles']
    del df['Quinta']
    del df['Alenquer']

    del df['living_area']
    del df['total_area']
    del df['plot_area']
    del df['price']
   
def create_features():
    '''Creates the features column'''
    # swimming pool features check
    df['teste'] = np.logical_or(df['title'].str.contains('pool', case=True).astype(int), df['features'].str.contains('pool', case=True).astype(int)) 
    df['teste'] = df['teste'].replace(to_replace=True,value='1')
    df['teste'] = df['teste'].replace(to_replace=False,value='0')

    df['pool'] = np.logical_or(df['teste'].str.contains('1', case=True).astype(int), df['features'].str.contains('piscina', case=True).astype(int)) 
    df['pool'] = df['pool'].replace(to_replace=True,value='1')
    df['pool'] = df['pool'].replace(to_replace=False,value='0')

    del df['teste']
    
    # swimming garage features check
    df['garage'] = np.logical_or(df['title'].str.contains('arage', case=True).astype(int), df['features'].str.contains('arage', case=True).astype(int)) 
    df['garage'] = df['garage'].replace(to_replace=True,value='1')
    df['garage'] = df['garage'].replace(to_replace=False,value='0')
    
    # makes all lowercase letters in the features and title columns    
    df['lower_features'] = df['features'].map(lambda x: x.lower())
    df['lower_title'] = df['title'].map(lambda x: x.lower())
    
    # sea view garage features check
    df['sea view'] = np.logical_or(df['lower_title'].str.contains('sea view', case=True).astype(int), df['lower_features'].str.contains('sea view', case=True).astype(int)) 
    df['sea view'] = df['sea view'].replace(to_replace=True,value='1')
    df['sea view'] = df['sea view'].replace(to_replace=False,value='0')
    
    del df['lower_features']
    del df['lower_title']

# Show the 10 first rows
df.head(20)

# it is necessary to change the file path
# creates a cvs file with the script output
df.to_csv('/home/jaremciuc/data_analysis_test/deliverable_part_1.cvs', index=False, header=True, sep=';')
