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
        print(GREEN + "Downloaded " + WHITE + audio.title + "\n")
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
        for line in f:
            lst.append(line)
    return lst

def progress_bar(percentage:int)->str:
    """Create a progress bar

    Args:
        percentage (int): Percentage of the progress

    Returns:
        str: Progress bar
    """
    size = 25
    bar = "["
    bar += "=" * int(percentage/100 * size)
    bar += " " * (size - int(percentage/100 * size))
    bar += "]"
    return bar


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    path = filedialog.askdirectory()
    urls = URL_from_txt(file_path)
    num_urls = len(urls)
    num_downloaded = 0
    for url in urls:
        download_video(url, path)
        num_downloaded += 1
        print(progress_bar(num_downloaded/num_urls * 100) + " " + str(num_downloaded/num_urls * 100) + "%" + "\n")
    
    print("Download completed")