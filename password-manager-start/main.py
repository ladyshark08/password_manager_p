import tkinter
from tkinter import *
from tkinter import messagebox
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random
import pyperclip
import json


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


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()

    try:
        with open("data.json") as data:
            password_file = json.load(data)
            password = password_file[website]["password"]
            email = password_file[website]["email"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
    except KeyError:
        messagebox.showinfo(title=f"Error", message=f"No details for the {website} exists")
    except FileNotFoundError:
        messagebox.showinfo(title=f"Error", message=f"No Data File found")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {"email": username,
                  "password": password
                  }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="oops", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as pfile:
                data_file = json.load(pfile)
                data_file.update(new_data)

            with open("data.json", "w") as pfile:
                json.dump(data_file, pfile, indent=4)

        except FileNotFoundError:
            with open("data.json", "w") as pfile:
                json.dump(new_data, pfile, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(title="Success", message=f"Added {website} to the data storage")


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
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

gen_button = Button(text="Generate", command=generate_password)
gen_button.grid(row=3, column=3)
add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1)

search_button = Button(text="Search", command=search_password)
search_button.grid(row=1, column=3)
window.mainloop()
