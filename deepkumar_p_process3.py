import pandas as pd

#Name of the input CSV
INPUT_FILE = 'ForProcess3.csv'

#Read the CSV file
dataframe = pd.read_csv(INPUT_FILE, header = 0)

#Features we are really interested in
features = ['CRM_ATPT_CPTD_CD', 'LAW_CAT_CD', 'SUSP_AGE_GROUP', 'SUSP_RACE', 'SUSP_SEX', 'VIC_AGE_GROUP', 'VIC_RACE', 'VIC_SEX', 'PATROL_BORO', 'PREM_TYP_DESC', 'OFNS_DESC']

raw_data = dataframe[features]

#Data set is fully processed and can be used for analysis
raw_data.to_excel("processed-dataset.xlsx", index = False);