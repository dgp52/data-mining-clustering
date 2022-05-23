import pandas as pd
from datetime import datetime

#Name of the input CSV
INPUT_FILE = 'NYPD_Complaint_Data_Historic.csv'

#Read the CSV file
dataframe = pd.read_csv(INPUT_FILE, header = 0)

#Try to convert date into pandas date time object. Drop instances where date is not in a correct format.
dataframe['CMPLNT_FR_DT'] = pd.to_datetime(dataframe['CMPLNT_FR_DT'], errors='coerce')
dataframe = dataframe.dropna(subset=['CMPLNT_FR_DT'])

#Some of these attributes has continuous data and others are not important for clustering (these atrtibutes wont give us much information)
dataframe.drop(['CMPLNT_NUM', 'ADDR_PCT_CD', 'CMPLNT_TO_DT', 'CMPLNT_TO_TM', 'RPT_DT', 'KY_CD', 
   'PARKS_NM', 'PD_CD', 'PD_DESC', 'LOC_OF_OCCUR_DESC', 'JURIS_DESC', 'HOUSING_PSA', 'X_COORD_CD', 
   'Y_COORD_CD', 'TRANSIT_DISTRICT', 'Latitude', 'Longitude', 'Lat_Lon', 'HADEVELOPT',
   'STATION_NAME', 'JURISDICTION_CODE', 'CMPLNT_FR_TM'], axis=1, inplace=True)

#Only take instances where complaints are made in 2019 or more and where the borough is Brooklyn
dataframe = dataframe[(dataframe['CMPLNT_FR_DT'] > '1/1/2019') & (dataframe['BORO_NM'] == "BROOKLYN")]
dataframe['PATROL_BORO'] = dataframe['PATROL_BORO'].astype(str)
dataframe['CRM_ATPT_CPTD_CD'] = dataframe['CRM_ATPT_CPTD_CD'].astype(str)
dataframe['LAW_CAT_CD'] = dataframe['LAW_CAT_CD'].astype(str)
dataframe['SUSP_AGE_GROUP'] = dataframe['SUSP_AGE_GROUP'].astype(str)
dataframe['SUSP_RACE'] = dataframe['SUSP_RACE'].astype(str)
dataframe['SUSP_SEX'] = dataframe['SUSP_SEX'].astype(str)
dataframe['VIC_AGE_GROUP'] = dataframe['VIC_AGE_GROUP'].astype(str)
dataframe['VIC_RACE'] = dataframe['VIC_RACE'].astype(str)
dataframe['VIC_SEX'] = dataframe['VIC_SEX'].astype(str)
dataframe['PREM_TYP_DESC'] = dataframe['PREM_TYP_DESC'].astype(str)
dataframe['OFNS_DESC'] = dataframe['OFNS_DESC'].astype(str)

#Remove all na rows
newdataframe =  dataframe.dropna()
#Drop the complaint date column
newdataframe.drop(['CMPLNT_FR_DT'], axis=1, inplace=True)

droppedNA =  dataframe.dropna()

#Write to a file for further processing of data
droppedNA.to_excel("ForProcess2.xlsx", index = False);