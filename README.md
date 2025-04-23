# wordle

A fun and interactive Wordle-style game built using Python's Tkinter library. Inspired by the popular word puzzle game, this version lets you guess a 5-letter word in 6 attempts with visual feedback and sound effects.

🖼️ Features
🎨 Dark Theme UI with visual feedback:

🟩 Green: Correct letter in the correct position

🟨 Yellow: Correct letter in the wrong position

⬛ Gray: Incorrect letter

🔊 Sound Effects:

Key press

Error input

Win alert

⌨️ Keyboard Navigation:

Auto-focus to the next cell

Backspace moves to previous cell if current is empty

🔁 New Game Button for fresh challenges

❗ Input validation with shake animation on invalid guesses

🛠️ Requirements
Python 3.7.x

Windows OS (due to use of winsound module)

🚀 How to Run
Clone the repository or download the .py file.

Run the game:

bash
Copy
Edit
python wordle_game.py
Ensure you're on Windows, or replace winsound with cross-platform alternatives like playsound or pygame.

🧠 Gameplay Rules
Enter a valid 5-letter word using the on-screen entries.

You have 6 attempts to guess the hidden word.

Submit the guess using the Submit Guess button.

A new word can be generated with the New Game button.

📦 Word Bank
The game includes a built-in list of over 60 common English words. You can easily customize or extend it in the self.word_list section of the code.

📸 Screenshot

⚠️ Known Issues
winsound is not available on non-Windows platforms.

Words are case-insensitive, but entry forces uppercase.

🧑‍💻 Author
Developed with ❤️ using Python and Tkinter.
