import tkinter as tk
from tkinter import ttk

class VerticalScrollbarFrame(tk.Frame):
    """
    Vertical scrollable frame. All widgets with master VerticalScrollbarFrame.content_frame
    will be displayed in the scrollable frame.
    """
    def __init__(self, master=None):
        super().__init__()
        self.master = master

        self.scroll_canvas = tk.Canvas(self)
        self.content_frame = content_frame = tk.Frame(self.scroll_canvas)

        self.v_scrollbar = tk.Scrollbar(self,
                                        orient='vertical',
                                        command=self.scroll_canvas.yview)
        self.scroll_canvas.configure(yscrollcommand=self.v_scrollbar.set)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.scroll_canvas.grid(column=0, row=0, sticky='nesw')
        self.v_scrollbar.grid(column=1, row=0, sticky='nesw')

        self.scroll_frame = self.scroll_canvas.create_window((0,0),
                                                            window=self.content_frame,
                                                            anchor='nw',
                                                            tags='self.content_frame')

        self.bind('<Configure>', self.on_frame_configure)
        self.bind_all('<MouseWheel>', self.mouse_scroll)
        self.scroll_canvas.bind('<Configure>', self.on_configure)
        #self.master.bind('<MouseWheel>', self.mouse_scroll)
        #self.content_frame.bind('<Configure>', self.on_frame_configure)

    def on_frame_configure(self, event=None):
        """
        Updates the scrollregion of the canvas.
        """
        self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox('all'))

    def on_configure(self, event=None):
        """
        Updates the contents for the scroll canvas.
        """
        if event:
            w, h = event.width, event.height
        else:
            w, h = 0, 0
        natural = self.content_frame.winfo_reqwidth()
        self.scroll_canvas.itemconfigure(self.scroll_frame, width=w if w > natural else natural)

    def mouse_scroll(self, event):
        """
        Method to make scrolling with the mousewheel working.
        """
        if event.delta:
            self.scroll_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.scroll_canvas.yview_scroll(move, "units")

class HorizontalScrollbarFrame(tk.Frame):
    """
    Horizontal scrollable frame. All widgets with master HorizontalScrollbarFrame.content_frame
    will be displayed in the scrollable frame.
    """
    def __init__(self, master=None):
        super().__init__()
        self.master = master

        self.scroll_canvas = tk.Canvas(self)
        self.content_frame = content_frame = tk.Frame(self.scroll_canvas)

        self.h_scrollbar = tk.Scrollbar(self,
                                        orient='horizontal',
                                        command=self.scroll_canvas.xview)
        self.scroll_canvas.configure(xscrollcommand=self.h_scrollbar.set)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.scroll_canvas.grid(column=0, row=0, sticky='nesw')
        self.h_scrollbar.grid(column=0, row=1, sticky='nesw')

        self.scroll_frame = self.scroll_canvas.create_window((0,0),
                                                            window=self.content_frame,
                                                            anchor='nw',
                                                            tags='self.content_frame')

        self.bind('<Configure>', self.on_frame_configure)
        self.bind_all('<MouseWheel>', self.mouse_scroll)
        self.scroll_canvas.bind('<Configure>', self.on_configure)
        #self.master.bind('<MouseWheel>', self.mouse_scroll)
        #self.content_frame.bind('<Configure>', self.on_frame_configure)

    def on_frame_configure(self, event=None):
        """
        Updates the scrollregion of the canvas.
        """
        self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox('all'))

    def on_configure(self, event=None):
        """
        Updates the contents for the scroll canvas.
        """
        if event:
            w, h = event.width, event.height
        else:
            w, h = 0, 0
        natural = self.content_frame.winfo_reqheight()
        self.scroll_canvas.itemconfigure(self.scroll_frame, height=h if h > natural else natural)

    def mouse_scroll(self, event):
        """
        Method to make scrolling with the mousewheel working.
        """
        if event.delta:
            self.scroll_canvas.xview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = -1
            else:
                move = 1

            self.scroll_canvas.xview_scroll(move, "units")
