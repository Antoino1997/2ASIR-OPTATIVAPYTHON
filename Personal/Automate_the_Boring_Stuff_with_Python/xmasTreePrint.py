# Versión FOR

import random

print('Enter the tree size:')
size = int(input())

for row_num in range(1, size + 1):
    spaces = ' ' * (size - row_num)
    num_branches = row_num * 2 - 1
    branches_row = ""

    for j in range(num_branches):
        if random.randint(1, 4) == 1:
            branches_row += 'o'
        else:
            branches_row += '^'

    print(spaces + branches_row)

trunk_spaces = ' ' * (size - 1)
print(trunk_spaces + '#')
print(trunk_spaces + '#')

# Versión WHILE

import random

print('Enter the tree size:')
size = int(input())
row = 1
while row <= size:
    print(' ' * (size - row), end='')

    col = 0
    num_branches = row * 2 - 1
    while col < num_branches:
        char = 'o' if random.randint(1, 4) == 1 else '^'
        print(char, end='')
        col += 1

    print()
    row += 1

t = 0
while t < 2:
    print(' ' * (size - 1) + '#')

    t += 1
