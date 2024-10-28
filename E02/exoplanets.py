import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#importo il file csv e stampo il dataframe
df_exoplanets = pd.read_csv('ExoplanetsPars_2024.csv', comment='#')
print(df_exoplanets)
print(df_exoplanets.columns)
selcol = df_exoplanets[['pl_name', 'hostname']]

##############


mass = df_exoplanets['pl_bmassj']
time = df_exoplanets['pl_orbper']
log_mass= np.log(mass)
log_time= np.log(time)

plt.scatter( log_time,log_mass, color='royalblue', s=32, label='piccoli')
plt.xlabel('X', fontsize=16)
plt.ylabel('Y', fontsize=16)
#plt.ylim(-12,10 )

plt.legend(fontsize=14)
plt.show()


#############
rapp=df_exoplanets['pl_orbsmax']/df_exoplanets['st_mass']
log_rapp=np.log(rapp)
plt.scatter( log_time,log_rapp, color='royalblue', s=32, label='piccoli')
plt.xlabel('X', fontsize=16)
plt.ylabel('Y', fontsize=16)
#plt.ylim(-12,20 )

plt.legend(fontsize=14)
plt.show()


######ora faccio proprio gli assi logaritmici#######

# selezione basata su contenuto celle (singola colonna)
df1=df_exoplanets.loc[( df_exoplanets['discoverymethod'] == 'Transit')]
df2=df_exoplanets.loc[( df_exoplanets['discoverymethod'] == 'Radial velocity')]
mass1 = df1['pl_bmassj']
time1 = df1['pl_orbper']
mass2=df2['pl_bmassj']
time2=df2['pl_orbper']
print(mass1)
print(mass2)



plt.scatter( time1,mass1, color='red', s=32, label='Transit',alpha=.1)
plt.scatter( time2,mass2, color='royalblue', s=64, label='Radial velocity',alpha=1)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('X', fontsize=16)
plt.ylabel('Y', fontsize=16)
#plt.ylim(-10000,10000 )

plt.legend(fontsize=14)
plt.show()











#o bin log e plot con asse log
#per istogramma è richiesto di fare il logarismo dei dati
#plt.plot di uno e dell'altro prima di show li fa entrambi



#trovare periodo orbitale e mettendo 0 al centro del transoito e fare vedere tutti i dati tra ...



plt.hist(mass1,bins=10, color='skyblue', edgecolor='black',alpha=.1)
plt.hist(mass2,bins=10, color='lightgreen', edgecolor='black')
plt.show()
