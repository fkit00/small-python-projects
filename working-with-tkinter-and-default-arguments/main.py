import tkinter

window= tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# first we have to create a component and then put it somehwere
my_label = tkinter.Label(text='I am a label', font=("Arial", 24, "bold"))
# pack puts it on the screen 
my_label.pack()

input = tkinter.Entry()
input.pack()
answer=input.get()

def button_clicked():
    print("i got clicked")
    answer=input.get()
    my_label.config(text=answer)

button=tkinter.Button(text="Click me", command=button_clicked)
button.pack()

#entry component




window.mainloop()