import xxlimited
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
        return str([self.state, self.x, self.y])

    def __repr__(self):
        return str([self.state, self.x, self.y])

class AdjacencyElementNode:
    def __init__(self):
        self.up = None
        self.down = None
        self.right = None
        self.left = None

    def update_up(self, up):
        self.up = up

    def update_down(self, down):
        self.down = down

    def update_right(self, right):
        self.right = right

    def update_left(self, left):
        self.left = left

    def __repr__(self):
        return str([self.up, self.down, self.right, self.left])

def get_map_size(lines):
    x = lines[0].split(" ")[0]
    y = lines[0].split(" ")[1]
    return (int(x),int(y))

def get_game_map_matrix():
    with open('./data/game1.txt') as game_data:
        lines = game_data.read().splitlines()
        map_size = get_map_size(lines)
        map_matrix = np.zeros((map_size[0], map_size[1]), str)
        for row_index in range(0, map_size[0]):
            for column_index in range(0, map_size[1]):
                map_matrix[row_index, column_index] = lines[row_index+1][column_index]
        return map_matrix, map_size

def create_adjacency_matrix(map_matrix, map_size):
    x_size, y_size = map_size
    nodes = np.empty(map_size, Node)
    for row_index in range(0, x_size):
        for column_index in range(0, y_size):
            nodes[row_index][column_index] = Node(map_matrix[row_index][column_index], row_index, column_index)

    adjacency_matrix = {}
    
    for row_index in range(0, x_size):
        for column_index in range(0, y_size):
            adjacency_element = AdjacencyElementNode()
            node = nodes[row_index][column_index]

            if row_index-1 >= 0:
                adjacency_element.update_up(nodes[row_index-1][column_index])
            if row_index+1 < y_size:
                adjacency_element.update_down(nodes[row_index+1][column_index])
            if column_index-1 >= 0:
                adjacency_element.update_left(nodes[row_index][column_index-1])  
            if column_index+1 < x_size:
                adjacency_element.update_right(nodes[row_index][column_index+1])

            adjacency_matrix[node] = adjacency_element                          

    return adjacency_matrix, nodes

def solve_game():
    map_matrix, map_size = get_game_map_matrix()
    adjacency_matrix, nodes = create_adjacency_matrix(map_matrix, map_size)
    
solve_game()
