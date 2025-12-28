"""
Real Time weather API with CSV storage
"""
import os
import csv
from datetime import datetime
import requests

FILENAME = "weather_log.csv"
API_KEY = "get your own key" # use yours form openweather

if not os.path.exists(FILENAME):
    with open(FILENAME,'w',newline="",encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['date','city','temp','conditions'])
 
def log_weather():
    city = input('Enter your city name: ').strip()
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME,'r',newline="",encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['date'] == date and row['city'].lower()==city:
                print('Entry for this city and date exsits')
                return
            
    try:
        url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url)
        print(res)
        data = res.json()

        if res.status_code != 200:
            print(f'API Error ')
            return
        
        temp = data['main']['temp']
        # print(data)
        condition = data['weather'][0]['main']

        with open(FILENAME,'a',newline="",encoding='utf-8') as f:
            writer =  csv.writer(f)
            writer.writerow([date,city.title(),temp,condition])
            print(f'Logged:{temp} {condition} in {city.title()} on {date}')

    except Exception as e:
        print(e)
        print('faild to make an api call')
        # print(e)
        
def view_logs():
    with open(FILENAME,"r",encoding='utf-8') as f:
        reader = list(csv.reader(f))
        if len(reader) <= 1:
            print('No entries')
            return
        for row in reader[1:]:
            print(f'{row[0]} : {row[1]} : {row[2]} : {row[3]}')


def main():
    while 1:
        print('Real time weather logger:')
        print('1.add weather log')
        print('2 View weather logs')

        choice = input('choose an option: ').strip()

        match choice:
            case "1": log_weather()
            case "2":view_logs()
            case _ : print('Invalid choice')


if __name__ == "__main__":
    main()
