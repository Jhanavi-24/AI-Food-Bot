import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer
def myappplay(song):
    root = Tk()
    root.title("Music Player")
    root.geometry("920x600+290+85")
    root.configure(background='#0f1a2b')
    root.resizable(False, False)

    mixer.init()
    def AddMusic():
        if song.endswith(".mp3"):
            Playlist.insert(END, song)


    def PlayMusic():
        
        Music_Name = Playlist.get(ACTIVE)
        print(Music_Name[0:-4])
        mixer.music.load(Playlist.get(ACTIVE))
        mixer.music.play()


# icon
    image_icon = PhotoImage(
        file="C:/Users/lenovo/Desktop/foolinks/images/logo.png")
    root.iconphoto(False, image_icon)

    Top = PhotoImage(
        file="C:/Users/lenovo/Desktop/foolinks/images/top.png")
    Label(root, image=Top, bg="#0f1a2b").pack()

# logo
    # if song.endswith(".mp3"):
    #         Playlist.insert(END, song)
    logo = PhotoImage(
        file="C:/Users/lenovo/Desktop/foolinks/images/logo.png")
    Label(root, image=logo, bg="#0f1a2b", bd=0).place(x=70, y=115)

# Button
    ButtonPlay = PhotoImage(
        file="C:/Users/lenovo/Desktop/foolinks/images/play.png")
    Button(root, image=ButtonPlay, bg="#0f1a2b", bd=0,
        command=PlayMusic).place(x=100, y=400)
    
    ButtonStop = PhotoImage(
    file="C:/Users/lenovo/Desktop/foolinks/images/stop.png")
    Button(root, image=ButtonStop, bg="#0f1a2b", bd=0,
        command=mixer.music.stop).place(x=30, y=500)

    ButtonResume = PhotoImage(
        file="C:/Users/lenovo/Desktop/foolinks/images/resume.png")
    Button(root, image=ButtonResume, bg="#0f1a2b", bd=0,
        command=mixer.music.unpause).place(x=115, y=500)

    ButtonPause = PhotoImage(
        file="C:/Users/lenovo/Desktop/foolinks/images/pause.png")
    Button(root, image=ButtonPause, bg="#0f1a2b", bd=0,
        command=mixer.music.pause).place(x=200, y=500)

# Label
    Menu = PhotoImage(
        file="C:/Users/lenovo/Desktop/foolinks/images/menu.png")
    Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)

    Frame_Music = Frame(root, bd=2, relief=RIDGE)
    Frame_Music.place(x=330, y=350, width=560, height=200)

    Button(root, text="Hi click here to listeon your recipe", width=15, height=2, font=("arial",
        10, "bold"), fg="Black", bg="#21b3de", command=AddMusic).place(x=330, y=300)

    Scroll = Scrollbar(Frame_Music)
    Playlist = Listbox(Frame_Music, width=100, font=("Aloja", 10), bg="#000000",
                    fg="white", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
    Scroll.config(command=Playlist.yview)
    Scroll.pack(side=RIGHT, fill=Y)
    Playlist.pack(side=LEFT, fill=BOTH)

# Execute Tkinter
    root.mainloop()

