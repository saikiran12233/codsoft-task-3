import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("password creator")
        self.root.geometry('470x210+200+150')

        self.label=tk.Label(root,text='Password Generator',
             font=("Comic Sans MS",15),width=60,bd=5,bg='red', fg='black')
        self.label.pack(side='top')

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.place(x=100,y=70)

        self.username_entry = tk.Entry(root)
        self.username_entry.place(x=320,y=70)

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.place(x=100,y=100)

        self.length_entry = tk.Entry(root)
        self.length_entry.place(x=320,y=100)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password,bd=5,bg='skyblue', fg='black',font=("sarif",10))
        self.generate_button.pack(side='bottom')

        self.password_label = tk.Label(root, text="")
        self.password_label.pack(side='bottom')

    def generate_password(self):
        username = self.username_entry.get()
        length = self.length_entry.get()

        if not length.isdigit():
            messagebox.showerror("Error", "Please enter a valid number for password length.")
            return

        length = int(length)
        if length <= 0:
            messagebox.showerror("Error", "Password length should be greater than 0.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=f"Generated Password for {username}: {password}")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()