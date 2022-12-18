import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('350x150')
root.resizable(True, False)
root.title('Tkinter Entry Demo')
root.configure(background = '#d9d9d9')

email = tk.StringVar()
password = tk.StringVar()

def login_clicked():
    msg = f'You entered email: {email.get()} and password: {password.get()}'
    showinfo(title='Information', message=msg)


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# mail
email_label = ttk.Label(signin, text='Email Address:').pack(fill='x', expand=True)
email_entry = ttk.Entry(signin, textvariable=email).pack(fill='x', expand=True)

# pw
pw_label = ttk.Label(signin, text='Password:').pack(fill='x', expand=True)
pw_entry = ttk.Entry(signin, textvariable=password, show='•').pack(fill='x', expand=True)

# login btn
login_button = ttk.Button(signin, text='Login', command=login_clicked).pack(fill='x', expand=True, pady=10)


root.mainloop()
