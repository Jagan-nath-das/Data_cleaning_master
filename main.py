# This is a data cleaning application

"""
Please create a python application that can take datasets and clean the data
- It should ask for datasets path and name
- it should check number of duplicats and remove all the duplicates 
- it should keep a copy of all the duplicates
- it should check for missing values 
- if any column that is numeric it should replace nulls with mean else it should drop that rows
- at end it should save the data as clean data and also return 
- duplicates records, clean_data 
"""

# importing dependencies
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random

# Get files in working directory
# print("Files in working directory", os.listdir(os.getcwd()))

data_path = 'sales.xlsx'
data_name = 'Jan_sales'


def data_cleaning_master(data_path, data_name):

    print('Thank you for giving the details!')

    sec = random.randint(1,4) # generating random numbers

    #print delay message
    print(f'Please wait for {sec} seconds! Checking file path')
    time.sleep(sec)

    # checking if the path exists
    if not os.path.exists(data_path):
        print(f'Incorrect path! Please try again with correct path. {data_path}')
        return
    else: 
        # checking the file type
        if data_path.endswith('.csv'):
            print('Dataset is csv!')
            data = pd.read_csv(data_path, encoding_errors= 'ignore')

        elif data_path.endswith('.xlsx'):
            print('Dataset is excel!')
            data = pd.read_excel(data_path)

        else:
            print('Unknown file type')
            return

    
    #print delay message
    print(f'Please wait for {sec} seconds! Checking total columns and rows')
    time.sleep(sec)
    
    # Showing number of records
    print(f'Dataset contains {data.shape[0]} \n Total Columns {data.shape[1]}')


    # Start Cleaning

    #print delay message
    print(f'Please wait for {sec} seconds! Checking total duplicates')
    time.sleep(sec)
    
    # Checking Duplicates
    duplicates = data.duplicated()
    total_duplicates = data.duplicated().sum()

    print(f'Datasets has total duplicate records:{total_duplicates}')

    
    #print delay message
    print(f'Please wait for {sec} seconds! Saving total duplicate rows')
    time.sleep(sec)
    

    # Saving the Duplicates
    if total_duplicates > 0:
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f'{data_name}_duplicates.csv', index= None)

    # Deleting duplicates
    df = data.drop_duplicates()


    
    #print delay message
    print(f'Please wait for {sec} seconds! Checking for missing values')
    time.sleep(sec)
    

    # find missing values
    total_missing_values = df.isnull().sum().sum()
    missing_value_columns = df.isnull().sum()

    print(f'Dataset has Total missing values: {total_missing_values}')
    print(f'Dataset contain missing value by columns: \n{missing_value_columns}')

    # Dealing with missing values
    # fillna -- For Int & Float
    # dropna -- For Object

    columns = df.columns

    for col in columns:
        # Filling mean for numeric colmuns all rows
        if df[col].dtype in (int, float):
            df[col] = df[col].fillna(df[col].mean())
        else:
            # dropping all rows wih missing records for non numeric col
            df.dropna(subset = col, inplace = True)


    
    #print delay message
    print(f'Please wait for {sec} seconds! Exporting datasets')
    time.sleep(sec)
    

    # Data is cleaned
    print(f'Congrats! Dataset is cleaned! \nTotal rows {df.shape[0]} \n Total Columns {df.shape[1]}')

    # Saving the clean dataset
    df.to_csv(f'{data_name}_clean_data.csv', index = None)
    print("Dataset is saved")


if __name__ == "__main__":
    
    print("Welcome to data cleaning Master! ")
    
    # ask path & file name
    data_path = input("Please enter dataset path: ")
    data_name = input("Please enter dataset name: ")

    #calling function
    data_cleaning_master(data_path, data_name)