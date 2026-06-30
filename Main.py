import customtkinter as ctk
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

    # Clear the entry fields
    Title_Entry.delete(0, ctk.END)
    User_Entry.delete(0, ctk.END)
    Password_Entry.delete(0, ctk.END)
    Website_Entry.delete(0, ctk.END)

    # Success message
    messagebox.showinfo("Success", "Data saved successfully!")

# GUI Tkinter -----------------------------------------------------------------------------------------------------------------------------

root = ctk.CTk()
root.title("Password Manager")
root.geometry("600x600")

App_Name = ctk.CTkLabel(
    root,
    text ="Password Manager Tool",
    font=("Arial", 20, "bold")
    ).pack(pady=90)

Title_Name = ctk.CTkLabel(root, text ="Enter Title", font=("Arial", 12)).pack(pady=2)
Title_Entry = ctk.CTkEntry(root)
Title_Entry.pack(pady=5)

User_Name = ctk.CTkLabel(root, text ="Enter Username", font=("Arial", 12)).pack(pady=2)
User_Entry = ctk.CTkEntry(root)
User_Entry.pack(pady=5)

Password_Lable = ctk.CTkLabel(root, text ="Enter Password", font=("Arial", 12)).pack(pady=2)
Password_Entry = ctk.CTkEntry(root)
Password_Entry.pack(pady=5)

Website_Lable = ctk.CTkLabel(root, text ="Enter Website Link", font=("Arial", 12)).pack(pady=2)
Website_Entry = ctk.CTkEntry(root)
Website_Entry.pack(pady=5)

submit_btn = ctk.CTkButton(
    root,
    text ="Submit",
    command= submit
    ) 
submit_btn.pack(pady=10)


root.mainloop()
