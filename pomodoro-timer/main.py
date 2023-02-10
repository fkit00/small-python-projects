from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def on_start():
    count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60 

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
       window.after(1000, count_down, count-1)


# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# this helps with the countdown 




# we want to put the image on the screen - we do this with canvas

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pic= PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=pic)
timer_text = canvas.create_text(100, 130, text ="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

title=Label(text ="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN)
title.grid(row=0,column=1)
start= Button(text="Start", font=(FONT_NAME, 12, "normal"), highlightthickness=0, command=on_start)
start.grid(row=2, column=0)
reset= Button(text="Reset", font=(FONT_NAME, 12, "normal"),highlightthickness=0)
reset.grid(row=2, column=2)
checkmark= Label(text="✔", font=(FONT_NAME, 20, "normal"), fg=GREEN)
checkmark.grid(row=2, column=1)


window.mainloop()