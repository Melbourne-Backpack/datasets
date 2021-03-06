# import libraries general libraries
import pandas as pd
import numpy as np

# Modules for data visualization
import seaborn as sns
import matplotlib.pyplot as plt

import os

pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)

plt.rcParams['figure.figsize'] = [6, 6]

# ignore DeprecationWarning Error Messages
import warnings

warnings.filterwarnings('ignore')



def whitespace_remover(df):
    """
    The function will remove extra leading and trailing whitespace from the data.
    Takes the data frame as a parameter and checks the data type of each column.
    If the column's datatype is 'Object.', apply strip function; else, it does nothing.
    Use the whitespace_remover() process on the data frame, which successfully removes the extra whitespace from the columns.
    https://www.geeksforgeeks.org/pandas-strip-whitespace-from-entire-dataframe/
    """
    df = df.convert_dtypes()
    # iterating over the columns
    for i in df.columns:

        # checking datatype of each columns
        if df[i].dtype == 'str':

            # applying strip function on column
            df[i] = df[i].map(str.strip)
        else:
            # if condition is False then it will do nothing.
            pass
        
        

def write_interim_path(df, csv_name, folder_name): 
    # set the path of the cleaned data to data 
    interim_data_path = os.path.join(os.path.pardir, '..', 'data','interim', folder_name)

    write_interim_path = os.path.join(interim_data_path, csv_name)
    
    # To write the data from the data frame into a file, use the to_csv function.
    df.to_csv(write_interim_path, index=False)
    print(f'cleaned {csv_name} data was successfully saved!\n\n\n')
    
    