from tabnanny import check
import customtkinter as ctk

app = ctk.CTk()
app.title("YT Video Downloader")
app.geometry("1200x700")

entry = ctk.CTkEntry(app, placeholder_text="Paste the URL", width=800, height=40)
entry.place(x=300, y=200)

app.mainloop()