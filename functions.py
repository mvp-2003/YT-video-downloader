import requests, validators
from customtkinter import filedialog
from urllib.parse import urlparse, parse_qs
from pytube import YouTube

def valid_url(url):
    if not validators.url(url):
        return False
    
    parsed_url = urlparse(url)
    if parsed_url.netloc not in ['www.youtube.com', 'youtu.be']:
        return False
    query = parse_qs(parsed_url.query)
    if 'v' not in query:
        return False
    response = requests.get(url)
    if response.status_code != 200:
        return False
    return True
    
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

def finalize(selected_link_value, selected_folder_value, entry_link, entry_folder):
    selected_link_value.configure(text=entry_link.get())
    selected_folder_value.configure(text=entry_folder.get())


def download_video(url, path):
    try:
        video = YouTube(url).streams.get_highest_resolution()
        if video is not None:
            video.download(path)
    except Exception as e:
        print(e)
