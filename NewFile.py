import customtkinter as ctk

# -------------------- App Setup --------------------
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Modern Password Manager Dashboard")
app.geometry("1100x650")
app.configure(fg_color="#14161a")  # Deep dark backdrop

# Configure main layout: 2 columns (Sidebar and Content Area)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Style Configuration Constants
FONT_FAMILY = "Segoe UI"
COLOR_SIDEBAR = "#1a1c23"
COLOR_CONTENT_BG = "#14161a"
COLOR_CARD_BG = "#21242c"
COLOR_INPUT_BG = "#1a1c23"
COLOR_PRIMARY_BLUE = "#2575fc"
COLOR_TEXT_MUTED = "#8a909a"

pages = {}
sidebar_buttons = {}

def show_page(page_name):
    """Handles switching pages and updating sidebar button active states."""
    # Hide all pages
    for page in pages.values():
        page.grid_remove()
    
    # Reset all sidebar button styles
    for name, btn in sidebar_buttons.items():
        if name == page_name:
            btn.configure(fg_color="#282c37", text_color="#ffffff")
        else:
            btn.configure(fg_color="transparent", text_color=COLOR_TEXT_MUTED)
            
    # Show target page
    pages[page_name].grid(row=0, column=0, sticky="nsew")

# -------------------- Sidebar Frame --------------------
sidebar = ctk.CTkFrame(master=app, width=220, corner_radius=0, fg_color=COLOR_SIDEBAR, border_width=0)
sidebar.grid(row=0, column=0, sticky="nsew")
sidebar.grid_propagate(False)

# Sidebar Title
sidebar_title = ctk.CTkLabel(
    sidebar, 
    text="DASHBOARD", 
    font=(FONT_FAMILY, 20, "bold"), 
    text_color=COLOR_PRIMARY_BLUE
)
sidebar_title.pack(pady=(40, 30), padx=25, anchor="w")

# Helper function to generate uniform menu buttons
def create_menu_btn(text_name):
    btn = ctk.CTkButton(
        sidebar, 
        text=f"  {text_name}", 
        font=(FONT_FAMILY, 14, "normal"),  # <-- FIXED: Changed "medium" to "normal"
        height=42,
        corner_radius=8,
        fg_color="transparent",
        text_color=COLOR_TEXT_MUTED,
        hover_color="#22252e",
        anchor="w", 
        command=lambda: show_page(text_name)
    )
    btn.pack(fill="x", padx=15, pady=6)
    sidebar_buttons[text_name] = btn

# Create menu items
create_menu_btn("Home")
create_menu_btn("Password Manager")
create_menu_btn("About")

# -------------------- Content Container --------------------
content_container = ctk.CTkFrame(master=app, fg_color=COLOR_CONTENT_BG)
content_container.grid(row=0, column=1, sticky="nsew", padx=30, pady=30)
content_container.grid_rowconfigure(0, weight=1)
content_container.grid_columnconfigure(0, weight=1)

# Generate page shells
pages["Home"] = ctk.CTkFrame(master=content_container, fg_color="transparent")
pages["Password Manager"] = ctk.CTkFrame(master=content_container, fg_color="transparent")
pages["About"] = ctk.CTkFrame(master=content_container, fg_color="transparent")

# -------------------- 1. Home Page --------------------
label_home = ctk.CTkLabel(master=pages["Home"], text="Welcome to the Home Screen", font=(FONT_FAMILY, 22, "bold"), text_color="#ffffff")
label_home.pack(pady=50, padx=50, anchor="w")

# -------------------- 2. Password Manager Page (Modern Form) --------------------
# Center alignment configuration
pages["Password Manager"].grid_rowconfigure(0, weight=1)
pages["Password Manager"].grid_columnconfigure(0, weight=1)

# Password Manager Card Container
card = ctk.CTkFrame(master=pages["Password Manager"], corner_radius=16, fg_color=COLOR_CARD_BG, border_width=1, border_color="#2d313b")
card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
card.grid_rowconfigure(0, weight=1)
card.grid_columnconfigure(0, weight=1)

# Inner Grid Form
form = ctk.CTkFrame(card, fg_color="transparent")
form.grid(row=0, column=0, padx=50, pady=40)

# Main Title
title = ctk.CTkLabel(
    form, 
    text="Save Your Password", 
    font=(FONT_FAMILY, 26, "bold"),
    text_color="#ffffff"
)
title.grid(row=0, column=0, columnspan=2, pady=(0, 35))

# Setup structural parameters matching the UI design
fields_data = [
    {"name": "Username", "placeholder": "Enter username...", "show": None},
    {"name": "Email", "placeholder": "e.g., example@email.com", "show": None},
    {"name": "Password", "placeholder": "••••••••", "show": "*"},
    {"name": "API Key", "placeholder": "Enter API key...", "show": None},
    {"name": "Token Length", "placeholder": "16", "show": None}
]

entries = {}

for i, field in enumerate(fields_data, start=1):
    # Field Label
    label = ctk.CTkLabel(
        form, 
        text=field["name"], 
        font=(FONT_FAMILY, 14),
        text_color="#d1d4db",
        width=140, 
        anchor="w"
    )
    label.grid(row=i, column=0, padx=(0, 30), pady=12, sticky="w")

    # Form Text Entry
    entry = ctk.CTkEntry(
        form, 
        width=320, 
        height=38,
        font=(FONT_FAMILY, 13),
        fg_color=COLOR_INPUT_BG,
        border_color="#2e323d",
        border_width=1,
        text_color="#ffffff",
        placeholder_text=field["placeholder"],
        placeholder_text_color="#565c66",
        corner_radius=8,
        show=field["show"]
    )
    entry.grid(row=i, column=1, pady=12)
    entries[field["name"]] = entry

# Modern Primary Action Button
save_btn = ctk.CTkButton(
    form, 
    text="Save Changes", 
    font=(FONT_FAMILY, 14, "bold"),
    fg_color=COLOR_PRIMARY_BLUE,
    hover_color="#1a62de",
    text_color="#ffffff",
    width=200, 
    height=40,
    corner_radius=8
)
save_btn.grid(row=len(fields_data) + 1, column=0, columnspan=2, pady=(35, 0))

# -------------------- 3. About Page --------------------
label_about = ctk.CTkLabel(master=pages["About"], text="System Password Manager Panel\nVersion 1.0.0", font=(FONT_FAMILY, 14), text_color=COLOR_TEXT_MUTED, justify="left")
label_about.pack(pady=50, padx=50, anchor="w")

# -------------------- Application Loop initialization --------------------
# Present Password Manager by default to reflect the target mockup state
show_page("Password Manager")

app.mainloop()
