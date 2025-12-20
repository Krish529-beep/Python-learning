"""
Daily learing Journal Logger
"""

import datetime
emtry = input("What did yoyu learn today").strip()
rating = input("Rate your productivity today (1-5,optional)").strip()

now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d - %I:%M %p")

journal_entry = "\n" + "-" * 50
journal_entry = f'\n {date_str} \n {emtry}'
if rating:
    journal_entry+= f'\n productivity rating:{rating} \n'
journal_entry+= "\n" + "-" * 50

with open("main.txt","a+",encoding="utf-8") as f:
    f.write(journal_entry)

print(f'\n your journal entry has been saved to "main.txt" file.')