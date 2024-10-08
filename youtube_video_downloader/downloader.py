import customtkinter as ctk
from functions import *
import threading
import logging

logging.basicConfig(level=logging.INFO)

ctk.set_default_color_theme("green")
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("YT Video Downloader")
app.geometry("1200x700")

try:
    app.iconbitmap("Logo.ico")
except Exception as e:
    logging.warning(f"Could not set icon: {e}")

entry_link = ctk.CTkEntry(app, placeholder_text="Paste the URL", width=800, height=40)
entry_link.place(x=375, y=200)

entry_folder = ctk.CTkEntry(app, placeholder_text="Choose the folder to download", width=800, height=40)
entry_folder.place(x=375, y=300)
entry_folder.configure(state='disabled')

invalid_url_label = ctk.CTkLabel(app, text="", text_color="red", font=("Arial", 16))
invalid_url_label.place(x=1185, y=200)

select_button = ctk.CTkButton(app, text="Choose folder", width=80, height=40, command=lambda: first_check(entry_folder, entry_link, invalid_url_label))
select_button.place(x=1185, y=300)

upload_button = ctk.CTkButton(app, text="Select", width=60, height=45, command=lambda: finalize(selected_link_value, selected_folder_value, entry_link, entry_folder, download_button, invalid_url_label))
upload_button.place(x=775, y=350)

selected_link = ctk.CTkLabel(app, text="URL: ", font=("Arial", 16))
selected_link.place(x=320, y=425)

selected_folder = ctk.CTkLabel(app, text="Folder: ", font=("Arial", 16))
selected_folder.place(x=320, y=475)

selected_link_value = ctk.CTkLabel(app, text="", fg_color="gray", font=("Arial", 14), height=30, width=800)
selected_link_value.place(x=375, y=425)

selected_folder_value = ctk.CTkLabel(app, text="", fg_color="gray", font=("Arial", 14), height=30, width=800)
selected_folder_value.place(x=375, y=475)

download_button = ctk.CTkButton(app, text="Download", width=60, height=45, command=lambda: download_video(selected_link_value.cget("text"), selected_folder_value.cget("text"), final_message_box))
download_button.place(x=775, y=525)
download_button.configure(state='disabled')

final_message_box = ctk.CTkLabel(app, text="", font=("Arial", 16), height=30, width=800)
final_message_box.place(x=400, y=625)

def on_close(event=None):
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_close)

if __name__ == "__main__":
    app.mainloop()