"""
friendship calculator
"""

def friendship_cal(name1,name2):
    name1,name2 = name1.lower(),name2.lower()
    score = 0
    shared_ltters = set(name1) & set(name2)
    vowels = set('aeiou')
    
    score += len(shared_ltters) * 10
    score += len(vowels & shared_ltters) * 10
    
    return min(score,100)

def run_friendship_cal():
    print('Friendship compatibility calculator')
    name1 = input('Enter 1st name: ')
    name2 = input('Enter 2nd name: ')

    score = friendship_cal(name1=name1,name2=name2)

    print(f'\n {score}')


run_friendship_cal()