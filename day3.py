"""
Simple bill spliter
"""
def get_float(prompt):
    while 1:
        try:
            return float(input(prompt))
        except ValueError:
            print('! pls enter a valid number')

people = int(input("How many people are you ?"))
names = [] 

for i in range (0,people):
    name = input(f'Enter the name of person {i+1}').strip()
    names.append(name)

total_bill = get_float("Enter the bill amount in number only ")

share = round(total_bill / people)

print("\n" + "*" * 40)
print(f'Total bill:{total_bill}')
print(f'Each person owes {share}')

for name in names:
    print(f'{name} owes {share} r')

print("\n" + "*" * 40)