# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 02:58:04 2023

@author: sai
"""

#upgrade pandas to latest or specific version
#on base terminal write
#conda install --upgrade pandas

#conda install -c anaconda pandas

#conda install update pandas==2.0.3  (latest version)

import pandas as pd
pd.__version__

###################################################################

#create using constructor
#create pandas Dataframe from list

import pandas as pd
technologies=[ ["spark",20000,"30days"],
              ["pandas",20000,"40days"]]
df=pd.DataFrame(technologies)
print(df)

'''
#since we have not given labels to columns and indexes, DataFrame 
by default assigns incremental sequence numbers as labels
to both rows and columns, these are called index.

'''

#Add column and row to DataFrame


column_names=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)

########################################################
#to check type of dataframe
df.dtypes

#########################################################
#you can also assign custom data types to columns,
#Set custom types to DataFrame.

technologies={
    'Courses' : ["spark","pyspark","Hadoop","Spyder","Python","pandas","oracle"],
    'Fee' : [20000,25000,30000,35000,40000,45000,50000],
    'Duration' : ['30days','35days','40days','45days','50days','55days','60days'],
    'Discount' : [11.8,13,8,23.8,48,65.4,64]
    }
df=pd.DataFrame(technologies)
print(df.dtypes)

####################################################################
#IMP
#Convert all types to all possible types
df2=df.convert_dtypes()  #convert object to string
print(df2.dtypes)


#change all column to same types
df=df.astype(str)    #convert all types into objects
print(df.dtypes)

#change type for one or multiple column
df=df.astype({"Fee":int,"Discount":float,"Duration":str})
print(df.dtypes)


#convert data types of all column in list
df=pd.DataFrame(technologies)
df.dtypes
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
print(df.dtypes)

#ignore errors 
df=df.astype({"Courses":int},errors='ignore')
#it ignores error and does not change data type
df.dtypes

################################################################

#generate error
df=df.astype({"Courses":int},errors='raise')

#converts feed column to numeric type

####################################################################
df.to_csv('data_file.csv')  #above dataframe are converted in to csv file
#we can also give the absolute path
#######################################################

#to create dataframe for csv file

df=pd.read_csv("data_file.csv")
df
######################################################################

#pandas dataframe - Basic operation
# create dataframe with None/Null to work with examples

import pandas as pd
import numpy as np

technologies=({
    'Courses' : ["spark","pyspark","Hadoop","Spyder","Python","pandas","None","oracle"],
    'Fee' : [20000,25000,30000,35000,np.nan,40000,45000,50000],
    'Duration' : ['30days','35days','40days','45days','50days','55days',' ','60days'],
    'Discount' : [11.8,13,8,23.8,48,65.4,64,9]
    })

row_lable = ['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies, index=row_lable)
print(df)

#################################################################
#ML project development cycle
#EDA - Exploratly Data Analysis
#preprocessing/Feature engineering
#Decide model
#implementation

#################################################################
#dataframe properties

df.shape

df.size

df.columns

df.columns.values

df.index

df.dtypes













































