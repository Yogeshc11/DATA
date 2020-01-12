#defining outliers
import pandas as pd
import numpy as np

def iqr_outlier(array):
    a=np.nanpercentile(array, 25)
    b=np.nanpercentile(array,75)
    iqr=b-a
    upper_bound=b+(iqr*1.5)
    lower_bound=a-(iqr*1.5)
    return [i for i in array if ((i > upper_bound) or (i < lower_bound))]

#BASIC EXPLORATION
def basic_exploration(df):
    #shape
    df.shape
    print('Rows:{},Columns:{}'.format(str(df.shape[0]),str(df.shape[1])))
    #Info
    print(df.info)
    #Discribe
    print("discription for Numerical columns")
    print(df.describe)
    print("discription for object columns")
    print(df.describe(exclude='object'))
    null_df=pd.DataFrame(df.isnull().sum())
    null_df.columns=["count"]
    #filter
    print(null_df[null_df["count"]>0])
    # outlier
    df_num=df.select_dtypes(exclude='object')
    df_num_col=df_num.columns
    for c in df_num_col:
        print(c)
        print(iqr_outlier(df_num[c]))

if __name__ == "__main__":
    mall=pd.read_csv('mall_data.txt')
    print(basic_exploration(mall))