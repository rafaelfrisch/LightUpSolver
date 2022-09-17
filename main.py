import numpy as np

def get_map_size(lines):
    x = lines[0].split(" ")[0]
    y = lines[0].split(" ")[1]
    return int(x),int(y)

def get_game_map_matrix():
    with open('./data/game1.txt') as game_data:
        lines = game_data.read().splitlines()
        x, y = get_map_size(lines)
        map_matrix = np.zeros((x, y), str)
        for x_index in range(0, x):
            for y_index in range(0, y):
                map_matrix[x_index, y_index] = lines[x_index+1][y_index]
        return map_matrix

map_matrix = get_game_map_matrix()
print(map_matrix)
