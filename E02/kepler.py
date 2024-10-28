import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#importo il file csv e stampo il dataframe
df_kepler = pd.read_csv('kplr010666592-2011240104155_slc.csv')
print(df_kepler)

#plotto il flusso in funzione del tempo
ax = df_kepler['TIME']
ay = df_kepler['PDCSAP_FLUX']
plt.plot(ax,ay,'*')
plt.xlabel('TIME')
plt.ylabel('FLUSSO')
plt.errorbar(ax, ay, yerr=df_kepler['PDCSAP_FLUX_ERR'], fmt='o' )
plt.show()

#salvo la figura in formato png
plt.savefig('Kepler_data.png')

#adesso faccio zoom su minimo
# selezione basata su contenuto celle
df=df_kepler.loc[( df_kepler['TIME'] > 941.40) & ( df_kepler['TIME'] < 941.65)]
ax1 = df['TIME']
ay1 = df['PDCSAP_FLUX']
plt.plot(ax1,ay1,'*')
plt.xlabel('TIME')
plt.ylabel('FLUSSO')
plt.errorbar(ax1, ay1, yerr=df['PDCSAP_FLUX_ERR'], fmt='o' )
plt.show()

#tratto il secondo grafico come inset

fig, ax = plt.subplots(figsize=(12,6))
ax2 = df_kepler['TIME']
ay2 = df_kepler['PDCSAP_FLUX']
plt.xlabel('TIME')
plt.ylabel('FLUSSO')
plt.errorbar(ax2, ay2, yerr=df_kepler['PDCSAP_FLUX_ERR'], fmt='o' )
ins_ax = ax.inset_axes([0.5,0.5,0.2, 0.2]) # w.r.t. ax
ins_ax.errorbar( df['TIME'], df['PDCSAP_FLUX'], fmt='o')
plt.plot()
plt.show()
