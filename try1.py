import math
import random
import copy


#

class Hexagon:

    # ships
    carrier_size = 5
    battleship_size = 4
    cruiser_size = 3
    destroyer_size = 2
    submarine_size = 1
    #components of the puzzle board
    def __init__(self):
        self.x = 0
        self.y = 0
        self.item = None  #'ship' if there is part of a ship on this hexagon or else 'sea'


def init_board(n):
    """
    if we remove the top right corner and bottom left corner of a square, we can get the shape which can represent a
    hexagon gameboard and we can use coordinates to represent each small hexagon.
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
    #print(deleted)
    return board


def adjacent_hexagon(hex:Hexagon,board):
    adjacent_list = []
    adjacent = [(hex.x-1,hex.y-1),(hex.x-1,hex.y),(hex.x,hex.y-1),(hex.x,hex.y+1),(hex.x+1,hex.y),(hex.x+1,hex.y+1)]
    for coordinate in adjacent:
        for hexagon in board:
            if coordinate[0] == hexagon.x and coordinate[1] == hexagon.y:
                adjacent_list.append(coordinate)

    return adjacent_list




def place_ship(x,y,length,direct, board):
    if direct == 0:
        start = (x,y)
        end = (x,y+length-1)
        coordinates = hex_on_line(start,end)
        for hex in board:
            if (hex.x,hex.y) in coordinates:
                hex.item = 'ship'
        adjacent_hex = []
        for hex in board:
            if (hex.x,hex.y) in coordinates:
                adjacent_hex += adjacent_hexagon(hex,board)
                adj = set(adjacent_hex)
                ship = set(coordinates)
                surround = adj - ship
                #print(surround)
        for hex in board:
            if (hex.x,hex.y) in surround:
                hex.item = 'surround'

    elif direct == 1:
        start = (x, y)
        end = (x + length -1, y)
        coordinates = hex_on_line(start, end)
        for hex in board:
            if (hex.x, hex.y) in coordinates:
                hex.item = 'ship'
        adjacent_hex = []
        for hex in board:
            if (hex.x, hex.y) in coordinates:
                adjacent_hex += adjacent_hexagon(hex, board)
                adj = set(adjacent_hex)
                ship = set(coordinates)
                surround = adj - ship
                # print(surround)
        for hex in board:
            if (hex.x, hex.y) in surround:
                hex.item = 'surround'

    elif direct == 2:
        start = (x, y)
        end = (x + length -1, y + length -1)
        coordinates = hex_on_line(start, end)
        for hex in board:
            if (hex.x, hex.y) in coordinates:
                hex.item = 'ship'
        adjacent_hex = []
        for hex in board:
            if (hex.x, hex.y) in coordinates:
                adjacent_hex += adjacent_hexagon(hex, board)
                adj = set(adjacent_hex)
                ship = set(coordinates)
                surround = adj - ship
                # print(surround)
        for hex in board:
            if (hex.x, hex.y) in surround:
                hex.item = 'surround'
    return


def hex_on_line(start,end):
    hexagon_list = []
    if start[0] == end[0]:
        for i in range(start[1],end[1]+1):
            hexagon_list.append((start[0],i))

    if start[1] == end[1]:
        for i in range(start[0],end[0]+1):
            hexagon_list.append((i,start[1]))

    if start[1]-start[0] == end[1]-end[0]:
        for i in range(start[0], end[0]+1):
            hexagon_list.append((i,i))


    return hexagon_list


def find_possible_position(length,board):
    """
    find all possible positions for placing ship which length is length
    :param num: the length for ship
    :return: all possible placements
    """
    directions = [0,1,2] # three directions: 0 for horizontal, 1 for vertical, 2 for inclined
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
                            if h.x == coor[0] and h.y == coor[1] and h.item == None:
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
                            if h.x == coor[0] and h.y == coor[1] and h.item == None:
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
                            if h.x == coor[0] and h.y == coor[1] and h.item == None:
                                count += 1
                    if count == length:
                        direct_inclined[coordinate] = length

    return direct_horizontal,direct_vertical,direct_inclined

def create_puzzle(bordersize, carriers, battleships, cruisers, destroyers, submarines):
    carrier_size = 5
    battleship_size = 4
    cruiser_size = 3
    destroyer_size = 2
    submarine_size = 1
    ship_list = []
    for i in range(0, carriers):
        ship_list.append(carrier_size)
    for i in range(0, battleships):
        ship_list.append(battleship_size)
    for i in range(0,cruisers):
        ship_list.append(cruiser_size)
    for i in range(0,destroyers):
        ship_list.append(destroyer_size)
    for i in range(0,submarines):
        ship_list.append(submarine_size)




if __name__ == '__main__':
    board = init_board(4)
    place_ship(1,0,5,2,board)
    for hex in board:
        print(hex.item)

