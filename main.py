import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import ttkbootstrap as tkb
from pytube import YouTube

class VideoDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Downloader App")

        # Variables
        self.video_link_var = tk.StringVar()
        self.directory_var = tk.StringVar()

        # GUI components
        self.create_widgets()

    def create_widgets(self):
        # Video Link Entry
        video_label = tkb.Label(self.root, text="Video Link:")
        video_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        video_entry = ttk.Entry(self.root, textvariable=self.video_link_var, width=50)
        video_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

        # Directory Selection
        dir_label = tkb.Label(self.root, text="Save to:")
        dir_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        dir_entry = ttk.Entry(self.root, textvariable=self.directory_var, width=40)
        dir_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        dir_button = tkb.Button(self.root, text="Browse", command=self.select_directory)
        dir_button.grid(row=1, column=2, padx=5, pady=10, sticky="ew")

        # Download Button
        download_button = tkb.Button(self.root, text="Download", command=self.download_video)
        download_button.grid(row=2, column=0, columnspan=3, pady=10)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_var.set(directory)

    def download_video(self):
        video_link = self.video_link_var.get()
        save_path = self.directory_var.get()

        if video_link and save_path:
            try:
                yt = YouTube(video_link)
                video = yt.streams.filter(progressive=True, file_extension="mp4").first()
                video.download(save_path)
                tk.messagebox.showinfo("Success", "Download completed successfully!")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            tk.messagebox.showwarning("Warning", "Please provide a valid video link and select a save directory.")

if __name__ == "__main__":
    root = tkb.Window(themename="superhero")
    app = VideoDownloaderApp(root)
    root.mainloop()