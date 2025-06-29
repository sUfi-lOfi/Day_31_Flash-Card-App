from tkinter import *
import pandas
import random
df = pandas.read_csv("./data/french_words.csv")
list_of_dicts = df.to_dict(orient="records")
rand_word = random.choice(list_of_dicts)

def start_guesser():
    global rand_word,flip_timer
    if not list_of_dicts:
        canvas.itemconfig(canvas_lang, text="end!!", fill="#000000")
        right_btn.config(state="disabled")
        return
    rand_word = random.choice(list_of_dicts)
    try:
        window.after_cancel(flip_timer)
    except:
        pass
    canvas.itemconfig(canvas_img,image = card_front_img)
    canvas.itemconfig(canvas_lang,text = "French",fill="#000000")
    canvas.itemconfig(canvas_word,text = rand_word["French"],fill="#000000")
    flip_timer = window.after(3000,flip_card)
def flip_card():
        canvas.itemconfig(canvas_img, image=card_back_img)
        canvas.itemconfig(canvas_lang, text="English",fill="#FFFFFF")
        canvas.itemconfig(canvas_word, text=rand_word["English"],fill="#FFFFFF")


def right():
    global list_of_dicts,df
    list_of_dicts.remove(rand_word)
    df = pandas.DataFrame(list_of_dicts)
    df.to_csv("./data/french_words.csv",index = False)
    start_guesser()


#----------------------UI Setup-------------------#
BACKGROUND_COLOR = "#B1DDC6"
#------Window Config-----#
window = Tk()
window.config(bg = BACKGROUND_COLOR,pady=50,padx=50)
window.title("Flash Card Quiz App")

#--------------Canvas Config-----------#

canvas = Canvas(height=526,width = 800,highlightthickness=0,bg = BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400,263,image = card_front_img)
canvas_lang = canvas.create_text(400,150,text="Lang",font=("Ariel",40,"italic"),fill="black")
canvas_word = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"),fill="black")

#-------------------Button-----------------#
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img,bg = BACKGROUND_COLOR,highlightthickness=0,borderwidth=0,command=start_guesser,activebackground=BACKGROUND_COLOR)
right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img,bg = BACKGROUND_COLOR,highlightthickness=0,borderwidth=0,command=right,activebackground=BACKGROUND_COLOR)

#---------------Grid Configurations--------------#
canvas.grid(row = 1,column=1,columnspan=2)
wrong_btn.grid(row = 2, column=1)
right_btn.grid(row = 2,column=2)

start_guesser()












window.mainloop()
