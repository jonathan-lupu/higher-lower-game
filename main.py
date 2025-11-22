import tkinter as tk
from game import Game


class GameUI:
    def __init__(self, master):
        # Colour variables
        self.bg_colour = "#2b2b2b"  #Gray
        self.orange_colour = "#ed712e"  #Orange

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

        high_score_label = tk.Label(
            self.frame,
            text=f"High Score: {self.game.high_score}",
            fg=self.orange_colour,
            bg=self.bg_colour,
            font=("Consolas", 16),
        )
        high_score_label.pack(pady=10)

        # Help button
        help_btn = tk.Button(
            self.frame,
            text="Help",
            fg="blue",
            command=lambda: self.help_msg()
        )
        help_btn.pack(pady=10, side="bottom", anchor="e")

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

        if is_correct and not self.game.deck.is_empty():
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

            # sets highscore
            self.game.set_high_score()

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

    def help_msg(self):
        """
        Opens help popup to provide instructions to the user, using an overlay with tk.Toplevel
        :return: None
        """
        overlay = tk.Toplevel(self.master)
        overlay.transient(self.master)
        overlay.grab_set()
        overlay.overrideredirect(True)

        # Gets measurements of master widgets
        w = self.master.winfo_width()
        h = self.master.winfo_height()
        x = self.master.winfo_rootx()
        y = self.master.winfo_rooty()

        overlay.geometry(f"{w}x{h}+{x}+{y}")

        dim = tk.Frame(overlay, bg=self.bg_colour)
        dim.place(relwidth=1, relheight=1)

        panel = tk.Frame(overlay, bg="white", padx=10, pady=10)
        panel.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(panel, text="How to Play:", font=("Consolas", 14), bg="white", fg=self.orange_colour).pack(anchor="w")
        tk.Label(panel, text="""
        • Using buttons, make a guess whether the next card will be higher or lower
        • If the guess is correct, rewarded a point
        • A tie results in no change in score
        • If the guess was incorrect, then Game Over
        • Note: In this implementation of the game Ace is considered as a 1
        """, bg="white", fg=self.orange_colour, justify="left").pack(anchor="e", pady=5)

        tk.Button(panel, text="Close", command=overlay.destroy).pack(pady=10, side="bottom")

root = tk.Tk()
root.geometry("500x400")
root.resizable(width=False, height=False)
GameUI(root)
root.mainloop()
