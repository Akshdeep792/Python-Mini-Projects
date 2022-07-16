import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=600, height=400)
window.config(padx = 20, pady= 20)


# Label

my_label = tkinter.Label(text="I Am a Label", font=("Aerial", 24, "bold"))
my_label.pack(side="left")



# button

def button_clicked():
    # my_label["text"] = "I am the new Label"
    new_text = entry.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

entry = tkinter.Entry(width=18)
entry.pack()
# instead of pack use grid or place. Grid is more flexible 


window.mainloop()