from tkinter import *
from pytube import YouTube

root=Tk()

root.geometry('500x400')
root.resizable(0,0)
root.title('Youtube video downolader by @Sapar')

Label(root,text="Youtube Video Downolader" , font ="arial 20 bold").pack()

link=StringVar()
linked=StringVar()
Label(root,text='Pastle Link Here:',font='arial 15 bold').place(x=160,y=60)
link_enter=Entry(root,width=70,textvariable=link).place(x=32,y=90)
Label(root,text='Разришение видео',font='arial 15 bold').place(x=160,y=110)
resize=Entry(root,width=20,textvariable=linked).place(x=180,y=140)

try:
    def Downolader_Adaptive():
        url=YouTube(str(link.get()))
        video=url.streams.get_highest_resolution()

        Label(root,text="{} мб".format(video.filesize),font='arial 15').place(x=180,y=340)
        video.download()
        Label(root,text="DOWNOLADED",font='arial 15').place(x=180,y=300)


    def Downolader_Progressive():
        url=YouTube(str(link.get()))
        
        video=url.streams.filter(progressive=True).first()

        Label(root,text="{} мб".format(video.filesize),font='arial 15').place(x=180,y=340)

        video.download()
        Label(root,text="DOWNOLADED",font='arial 15').place(x=180,y=300)


  


     
except:
    Label(root,text="Ошибки непредусмотрены ",font='arial 15').place(x=180,y=360)
button=Button(root,text="Высокое качество",font='arial 15 bold',bg='pale violet red',padx=2,command=Downolader_Adaptive).place(x=150,y=170)
button1=Button(root,text="Низкое качество",font='arial 15 bold',bg='pale violet red',padx=2,command=Downolader_Progressive).place(x=160,y=220)

try:
    def My_resize():
        url=YouTube(str(link.get()))

        video=url.streams.filter(res='{}p'.format(linked.get())).desc().first()
        print(video)
        video.download()
        Label(root,text="DOWNOLADED",font='arial 15').place(x=180,y=300)

    
except:
    Label(root,text="Не правильное разрешение ",font='arial 15').place(x=180,y=320)
Button(root,text="Мое качество",font='arial 15 bold',bg='pale violet red',padx=2,command=My_resize).place(x=170,y=270)  


root.mainloop()
