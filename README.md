# 590PZ-Project
Hexagon Battleship by Yisheng Sun & Shixiang Gao

1.	Simple version of battleship game (https://lukerissacher.com/battleships)

Our Hexagon Battleship game is based on this simple version of battleship.

Battleship is similar with the classic game Minesweeper. The simple version of it has a n*n square board, there are several numbers of ships on that board (the board cell has no ship is water), but you don’t know where they are. To locate their positions, you have some clues and hints can help you. 

First, you can know what lengths of boats are on the chessboard and how many boats are there for each length. For example, there are one 3-part long ship, two 2-part long ships, and three 1-part long ship showed in the square box.

Second, for each row and column, you can get a number which shows how many ship parts are in this row or column. For example, the number “1” circled means in that column there is only one ship part. And the number “3” circled means there are 3 ship parts in that row. 

In addition, there will be some cells randomly chose which directly tell you what in that cell. You can know what it is based on the picture showed such as water, ship head, ship body or only a 1-part ship. For example, you can directly know there is a 1-part long ship in the left down corner of the board. So if you are lucky enough, you can get more information of ship locations. If you are not, maybe you only get some water cells.

**An important rule: if a ship has been placed, the cells surrended the ship cannot be placed ship any more. This can be another important clue for players.**
 
![ad](https://github.com/YishengSun/590PZ-Project/blob/master/example1.png)

2. Changes in Hexagon Battleship 

We made some changes in our Hexagon Battleship. 

First, we transfer the square cells to hexagon cells. And therefore the total game board become a bigger hexagon board. As you can see below. 

Second, we remove the 1-part long ship so we have length 2-5 ships. 

Third, because the board become a hexagon, number clues for row and col are not enough. There will be 3 directions needed to be confirmed. As you can see in the pic below, "1" means only 1 ship part in red line, "0" means no ship part in blue line and "4" means 4 ship parts in yellow line. 

![ad](https://github.com/YishengSun/590PZ-Project/blob/master/example2.png)

3. How to play Hexagon Battleship 

download or clone --> install required libs --> run interface.py --> customize the game board size and numbers for each kind of ships --> If it is valid to put that many ships on the board, it will generate corresponding game. Else, you need to check the validity and input again. 

In the game, you can see all the clues and hints which I mentioned before. You can also restart game at any time. (Notice: if you restart the game with same parameter as last time, it will generate a random valid one.) After you think you finish, press submit, it will automatically check whether you are right. 

4. two parts of core codes

a. Define the small hexagon cell as a class, store them as an edited list. (like a suqare been cut off the rightup and left down corner)
```
class Hexagon:
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
    # print(deleted)
    return board
```
b. Generate a new valid game based on the customization using backtracking algorithm. Notice in each recursive, we select a random place method and once there is a place combination can run to the final, it will directly ouput as a board. **So that's why I say even though you input same parameters, it will give you different game boards at each time.** If all the methods have been checked wrong, return false. 
```
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

```
I highly recommend you to play a small size board first because it can help you understand the rules and also this game is truely harder than your expected. I print the answer in the console every time you generating a game. GLHF!

![ad](https://github.com/YishengSun/590PZ-Project/blob/master/example3.png)

Written by Yisheng Sun 12/12/2019
