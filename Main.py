import tkinter as tk
import json
from tkinter import messagebox

# JSON ---------------------------------------------------------------------------------------------------------------------------------

try:
    with open('Logins.json', 'r') as f:
        data = json.load(f) 
except:
    data = [] 

# Functions ---------------------------------------------------------------------------------------------------------------------------------

def submit():
    Title = Title_Entry.get()
    Username = User_Entry.get()
    Password = Password_Entry.get()
    Website = Website_Entry.get()

    new_login = {
    "Title" : Title,
    "Username" : Username,
    "Password" : Password,
    "Website" : Website
    }

    data.append(new_login)

    with open('Logins.json', 'w') as f:
        json.dump(data, f, indent=4)

    # 4. Clear the entry fields
    Title_Entry.delete(0, tk.END)
    User_Entry.delete(0, tk.END)
    Password_Entry.delete(0, tk.END)
    Website_Entry.delete(0, tk.END)

    # Success message
    messagebox.showinfo("Success", "Data saved successfully!")

# GUI Tkinter -----------------------------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title("Password Manager")
root.geometry("600x600")

App_Name = tk.Label(
    root,
    text ="Password Manager Tool",
    font=("Arial", 20, "bold")
    ).pack(pady=90)

Title_Name = tk.Label(root, text ="Enter Title", font=("Arial", 12)).pack(pady=2)
Title_Entry = tk.Entry(root)
Title_Entry.pack(pady=5)

User_Name = tk.Label(root, text ="Enter Username", font=("Arial", 12)).pack(pady=2)
User_Entry = tk.Entry(root)
User_Entry.pack(pady=5)

Password_Lable = tk.Label(root, text ="Enter Password", font=("Arial", 12)).pack(pady=2)
Password_Entry = tk.Entry(root)
Password_Entry.pack(pady=5)

Website_Lable = tk.Label(root, text ="Enter Website Link", font=("Arial", 12)).pack(pady=2)
Website_Entry = tk.Entry(root)
Website_Entry.pack(pady=5)

submit_btn = tk.Button(
    root,
    text ="Submit",
    command= submit
    ) 
submit_btn.pack(pady=10)

root.mainloop()
