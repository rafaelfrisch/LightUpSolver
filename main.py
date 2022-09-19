import numpy as np

game_file_path = './data/falsegame.txt'

class NodeStates:
    LIGHT = "L"
    WALL = "#"
    EMPTY = "."
    WALL_LIGHT_0 = "0"
    WALL_LIGHT_1 = "1"
    WALL_LIGHT_2 = "2"
    WALL_LIGHT_3 = "3"
    WALL_LIGHT_4 = "4"

class GameStates:
    INVALID = 0
    VALID = 1
    COMPLETED = 2

class Node:
    def __init__(self, state, x, y):
        self.state = state
        self.x = x
        self.y = y

    def node_is_wall(self):
        is_not_wall = self.state == NodeStates.LIGHT or self.state == NodeStates.EMPTY
        return not is_not_wall

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

    def adjacency_array(self):
        return [self.up, self.down, self.right, self.left]

    def __repr__(self):
        return str([self.up, self.down, self.right, self.left])

class Backtracker:
    def __init__(self, adjacency_matrix, nodes, map_size):
        self.adjacency_matrix = adjacency_matrix
        self.board = nodes
        self.map_size = map_size
    
    def print_board(self):
        print("BOARD:")
        for row_index in range(0, self.map_size[0]):
            for column_index in range(0, self.map_size[1]):
                print(self.board[row_index][column_index].state, end="")
            print("")           

    def solve(self):
        wall_nodes_not_solved = []
        for node in self.adjacency_matrix:
            # WALL 4 elements should always have 4 lights around
            if (node.state == NodeStates.WALL_LIGHT_4):
                adjacency_element_node = self.adjacency_matrix[node]
                for adjacenty_node in adjacency_element_node.adjacency_array():
                    adjacenty_node.state = NodeStates.LIGHT
            elif (node.node_is_wall()):
                wall_nodes_not_solved.append(node)
        self.backtrack(wall_nodes_not_solved)
        self.print_board()

    def can_place_light_ray(self, node):
        adjacency_element_node = self.adjacency_matrix[node]
        
        x_position_node = node.x
        y_position_node = node.y

        # check if theres is light in every direction

        up_node = adjacency_element_node.up
        for index in range(1, node.x+1):
            if(up_node is None):
                break
            if(up_node.node_is_wall()):
                break
            if(up_node.state == NodeStates.LIGHT):
                return False

            up_node = self.board[x_position_node-index][y_position_node]


        down_node = adjacency_element_node.down
        for index in range(1, self.map_size[1] - node.x):
            if(down_node is None):
                break
            if(down_node.node_is_wall()):
                break
            if(down_node.state == NodeStates.LIGHT):
                return False

            down_node = self.board[x_position_node+index][y_position_node]

        right_node = adjacency_element_node.right
        for index in range(1, self.map_size[1] - node.y):
            
            if(right_node is None):
                break
            if(right_node.node_is_wall()):
                break
            if(right_node.state == NodeStates.LIGHT):
                return False
            
            right_node = self.board[x_position_node][y_position_node+index]

        left_node = adjacency_element_node.left
        
        for index in range(1, node.y+1):
            if(left_node is None):
                break
            if(left_node.node_is_wall()):
                break
            if(left_node.state == NodeStates.LIGHT):
                return False
            left_node = self.board[x_position_node][y_position_node-index]

        return True

    def get_game_state(self):
        for node in self.adjacency_matrix:
            if(node.state == NodeStates.LIGHT):
                valid = self.can_place_light_ray(node)
                #print(valid, node)

    def backtrack(self, wall_nodes_not_solved):
        self.get_game_state()



def get_map_size(lines):
    x = lines[0].split(" ")[0]
    y = lines[0].split(" ")[1]
    return (int(x),int(y))

def get_game_map_matrix():
    with open(game_file_path) as game_data:
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
    backtracker = Backtracker(adjacency_matrix, nodes, map_size)
    backtracker.solve()

solve_game()
