# 590PZ-Project
Hexagon Battleship by Yisheng Sun & Shixiang Gao

1.	Simple version of battleship game (https://lukerissacher.com/battleships)

Our Hexagon Battleship game is based on this simple version of battleship.

Battleship is similar with the classic game Minesweeper. The simple version of it has a n*n square board, there are several numbers of ships on that board (the board cell has no ship is water), but you don’t know where they are. To locate their positions, you have some clues and hints can help you. 

First, you can know what lengths of boats are on the chessboard and how many boats are there for each length. For example, there are one 3-part long ship, two 2-part long ships, and three 1-part long ship showed in the square box.

Second, for each row and column, you can get a number which shows how many ship parts are in this row or column. For example, the number “1” circled means in that column there is only one ship part. And the number “3” circled means there are 3 ship parts in that row. 

In addition, there will be some cells randomly chose which directly tell you what in that cell. You can know what it is based on the picture showed such as water, ship head, ship body or only a 1-part ship. For example, you can directly know there is a 1-part long ship in the left down corner of the board. So if you are lucky enough, you can get more information of ship locations. If you are not, maybe you only get some water cells.

[b]An important rule: 
 
![ad](https://github.com/YishengSun/590PZ-Project/blob/master/example1.png)

2. Changes in Hexagon Battleship 

We made some changes in our Hexagon Battleship. 

First, we transfer the square cells to hexagon cells. And therefore the total game board become a bigger hexagon board. As you can see below. 

Second, we remove the 1-part long ship so we have length 2-5 ships. 

Third, because the board become a hexagon, number clues for row and col are not enough. There will be 3 directions needed to be confirmed. As you can see in the pic below, "1" means only 1 ship part in red line, "0" means no ship part in blue line and "4" means 4 ship parts in yellow line. 

![ad](https://github.com/YishengSun/590PZ-Project/blob/master/example2.png)

3. How to play Hexagon Battleship 
download or clone --> install required libs --> run interface.py --> customize the game board size and numbers for each kind of ships --> If it is valid to put that much ships on the board, it will generate corresponding game. Else, you need to check the validity and input again. 

In the game, you can see all the clues and hints which I mentioned before. You can also restart game at any time. (Notice: if you restart the game with same parameter as last time, it will generate a random valid one.) After you think you finish, press submit, it will automatically check whether you are right. 

4. core codes
a. Define the small hexagon cell as a class, store them as a list, but because the hexgon property the 
class Hexagon:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.item = 0  #'ship' if there is part of a ship on this hexagon or else 'sea'
        # item = 100
        self.direction = -1  # The direction in which the boat is placed,-1 means no direction
        self.show = ". "
   
