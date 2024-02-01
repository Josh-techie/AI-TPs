import tkinter as tk
from min_max import minmax, evaluate, game_over, get_children


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = 'X'
        self.board = [' ']*9

        self.buttons = [tk.Button(root, text=' ', font=('normal', 20), width=6, height=3, command=lambda i=i: self.on_click(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)

    def on_click(self, index):
        if self.board[index] == ' ' and not game_over(self.board):
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if game_over(self.board):
                self.display_winner()
            else:
                self.switch_player()
                self.ai_move()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def ai_move(self):
        if not game_over(self.board):
            best_move = self.get_best_move()
            self.board[best_move] = self.current_player
            self.buttons[best_move].config(text=self.current_player)
            if game_over(self.board):
                self.display_winner()
            else:
                self.switch_player()

    def get_best_move(self):
        best_value = -float('inf')
        best_move = -1

        for i, cell in enumerate(self.board):
            if cell == ' ':
                self.board[i] = 'X'  # Assume AI is 'X' for evaluation
                move_value = minmax(self.board, 3, False)  # You may adjust the depth

                if move_value > best_value:
                    best_value = move_value
                    best_move = i

                self.board[i] = ' '
                # Reset the cell for further exploration

        return best_move

    def display_winner(self):
        winner = evaluate(self.board)
        if winner == 1:
            winner_str = "Player X wins!"
        elif winner == -1:
            winner_str = "Player O wins!"
        else:
            winner_str = "It's a draw!"

        tk.messagebox.showinfo("Game Over", winner_str)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
