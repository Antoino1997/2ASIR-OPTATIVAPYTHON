# Versión FOR

print('Enter the tree size:')
size = int(input())

for row_num in range(1, size + 1):
    spaces = ' ' * (size - row_num)
    branches = '^' * (row_num * 2 - 1)
    print(spaces + branches)

trunk_spaces = ' ' * (size - 1)
print(trunk_spaces + '#')
print(trunk_spaces + '#')

# Versión WHILE

size = int(input('Enter the tree size: '))
row = 1
while row <= size:
    print(' ' * (size - row) + '^' * (row * 2 - 1))
    row += 1

print(' ' * (size - 1) + '#')
print(' ' * (size - 1) + '#')