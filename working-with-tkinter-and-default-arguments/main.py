import tkinter

window= tkinter.Tk()
window.title("My first GUI program")

# first we have to create a component and then put it somehwere
my_label = tkinter.label(text='I am a label')
# pack puts it on the screen 
my_label.pack()


window.mainloop()