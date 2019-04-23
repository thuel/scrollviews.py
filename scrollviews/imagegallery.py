import tkinter as tk
from tkinter import ttk
from pathlib import Path
from PIL import Image, ImageTk

class ImageGallery(tk.Tk):
    def __init__(self, image_paths):
        super().__init__()
        self.images = image_paths

        self.ims = []

        self.gallery_frame = VerticalScrollbarFrame(self)
        self.image_frame = self.gallery_frame.content_frame

        self.geometry("800x600")

        self.setup_images(self.images)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.gallery_frame.grid(column=0, row=0, sticky='nesw')
        self.gallery_frame.on_configure()

    def setup_images(self, image_paths):
        for row, image in enumerate(image_paths):
            self.image_frame.rowconfigure(row, weight=0)
            col = 0
            load = Image.open(image)
            load.thumbnail((200,200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(load)

            image_lbl = ttk.Label(self.image_frame, image=photo)
            image_lbl.image = photo
            image_lbl.grid(column=col, row=row, sticky='nesw')
            self.ims.append(image_lbl)

            caption_lbl = ttk.Label(self.image_frame, text=image.name)
            caption_lbl.grid(column=col+1, row=row, sticky='nesw')
