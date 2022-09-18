import numpy as np

class NodeStates:
    LIGHT = "L"
    WALL = "#"
    EMPTY = "."
    WALL0 = "0"
    WALL1 = "1"
    WALL2 = "2"
    WALL3 = "3"
    WALL4 = "4"

class OverallStates:
    INVALID = 0
    VALID = 1
    COMPLETE = 2
    CANNOT_FINISH = 3

class Node:
    def __init__(self, state, x, y):
        self.state = state
        self.x = x
        self.y = y

    def __str__(self):
        return self.state

    def __repr__(self):
        return self.state

class AdjancyElementNode:
    def __init__(self, up, down, right, left):
        self.up = up
        self.down = down
        self.right = right
        self.left = left

def get_map_size(lines):
    x = lines[0].split(" ")[0]
    y = lines[0].split(" ")[1]
    return (int(x),int(y))

def get_game_map_matrix():
    with open('./data/game1.txt') as game_data:
        lines = game_data.read().splitlines()
        map_size = get_map_size(lines)
        map_matrix = np.zeros((map_size[0], map_size[1]), str)
        for x_index in range(0, map_size[0]):
            for y_index in range(0, map_size[1]):
                map_matrix[x_index, y_index] = lines[x_index+1][y_index]
        return map_matrix, map_size

def create_adjacency_matrix(map_matrix, map_size):
    x_size, y_size = map_size
    nodes = np.empty(map_size, Node)
    for x_index in range(0, x_size):
        for y_index in range(0, y_size):
            nodes[x_index][y_index] = Node(map_matrix[x_index][y_index], x_index, y_index)

    adjacency_matrix = {}
    print(nodes)
    return adjacency_matrix, nodes

def solve_game():
    map_matrix, map_size = get_game_map_matrix()
    adjacency_matrix, nodes = create_adjacency_matrix(map_matrix, map_size)

solve_game()
