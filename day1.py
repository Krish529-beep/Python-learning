'''
Self intro Script Generator!!
'''

import datetime
name = input("Enter your name:").strip()
age = input("Enter your age:").strip()
city = input("Enter your city name:").strip()
profession = input("enter yout profession:").strip()
hobby = input("Hobby would be very helpful:").strip()

intro_msg = (
    f"Hello! my name is {name} , I'm {age} years old and i live in {city}."
    f"I work as a {profession} and I absolutely enjoy {hobby} in my free time. "
    f"Nice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_msg += f'\n Logged on {current_date}'

border = '*' * 75
final_output = f'{border} \n {intro_msg} \n {border}'

print("\n",final_output)
