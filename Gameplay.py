import Gamerules,Interface
import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title('Battleship')
    frame_board = tk.Frame(window, width = WIN_WIDTH, height = WIN_HEIGHT)
    Interface.drawGrid(frame_board)
    frame_board.pack(side = tk.TOP, fill = tk.Y)
    window.mainloop()



