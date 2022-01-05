import tkinter.filedialog
from pytube import YouTube
from tkinter import *
from tkinter import messagebox
PINk = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
def Download_video():
    try:
        url = web_entry.get()
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        try:
            output = tkinter.filedialog.askdirectory()
        except:
            messagebox.showerror(title="Output_Path", message="Please select valid output path")
            return
        stream.download(output_path= output)
        messagebox.showinfo(title="Successful",message="Your file Download successful")
    except:
        messagebox.showerror(title="Url Incorrect",message="Please check the URL")

def Download_audio():
    try:
        url = web_entry.get()
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        try:
            output = tkinter.filedialog.askdirectory()
        except:
            messagebox.showerror(title="Output_Path", message="Please select valid output path")
            return
        stream.download(output_path=output)
        messagebox.showinfo(title="Successful", message="Your file Download successful")
    except:
        messagebox.showerror(title="Url Incorrect", message="Please check the URL")

def Reset():
    web_entry.delete(0, 'end')

if __name__ == '__main__':

    window = Tk()
    window.title("Youtube Video Downloader")
    window.config(bg=YELLOW)
    window.config(padx=80, pady=80)
    canvas = Canvas(width=100, height=100)
    website = Label(text="URL", font=(FONT_NAME, 18, "bold"), justify=CENTER)
    website.grid(column=0, row=1)
    web_entry = Entry(width=45)
    web_entry.grid(column=1, row=1, columnspan=3)
    dwnd_vd = Button(text="Download Video", width=25, fg=RED, command=Download_video)
    dwnd_vd.grid(column=1, row=3)
    dwnd_ad = Button(text="Download Audio", width=25, fg=RED, command=Download_audio)
    dwnd_ad.grid(column=3, row=3)
    reset = Button(text="Reset", width=10, fg=RED, command=Reset)
    reset.grid(column=2, row=4)
    window.mainloop()