import tkinter

window= tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=100)

# first we have to create a component and then put it somehwere
# # pack puts it on the screen - takes params on layout
# .place()  will give u more finseese
# grid is beautiful 

def button_clicked():
    
    answer=float(input.get()) * 1.609
    conversion.config(text=answer)


input = tkinter.Entry()
input.grid(column=1,row=0)
answer=input.get()

conversion = tkinter.Label(text="0", font=("Arial", 24, "bold"))
conversion.grid(column=1,row=1)

equal_to = tkinter.Label(text="is equal to", font=("Arial", 24, "bold"))
equal_to.grid(column=0, row=1)

miles=tkinter.Label(text="miles", font=("Arial", 24, "bold"))
miles.grid(column=2,row=0)

km=tkinter.Label(text="Km", font=("Arial", 24, "bold"))
km.grid(column=2,row=1)

button=tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)



#entry component




window.mainloop()