import requests, validators
from customtkinter import filedialog
from pytube import YouTube

def valid_url(url):
    if validators.url(url) and YouTube(url):
        return True
    return False
    
def first_check(entry_folder, entry_link, invalid_url_label):
    url = entry_link.get()
    if not valid_url(url):
        invalid_url_label.configure(text="Invalid URL")
        return
    invalid_url_label.configure(text="")
    folder = filedialog.askdirectory()
    entry_folder.configure(state='normal')
    entry_folder.insert(0, folder)
    entry_folder.configure(state='disabled')


def download_video(url, path):
    try:
        video = YouTube(url).streams.get_highest_resolution()
        if video is not None:
            video.download(path)
    except Exception as e:
        print(e)
