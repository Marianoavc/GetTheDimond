import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class MinesweeperBetGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Find the Diamonds!")
        self.root.geometry("600x700")

        self.balance = 10.00  # Saldo inicial
        self.bet = 1.00  # Apuesta inicial
        self.mines = 3  # Número inicial de minas
        self.rows = 5  # Número de filas del tablero
        self.cols = 5  # Número de columnas del tablero

        self.load_images()  # Cargar imágenes
        self.create_widgets()  # Crear los widgets
        self.reset_game()  # Reiniciar el juego

    def load_images(self):
        # Cargar y redimensionar las imágenes de los diamantes y minas
        self.diamond_img = ImageTk.PhotoImage(Image.open("image/diamond.png").resize((40, 40), Image.Resampling.LANCZOS))
        self.mine_img = ImageTk.PhotoImage(Image.open("image/mine.png").resize((40, 40), Image.Resampling.LANCZOS))

    def create_widgets(self):
        # Crear el frame de información
        self.info_frame = tk.Frame(self.root, bg="blue")
        self.info_frame.pack(pady=10)

        # Etiquetas de información
        self.bet_label = tk.Label(self.info_frame, text=f"Bet: {self.bet} PEN", bg="blue", fg="white")
        self.bet_label.grid(row=0, column=0, padx=5)
        self.mine_label = tk.Label(self.info_frame, text=f"Mines: {self.mines}", bg="blue", fg="white")
        self.mine_label.grid(row=0, column=1, padx=5)
        self.balance_label = tk.Label(self.info_frame, text=f"Balance: {self.balance:.2f} PEN", bg="blue", fg="white")
        self.balance_label.grid(row=0, column=2, padx=5)
        self.current_win_label = tk.Label(self.info_frame, text=f"Current Win: {0.0:.2f} PEN", bg="blue", fg="white")
        self.current_win_label.grid(row=0, column=3, padx=5)

        # Crear el frame de control
        self.control_frame = tk.Frame(self.root, bg="blue")
        self.control_frame.pack(pady=10)

        # Botones de control
        self.increase_bet_button = tk.Button(self.control_frame, text="+ Bet", command=self.increase_bet)
        self.increase_bet_button.grid(row=0, column=0, padx=5)
        self.decrease_bet_button = tk.Button(self.control_frame, text="- Bet", command=self.decrease_bet)
        self.decrease_bet_button.grid(row=0, column=1, padx=5)
        self.increase_mines_button = tk.Button(self.control_frame, text="+ Mines", command=self.increase_mines)
        self.increase_mines_button.grid(row=0, column=2, padx=5)
        self.decrease_mines_button = tk.Button(self.control_frame, text="- Mines", command=self.decrease_mines)
        self.decrease_mines_button.grid(row=0, column=3, padx=5)
        self.start_button = tk.Button(self.control_frame, text="Start", command=self.start_game)
        self.start_button.grid(row=0, column=4, padx=5)
        self.cashout_button = tk.Button(self.control_frame, text="Cash Out", command=self.cash_out)
        self.cashout_button.grid(row=0, column=5, padx=5)

        # Crear el frame del tablero
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(pady=10)
        self.board_buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.create_board()  # Crear el tablero

    def increase_bet(self):
        # Incrementar la apuesta
        self.bet += 1.00
        self.update_labels()

    def decrease_bet(self):
        # Disminuir la apuesta (sin bajar de 1.00)
        if self.bet > 1.00:
            self.bet -= 1.00
        self.update_labels()

    def increase_mines(self):
        # Incrementar el número de minas
        self.mines += 1
        self.update_labels()

    def decrease_mines(self):
        # Disminuir el número de minas (sin bajar de 1)
        if self.mines > 1:
            self.mines -= 1
        self.update_labels()

    def update_labels(self):
        # Actualizar las etiquetas de información
        self.bet_label.config(text=f"Bet: {self.bet} PEN")
        self.mine_label.config(text=f"Mines: {self.mines}")
        self.balance_label.config(text=f"Balance: {self.balance:.2f} PEN")
        self.current_win_label.config(text=f"Current Win: {self.current_win:.2f} PEN")

    def start_game(self):
        # Iniciar un nuevo juego
        self.reset_game()
        self.balance -= self.bet
        self.update_labels()

    def reset_game(self):
        # Reiniciar el tablero y las variables del juego
        self.clear_board()
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.diamonds_found = 0
        self.current_win = 0.0
        self.game_over = False
        self.create_mines()
        self.update_labels()

    def clear_board(self):
        # Limpiar el tablero (restaurar botones a su estado inicial)
        for r in range(self.rows):
            for c in range(self.cols):
                btn = self.board_buttons[r][c]
                if btn:
                    btn.config(image="", bg="SystemButtonFace", state="normal")

    def create_board(self):
        # Crear el tablero con botones
        for r in range(self.rows):
            for c in range(self.cols):
                btn = tk.Button(self.board_frame, width=8, height=4, command=lambda r=r, c=c: self.reveal_cell(r, c))
                btn.grid(row=r, column=c, padx=2, pady=2)
                self.board_buttons[r][c] = btn

    def create_mines(self):
        # Colocar minas aleatoriamente en el tablero
        mine_positions = random.sample(range(self.rows * self.cols), self.mines)
        for pos in mine_positions:
            r = pos // self.cols
            c = pos % self.cols
            self.board[r][c] = -1

    def reveal_cell(self, r, c):
        # Revelar el contenido de una celda
        if self.game_over:
            return

        btn = self.board_buttons[r][c]

        if self.board[r][c] == -1:
            btn.config(image=self.mine_img, bg="red")
        else:
            btn.config(image=self.diamond_img, bg="green")

        btn.config(state="disabled")

        if self.board[r][c] == -1:
            self.game_over = True
            self.current_win = 0.0
            self.update_labels()
            messagebox.showinfo("Game Over", "You hit a mine! Game over.")
            self.clear_board()
        else:
            self.diamonds_found += 1
            self.current_win = self.bet * self.diamonds_found * (1 + self.mines / 10.0)
            self.update_labels()

            if self.diamonds_found == (self.rows * self.cols - self.mines):
                messagebox.showinfo("Congratulations", "You've found all diamonds!")
                self.game_over = True
                self.clear_board()

    def cash_out(self):
        # Retirar las ganancias acumuladas
        if not self.game_over:
            self.balance += self.current_win
            messagebox.showinfo("Cash Out", f"You cashed out with {self.current_win:.2f} PEN!")
            self.game_over = True
            self.current_win = 0.0
            self.update_labels()
            self.clear_board()

if __name__ == "__main__":
    root = tk.Tk()
    game = MinesweeperBetGame(root)
    root.mainloop()
