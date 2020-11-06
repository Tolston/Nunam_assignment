#importing pandas
import pandas as pd

#importing detail.csv file and Using Absolute Time for DateTimeIndex 

xl = pd.read_csv("detail.csv", parse_dates =["Absolute Time"], index_col ="Absolute Time")
minute_sample_detail_data=xl.resample('1T').sum()                   #down sampling the data to 1 minute/sample 
csvfile ='detailDownsampled.csv'
minute_sample_detail_data.to_csv(csvfile, index=True)               #exporting to detailDownsampled.csv


#importing detailVol.csv file and Using Absolute Time for DateTimeIndex 

xl1 = pd.read_csv("detailVol.csv", parse_dates =["Realtime"], index_col ="Realtime")
minute_sample_detailVol_data=xl1.resample('1T').mean()               #down sampling the data to 1 minute/sample
csvfile1 = 'detailVolDownsampled.csv'
minute_sample_detailVol_data.to_csv(csvfile1, index=True)            #exporting to detailVolDownsampled.csv


#importing detailTemp.csv file and Using Absolute Time for DateTimeIndex 

xl2 = pd.read_csv("detailTemp.csv", parse_dates =["Realtime"], index_col ="Realtime")
minute_sample_detailTemp_data=xl2.resample('1T').sum()               #down sampling the data to 1 minute/sample
csvfile2 = 'detailTempDownsampled.csv'
minute_sample_detailTemp_data.to_csv(csvfile2, index=True)           #exporting to detailTimeDownsampled.csv