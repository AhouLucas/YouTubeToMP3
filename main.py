import tkinter as tk
from tkinter import filedialog  
from tkinter import ttk
import os
import subprocess
import ffmpeg
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
        print("="*50)
        # Fetch video title
        title = subprocess.run(['yt-dlp', '--get-title', url], capture_output=True, text=True).stdout.strip()
        print(BLUE + "Dowloading " + WHITE + title)
        
        # Download video
        subprocess.run(['yt-dlp', '--no-playlist', '-x', '--audio-format', 'mp3', url, '-o', f'{path}/%(title)s.%(ext)s'])

        print(GREEN + title + WHITE + " downloaded successfully")
        print("="*50)
    except Exception as e:
        print(RED + "Error: " + WHITE + str(e) + "\n")
        print("="*50)


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

def remove_duplicate_urls(lst:list)->list:
    """Remove duplicate URLs from a list

    Args:
        lst (list): List of URLs

    Returns:
        list: List of unique URLs
    """
    return list(set(lst))

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    path = filedialog.askdirectory()
    urls = URL_from_txt(file_path)
    urls = remove_duplicate_urls(urls)
    num_urls = len(urls)
    num_downloaded = 0
    for url in urls:
        print(GREEN + f"[{num_downloaded+1}/{num_urls}] Downloading...\n" + WHITE)
        download_video(url, path)
        num_downloaded += 1
    
    print("Download completed")