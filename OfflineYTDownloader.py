import yt_dlp
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Function to download the video
def download_video():
    link = url_entry.get()  # Get the YouTube URL from the input field
    
    if not link:
        messagebox.showerror("Error", "Please enter a YouTube URL!")
        return

    # Ask user where to save the downloaded video
    download_path = filedialog.askdirectory(title="Select Download Folder")

    if not download_path:
        return  # If the user cancels the folder selection, do nothing

    ydl_opts = {
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save the video with its title as the filename
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Set up the GUI window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Add a label and entry box for the YouTube URL
url_label = tk.Label(root, text="Enter YouTube Video URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# Add a button to start the download
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

# Start the GUI main loop
root.mainloop()
