
# coding:utf-8
import pandas as pd
from pandas import DataFrame
from pandas import Series

def booknamesplit(df,bookdir,sheetname):
    df=pd.read_excel(bookdir,sheet_name=sheetname,header=1)
#   df.columns=['isbn','bookname','bookprice','banci','fenlei','zhuyizhe']
#   DataFrame.drop_duplicates(df,subset='bookname',keep='first',inplace=True)
    df['bookname']=df['bookname'].str.split(expand=True)#[0]
    df['bookname']=df['bookname'].str.split('(',expand=True)#[0]
    df['bookname']=df['bookname'].str.split('/',expand=True)#[0]
    df['bookname']=df['bookname'].str.split('<',expand=True)#[0]
    return df

#   DataFrame.to_excel(df,newbookdir,sheet_name='Sheet1',index=False,header=True)

df1=DataFrame()
df2=DataFrame()
bookdir='20190115书单查重.xlsx'
sheetname1='Sheet1'
sheetname2='Sheet2'
df1=booknamesplit(df1,bookdir,sheetname1)
df2=booknamesplit(df2,bookdir,sheetname2)
#rdf=pd.concat([df1,df2],ignore_index=True)
rdf=df1.append(df2,sort=True)
DataFrame.drop_duplicates(rdf,subset='bookname',keep=False,inplace=True)
rdfnew=rdf.dropna(subset=['定价'])
DataFrame.to_excel(rdfnew,'BookDeduplication.xlsx',sheet_name='Sheet1',index=False,header=True)