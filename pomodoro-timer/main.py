from tkinter import *
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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# we want to put the image on the screen - we do this with canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pic= PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=pic)
canvas.create_text(100, 130, text ="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)
title=Label(text ="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN)
title.grid(row=0,column=1)
start= Button(text="Start", font=(FONT_NAME, 12, "normal"))
start.grid(row=2, column=0)
reset= Button(text="Reset", font=(FONT_NAME, 12, "normal"))
reset.grid(row=2, column=2)
checkmark= Label(text="✔", font=(FONT_NAME, 40, "normal"), fg=GREEN)
checkmark.grid(row=2, column=1)


window.mainloop()