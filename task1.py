#pip install pylint --- already installed

#importing pandas
import pandas as pd

#creating 3 dataframes for three file ["detail.csv","detailVol.csv","detailTemp.csv"]
df=pd.DataFrame()           
df1=pd.DataFrame()
df2=pd.DataFrame()

#looping to to parse sheets of detail_67_ , detailVol_67_, detailTemp_67_
for i in range(0,7):
    if i>0:
        nam=str('Detail_67_1_1_'+str(i))        #getting individual sheet names for detail_67_1_1_1 till detail_67_1_1_6
        name1=str('DetailVol_67_1_1_'+str(i))   #getting individual sheet names for detailVol_67_1_1_1 till detailVol_67_1_1_6
        name2=str('DetailTemp_67_1_1_'+str(i))  #getting individual sheet names for detailTemp_67_1_1_1 till detailTemp_67_1_1_6
    else:
        name='Detail_67_1_1'                    #getting first sheet name i.e detail_67_1_1
        name1='DetailVol_67_1_1'                #getting first sheet name i.e detailVol_67_1_1
        name2='DetailTemp_67_1_1'               #getting first sheet name i.e detailTemp_67_1_1
        
    #combining multiple sheet data into one sheet    
    
    #importing detail_67_ sheets from data.xls and appending to its coresponding dataframe
    xl=pd.read_excel(r'Data Engineer\\Data\\data.xls',sheet_name=name)
    df=df.append(xl)                           
    
    
    #importing detailVol_67_ sheets from data.xls and appending to its coresponding dataframe
    xl1=pd.read_excel(r'Data Engineer\\Data\\data.xls',sheet_name=name1)
    df1=df1.append(xl1)
    
    
    #importing detail_67_ sheets(first,1,2) from data.xls and  sheets(3,4,5,6) data_1.xls and appending to its coresponding dataframe
    if i<3:
        xl2=pd.read_excel(r'Data Engineer\\Data\\data.xls',sheet_name=name2)
    else:
        xl2=pd.read_excel(r'Data Engineer\\Data\\data_1.xls',sheet_name=name2)
    df2=df2.append(xl2)
    
#writing appended dataframe of details_67_ to details.csv file
csvfile = 'detail.csv'
df.to_csv(csvfile, index=False)


#writing appended dataframe of detailsVol_67_ to details.csv file
csvfile1 = 'detailVol.csv'
df1.to_csv(csvfile1, index=False)


#writing appended dataframe of detailsTemp_67_ to details.csv file
csvfile2 = 'detailTemp.csv'
df2.to_csv(csvfile2, index=False)