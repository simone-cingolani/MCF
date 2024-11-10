import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#importo il file csv e stampo il dataframe
df_0 = pd.read_csv('hit_times_M0.csv', comment='#')
df_1 = pd.read_csv('hit_times_M1.csv', comment='#')
df_2 = pd.read_csv('hit_times_M2.csv', comment='#')
df_3 = pd.read_csv('hit_times_M3.csv', comment='#')

#plot istogramma dei tempi di hit

plt.hist(df_0['hit_time'],bins=50,color='skyblue', edgecolor='black',alpha=1)
plt.title('Istogramma dei tempi')
plt.show()

time=df_0['hit_time']
'''
#creo array vuoto che userò per differenze temporali
time_diff=np.empty(len(df_0['hit_time'])-1)
for i in range(1,len(df_0['hit_time'])+1):
    time_diff[i-1]=df_0['hit_time'][i]-df_0['hit_time'][i-1]
'''

time_diff=np.diff(time)
print(time_diff)
print(np.log(time_diff))
plt.hist(np.log10(time_diff),bins=50,range=(0,7), color='skyblue', edgecolor='black',alpha=1)
#qui attenzione ai valori -inf, posso risolvere dando range oppure usando mask o altri metodi di numpy
plt.title('Istogramma delle differenze dei tempi logaritmiche')
plt.show()


#faccio import di reco
import Hint from  reco
#definisco funzioni che leggono e riempiono di oggetti Hit
def file_0(df):
    l=0
    for ir, rr in df.iterrows():
        l=ir
    array_0=np.empty(l)
    for ir, rr in df.iterrows():
        obj=Hit(rr[mod_id],rr[det_id],rr[hit_time])
        array_0[ir]=obj
        
        

























