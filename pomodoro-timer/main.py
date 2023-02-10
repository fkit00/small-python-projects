from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def on_start():
    global reps
    reps += 1
    work_secs= WORK_MIN * 60
    short_break = SHORT_BREAK_MIN*60
    long_break= LONG_BREAK_MIN*60
    if reps % 8 ==0:
        count_down(long_break)
        title.config(text="Break", fg=RED)
    elif reps % 2 ==0:
        count_down(short_break)
        title.config(text="Break", fg=PINK)
        
    else:
        count_down(work_secs)
        title.config(text="Work", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec ==0:
        count_sec="00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
       window.after(1000, count_down, count-1)
    else:
        on_start()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark +="✔",
            checkmark.config(text=mark)




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
checkmark= Label(text="", font=(FONT_NAME, 20, "normal"), fg=GREEN)
checkmark.grid(row=2, column=1)


window.mainloop()