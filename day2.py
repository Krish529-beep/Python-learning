''' 
Stylish Bio Generator
'''
import textwrap


name = input("Enter your name:").strip()
passion = input("Enter your passion one-liner:").strip()
profession = input("Enter your profession:").strip()
emoji = input("enter yout emoji:").strip()
handle = input("handle:").strip()

print('\n Choose your style:')
print('\n 1.Simple Lines')
print('\n 2.verticl flare')
print('\n 3.emoji sandwich')

style = input("\nEnter 1,2 or 3").strip()

def genrate_bio(style):
    if style =="1":
        return f'{emoji} {name} | {profession} \n {passion} \n {handle}'
    elif style == "2":
        return f'{emoji} {name} \n {profession} \n {passion} \n {handle}'
    elif style == "3":
        return f'{emoji*3}\n {name} - {profession} \n {passion} \n {handle} \n {emoji*3}'

bio = genrate_bio(style)

print('\n Your Stylish bio:\n')
print('*' * 50)

print(textwrap.dedent(bio))
print('*' * 50)

save = input("Do you want to save this ? (Y/N)").lower()

if save == "y":
    filename = f'{name.lower().replace(' ','_')}_bio.txt'
    with open(filename,"w",encoding="utf-8") as f:
        f.write(bio)
    print('file saved!')

