# 590PZ-Project
Hexagon Battleship by Yisheng Sun & Shixiang Gao

1.	Simple version of battleship game (https://lukerissacher.com/battleships)

Our Hexagon Battleship game is based on this simple version of battleship.

Battleship is similar with the classic game Minesweeper. The simple version of it has a n*n square board, there are several numbers of ships on that board (the board cell has no ship is water), but you don’t know where they are. To locate their positions, you have some clues and hints can help you. 

First, you can know what lengths of boats are on the chessboard and how many boats are there for each length. For example, there are one 3-part long ship, two 2-part long ships, and three 1-part long ship showed in the square box.

Second, for each row and column, you can get a number which shows how many ship parts are in this row or column. For example, the number “1” circled means in that column there is only one ship part. And the number “3” circled means there are 3 ship parts in that row. 

In addition, there will be some cells randomly chose which directly tell you what in that cell. You can know what it is based on the picture showed such as water, ship head, ship body or only a 1-part ship. For example, you can directly know there is a 1-part long ship in the left down corner of the board. So if you are lucky enough, you can get more information of ship locations. If you are not, maybe you only get some water cells 
 
![ad](https://github.com/YishengSun/590PZ-Project/blob/master/example1.png)

2. Changes in Hexagon Battleship 

We made some changes in our Hexagon Battleship. 

First, we transfer the square cells to hexagon cells. And therefore the total game board become a bigger hexagon board. As you can see below. 

Second, we remove the 1-part long ship so we have length 2-5 ships. 

Third, because the board become a hexagon, number clues for row and col are not enough. There will be 3 directions needed to be confirmed. As you can see in the pic below, "1" means only 1 ship part in red line, "0" means no ship part in blue line and "4" means 4 ship parts in yellow line. 

![ad](https://github.com/YishengSun/590PZ-Project/blob/master/example2.png)

3. How to play Hexagon Battleship 
download 
