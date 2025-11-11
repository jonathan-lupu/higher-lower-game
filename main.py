from game import Game
import tkinter as tk

game = Game()
# game.game_loop()

class GameUI:
    def __init__(self, master):
        self.game = Game()
        self.game.start_game()
        self.master = master
        self.master.title("Higher or Lower game")


        self.label = tk.Label(master, text=f"Card: {self.game.previous_card}")
        self.label.pack(pady=10)

        self.result = tk.Label(master, text="Make a guess")
        self.result.pack()

        self.higher_btn = tk.Button(master, text="Higher", command=lambda: self.make_guess("higher",master))
        self.higher_btn.pack(side="left", padx=5)

        self.lower_btn = tk.Button(master, text="Lower", command=lambda: self.make_guess("lower", master))
        self.lower_btn.pack(side="right", padx=5)

    def make_guess(self, direction, master):
        is_correct, msg = self.game.handle_guess(direction)
        if is_correct:
            self.result.config(text=msg)
            print(msg)
            print(self.game.previous_card)
            self.game.next_round()
            self.label.config(text=f"Card: {self.game.previous_card}")
            self.result.config(text=f"{msg} | Score: {self.game.score}")

        else:

            self.higher_btn.config(state="disabled")
            self.lower_btn.config(state="disabled")
            self.result.config(text=msg)
            self.restart_btn = tk.Button(master, text="Restart Game", command=lambda: self.restart())
            self.restart_btn.pack(side="bottom", padx=5)

    def restart(self):
        self.game.start_game()
        self.higher_btn.config(state="active")
        self.lower_btn.config(state="active")
        self.label.config(text=f"Card: {self.game.previous_card}")


root = tk.Tk()
GameUI(root)
root.mainloop()




