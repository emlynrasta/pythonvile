from tkinter import *


def register_user():
    username_info = username.get()
    email_info = email.get()
    password_info = password.get()

    with open('user_infor.txt', 'a') as data_file:
        data_file.write(f"{username_info} || {email_info} || {password_info}\n")

    username_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen_1, text='Registration success', fg='green', font=('calibri', 11)).pack()


def register():
    global screen_1
    global username, email, password
    global username_entry, email_entry, password_entry

    screen_1 = Toplevel(screen)
    screen_1.geometry('300x250')
    screen_1.title('Register')

    username = StringVar()
    email = StringVar()
    password = StringVar()

    Label(screen_1, text='Please enter your details below! ').pack()
    Label(screen_1, text='').pack()
    Label(screen_1, text='Username').pack()
    username_entry = Entry(screen_1, textvariable=username)
    username_entry.focus()
    username_entry.pack()
    Label(screen_1, text='Email').pack()
    email_entry = Entry(screen_1, textvariable=email)
    email_entry.pack()
    Label(screen_1, text='Password').pack()
    password_entry = Entry(screen_1, textvariable=password)
    password_entry.pack()
    Label(screen_1, text='').pack()
    Button(screen_1, text='Register', width='10', height='1', command=register_user).pack()


def login():
    pass


def main_screen():
    global screen

    screen = Tk()
    screen.geometry('300x250')
    screen.title('Notes 1.0')
    Label(text='Notes 1.0', bg='grey', width='300', height='2', font=('Calibri', 13)).pack()
    Label(text='').pack()
    Button(text='Login', height='2', width='30', command=login).pack()
    Label(text='').pack()
    Button(text='Register', height='2', width='30', command=register).pack()

    screen.mainloop()


main_screen()
