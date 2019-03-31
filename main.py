from tkinter import *

passwords = [('wentzj', 'password1'), ('admin', 'pass')]
root = Tk()
root.title("Login Screen")


def get_password():
    pass


def login_screen():
    username_input = ""
    password_input = ""
    heading = Label(root, text="Please Sign In", font=("arial", 15, "bold"))
    heading.grid(row=0, columnspan=3)
    # this creates two labels for Name and Password to label the entry fields
    name_label = Label(root, text="Name: ")
    pass_label = Label(root, text="Password: ")

    # this creates the two entry fields for the username and password.
    username_entry = Entry(root, textvariable=username_input)
    password_entry = Entry(root, textvariable=password_input)

    # places the two labels on the windows grid in rows 1 and 2 both East aligned to the right.
    name_label.grid(row=1, sticky=E)
    pass_label.grid(row=2, sticky=E)

    # places the entry field in the first and second rows of column 2
    username_entry.grid(row=1, column=1)
    password_entry.grid(row=2, column=1)

    save_pass = Checkbutton(root, text="Keep me logged in")
    # covers two columns
    save_pass.grid(row=1, column=2)

    submit_username = Button(root, text="Submit")
    submit_username.grid(row=2, column=2)

    return username_input, password_input


username, password = login_screen()
print("Username: " + str(passwords[0][0]) + "\nPassword: " + str(passwords[0][1]))

root.mainloop()

