from tkinter import * 
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random

def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letters=[random.choice(letters) for _ in range(nr_letters)]
    pass_symb=[random.choice(symbols) for _ in range(nr_symbols)]
    pass_num=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list=pass_letters+pass_symb+pass_num
    random.shuffle(password_list)
    password ="".join(password_list)

    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    
    website=web_input.get()
    email = email_input.get()
    passwd= pass_input.get()
    new_data={website:{
        "email":email,
        "password":passwd

    }}
   

    if len(website) == 0 or len(passwd) ==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you've provided: \n Email: {email} \n Password: {passwd}\n Is it okay to save?")
        if is_ok:
            ## split into one read where u can update and one write 
            try:
                with open("python\\small-python-projects\\password-manager\\pass_file.json", "r") as data_file:
                # reading the old data 
                    print("problem here")
                    data = json.load(data_file)
                    
            except FileNotFoundError:
                with open("python\\small-python-projects\\password-manager\\pass_file.json", "w") as data_file:
                        json.dump(new_data, data_file, indent =4)
            else:
                #updating old data 
                print('made it to the else')
                data.update(new_data)
                with open("python\\small-python-projects\\password-manager\\pass_file.json", "w") as data_file:
                    #saving updated data 
                    json.dump(data, data_file, indent =4)
            finally:        
                web_input.delete(0, END)
                pass_input.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

pic= PhotoImage(file='python\\small-python-projects\\password-manager\\logo.png')
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

pass_button= Button(text= "Generate Password", command=gen_password)
pass_button.grid(row=3, column=2)

add_button=Button(text="Add", width=36, command=add_to_file)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()