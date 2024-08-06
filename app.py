import random
import tkinter as tk
from PIL import Image, ImageTk
import difficultyList

chosen_word = ''
shuffled_word = ''
score = 0
counter = 0
color = 'red'


def get_shuffled_word():
    global chosen_word, shuffled_word
    chosen_word = random.choice(difficultyList.easiest_words)
    char_word = list(chosen_word)
    random.shuffle(char_word)
    shuffled_word = ''.join(char_word)


def shuffling():
    global color
    global counter
    global score
    global chosen_word, shuffled_word
    answer = user_field.get()
    if counter <= 5:
        if answer == chosen_word:
            game_end.config(text="Congrats, you found the word!")
            score += 1
            if score < 2:
                color = 'red'
            elif score >= 2 and score <= 4:
                color = 'yellow'
            else:
                color = 'green'
            game_score.config(text=f"Score: {score}/5 ", bg=color)
            get_shuffled_word()
            word_label.config(text=shuffled_word)
            word_label.pack(pady=5)

        else:
            game_end.config(text="Wrong, Try again")
            get_shuffled_word()
            word_label.config(text=shuffled_word)
            word_label.pack(pady=5)
        counter += 1
    if counter >= 5:
        verify_button.config(state="disabled")
        if score <= 2:
            game_end.config(text="Game Over, better luck next time!")
        elif 3 < score <= 4:
            game_end.config(text="Game Over, good job! ")
        elif score == 5:
            game_end.config(text="Game Over, Perfect score!")


root = tk.Tk()
root.title("Word Scramble Game")

#Image
image_path = "appPic.png"
image = Image.open(image_path)
image_resize = image.resize((400, 350))
photo = ImageTk.PhotoImage(image_resize)
image_label = tk.Label(root, image=photo)
image_label.pack(pady=5)

#Label
tk.Label(root, text="Unscramble This Word").pack(pady=5)

#Score
game_score = tk.Label(root, text=f"Score: {score}/5 ", bg=color)
game_score.place(x=320, y=365)

#Word
get_shuffled_word()
word_label = tk.Label(root, text=shuffled_word)
word_label.pack(pady=5)

#TextField
tk.Label(root, text="Enter unscrambled word").pack(pady=5)
user_field = tk.Entry(root)
user_field.pack(pady=5)

#Button
verify_button = tk.Button(root, text="Verify word", command=shuffling)
verify_button.pack(pady=5)
game_end = tk.Label(text="")
game_end.pack(pady=5)

root.mainloop()
