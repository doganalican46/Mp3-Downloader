from tkinter import *
from pytube import YouTube
import os

window = Tk()

def center_window(width=640, height=300):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

def download():
    Option = str(var.get())
    Link = str(txtfld.get())
    if Link == "":
        lbl3.config(text="YouTube Link'i girin!", fg='red')
    elif Option == "0":
        lbl3.config(text="MP4 veya MP3 seçin!", fg='red')
    else:
        yt = YouTube(Link)
        if Option == "1":
            stream = yt.streams.get_by_itag(18)
            stream.download(filename=yt.title + '.mp4')
            move_to_desktop(yt.title + '.mp4')
            lbl3.config(text="İndirme tamamlandı: " + yt.title + '.mp4', fg='green')
        elif Option == "2":
            stream = yt.streams.get_by_itag(251)
            stream.download(filename=yt.title + '.mp3')
            move_to_desktop(yt.title + '.mp3')
            lbl3.config(text="İndirme tamamlandı: " + yt.title + '.mp3', fg='green')
        
        txtfld.delete(0, END)

def move_to_desktop(file_name):
    desktop_path = "C:\\Users\\dogan\\OneDrive\\Masaüstü"  
    dest_path = os.path.join(desktop_path, 'YouTube İndirdiklerim')
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    os.replace(file_name, os.path.join(dest_path, os.path.basename(file_name)))

window.configure(bg='white')
center_window()

# logo_image = PhotoImage(file="C:\Users\dogan\OneDrive\Masaüstü\Mp3 Downloader\dist\CahaLogo.png")
# logo_image = logo_image.subsample(5)  
# logo_label = Label(window, image=logo_image, bg='white')
# logo_label.place(x=0, y=0)

lbl=Label(window, text="YouTube Downloader", bg='white', fg='red', font=("System", 34))
lbl.place(x=100, y=15)
lbl1=Label(window, text="---Alleyyyy---", bg='white', fg='black', font=("System", 17))
lbl1.place(x=200, y=60)

lbl2=Label(window, text="Video linki:", bg='white', fg='black', font=("System", 13))
lbl2.place(x=10, y=142)
txtfld=Entry(window, text="This is Entry Widget", bd="5",width="55")
txtfld.place(x=120, y=140)

btn=Button(window, text="İNDİR", bg='red', fg='white', command=download)
btn.place(x=500, y=138)

var = IntVar()
R1 = Radiobutton(window, text="MP4",bg='white', fg='black', variable=var, value=1)
R1.place(x=120, y=185)

R2 = Radiobutton(window, text="MP3",bg='white', fg='black', variable=var, value=2)
R2.place(x=270, y=185)

lbl3=Label(window, text="", bg='white', fg='black', width="40", font=("System", 13))
lbl3.place(x=50, y=210)

window.title('Alleyyyy- Youtube Downloader')
window.mainloop()
