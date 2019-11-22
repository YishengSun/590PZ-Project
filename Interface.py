from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox as msgbox
import Gamerules


def resize_image(path,size):
    new_image = path.resize((size,size))
    return new_image
empty_hex0 = Image.open('empty_hex.jpg')
empty_hex1 = resize_image(empty_hex0,30)


sea_hex0 = Image.open('sea_hex.JPG')
sea_hex1 = resize_image(sea_hex0,30)

shipbody_d_0_temp = Image.open('shipbody0.JPG')
shipbody_d_0 = resize_image(shipbody_d_0_temp,30)


shipbody_d_1_temp = Image.open('shipbody1.JPG')
shipbody_d_1 = resize_image(shipbody_d_1_temp, 30)

shipbody_d_2_temp = Image.open('shipbody2.JPG')
shipbody_d_2 = resize_image(shipbody_d_2_temp, 30)

shipstart_d_0_temp = Image.open('shipstart0.JPG')
shipstart_d_0 = resize_image(shipstart_d_0_temp,30)


shipstart_d_1_temp = Image.open('shipstart1.JPG')
shipstart_d_1 = resize_image(shipstart_d_1_temp, 30)

shipstart_d_2_temp = Image.open('shipstart2.JPG')
shipstart_d_2 = resize_image(shipstart_d_2_temp, 30)

shipend_d_0_temp = Image.open('shipend0.JPG')
shipend_d_0 = resize_image(shipend_d_0_temp,30)


shipend_d_1_temp = Image.open('shipend1.JPG')
shipend_d_1 = resize_image(shipend_d_1_temp, 30)

shipend_d_2_temp = Image.open('shipend2.JPG')
shipend_d_2 = resize_image(shipend_d_2_temp, 30)




#create an empty gameboard for player
player_board = Gamerules.init_board(4)
game_board = Gamerules.init_board(4)
Gamerules.place(game_board,[5,4,2])



def coordinate_formatted(coordinate,n):
    #change the clue from gameboard to the interface to use
    #(0,0) = (30,150) (1,0) = (60,135)
    c_x = coordinate[0]
    c_y = coordinate[1]
    board_x = (c_x+1)*30
    board_y = 30*(n+1) - c_x*15 + c_y*30
    return board_x,board_y


def coordinate_interface_to_board(coordinate,n):
    #change the coordinate we get from the interface to gameboard
    #(30,150) = (0,0)
    c_x = coordinate[0]
    c_y = coordinate[1]
    gameboard_x = int(c_x/30-1)
    gameboard_y = int((c_y - 30*(n+1))/30 + 0.5*gameboard_x)
    return gameboard_x,gameboard_y


def drawGrid(frame, GRID_SIZE, clue_list,  playerboard, n_clues, XPAD=30, YPAD=30, IMG_SIZE=30):
    size = GRID_SIZE
    global empty_hex,sea_hex,shipbody_0,shipbody_1,shipbody_2
    empty_hex = ImageTk.PhotoImage(empty_hex1)
    sea_hex = ImageTk.PhotoImage(sea_hex1)
    shipbody_0 = ImageTk.PhotoImage(shipbody_d_0)
    shipbody_1 = ImageTk.PhotoImage(shipbody_d_1)
    shipbody_2 = ImageTk.PhotoImage(shipbody_d_2)
    shipstart_0 = ImageTk.PhotoImage(shipstart_d_0)
    shipstart_1 = ImageTk.PhotoImage(shipstart_d_1)
    shipstart_2 = ImageTk.PhotoImage(shipstart_d_2)
    shipend_0 = ImageTk.PhotoImage(shipend_d_0)
    shipend_1 = ImageTk.PhotoImage(shipend_d_1)
    shipend_2 = ImageTk.PhotoImage(shipend_d_2)

    for yi in range(0, GRID_SIZE):
        xi = XPAD + (GRID_SIZE - yi) * IMG_SIZE
        for i in range(0, size):
            l = tk.Label(frame, image=empty_hex)
            l.pack()
            l.image = empty_hex
            l.place(anchor= tk.NW, x=xi + yi*15, y=YPAD + yi * IMG_SIZE)
            l.bind('<Button-1>', lambda e: on_click(e,playerboard,GRID_SIZE))
            xi += IMG_SIZE
        size += 1

    size = 2*GRID_SIZE -2
    for yi in range(GRID_SIZE, 2 * GRID_SIZE - 1):
        xi = XPAD + (yi - GRID_SIZE+2) * IMG_SIZE
        for i in range(0, size):
            l = tk.Label(frame, image = empty_hex)
            l.pack()
            l.image = empty_hex
            l.place(anchor=tk.NW, x=xi + (2*GRID_SIZE-yi-2)*15, y=YPAD + yi * IMG_SIZE)
            l.bind('<Button-1>', lambda e: on_click(e,playerboard,GRID_SIZE))
            xi += IMG_SIZE
        size -= 1


    horizontal_clue = n_clues[0]
    l = len(horizontal_clue)
    mid = int(0.5 * (l+1))
    for k in range(mid):
        clue_num_l = tk.Label(frame, text= horizontal_clue[k])
        clue_num_l.pack()
        clue_num_l.text = horizontal_clue[k]
        clue_num_l.place(anchor=tk.NW, x=30*(GRID_SIZE+1)-15*(k+1) , y=5+30*(k+1))

    for k in range(mid,l):
        clue_num_l = tk.Label(frame, text=horizontal_clue[k])
        clue_num_l.pack()
        clue_num_l.text = horizontal_clue[k]
        clue_num_l.place(anchor=tk.NW, x= 30*(GRID_SIZE+1)-15*(2*(GRID_SIZE)-1-k), y=5 + 30 * (k + 1))


    ne_to_sw = n_clues[1]
    for t in range(mid):
        clue_num_l = tk.Label(frame, text=ne_to_sw[t])
        clue_num_l.pack()
        clue_num_l.text = ne_to_sw[t]
        clue_num_l.place(anchor=tk.NW, x=30 * (GRID_SIZE + 1) + 30 * (t + 1)-10, y= 10)

    for t in range(mid,l):
        clue_num_l = tk.Label(frame, text=ne_to_sw[t])
        clue_num_l.pack()
        clue_num_l.text = ne_to_sw[t]
        clue_num_l.place(anchor=tk.NW, x=30 * (GRID_SIZE + 1)*2 + 15 * (t - GRID_SIZE)-20, y=35 + 30 * (t - GRID_SIZE))


    nw_to_se = n_clues[2]
    for m in range(mid):
        clue_num_l = tk.Label(frame, text=nw_to_se[m])
        clue_num_l.pack()
        clue_num_l.text = nw_to_se[m]
        clue_num_l.place(anchor=tk.NW, x=30 * (GRID_SIZE + 1) + 1.5*30*GRID_SIZE - 15 * (m + 1), y= 30*(GRID_SIZE+1) + m*30 )

    for m in range(mid,l):
        clue_num_l = tk.Label(frame, text=nw_to_se[m])
        clue_num_l.pack()
        clue_num_l.text = nw_to_se[m]
        clue_num_l.place(anchor=tk.NW, x=30 * (GRID_SIZE + 1) * 2 - 30 * (m - GRID_SIZE+2)-2, y=30 * (GRID_SIZE)*2)

    # draw clues in the game board
    for clue in clue_list:
        #print(clue_list)
        clue_x = clue[0]
        clue_y = clue[1]
        for hex in playerboard:
            if hex.x == clue_x and hex.y == clue_y:
                hex.item = 100
        coordinate = (clue_x,clue_y)
        formatted = coordinate_formatted(coordinate,GRID_SIZE)
        if clue[2] >= 100 and clue[2] < 200:

            if clue[3] == 0:
                l_clue = tk.Label(frame,image = shipbody_0)
                l_clue.pack()
                l_clue.image = shipbody_0
                l_clue.place(anchor=tk.NW, x=formatted[1], y=formatted[0])
                #l_clue.bind('<Button-1>', lambda e: on_click(e))
            elif clue[3] == 1:
                l_clue = tk.Label(frame, image= shipbody_1)
                l_clue.pack()
                l_clue.image = shipbody_1
                l_clue.place(anchor=tk.NW, x=formatted[1], y=formatted[0])
                #l_clue.bind('<Button-1>', lambda e: on_click(e))
            elif clue[3] == 2:
                l_clue = tk.Label(frame,image = shipbody_2)
                l_clue.pack()
                l_clue.image = shipbody_2
                l_clue.place(anchor=tk.NW, x=formatted[1], y=formatted[0])
                #l_clue.bind('<Button-1>', lambda e: on_click(e))

        elif clue[2] >= 200 and clue[2] < 300:
            if clue[3] == 0:
                l_clue = tk.Label(frame,image = shipstart_0)
                l_clue.pack()
                l_clue.image = shipstart_0
                l_clue.place(anchor=tk.NW, x=formatted[1], y=formatted[0])
                #l_clue.bind('<Button-1>', lambda e: on_click(e))
            elif clue[3] == 1:
                l_clue = tk.Label(frame, image= shipstart_1)
                l_clue.pack()
                l_clue.image = shipstart_1
                l_clue.place(anchor=tk.NW, x=formatted[1], y=formatted[0])
                #l_clue.bind('<Button-1>', lambda e: on_click(e))
            elif clue[3] == 2:
                l_clue = tk.Label(frame,image = shipstart_2)
                l_clue.pack()
                l_clue.image = shipstart_2
                l_clue.place(anchor=tk.NW, x=formatted[1], y=formatted[0])
                #l_clue.bind('<Button-1>', lambda e: on_click(e))

        elif clue[2] >= 300:
            if clue[3] == 0:
                l_clue = tk.Label(frame,image = shipend_0)
                l_clue.pack()
                l_clue.image = shipend_0
                l_clue.place(anchor=tk.NW, x=formatted[1], y=formatted[0])
                #l_clue.bind('<Button-1>', lambda e: on_click(e))
            elif clue[3] == 1:
                l_clue = tk.Label(frame, image= shipend_1)
                l_clue.pack()
                l_clue.image = shipend_1
                l_clue.place(anchor=tk.NW, x=formatted[1], y=formatted[0])
                #l_clue.bind('<Button-1>', lambda e: on_click(e))
            elif clue[3] == 2:
                l_clue = tk.Label(frame,image = shipend_2)
                l_clue.pack()
                l_clue.image = shipend_2
                l_clue.place(anchor=tk.NW, x=formatted[1], y=formatted[0])
                #l_clue.bind('<Button-1>', lambda e: on_click(e))



        else:
            for hex in playerboard:
                if hex.x == clue_x and hex.y == clue_y:
                    hex.item = 0
            l_clue = tk.Label(frame, image = sea_hex)
            l_clue.pack()
            l_clue.image = sea_hex
            l_clue.place(anchor = tk.NW, x = formatted[1], y = formatted[0])
            #l_clue.bind('<Button-1>', lambda e: on_click(e))




def getCoordinates(widget):
    row = widget.winfo_y()
    col = widget.winfo_x()
    return row, col

def getImage(widget):
    hex_image = widget.image_names()
    return hex_image


def on_click(event,playerboard,gamesize):
    #如果本来是empty 点击变成水 如果是水，点击变成船（默认船体）如果是船 点击变水
    #print(event.widget.image)
    if event.widget.image == empty_hex:
        event.widget.config(image=sea_hex)
        event.widget.image = sea_hex
        a,b = getCoordinates(event.widget)
        gameboard_coordinate = coordinate_interface_to_board((a,b),gamesize)
        print(gameboard_coordinate)
        for hex in playerboard:
            if hex.x == gameboard_coordinate[0] and hex.y == gameboard_coordinate[1]:
                hex.item = 0

    elif event.widget.image == sea_hex:
        event.widget.config(image=shipbody_0)
        event.widget.image = shipbody_0
        a, b = getCoordinates(event.widget)
        gameboard_coordinate = coordinate_interface_to_board((a, b), gamesize)
        for hex in playerboard:
            if hex.x == gameboard_coordinate[0] and hex.y == gameboard_coordinate[1]:
                hex.item = 100

    elif event.widget.image == shipbody_0:
        event.widget.config(image=shipbody_1)
        event.widget.image = shipbody_1
        a, b = getCoordinates(event.widget)
        gameboard_coordinate = coordinate_interface_to_board((a, b), gamesize)
        for hex in playerboard:
            if hex.x == gameboard_coordinate[0] and hex.y == gameboard_coordinate[1]:
                hex.item = 100

    elif event.widget.image == shipbody_1:
        event.widget.config(image=shipbody_2)
        event.widget.image = shipbody_2
        a, b = getCoordinates(event.widget)
        gameboard_coordinate = coordinate_interface_to_board((a, b), gamesize)
        for hex in playerboard:
            if hex.x == gameboard_coordinate[0] and hex.y == gameboard_coordinate[1]:
                hex.item = 100

    elif event.widget.image == shipbody_2:
        event.widget.config(image=empty_hex)
        event.widget.image = empty_hex
        a, b = getCoordinates(event.widget)
        gameboard_coordinate = coordinate_interface_to_board((a, b), gamesize)
        for hex in playerboard:
            if hex.x == gameboard_coordinate[0] and hex.y == gameboard_coordinate[1]:
                hex.item = 0


def draw_gameboard():
    PLAY_SIZE = int(entry0.get())
    carrier_num = int(entry5.get())
    battleship_num = int(entry4.get())
    cruiser_num= int(entry3.get())
    destroyer_num = int(entry2.get())
    ships_list = [5] * int(carrier_num) + [4] * int(battleship_num) + [3] * int(cruiser_num) + [2] * int(destroyer_num)
    board = Gamerules.init_board(PLAY_SIZE)
    WIN_HEIGHT = 260 + PLAY_SIZE * 30
    WIN_WIDTH = 60 + (3 * PLAY_SIZE - 1) * 30
    player_board = Gamerules.init_board(PLAY_SIZE)
    answer = Gamerules.place(board, ships_list)
    num_clues = Gamerules.get_number_clues(answer)

    if answer:
        Gamerules.show_board(board)
        clues = Gamerules.give_clue(board,PLAY_SIZE)
        frame_board = tk.Frame(window, width=WIN_WIDTH, height=WIN_HEIGHT)
        drawGrid(frame_board, PLAY_SIZE, clues, player_board, num_clues)
        frame_board.pack(side=tk.LEFT, fill=tk.Y)
        play_btn.pack_forget()

        submit_btn = tk.Button(input_total, text='SUBMIT',command = lambda : compare(player_board,answer))
        submit_btn.pack(side=tk.LEFT, fill=tk.X, expand=tk.NO)

        restart_btn = tk.Button(input_total, text='RESTART',command = lambda: redraw(frame_board,submit_btn,restart_btn))
        restart_btn.pack(side=tk.RIGHT, fill=tk.X, expand=tk.NO)

        ## show me the answer
    else:
        msgbox.showinfo("Invalid Input!", "We can't generate a board for you based on your inputs, please change your decision!")


def redraw(tframe,btn1,btn2):
    tframe.pack_forget()
    btn1.pack_forget()
    btn2.pack_forget()
    draw_gameboard()

def compare(playerAnswer,rightAnswer):
    playerAnswer_list = []
    for hex in playerAnswer:
        if hex.item>=100:
            playerAnswer_list.append(1)
        else:
            playerAnswer_list.append(0)
    rightAnswer_list = []
    for hex in rightAnswer:
        if hex.item>=100:
            rightAnswer_list.append(1)
        else:
            rightAnswer_list.append(0)

    if playerAnswer_list == rightAnswer_list:
        msgbox.showinfo("Congratulations!", "Congratulations! You WIN!")
    else:
        msgbox.showinfo("Sorry!", "Sorry! You are not right this time!")


if __name__ == '__main__':
    window = tk.Tk()
    window.title('Battleship')

    input_total = tk.Frame(window)
    input_total.pack(side=tk.RIGHT, fill=tk.X, expand=tk.YES)

    inputbox0 = tk.Frame(input_total)
    inputbox0.pack(side=tk.TOP, fill=tk.Y, expand=tk.YES)
    Label0 = tk.Label(inputbox0, text="Board Size:")
    Label0.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
    entry0 = tk.Entry(inputbox0, width=3, font=('StSong', 10), foreground='green')
    entry0.pack(side=tk.RIGHT, fill=tk.X, expand=tk.YES)

    inputbox5 = tk.Frame(input_total)
    inputbox5.pack(side=tk.TOP, fill=tk.Y, expand=tk.YES)
    Label5 = tk.Label(inputbox5,text="Carrier(length=5):")
    Label5.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
    entry5 = tk.Entry(inputbox5, width=3, font=('StSong', 10), foreground='green')
    entry5.pack(side=tk.RIGHT, fill=tk.X, expand=tk.YES)

    inputbox4 = tk.Frame(input_total)
    inputbox4.pack(side=tk.TOP, fill=tk.Y, expand=tk.YES)
    Label4 = tk.Label(inputbox4, text="Battleship(length=4):")
    Label4.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
    entry4 = tk.Entry(inputbox4, width=3, font=('StSong', 10), foreground='green')
    entry4.pack(side=tk.RIGHT, fill=tk.X, expand=tk.YES)

    inputbox3 = tk.Frame(input_total)
    inputbox3.pack(side=tk.TOP, fill=tk.Y, expand=tk.YES)
    Label3 = tk.Label(inputbox3, text="Cruiser(length=3):")
    Label3.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
    entry3 = tk.Entry(inputbox3, width=3, font=('StSong', 10), foreground='green')
    entry3.pack(side=tk.RIGHT, fill=tk.X, expand=tk.YES)

    inputbox2 = tk.Frame(input_total)
    inputbox2.pack(side=tk.TOP, fill=tk.Y, expand=tk.YES)
    Label2 = tk.Label(inputbox2, text="Destroyer(length=2):")
    Label2.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
    entry2 = tk.Entry(inputbox2, width=3, font=('StSong', 10), foreground='green')
    entry2.pack(side=tk.RIGHT, fill=tk.X, expand=tk.YES)

    play_btn = tk.Button(input_total, text='PLAY',command=draw_gameboard)
    play_btn.pack(side=tk.TOP, fill=tk.Y, expand=tk.NO)

    window.mainloop()
