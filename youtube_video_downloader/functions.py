import requests
import validators
from customtkinter import filedialog
from urllib.parse import urlparse, parse_qs
from pytube import YouTube
import threading
import logging

logging.basicConfig(level=logging.INFO)

lock = threading.Lock()

def valid_url(url):
    """Validate the provided URL."""
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

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return False
    except requests.RequestException as e:
        logging.error(f"Network error: {e}")
        return False

    return True

def first_check(entry_folder, entry_link, invalid_url_label):
    """Perform the first check on the provided URL and folder."""
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
    """Finalize the URL and folder selection."""
    url = entry_link.get()
    if url == "":
        invalid_url_label.configure(text="URL not provided")
        return
    if not valid_url(url):
        invalid_url_label.configure(text="Invalid URL")
        return
    
    entry_folder.delete(0, 'end')
    folder = entry_folder.get()
    link = entry_link.get()

    if not folder and not link:
        selected_folder_value.configure(text="Please select a folder", text_color="red")
        selected_link_value.configure(text="Please provide a URL", text_color="red")
        download_button.configure(state='disabled')
    elif not link:
        selected_link_value.configure(text="Please provide a URL", text_color="red")
        selected_folder_value.configure(text=folder, text_color="black")
        download_button.configure(state='disabled')
    elif not folder:
        selected_folder_value.configure(text="Please select a folder", text_color="red")
        selected_link_value.configure(text=link, text_color="black")
        download_button.configure(state='disabled')
    else:
        selected_link_value.configure(text=link, text_color="black")
        selected_folder_value.configure(text=folder, text_color="black")
        entry_link.delete(0, 'end')
        entry_folder.configure(state='normal')
        entry_folder.delete(0, 'end')
        download_button.configure(state='normal')

def download_video(url, path, final_message_box):
    """Download the video from the provided URL to the specified path."""
    final_message_box.configure(text="")
    if url == "" or path == "":
        return
    try:
        video = YouTube(url)
        st = video.streams.filter(progressive=True, file_extension='mp4')
        hrs = st.get_highest_resolution()
        if hrs is not None:
            def download():
                with lock:
                    hrs.download(path)
                final_message_box.configure(text="Download successful!", text_color="green", font=("Arial", 24))
            
            down_th = threading.Thread(target=download)
            down_th.start()
            
    except Exception as e:
        logging.error(f"Error downloading video: {e}")
        final_message_box.configure(text="An error occurred while downloading the video", text_color="red")