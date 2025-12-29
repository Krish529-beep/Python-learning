""" 
Plot graphs from this data
"""

import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILENAME = "weather_log.csv"

def visualize_weather():
    dates = []
    temps = []
    conditions = defaultdict(int)

    with open(FILENAME,'r',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                dates.append(row['date'])
                temps.append(row['temp'])
                conditions[row['conditions']] += 1
            except:
                continue
    
    if not dates: 
        print('No data is avaliable ')
        return
    
    plt.figure(figsize=(10,7))
    plt.plot(dates,temps,marker='o')
    plt.title('Temp over time')
    plt.xlabel('Date')
    plt.ylabel('temps')
    plt.tight_layout()
    plt.grid()
    plt.show()

    plt.figure(figsize=(7,5))
    plt.bar(conditions.keys(),conditions.values(),color='skyblue')
    plt.xlabel('Condition')
    plt.ylabel('Days')
    plt.show()

visualize_weather()
