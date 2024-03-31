from pytube import YouTube
import tkinter as tk
from tkinter import filedialog  
from tkinter import ttk
import os
from colorama import Fore, Style, init

# Colorama
WHITE = "\u001b[37m";
GREEN = "\u001b[32m";
RED = "\u001b[31m";
BLUE = "\u001b[34m";

def download_video(url:str, path:str):
    """Download video from youtube

    Args:
        url (str): URL of the video
        path (str): Path to save the video
    """
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        print(BLUE + "Dowloading " + WHITE + audio.title)
        output_file = audio.download(output_path=path)

        base, ext = os.path.splitext(output_file)
        new_file = base + '.mp3'
        os.rename(output_file, new_file)
        print(GREEN + f"{audio.title}" + WHITE + " has been succesfully downloaded.\n")
    except Exception as e:
        print(RED + "Error downloading " + WHITE + url + "\n")


def URL_from_txt(path:str)->list:
    """Read URLs from a text file

    Args:
        path (str): Path to the text file

    Returns:
        list: List of URLs
    """
    lst = []
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            lst.append(line.strip())
    return lst


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    path = filedialog.askdirectory()
    urls = URL_from_txt(file_path)
    num_urls = len(urls)
    num_downloaded = 0
    for url in urls:
        print(GREEN + f"[{num_downloaded+1}/{num_urls}] Downloading...\n" + WHITE)
        download_video(url, path)
        num_downloaded += 1
    
    print("Download completed")