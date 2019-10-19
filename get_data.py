import pandas
import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as date
dict = []
with open('data/LosAngeles.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            dict.append(
                {
                    "date": row[0],
                    "parameter": row[1],
                    "location": row[2],
                    "value": row[3],
                    "unit": row[4],
                    "city": row[5],
                    "attribution": row[6],
                    "averagingperiod": row[7],
                    "coordinates": row[8],
                    "country": row[9],
                    "sourcename": row[10],
                    "sourcetype": row[11],
                    "mobile": row[12]
                }
            )
            line_count += 1
    print(f'Processed {line_count} lines.')

LAList_co = [float(item['value']) for item in dict if item['parameter'] == 'co' and item['location'] == 'Anaheim']
LAList_time = [item['date'] for item in dict if item['parameter'] == 'co' and item['location'] == 'Anaheim']
#LAList_no2 = [float(item['value']) for item in dict if item['parameter'] == 'no2']
'''
LAList_o3 = [float(item['value']) for item in dict if item['parameter'] == 'o3']
LAList_so2 = [float(item['value']) for item in dict if item['parameter'] == 'so2']
LAList_pm10 = [float(item['value']) for item in dict if item['parameter'] == 'pm10']
LAList_pm25 = [float(item['value']) for item in dict if item['parameter'] == 'pm25']
print("Quantidade de co:" + str(sum(LAList_co)/len(LAList_co)))
print("Quantidade de no2:" + str(sum(LAList_no2)/len(LAList_no2)))
print("Quantidade de o3:" + str(sum(LAList_o3)/len(LAList_o3)))
print("Quantidade de so2:" + str(sum(LAList_so2)/len(LAList_so2)))
print("Quantidade de pm10:" + str(sum(LAList_pm10)/len(LAList_pm10)))
print("Quantidade de pm25:" + str(sum(LAList_pm25)/len(LAList_pm25)))
'''
print(LAList_co)
aloha = []
for i in range(0, len(LAList_co)):
    aloha.append(i)
plt.plot(aloha, LAList_co)
plt.xlabel('CO em ppm')
plt.ylabel('Data')
plt.show()
'''
LAList_better_time = []
for time in LAList_time:
    time_split = time.split(',')
    LAList_better_time.append(time_split[0][5:24])  
print(LAList_better_time)
dates = date.date2num(LAList_better_time)
plt.plot_date(LAList_better_time, LAList_co, tz="US/Eastern", xdate=True)
plt.xlabel('CO em ppm')
plt.ylabel('Data')
plt.show()'''