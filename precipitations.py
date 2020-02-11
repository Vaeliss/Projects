import csv
import matplotlib.pyplot as plt
from datetime import datetime

fig,ax = plt.subplots(figsize=(15,9))
plt.style.use('ggplot')

#costruzione dello scheletro del grafico
ax.set_ylabel('daily precipitations',fontsize=10)
fig.autofmt_xdate()
ax.tick_params(axis='both',labelsize=14)

#sitka
filename_sitka = './sitka_weather_2018_simple.csv'
with open(filename_sitka) as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    daily_sitka = []
    dates = []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            daily_sitka.append(float(row[3]))
        except:
            print('Data missing for ' + row[2])
        else:
           dates.append(current_date)



#costruzione del grafico
ax.plot(dates,daily_sitka, c='blue',linewidth=3,alpha=0.7)


#death valley
filename_death = './death_valley_2018_simple.csv'
with open(filename_death) as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    daily_death = []
    dates = []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            daily_death.append(float(row[3]))
        except:
            print('Data missing for ' + row[2])
        else:
           dates.append(current_date)


#costruzione del grafico
ax.plot(dates,daily_death, c='red',linewidth=3,alpha=0.7)


ax.set_title('Daily precipitations comparison:\nSitka,AK vs Death Valley,CA',fontsize=20)
ax.axis([min(dates),max(dates),min(daily_sitka),max(daily_sitka)*1.1])
plt.show()
