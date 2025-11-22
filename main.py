import tkinter as tk
from tkinter.constants import SUNKEN

from game import Game

class GameUI:
    def __init__(self, master):
        self.bg_colour = "#2b2b2b"
        self.orange_colour = "#ed712e"

        self.master = master
        self.frame = tk.Frame(master, bg=self.bg_colour)
        self.frame.pack(fill="both", expand=True)

        self.master.title("Higher or Lower")

        self.game = Game()
        self.game.start_game()

        title = tk.Label(
            self.frame,
            text="Higher or Lower",
            fg="white",
            bg=self.bg_colour,
            font=("Consolas", 16),
        )
        title.pack(pady=10)

        # Displays the card
        self.card_label = tk.Label(
            self.frame,
            text=f"{self.game.previous_card}",
            fg=self.orange_colour,
            bg=self.bg_colour,
            font=("Consolas", 32)
        )
        self.card_label.pack(pady=20)

        # Higher/Lower Buttons
        btn_frame = tk.Frame(self.frame, bg=self.bg_colour)
        btn_frame.pack(pady=10)

        # Higher/Lower buttons
        self.higher_btn = tk.Button(
            btn_frame,
            text="Higher",
            width=10,
            command=lambda: self.make_guess("higher")
        )
        self.higher_btn.pack(side="left", padx=10)


        self.lower_btn = tk.Button(
            btn_frame,
            text="Lower",
            width=10,
            command=lambda: self.make_guess("lower")
        )
        self.lower_btn.pack(side="left", padx=10)

        # Will display correct/incorrect
        self.result = tk.Label(
            self.frame,
            text="Make a guess",
            fg="white",
            bg=self.bg_colour,
            font=("Consolas", 12)
        )
        self.result.pack(pady=10)

        # Displays the score
        self.score_label = tk.Label(
            self.frame,
            text="Score: 0",
            fg=self.orange_colour,
            bg=self.bg_colour,
            font=("Consolas", 12)
        )
        self.score_label.pack(pady=5)

    def make_guess(self, direction):
        """
        handles the button the user clicks and works through the logic given the direction
        :param direction: higher or lower depending on button pressed
        :return:None
        """
        is_correct, msg = self.game.handle_guess(direction)


        if is_correct:
            # Guess is correct and exits function
            self.result.config(text=msg)
            self.game.next_round()
            self.card_label.config(text=f"{self.game.previous_card}")
            self.score_label.config(text=f"Score: {self.game.score}")
        else:
            # Guess is incorrect - allow restart
            self.higher_btn.config(state="disabled")
            self.lower_btn.config(state="disabled")
            self.result.config(text=msg)

            tk.Button(
                self.frame,
                text="Restart Game",
                command=self.restart
            ).pack(side="bottom", padx=5)

    def restart(self):
        """
        restarts the game by redrawing GUI
        :return: None
        """
        self.frame.destroy()
        GameUI(self.master)


root = tk.Tk()
root.geometry("400x300")
root.resizable(width=False, height=False)
GameUI(root)
root.mainloop()