import pandas as pd
import numpy as np

#Name of the input CSV
INPUT_FILE = 'ForProcess2.csv'

#Read the CSV file
dataframe = pd.read_csv(INPUT_FILE, header = 0)

#Clean SuspAgeGroup and VicAgeGroup
dataframe[(dataframe['SUSP_AGE_GROUP'] == '-64') | (dataframe['SUSP_AGE_GROUP'] == '-80') | (dataframe['SUSP_AGE_GROUP'] == '-964') |
          (dataframe['SUSP_AGE_GROUP'] == '-965') | (dataframe['SUSP_AGE_GROUP'] == '-966') | (dataframe['SUSP_AGE_GROUP'] == '-973') |
          (dataframe['SUSP_AGE_GROUP'] == '2019') | (dataframe['SUSP_AGE_GROUP'] == '929')] = np.nan
dataframe[(dataframe['VIC_AGE_GROUP'] == '-67') | (dataframe['VIC_AGE_GROUP'] == '-69') | (dataframe['VIC_AGE_GROUP'] == '-71') |
          (dataframe['VIC_AGE_GROUP'] == '-934') | (dataframe['VIC_AGE_GROUP'] == '-943') | (dataframe['VIC_AGE_GROUP'] == '-967') |
          (dataframe['VIC_AGE_GROUP'] == '-974') | (dataframe['VIC_AGE_GROUP'] == '-978') | (dataframe['VIC_AGE_GROUP'] == '1013') |
          (dataframe['VIC_AGE_GROUP'] == '936') | (dataframe['VIC_AGE_GROUP'] == '951') ] = np.nan

#drop any na
dataframe = dataframe.replace('nan', np.nan)
newdataframe =  dataframe.dropna()

#Write to a file for further processing of data
newdataframe.to_excel("ForProcess3.xlsx", index = False);