def get_end_coordinates(directions):
    coords = [0, 0]

    for move in directions:
        move = move.upper()

        if move == 'N':
            coords[1] += 1
        elif move == 'S':
            coords[1] -= 1
        elif move == 'E':
            coords[0] += 1
        elif move == 'W':
            coords[0] -= 1

    return coords

user_directions = []

while True:
    print('Enter direction (N, S, E, W) or press Enter to finish:')
    user_input = input()

    if user_input == '':
        break

    if user_input.upper() in ['N', 'S', 'E', 'W']:
        user_directions.append(user_input)
    else:
        print("Invalid direction. Please use N, S, E, or W.")

final_pos = get_end_coordinates(user_directions)

print(f'The final coordinates are: {final_pos}')