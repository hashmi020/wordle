import tkinter as tk
from tkinter import messagebox
import random
import winsound

class WordleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Wordle Game")
        self.master.geometry("350x520")
        self.master.resizable(False, False)

        # Theme
        self.bg_color = "#121212"
        self.fg_color = "#ffffff"
        self.entry_bg = "#1e1e1e"
        self.correct_color = "#4caf50"
        self.partial_color = "#ffeb3b"
        self.wrong_color = "#555555"

        self.master.configure(bg=self.bg_color)

        self.word_list = [
           "apple", "mango", "grape", "peach", "lemon", "melon", "zebra", "eagle",
          "brick", "flame", "storm", "crane", "glide", "cloud", "sugar", "dream","enter",
          "bread", "crown", "bride", "chess", "liver", "plaza", "raven", "track","stood",
          "sweep", "plant", "grain", "frost", "blush", "light", "flock", "stone","drift"
          "chair", "table", "water", "earth", "heart","trace","grace", "craze","space"
          "flair", "flare", "brave", "crush", "drain", "crisp", "pride", "grasp",
           "crash", "grind", "prank",  "prism", "crane","argue","small","trash",
           "large", "Merge","lucky","lunch","lunar","laser","lunch","latch","stuck",
            "truck","crush","brust","trust","brisk","cramp","tramp","clock","shift",
    
        ]

        self.guess_count = 0
        self.max_guesses = 6

        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        self.guess_entries = []
        self.frame = tk.Frame(self.master, bg=self.bg_color)
        self.frame.pack(pady=20)

        for row in range(self.max_guesses):
            row_entries = []
            for col in range(5):
                var = tk.StringVar()
                entry = tk.Entry(self.frame, width=2, font=("Arial", 24), justify="center",
                                 textvariable=var, bg=self.entry_bg, fg=self.fg_color, insertbackground=self.fg_color,
                                 highlightthickness=1, highlightbackground="#333")

                entry.grid(row=row, column=col, padx=5, pady=5)
                entry.var = var
                var.trace_add("write", lambda *_, r=row, c=col: self.on_entry_input(r, c))
                entry.bind("<KeyRelease>", lambda e, r=row, c=col: self.on_keypress(e, r, c))
                row_entries.append(entry)

            self.guess_entries.append(row_entries)

        self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.check_guess,
                                       bg="#333333", fg="white", font=("Arial", 12), relief="flat")
        self.submit_button.pack(pady=5)

        self.new_game_button = tk.Button(self.master, text="New Game", command=self.new_game,
                                         bg="#444444", fg="white", font=("Arial", 12), relief="flat")
        self.new_game_button.pack(pady=5)

    def on_entry_input(self, row, col):
        entry = self.guess_entries[row][col]
        value = entry.var.get().upper()[:1]
        entry.var.set(value)

        if value:
            self.play_key_sound()
            if col < 4:
                self.guess_entries[row][col + 1].focus_set()

    def on_keypress(self, event, row, col):
        if event.keysym == "BackSpace" and not self.guess_entries[row][col].get() and col > 0:
            self.guess_entries[row][col - 1].focus_set()

    def new_game(self):
        self.target_word = random.choice(self.word_list).upper()
        self.guess_count = 0

        for row in self.guess_entries:
            for entry in row:
                entry.var.set("")
                entry.config(bg=self.entry_bg, fg=self.fg_color)

        self.guess_entries[0][0].focus_set()

    def check_guess(self):
        if self.guess_count >= self.max_guesses:
            messagebox.showinfo("Game Over", f"The word was {self.target_word}")
            return

        guess = ''.join([entry.get().upper() for entry in self.guess_entries[self.guess_count]])

        if len(guess) != 5 or not guess.isalpha():
            self.shake_row(self.guess_count)
            self.play_error_sound()
            return

        feedback = ['gray'] * 5
        target_copy = list(self.target_word)

        for i in range(5):
            if guess[i] == target_copy[i]:
                feedback[i] = 'green'
                target_copy[i] = None

        for i in range(5):
            if feedback[i] != 'green' and guess[i] in target_copy:
                feedback[i] = 'yellow'
                target_copy[target_copy.index(guess[i])] = None

        for i in range(5):
            entry = self.guess_entries[self.guess_count][i]
            color = self.correct_color if feedback[i] == 'green' else \
                    self.partial_color if feedback[i] == 'yellow' else self.wrong_color
            entry.config(bg=color, fg="black")

        if guess == self.target_word:
            self.play_win_sound()
            messagebox.showinfo("You Win!", "🎉 You guessed the word!")
        elif self.guess_count == self.max_guesses - 1:
            messagebox.showinfo("Game Over", f"Game Over! The word was {self.target_word}")

        self.guess_count += 1
        if self.guess_count < self.max_guesses:
            self.guess_entries[self.guess_count][0].focus_set()

    def shake_row(self, row):
        entries = self.guess_entries[row]
        x_offset = [-3, 3, -2, 2, 0]
        for i in range(5):
            entry = entries[i]
            original_x = entry.winfo_x()
            def shake(i=i, j=0):
                if j < len(x_offset):
                    entry.place(x=original_x + x_offset[j])
                    entry.after(30, lambda: shake(i, j + 1))
                else:
                    entry.place(x=original_x)
            shake()

    def play_key_sound(self):
        winsound.MessageBeep(winsound.MB_OK)  # Beep for key

    def play_error_sound(self):
        winsound.MessageBeep(winsound.MB_ICONHAND)  # Error sound

    def play_win_sound(self):
        winsound.MessageBeep(winsound.MB_ICONASTERISK)  # Success sound


# Run game
if __name__ == "__main__":
    root = tk.Tk()
    game = WordleGame(root)
    root.mainloop()
