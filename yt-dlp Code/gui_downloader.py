# NOTE: You need to have ffmpeg downloaded and added to the path variable for this to work, get it here: https://ffmpeg.org/download.html#build-windows
    # You also need to 'pip install yt-dlp'
    
    #  If throwing errors update using this command: pip install --upgrade yt-dlp

# To convert this to exe, use the following:
    # https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen
    # or
    # pyinstaller -F yourprogram.py


import os
from tkinter import filedialog, messagebox, StringVar, IntVar 
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from yt_dlp import YoutubeDL

# Global text size
TEXT_SIZE = 12
APP_TITLE = "YOUTUBE DOWNLOADER"
APP_SIZE = "500x500"
APP_THEME="solar"

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry(APP_SIZE)
        
        # Variables
        self.url_var = StringVar()
        self.format_var = StringVar(value="mp4")
        self.location_var = StringVar(value=os.path.expanduser("~/Downloads"))
        self.filename_var = StringVar()
        self.progress_var = IntVar(value=0)
        self.theme_var = StringVar(value=APP_THEME)

        # Build UI
        self.build_ui()

    def build_ui(self):
        # Theme Selector
        ttk.Label(self.root, text="Select Theme:", font=("Helvetica", TEXT_SIZE)).pack(pady=5)
        theme_frame = ttk.Frame(self.root)
        theme_frame.pack(pady=5)
        ttk.Combobox(theme_frame, values=ttk.Style().theme_names(), textvariable=self.theme_var, state="readonly", width=20).pack(side=LEFT, padx=5)
        ttk.Button(theme_frame, text="Apply Theme", command=self.apply_theme).pack(side=LEFT, padx=5)

        # URL Input
        ttk.Label(self.root, text="YouTube URL:", font=("Helvetica", TEXT_SIZE)).pack(pady=5)
        ttk.Entry(self.root, textvariable=self.url_var, width=50, font=("Helvetica", TEXT_SIZE)).pack(pady=5)

        # Format Selection (Video or Audio)
        ttk.Label(self.root, text="Format:", font=("Helvetica", TEXT_SIZE)).pack(pady=5)
        format_frame = ttk.Frame(self.root)
        format_frame.pack(pady=5)
        ttk.Radiobutton(format_frame, text="MP4 (Video)", variable=self.format_var, value="mp4").pack(side=LEFT, padx=10)
        ttk.Radiobutton(format_frame, text="MP3 (Audio)", variable=self.format_var, value="mp3").pack(side=LEFT, padx=10)

        # Save Location
        ttk.Label(self.root, text="Save Location:", font=("Helvetica", TEXT_SIZE)).pack(pady=5)
        location_frame = ttk.Frame(self.root)
        location_frame.pack(pady=5)
        ttk.Entry(location_frame, textvariable=self.location_var, width=40, font=("Helvetica", TEXT_SIZE)).pack(side=LEFT, padx=5)
        ttk.Button(location_frame, text="Browse", command=self.browse_location).pack(side=LEFT, padx=5)

        # File Name (Optional)
        ttk.Label(self.root, text="File Name (Optional):", font=("Helvetica", TEXT_SIZE)).pack(pady=5)
        ttk.Entry(self.root, textvariable=self.filename_var, width=50, font=("Helvetica", TEXT_SIZE)).pack(pady=5)

        # Download Button
        ttk.Button(self.root, text="Download", command=self.download, bootstyle=SUCCESS).pack(pady=20)

        # Progress Bar
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress_var, maximum=100, length=450)
        self.progress_bar.pack(side=BOTTOM, pady=10)

    def apply_theme(self):
        selected_theme = self.theme_var.get()
        self.root.style.theme_use(selected_theme)

    def browse_location(self):
        folder_selected = filedialog.askdirectory(initialdir=self.location_var.get())
        if folder_selected:
            self.location_var.set(folder_selected)

    def download(self):
        url = self.url_var.get().strip()
        file_format = self.format_var.get()
        location = self.location_var.get()
        filename = self.filename_var.get().strip()

        if not url:
            messagebox.showerror("Error", "Please enter a valid YouTube URL!")
            return

        self.progress_var.set(0)
        self.download_with_yt_dlp(url, file_format, location, filename)

    def download_with_yt_dlp(self, url, file_format, location, filename):
        try:
            ydl_opts = {
                'format': 'mp4' if file_format == 'mp4' else 'bestaudio/best',
                'outtmpl': os.path.join(location, f"{filename or '%(title)s'}.%(ext)s"),
                'progress_hooks': [self.ytdlp_progress_hook]
            }
            if file_format == "mp3":
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3'
                }]
            
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Success", "Download completed successfully!")

            self.url_var.set("")
            self.filename_var.set("")
            self.progress_var.set(0)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def ytdlp_progress_hook(self, d):
        if d['status'] == 'downloading':
            downloaded_bytes = d.get('downloaded_bytes', 0)
            total_bytes = d.get('total_bytes', 1)
            if total_bytes:
                progress = (downloaded_bytes / total_bytes) * 100
                self.progress_var.set(int(progress))
                self.root.update_idletasks()

if __name__ == "__main__":
    root = ttk.Window(themename=APP_THEME)
    app = YouTubeDownloaderApp(root)
    root.mainloop()
