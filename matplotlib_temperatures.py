import csv
import matplotlib.pyplot as plt
from datetime import datetime

#getting data from the csv file of death valley

filename = './death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    max_temp = []
    min_temp = []
    dates = []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            daily_max = int(row[4])
            daily_low = int(row[5])
        except:
            print('Data missing for ' + str(current_date))
        else:
            max_temp.append(daily_max)
            min_temp.append(daily_low)
            dates.append(current_date)

#style and creation of plot
plt.style.use('ggplot')
fig,ax = plt.subplots(figsize=(15,9))

#plot format
# ax.set_xlabel('Date',fontsize=14)
ax.set_ylabel('Temperature (°F)',fontsize=14)
ax.tick_params(axis='both',labelsize=14)
fig.autofmt_xdate()

#plotting the temps and styling in between
ax.plot(dates,max_temp,c='red',linewidth=3,alpha=0.5)
ax.plot(dates,min_temp,c='blue',linewidth=3,alpha=0.5)
ax.scatter(dates[min_temp.index(min(min_temp))],min(min_temp),c='blue',s=105)
ax.scatter(dates[max_temp.index(max(max_temp))],max(max_temp),c='red',s=105)
plt.fill_between(dates,max_temp,min_temp,facecolor='blue',alpha=0.1)



#getting data from the csv file of sitka

filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    max_temp = []
    min_temp = []
    dates = []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            daily_max = int(row[5])
            daily_low = int(row[6])
        except:
            print('Data missing for ' + str(current_date))
        else:
            max_temp.append(daily_max)
            min_temp.append(daily_low)
            dates.append(current_date)

#plotting the temps and styling in between, for sitka
ax.plot(dates,max_temp,c='orange',linewidth=3,alpha=0.5)
ax.plot(dates,min_temp,c='purple',linewidth=3,alpha=0.5)
ax.scatter(dates[min_temp.index(min(min_temp))],min(min_temp),c='purple',s=105)
ax.scatter(dates[max_temp.index(max(max_temp))],max(max_temp),c='orange',s=105)
plt.fill_between(dates,max_temp,min_temp,facecolor='purple',alpha=0.1)

ax.set_title('Daily high and low temperatures - comparison\nDeath Valley, CA and Sitka, AL\n2018',fontsize=20)
ax.axis([min(dates),max(dates),10,140])

plt.show()
        
