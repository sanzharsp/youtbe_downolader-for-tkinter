from tkinter import *
from pytube import YouTube

root=Tk()

root.geometry('500x300')
root.resizable(0,0)
root.title('Youtube video downolader by @Sapar')

Label(root,text="Youtube Video Downolader" , font ="arial 20 bold").pack()

link=StringVar()

Label(root,text='Pastle Link Here:',font='arial 15 bold').place(x=160,y=60)
link_enter=Entry(root,width=70,textvariable=link).place(x=32,y=90)



def Downolader_Adaptive():
    url=YouTube(str(link.get()))
    video=url.streams.filter(adaptive=True).first()
    video.download()
    Label(root,text="DOWNOLADED",font='arial 15').place(x=180,y=218)


def Downolader_Progressive():
    url=YouTube(str(link.get()))
    video=url.streams.filter(progressive=True).first()
    video.download()
    Label(root,text="DOWNOLADED",font='arial 15').place(x=180,y=218)
Button(root,text="Высокое качество",font='arial 15 bold',bg='pale violet red',padx=2,command=Downolader_Adaptive).place(x=150,y=150)
Button(root,text="Низкое качество",font='arial 15 bold',bg='pale violet red',padx=2,command=Downolader_Progressive).place(x=160,y=200)

root.mainloop()