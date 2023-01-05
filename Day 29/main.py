"""Password Manager"""
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import random
import string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password(length=16):
    """Generates A Random Password
        Args:
            length (int): The length of the generated password. Default is 16.

        Returns:
            str: The generated password."""
    letters = string.ascii_letters
    numbers = string.digits
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate the desired number of letters, numbers, and symbols
    password_chars = random.choices(letters, k=length // 2) + random.choices(numbers, k=length // 4) + random.choices(symbols, k=length // 4)

    # Shuffle the characters
    random.shuffle(password_chars)

    # Join the characters into a single string
    password = "".join(password_chars)

    password_entry.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    """Adds Password to File"""
    website_save = web_entry.get()
    email_save = email_entry.get()
    password_save = password_entry.get()

    if len(website_save) == 0 or len(email_save) == 0 or len(password_save) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields blank!")
    else:
        is_ok = messagebox.askokcancel(title=website_save, message=f"These are the "
            f"details entered: \nEmail: {email_save}\nPassword: {password_save}\nIs it ok to save?")
    if is_ok:
        with open("passwords.txt", "a", encoding="utf-8") as file:
            file.write(f"{website_save} | {email_save} | {password_save}\n")
        web_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas with Logo
img = PhotoImage(file="logo.png")
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100, image=img)
canvas.grid(column=1, row=0)

#Labels
website = Label(text="Website:")
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

#Buttons
generate_random_password = Button(text="Generate Password",width=18,
command=generate_random_password)
generate_random_password.grid(column=2, row=3, sticky=(W))

add_password = Button(text="Add", width=60, command=add_to_file)
add_password.grid(column=1, row=4, columnspan=2, sticky=(W))

#Entries
web_entry = Entry(width=60)
web_entry.grid(column=1, row=1, columnspan=2, sticky=(W))
web_entry.focus()

email_entry = Entry(width=60)
email_entry.grid(column=1, row=2, columnspan=2, sticky=(W))
email_entry.insert(0,"example@email.com")

password_entry = Entry(width=40)
password_entry.grid(column=1, row=3,sticky=(W))

window.mainloop()
