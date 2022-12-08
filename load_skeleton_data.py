from PIL import Image
import time
import math
import os
import numpy as np
import pandas as pd


drop_list=[]
drop_list.append(0)
drop_list.append(1)
drop_list.append(2)
for i in range(3,178,7):
    drop_list.append(i+3)
    drop_list.append(i+4)
    drop_list.append(i+5)
    drop_list.append(i+6)

def loadData(file):
    df=pd.read_csv(file)
    df_new = df.drop(df.columns[drop_list],axis = 1)
    arr=df_new.values
    #print(arr.shape)
    df_new1=arr.reshape(arr.shape[0],25,3)
    print(df_new1.shape)
    df_new1[:,:,0]=(df_new1[:,:,0]+1)/2
    df_new1[:, :, 1] = (df_new1[:, :, 1] + 2) / 2
    df_new1[:,:,2][df_new1[:,:,2]<0]=0.1
    df_new1=(df_new1*1000).astype("int")
    #final_array[final_array < 0] = 0
    #theData[:, 0][theData[:, 0] == 0] = -1
    #print(df_new1)
    return df_new1

#csv_path='path-to-dir-'
for file in os.listdir(csv_path):
    data=(loadData(os.path.join(csv_path,file)))
    print(data.shape)