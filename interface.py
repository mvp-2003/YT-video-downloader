import customtkinter as ctk
from functions import first_check

ctk.set_default_color_theme("green")
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("YT Video Downloader")
app.geometry("1200x700")

entry_link = ctk.CTkEntry(app, placeholder_text="Paste the URL", width=800, height=40)
entry_link.place(x=375, y=125)

entry_folder = ctk.CTkEntry(app, placeholder_text="Choose the folder to download", width=800, height=40)
entry_folder.place(x=375, y=175)
entry_folder.configure(state='disabled')

invalid_url_label = ctk.CTkLabel(app, text="", fg_color="gray", font=("Arial", 16))
invalid_url_label.place(x=1185, y=125)

select_button = ctk.CTkButton(app, text="Choose folder", width=80, height=40, command=lambda: first_check(entry_folder, entry_link, invalid_url_label))
select_button.place(x=1185, y=175)

upload_button = ctk.CTkButton(app, text="Select", width=60, height=45)
upload_button.place(x=775, y=225)

selected_link = ctk.CTkLabel(app, text="URL: ", font=("Arial", 16))
selected_link.place(x=320, y=300)

selected_folder = ctk.CTkLabel(app, text="Folder: ", font=("Arial", 16))
selected_folder.place(x=320, y=350)

selected_link_value = ctk.CTkLabel(app, text="", fg_color="gray", font=("Arial", 14), height=30, width=800)
selected_link_value.place(x=375, y=300)

selected_folder_value = ctk.CTkLabel(app, text="", fg_color="gray", font=("Arial", 14), height=30, width=800)
selected_folder_value.place(x=375, y=350)

app.mainloop()