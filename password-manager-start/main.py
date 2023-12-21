import tkinter
from tkinter import *
from tkinter import messagebox
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = []
    while len(password) < 14:
        if len(password) < 4:
            password.append(random.choice(ascii_lowercase))
            password.append(random.choice(ascii_uppercase))
            password.append(random.choice(digits))
            password.append(random.choice(punctuation))

        else:
            string_pick = random.randint(1, 5)
            if string_pick == 1:
                password.append(random.choice(ascii_lowercase))
            if string_pick == 2:
                password.append(random.choice(ascii_uppercase))
            if string_pick == 3:
                password.append(random.choice(digits))
            if string_pick == 4 or string_pick == 5:
                password.append(random.choice(punctuation))
    random.shuffle(password)
    result = "".join(password)
    password_entry.insert(0, result)
    pyperclip.copy(result)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()

    if len(website) and len(password) > 0:
        message = messagebox.askokcancel(website,
                                         f"Entered info:\nwebsite: {website}\npassword: {password}\nIs it ok to save?")
        if message:
            with open("data.txt", "a") as pfile:
                pfile.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showwarning(title="oops", message="Please don't leave any field empty")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo_image = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
#
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "hi@bye.ca")
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

gen_button = Button(text="Generate", command=generate_password)
gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=21, command=save)
add_button.grid(row=4, column=1)
window.mainloop()
