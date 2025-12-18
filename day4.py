"""
Minutes alive calculator
"""

def cal_min(age_years):
    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINS_IN_HOUR = 60

    total_days = age_years * DAYS_IN_YEAR
    total_hours = total_days * HOURS_IN_DAY
    total_mins = total_hours * MINS_IN_HOUR

    return round(total_days),round(total_hours),round(total_mins)

while 1:
    try:
        age = float(input("Enter your age in YEARS:"))
        days,hours,mins = cal_min(age)
        print('\n you are approx:')
        print(f' - {days} days old')
        print(f' - {hours} hours old')
        print(f' - {mins} mins old \n')

        again = input('would you like to try again:(y/n)').strip().lower()
        if again == 'y':
            continue
        else:
            break
    except :
        print("pls enter a valid age")