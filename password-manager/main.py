from tkinter import * 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

pic= PhotoImage(file='logo.png')
canvas= Canvas(height=200, width=200, highlightthickness=0)
canvas.create_image(100,100,image=pic)
canvas.grid(row=0, column=0)
window.mainloop()