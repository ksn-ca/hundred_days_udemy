from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
timer = None
current_card = {}


try:
    data = pd.read_csv('data/words_to_learn.csv').to_dict(orient='records')
except FileNotFoundError:    
    data = pd.read_csv('data/french_words.csv').to_dict(orient='records')


def new_word():
    global timer, current_card
    current_card = random.choice(data)
    canvas.itemconfig(flashcard, image=img)
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    canvas.itemconfig(language_text, text='French', fill='black')

    timer = window.after(3000, show_back)


def show_back():
    global timer, current_card
    window.after_cancel(timer)
    canvas.itemconfig(flashcard, image=back_img)
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')
    canvas.itemconfig(language_text, text='English', fill='white')

def learned_word():
    global current_card
    data.remove(current_card)
    df = pd.DataFrame(data=data)
    df.to_csv('data/words_to_learn.csv', index=False)
    new_word()



window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard = canvas.create_image(400, 263, image=img)
language_text = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file='images/right.png')
right_btn = Button(image=right_img, highlightthickness=0, command=learned_word)
right_btn.grid(row=1, column=0)

wrong_img = PhotoImage(file='images/wrong.png')
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=new_word)
wrong_btn.grid(row=1, column=1)



new_word()




window.mainloop()


