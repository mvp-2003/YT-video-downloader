import customtkinter as ctk

app = ctk.CTk()
app.title("YT Video Downloader")
app.geometry("1200x700")

entry = ctk.CTkEntry(app, placeholder_text="Paste the URL", width=800, height=40)
entry.place(x=300, y=200)

button = ctk.CTkButton(app, text = "Select", fg_color="green")
button.place(x=1150, y=205)

labelurl = ctk.CTkLabel(app, text = "URL", fg_color="black", bg_color="gray", height=40, width=800)
labelurl.place(x=200, y=250)

app.mainloop()