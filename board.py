import tkinter as tk


class GoBoard(tk.Tk):
    def __init__(self, board_size=19):
        super().__init__()
        self.board_size = board_size
        self.cell_size = 40
        self.current_player = "black"
        self.init_ui()

    def init_ui(self):
        self.canvas = tk.Canvas(self, width=self.board_size * self.cell_size,
                                height=self.board_size * self.cell_size)
        self.canvas.pack()

        self.pass_button = tk.Button(self, text="Pass", command=self.pass_turn)
        self.pass_button.pack(side=tk.LEFT)

        self.resign_button = tk.Button(self, text="Resign", command=self.resign_game)
        self.resign_button.pack(side=tk.RIGHT)

        self.draw_board()
        self.canvas.bind("<Button-1>", self.place_stone)

    def draw_board(self):
        for i in range(self.board_size):
            self.canvas.create_line((i + 1) * self.cell_size, self.cell_size,
                                    (i + 1) * self.cell_size, self.board_size * self.cell_size)
            self.canvas.create_line(self.cell_size, (i + 1) * self.cell_size,
                                    self.board_size * self.cell_size, (i + 1) * self.cell_size)

    def place_stone(self, event):
        row = event.y // self.cell_size
        col = event.x // self.cell_size
        x = (col + 1) * self.cell_size
        y = (row + 1) * self.cell_size

        if self.current_player == "black":
            self.canvas.create_oval(x - self.cell_size // 2, y - self.cell_size // 2,
                                    x + self.cell_size // 2, y + self.cell_size // 2, fill="black")
            self.current_player = "white"
        else:
            self.canvas.create_oval(x - self.cell_size // 2, y - self.cell_size // 2,
                                    x + self.cell_size // 2, y + self.cell_size // 2, fill="white")
            self.current_player = "black"

    def pass_turn(self):
        self.current_player = "white" if self.current_player == "black" else "black"
        print(f"{self.current_player.capitalize()} player's turn.")

    def resign_game(self):
        print(f"{self.current_player.capitalize()} player resigned.")
        self.quit()


def showBoard(size):
    app = GoBoard(size)
    app.mainloop()
