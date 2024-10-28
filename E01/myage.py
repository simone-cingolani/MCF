# import datetime
from datetime import datetime, timedelta
#timedelta è quello che mi dà le differenze temporali
"""
mydate_a=input('Cortesemente, dimmi che anno sei nato')
mydate_m=input('Cortesemente, dimmi che mese  sei nato')
mydate_g=input('Cortesemente, dimmi che giorno sei nato')
date_dict={"Giorno": mydate_g, "Mese": mydate_m, "Anno": mydate_a}
"""
mydate_str=input("Cortesemente, dimmi giorno, mese e anno in cui sei nato, nell'ordine descritto e separati da un trattino")
mydate = datetime.strptime(mydate_str, "%d-%m-%Y")
print('date:',       mydate       )
print('year:',  mydate.year  )
print('second:',mydate.second)
#ora calcolo l'età in anni, giorni e secondi:
date_now=datetime.now()
time_diff = date_now - mydate          #differenza in giorni
print(time_diff)
tots = time_diff.total_seconds()        #differenza in secondi
print(tots)
anno_corrente=date_now.year
anno_di_nascita= mydate.year
diff_a=anno_corrente-anno_di_nascita


#adesso printo i risultati incolonnati

date_dict={"Giorni ": time_diff, "Secondi ":tots , "Anni ": diff_a}
for s in date_dict:
    print('{: <20}{:}'.format(s,date_dict[s]))
