import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(100,100)
window.config(padx=50,pady=50)

def button_clicked():
    miles = float(miles_entry.get())
    new_text = str(miles*1.609)
    km_label.config(text=new_text)

miles_entry = tkinter.Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=("Arial", 12, "normal"))
miles_label.grid(column=2,row=0)

text_label = tkinter.Label(text="is equal to", font=("Arial", 12, "normal"))
text_label.grid(column=0,row=1)
text_label.config(padx=5, pady=5)

km_label = tkinter.Label(text="0", font=("Arial", 12, "normal"))
km_label.grid(column=1,row=1)
km_label.config(padx=5, pady=5)

km_text_label = tkinter.Label(text="Km", font=("Arial", 12, "normal"))
km_text_label.grid(column=2,row=1)
km_text_label.config(padx=5, pady=5)


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)
button.config(padx=5, pady=5)

window.mainloop()
