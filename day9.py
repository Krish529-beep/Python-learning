"""
Set a Countdown Timer
"""
import time

while True:
    try:
        seconds = int(input("Enter time in secs:"))
        if seconds < 1:
            print("Enter value greater than 1")
            continue
        break
    except ValueError:
        print('pls enter a valid time')

print('\n Timer starts')

for reamining in range(seconds,0,-1):
    mins,secs = divmod(reamining,60)
    time_formate = f'{mins:02}:{secs:02}'
    print(f'time left {time_formate}',end="\r")
    time.sleep(1)

print('\n time"s up')