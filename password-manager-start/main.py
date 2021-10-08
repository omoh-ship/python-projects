from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = u_name_entry.get()
    password = password_entry.get()
    data = f"{website} | {username} | {password}\n"

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Oops", message="You left an input box empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail: {username} "
                                                              f"\nPassword: {password} \n\nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(data)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

u_name_label = Label(text="Email/Username:")
u_name_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


# Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

u_name_entry = Entry(width=35)
u_name_entry.grid(row=2, column=1, columnspan=2)
u_name_entry.insert(0, "gloriaisedu@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


# Button
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2)

add = Button(text="Add",command=save, width=36)
add.grid(row=4, column=1, columnspan=2)



window.mainloop()
