import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink,on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color = 'white')
        finishlabel.configure(text = '')
        video.download()
        finishlabel.configure(text = 'Downloaded')
    except:
        finishlabel.configure(text = 'Download error', text_color = 'red')
    
def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    pPercentage.configure(text = per + '%')
    pPercentage.update()

    progressBar.set(float(percentage_of_compeletion) / 100)

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry('720x480')
app.title('YouTube Downloader')

title = customtkinter.CTkLabel(app, text = 'Insert a YouTube link')
title.pack(padx = 10, pady = 10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finishlabel = customtkinter.CTkLabel(app, text = '')
finishlabel.pack()

pPercentage = customtkinter.CTkLabel(app, text = '0%')
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(pady = 10, padx = 10)

downaload = customtkinter.CTkButton(app, text= 'Download', command = startDownload)
downaload.pack(padx = 10, pady = 10)

app.mainloop()