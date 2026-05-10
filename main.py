from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=220, width=220)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(110, 110, image=mypass_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label( text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=27)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=39)
add_button.grid(row=4, column=1, columnspan=3)

window.mainloop()