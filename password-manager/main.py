from tkinter import * 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
     f = open("pass_file.txt", "a")
     website=web_input.get()
     email = email_input.get()
     passwd= pass_input.get()
     f.write(f"{website}||{email}||{passwd}\n")
     f.close
     web_input.delete(0, END)
     pass_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

pic= PhotoImage(file='logo.png')
canvas= Canvas(height=200, width=200, highlightthickness=0)
canvas.create_image(100,100,image=pic)
canvas.grid(row=0, column=1)

web_label = Label(text="Website: ")
web_label.grid(row=1, column=0)

web_input = Entry(width=35)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus() # lands the cursor here


email_label= Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

email_input=Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)

email_input.insert(0, "fake.email@fakeemail.com")

pass_label= Label(text="Password: ")
pass_label.grid(row=3, column=0)

pass_input=Entry(width=21)
pass_input.grid(row=3, column=1)

pass_button= Button(text= "Generate Password")
pass_button.grid(row=3, column=2)

add_button=Button(text="Add", width=36, command=add_to_file)
add_button.grid(row=4, column=1, columnspan=2)








window.mainloop()