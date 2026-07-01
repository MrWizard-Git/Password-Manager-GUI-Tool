import customtkinter as ctk

# -------------------- App Setup --------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Modern App with Settings")
app.geometry("900x650")  # Bumped up height slightly to comfortably fit the form

# -------------------- Main Tabview --------------------
tabview = ctk.CTkTabview(master=app)
tabview.pack(padx=20, pady=20, fill="both", expand=True)

# Add tabs
tabview.add("Home")
tabview.add("Settings")
tabview.add("About")

# -------------------- 1. Home Tab --------------------
label_home = ctk.CTkLabel(master=tabview.tab("Home"), text="Welcome to the Home Screen!", font=("Segoe UI", 18))
label_home.pack(pady=40)

# -------------------- 2. Settings Tab (Merged Form) --------------------
# Configure the Settings tab layout to center the card
tabview.tab("Settings").grid_rowconfigure(0, weight=1)
tabview.tab("Settings").grid_columnconfigure(0, weight=1)

# Center Card inside the Settings Tab
card = ctk.CTkFrame(master=tabview.tab("Settings"), corner_radius=20)
card.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")

# Center everything inside the card
card.grid_rowconfigure(0, weight=1)
card.grid_columnconfigure(0, weight=1)

# Inner Form Container
form = ctk.CTkFrame(card, fg_color="transparent")
form.grid(row=0, column=0)

# Title inside Form
title = ctk.CTkLabel(
    form,
    text="User Settings",
    font=("Segoe UI", 24, "bold")
)
title.grid(row=0, column=0, columnspan=2, pady=(0, 30))

# Form Fields
fields = [
    "Username",
    "Email",
    "Password",
    "API Key",
    "Token Length"
]

entries = {}

for i, field in enumerate(fields, start=1):
    # Left-aligned labels
    label = ctk.CTkLabel(
        form,
        text=field,
        width=130,
        anchor="w"
    )
    label.grid(row=i, column=0, padx=(0, 20), pady=10, sticky="w")

    # Entry (Hides text if it's the password field)
    show_char = "*" if field == "Password" else None
    entry = ctk.CTkEntry(form, width=280, height=35, show=show_char)
    entry.grid(row=i, column=1, pady=10)
    entries[field] = entry

# Save Button
save_btn = ctk.CTkButton(
    form,
    text="Save Changes",
    width=180,
    height=38
)
save_btn.grid(
    row=len(fields) + 1,
    column=0,
    columnspan=2,
    pady=(30, 0)
)

# -------------------- 3. About Tab --------------------
label_about = ctk.CTkLabel(master=tabview.tab("About"), text="Version 1.0.0", font=("Segoe UI", 14))
label_about.pack(pady=40)

# -------------------- App Loop --------------------
app.mainloop()
