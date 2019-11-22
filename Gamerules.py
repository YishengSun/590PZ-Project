import math
import random
import copy
import numpy as np


class Hexagon:

    #components of the puzzle board
    def __init__(self):
        self.x = 0
        self.y = 0
        self.item = 0  #'ship' if there is part of a ship on this hexagon or else 'sea'
        # item = 100
        self.direction = -1  # The direction in which the boat is placed,-1 means no direction
        self.show = ". "

def init_board(n):
    """
    if we remove the top right corner and bottom left corner of a square, we can get the shape which can represent a
    hexagon gameboard and we can use coordinates   to represent each small hexagon.
    :param n: number of hexagons for each border
    :return:the hexagon gameboard described with squares
    """
    board = []
    for i in range(2*n - 1):
        for j in range(2*n - 1):
            hex = Hexagon()
            hex.x = i
            hex.y = j
            board.append(hex)

    deleted = []
    for i in range(0,n-1):
        for j in range(n,2*n-1):
            if i <= j-n:
                deleted.append((i,j))
    for i in range(n, 2*n-1):
        for j in range(0,n-1):
            if j <= i-n:
                deleted.append((i,j))

    for coordiante in deleted:
        for hexagon in board:
            if hexagon.x == coordiante[0] and hexagon.y == coordiante[1]:
                board.remove(hexagon)
    # print(deleted)
    return board

# for hex in init_board(4):
#     print(hex.item)


def adjacent_hexagon(hex:Hexagon, board):
    # Returns the coordinates of all adjacent cells of a cell
    adjacent_list = []
    adjacent = [(hex.x-1, hex.y-1),(hex.x-1, hex.y),(hex.x, hex.y-1),(hex.x, hex.y+1),(hex.x+1, hex.y),(hex.x+1, hex.y+1)]
    for coordinate in adjacent:
        for hexagon in board:
            if coordinate[0] == hexagon.x and coordinate[1] == hexagon.y:
                adjacent_list.append(coordinate)

    return adjacent_list
# print(adjacent_hexagon(init_board(4)[1],init_board(4)))


def hex_on_line(start, end):
    # Returns all points covered between the start and end points on the hexagon map
    hexagon_list = []
    if start[0] == end[0]:
        for i in range(start[1], end[1]+1):
            hexagon_list.append((start[0],i))

    if start[1] == end[1]:
        for i in range(start[0], end[0]+1):
            hexagon_list.append((i,start[1]))

    if start[1]-start[0] == end[1]-end[0]:
        for i in range(start[0], end[0]+1):
            hexagon_list.append((i,i+start[1]-start[0]))  #修正，无法表示（0，1） （2，3）等情况
    return hexagon_list


def place_ship(x, y, length, direct, boa):
    # Place the ship (starting coordinates, ship length, direction, board) and
    # return to the board display after placing the boat
    new_board = boa

    if direct == 0:
        start = (x, y)
        end = (x, y+length-1)
        coordinates = hex_on_line(start, end)
        for hex in new_board:
            if (hex.x, hex.y) in coordinates:
                hex.item = 100
                hex.show = 'X '
                hex.direction = 0
        for hex in new_board:
            if hex.x == start[0] and hex.y == start[1]:
                hex.item = 200
            elif hex.x == end[0] and hex.y == end[1]:
                hex.item = 300
        adjacent_hex = []
        for hex in new_board:
            if (hex.x, hex.y) in coordinates:
                adjacent_hex += adjacent_hexagon(hex, new_board)
                adj = set(adjacent_hex)
                ship = set(coordinates)
                surround = adj - ship
                #print(surround)
        for hex in new_board:
            if (hex.x,hex.y) in surround:
                hex.item += 1

    elif direct == 1:
        start = (x, y)
        end = (x + length -1, y)
        coordinates = hex_on_line(start, end)
        for hex in new_board:
            if (hex.x, hex.y) in coordinates:
                hex.item = 100
                hex.show = 'X '
                hex.direction = 1
        for hex in new_board:
            if hex.x == start[0] and hex.y == start[1]:
                hex.item = 200
            elif hex.x == end[0] and hex.y == end[1]:
                hex.item = 300
        adjacent_hex = []
        for hex in new_board:
            if (hex.x, hex.y) in coordinates:
                adjacent_hex += adjacent_hexagon(hex, new_board)
                adj = set(adjacent_hex)
                ship = set(coordinates)
                surround = adj - ship
                # print(surround)
        for hex in new_board:
            if (hex.x, hex.y) in surround:
                hex.item += 1

    elif direct == 2:
        start = (x, y)
        end = (x + length -1, y + length -1)
        coordinates = hex_on_line(start, end)
        for hex in new_board:
            if (hex.x, hex.y) in coordinates:
                hex.item = 100
                hex.show = 'X '
                hex.direction = 2
        for hex in new_board:
            if hex.x == start[0] and hex.y == start[1]:
                hex.item = 200
            elif hex.x == end[0] and hex.y == end[1]:
                hex.item = 300
        adjacent_hex = []
        for hex in new_board:
            if (hex.x, hex.y) in coordinates:
                adjacent_hex += adjacent_hexagon(hex, new_board)
                adj = set(adjacent_hex)
                ship = set(coordinates)
                surround = adj - ship
                # print(surround)
        for hex in new_board:
            if (hex.x, hex.y) in surround:
                hex.item += 1
    return new_board

def remove_ship(x, y, length, direct, boa):
    # remove ship and edit the board
    new_board = boa
    if direct == 0:
        start = (x, y)
        end = (x, y+length-1)
        coordinates = hex_on_line(start, end)
        for hex in new_board:
            if (hex.x, hex.y) in coordinates:
                hex.item -= 0
                hex.show = '.'
                hex.direction = -1
        adjacent_hex = []
        for hex in new_board:
            if (hex.x, hex.y) in coordinates:
                adjacent_hex += adjacent_hexagon(hex, new_board)
                adj = set(adjacent_hex)
                ship = set(coordinates)
                surround = adj - ship
                #print(surround)
        for hex in new_board:
            if (hex.x,hex.y) in surround:
                hex.item -= 1

    elif direct == 1:
        start = (x, y)
        end = (x + length -1, y)
        coordinates = hex_on_line(start, end)
        for hex in new_board:
            if (hex.x, hex.y) in coordinates:
                hex.item = 0
                hex.show = '.'
                hex.direction = -1
        adjacent_hex = []
        for hex in new_board:
            if (hex.x, hex.y) in coordinates:
                adjacent_hex += adjacent_hexagon(hex, new_board)
                adj = set(adjacent_hex)
                ship = set(coordinates)
                surround = adj - ship
                # print(surround)
        for hex in new_board:
            if (hex.x, hex.y) in surround:
                hex.item -= 1

    elif direct == 2:
        start = (x, y)
        end = (x + length - 1, y + length - 1)
        coordinates = hex_on_line(start, end)
        for hex in new_board:
            if (hex.x, hex.y) in coordinates:
                hex.item = 0
                hex.show = '.'
                hex.direction = -1
        adjacent_hex = []
        for hex in new_board:
            if (hex.x, hex.y) in coordinates:
                adjacent_hex += adjacent_hexagon(hex, new_board)
                adj = set(adjacent_hex)
                ship = set(coordinates)
                surround = adj - ship
                # print(surround)
        for hex in new_board:
            if (hex.x, hex.y) in surround:
                hex.item -= 1
    return new_board



def find_possible_position(length, board):
    """

    find all possible positions for placing ship which its length equals length
    :param length: the length for ship
    :return: all possible placements ({(5, 1): 7, (5, 2): 7, (6, 2): 7}, {(2, 6): 7}, {})
    """
    directions = [0, 1, 2] # three directions: 0 for horizontal, 1 for vertical, 2 for inclined
    board_coordinates = []
    for hex in board:
        board_coordinates.append((hex.x,hex.y))

    for direction in directions:

        if direction == 0:
            direct_horizontal = {}
            for hex in board:
                coordinate = (hex.x,hex.y)
                end = (hex.x,hex.y+length-1)
                if end in board_coordinates:
                    hex_line = hex_on_line(coordinate,end)
                    count = 0
                    for coor in hex_line:
                        for h in board:
                            if h.x == coor[0] and h.y == coor[1] and h.item == 0:
                                count += 1
                    if count == length:
                        direct_horizontal[coordinate] = length

        if direction == 1:
            direct_vertical = {}
            for hex in board:
                coordinate = (hex.x,hex.y)
                end = (hex.x+length-1,hex.y)
                if end in board_coordinates:
                    hex_line = hex_on_line(coordinate, end)
                    count = 0
                    for coor in hex_line:
                        for h in board:
                            if h.x == coor[0] and h.y == coor[1] and h.item == 0:
                                count += 1
                    if count == length:
                        direct_vertical[coordinate] = length

        if direction == 2:
            direct_inclined = {}
            for hex in board:
                coordinate = (hex.x,hex.y)
                end = (hex.x+length-1,hex.y+length-1)
                if end in board_coordinates:
                    hex_line = hex_on_line(coordinate, end)
                    count = 0
                    for coor in hex_line:
                        for h in board:
                            if h.x == coor[0] and h.y == coor[1] and h.item == 0:
                                count += 1
                    if count == length:
                        direct_inclined[coordinate] = length

    return direct_horizontal,direct_vertical,direct_inclined



def show_board(board):
    max_len = 0

    for hex in board:
        if hex.x > max_len:
            max_len = hex.x
    df = np.empty([max_len+1, max_len+1], dtype=str) #x, y 的最大值
    df[:] = " "
    for i in board:
        df[i.x][i.y] = i.show
    for i in df:
        print(''.join(i))


def place_methods_formatted(possible_positions):
    # ({(5, 1): 7, (5, 2): 7, (6, 2): 7}, {(2, 6): 7}, {})
    # Change the representation of a certain length of ship placement [[5,1,7,0],[5,2,7,0],[6,2,7,0],[2,6,7,1]]

    count = 0
    place_methods = []
    for direction in possible_positions:
        for start_cor in direction.keys():
            place_methods.append([start_cor[0], start_cor[1], direction[start_cor], count])

        count += 1
    return place_methods
gameboard = init_board(4)
m = find_possible_position(4,gameboard)
print(place_methods_formatted(m))
# 找到该长度船的所有放法
# 对于每一种放法放置后的新图，找之后船在新图上的放法

# Return all possible configurations, the result is too many possibilities, instead of random generation
# def place(board, reserve_depth):
#     if reserve_depth == 1:  #在修改之后要改成0
#         show_board(board)
#         return True
#
#     method = place_methods_formatted(find_possible_position(reserve_depth, board)) #某长度船放在棋盘上的所有放法
#     if len(method) != 0:
#         for i in range(len(method)):
#                 board = place_ship(method[i][0], method[i][1], method[i][2], method[i][3], board)
#                 if not place(board, reserve_depth-1):
#                     board = remove_ship(method[i][0], method[i][1], method[i][2], method[i][3], board)
#                 else:
#                     board = remove_ship(method[i][0], method[i][1], method[i][2], method[i][3], board)
#     else:
#         return False


# def place(board, reserve_depth):
#     if reserve_depth == 1:  #在修改之后要改成0
#         return True
#
#     method = place_methods_formatted(find_possible_position(reserve_depth, board)) #某长度船放在棋盘上的所有放法
#     l = len(method)
#     if l > 0:
#         for i in range(l):
#             m = random.sample(method,1)[0]
#             board = place_ship(m[0], m[1], m[2], m[3], board)
#             if not place(board, reserve_depth-1):
#                 board = remove_ship(m[0], m[1], m[2], m[3], board)
#                 method.remove(m)
#             else:
#                 return board
#
#     return False


def place(board, ship_list, i=0):
    """
    backtracking to
    1.judge the input
    2.and if the ships can be placed on, return board with ships on
    :param board: game board
    :param ship_list: [5,...,4,...,3...,2...]  5:1 4:2 3:1 2:0  [5,4,4,3]
    :param i: count variable;indicates the depth/length
    :return: if feasible,return gameboard with randomly
    """
    if i == len(ship_list): # All ships are on board. Return true / recursion exit
        return True

    method = place_methods_formatted(find_possible_position(ship_list[i], board))
    # All possible placing methods of a certain length of ship on the current board
    l = len(method)
    if l > 0:
        for count in range(l):
            m = random.sample(method, 1)[0] # randomly select a place method
            board = place_ship(m[0], m[1], m[2], m[3], board)

            if not place(board, ship_list, i+1): # recursion entry
                board = remove_ship(m[0], m[1], m[2], m[3], board) # if not, remove ship
                method.remove(m) # and remove this method to prevent repetition
            else:
                return board

    return False


def get_number_clues(board):
    """
    获得每个行列的clue number
    :param board:
    :return: [[row],[col],[incline]]
    """
    side_len = 0

    for cell in board:
        if cell.x == 0:
            side_len += 1
    max_len = side_len * 2 - 1
    row_clues = []
    col_clues = []
    for i in range(max_len):
        countx = 0
        county = 0
        for cell in board:
            if (cell.x == i) and (cell.item >= 100):
                countx += 1
            if (cell.y == i) and (cell.item >= 100):
                county += 1
            # 再加个countz
        row_clues.append(countx)
        col_clues.append(county)

    incline_clues = []
    i = 1
    for length in range(side_len, max_len + 1):
        cor_list = hex_on_line((0, length - i), (length - 1, 2 * length - i - 1))
        i += 2
        countz = 0
        for cor in cor_list:
            for cell in board:
                if cell.x == cor[0] and cell.y == cor[1] and cell.item >= 100:
                    countz += 1
        incline_clues.append(countz)

    j = 2 * side_len - 3
    for length in range(max_len - 1, side_len - 1, -1):
        cor_list = hex_on_line((length - j, 0), (2 * length - j - 1, length - 1))
        j -= 2
        countz = 0
        for cor in cor_list:
            for cell in board:
                if cell.x == cor[0] and cell.y == cor[1] and cell.item >= 100:
                    countz += 1
        incline_clues.append(countz)
    clues = [row_clues, col_clues, incline_clues]


    return clues

def give_clue(board,n=8):
    hex_num = len(board)
    random_list = []
    clue_list = []
    for i in range(0,2*n):
        random_list.append(random.randint(0,hex_num-1))
    for clue in random_list:
        c_x = board[clue].x
        c_y = board[clue].y
        c_item = board[clue].item
        c_direct = board[clue].direction
        clue_info = [c_x,c_y,c_item,c_direct]
        clue_list.append(clue_info)
    return clue_list



# if __name__=="__main__":
#     while 1 == 1:
#         board_size  = input("Please input the hexagon board's length of side: ")
#         carrier_num = input("Please input the number of carriers'(size=5): ")
#         battleship_num = input("Please input the number of battleships'(size=4) number: ")
#         cruiser_num = input("Please input the number of cruisers'(size=3) number: ")
#         destroyer_num = input("Please input the number of destroyers'(size=2) number: ")
#         submarine_num = input("Please input the number of submarines'(size=1) number: ")
#
#         gameboard = init_board(int(board_size)) #这个是答案
#         emptyboard = init_board(int(board_size)) #这个是空白board
#         ships_list = [5]*int(carrier_num)+[4]*int(battleship_num)+[3]*int(cruiser_num)+[2]*int(destroyer_num)+\
#                      [1]*int(submarine_num)
#         print("*******************************************")
#         print("*******************************************")
#         if place(gameboard, ships_list):
#             print("Your board has been generated, let's start the game!")
#             print("I can give you some hints:") #随机挑选三个点在图上显示出来
#             show_board(gameboard)
#         else:
#             print("We can't generate a board for you based on your inputs, please change your decision!")
#             pass






