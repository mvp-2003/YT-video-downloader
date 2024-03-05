import requests, validators
from customtkinter import filedialog
from urllib.parse import urlparse, parse_qs
from pytube import YouTube
import threading

def valid_url(url):
    if not validators.url(url):
        return False
    
    parsed_url = urlparse(url)
    if parsed_url.netloc not in ['www.youtube.com', 'youtu.be', 'www.youtu.be', 'youtube.com']:
        return False

    if parsed_url.netloc == 'youtu.be':
        if not parsed_url.path:
            return False
    else:
        query = parse_qs(parsed_url.query)
        if 'v' not in query:
            return False

    response = requests.get(url)
    if response.status_code != 200:
        return False

    return True
    
def first_check(entry_folder, entry_link, invalid_url_label):
    url = entry_link.get()
    if url == "":
        invalid_url_label.configure(text="URL not provided")
        return
    if not valid_url(url):
        invalid_url_label.configure(text="Invalid URL")
        return
    invalid_url_label.configure(text="")
    folder = filedialog.askdirectory()
    entry_folder.configure(state='normal')
    entry_folder.delete(0, 'end')
    entry_folder.insert(0, folder)
    entry_folder.configure(state='disabled')

def finalize(selected_link_value, selected_folder_value, entry_link, entry_folder, download_button, invalid_url_label):
    url = entry_link.get()
    if url == "":
        invalid_url_label.configure(text="URL not provided")
        return
    if not valid_url(url):
        invalid_url_label.configure(text="Invalid URL")
        return
    entry_folder.delete(0, 'end')
    if entry_folder.get() == "" and entry_link.get() == "":
        selected_folder_value.configure(text="")
        selected_link_value.configure(text="")
        selected_folder_value.configure(text="Please select a folder", text_color="red")
        selected_link_value.configure(text="Please provide a URL", text_color="red")
        download_button.configure(state='disabled')
    elif entry_link.get() == "":
        selected_folder_value.configure(text="")
        selected_link_value.configure(text="")
        selected_link_value.configure(text="Please provide a URL", text_color="red")
        selected_folder_value.configure(text=entry_folder.get(), text_color="black")
        download_button.configure(state='disabled')
    elif entry_folder.get() == "":
        selected_folder_value.configure(text="")
        selected_link_value.configure(text="")
        selected_link_value.configure(text=entry_link.get(), text_color="black")
        selected_folder_value.configure(text="Please select a folder", text_color="red")
        download_button.configure(state='disabled')
    else:
        selected_link_value.configure(text=entry_link.get(), text_color="black")
        selected_folder_value.configure(text=entry_folder.get(), text_color="black")
        entry_link.delete(0, 'end')
        entry_folder.configure(state='normal')
        entry_folder.delete(0, 'end')
        download_button.configure(state='normal')

def download_video(url, path, final_message_box):
    final_message_box.configure(text="")
    if url == "" or path == "":
        return
    try:
        video = YouTube(url)
        st = video.streams.filter(progressive=True, file_extension='mp4')
        hrs = st.get_highest_resolution()
        if hrs is not None:
            # deepcode ignore MissingAPI: <please specify a reason of ignoring this>
            down_th = threading.Thread(target=hrs.download, args=(path,))
            down_th.start()
            final_message_box.configure(text="Download successful!", text_color="green", font=("Arial", 24))
            
    except Exception as e:
        print(e)
        final_message_box.configure(text="An error occurred while downloading the video", text_color="red")