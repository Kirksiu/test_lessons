import random as r

list_of_numbers = list(range(1, 11))

list_of_colors = ['red', 'black']
zero = ['zero']
num, col = r.random(1, 10), r.choice(list_of_colors)
while True:
    user_num, user_col = input(f"Attempt {counter}, Input number and color: ").split()
    if num == int(user_num) and col == user_col:
        print('')


