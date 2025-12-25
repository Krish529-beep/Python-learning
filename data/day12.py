"""
Challenge:CLI Contact Book (Csv-powered)
"""

import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME,"w",encoding='utf-8',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name","phone","email"])

def add_contact():
    name = input("Name: ").strip()
    phone = input("phone: ").strip()
    email = input("email: ").strip()

    #check for duplicates
    with open(FILENAME,"r",encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["name"].lower() == name.lower():
                print('Contact name already exits')
                return

    #adding contact
    with open(FILENAME,"a",encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name,phone,email])
        print('Contact added') 


def view_contacts():
    with open(FILENAME,"r",encoding='utf-8') as f:
        reader = csv.reader(f)
        print(reader)
        rows = list(reader)

        if len(rows) < 1:
            print('No contact found')
            return
        
        print('your contacts:\n')

        for row in rows[1:]:
            if len(row) >= 3:
                print(f'{row[0]} | {row[1]} | {row[2]}')


def search_contact():
    term = input('Enter the name to serch').strip().lower()
    found = False

    with open(FILENAME,"r",encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row['name'].lower():
                print(f'{row['name']} | {row['phone']}')
                found =True

    if not found:
        print('No contact matching found')

def main():
    while 1:
        print('\nContact book')
        print('1.Add contact')
        print('2.View All Contacts')
        print('3.search all contacts')
        print('4.Exit')
        choice = input('Choose on option(1-4)').strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print('happy to see you leave')
            break
        else:
            print('Invalid choice number')

if __name__ == '__main__':
    main()


