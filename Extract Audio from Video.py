import moviepy.editor as me 
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

#Creating variable to store audio filename
filename=''

def convert():
        global filename
        filetypes=(("Audio files","*.mp3 , *.waw , *.ogg"),("All files","*.*"))
        
        #Loading the Video Clip
        video=me.VideoFileClip(filename)
        
        #Extracting the Audio
        audio=video.audio
        
        #Export the Audio
        file=asksaveasfilename(filetypes=filetypes)
        audio.write_audiofile(f'{file}{format.get()}')
        
        #Creating a label to display Converted
        label5=Label(root,text="Converted!!!",font=("Arial",18),fg="green")
        label5.config(bg="pink")
        label5.pack()
        label5.place(x=450,y=300)
        
def select():
    global filename
    filetypes = (
        ('video files', '*.WEBM , *.MPG, *.MP2 , *.MPEG , *.MPE , *.MPV , *.MP4 , *.M4P , *.M4V , *.AVI , *.WMV , *.MOV , *.QT , *.FLV , *.SWF , *.AVCHD'),
        ('All files', '*.*')
    )
    filename=askopenfilename(filetypes=filetypes)
    
    #Creating a label to diaplay video selected
    label3.config(text="Video Selected",fg="green")
    label3.config(bg="pink")
    
    #Creating a label 
    label4=Label(root,text="Select Audio format",font=("Arial",18))
    label4.config(bg="pink")
    label4.pack()
    label4.place(x=125,y=250)
    
    #Creating options to choose audio format
    options=[".mp3",".ogg",".wav"]
    format.set(".mp3")
    menu=OptionMenu(root,format,*options)
    menu.pack()
    menu.place(x=375,y=250)
    
    #Creating a button to convert video to audio
    button3=Button(root,text="Export",bg='light blue',font=("Harlow Solid",12),command=convert,width=10,height=1)
    button3.pack()
    button3.place(x=250,y=300)

#Creating the basic GUI window
root=Tk()

#The background color of GUI application
root.configure(bg='Light Coral') 

#The geometry of the GUI application
root.geometry("700x450")
root.minsize(600,350)
root.maxsize(600,350)

#The title of the GUI application
root.title("Video to Audio Converter")

#Creating a label for heading
label1=Label(root,text="Extract Audio from Video",font=("times new roman",32))
label1.config(bg="Crimson")
label1.pack()

#Creating a label to display Select any Video file
label2=Label(root,text="Select any Video file",font=("garamond",18))
label2.config(bg="Crimson")
label2.pack()
label2.place(x=190,y=100)

#Creating a button for choosing video
button1=Button(root,text="Choose file",bg='light blue',font=("Harlow Solid",12),command=select,width=10,height=1)
button1.pack()
button1.place(x=250,y=200)

label3=Label(root,font=("Footlight MT",18,"bold"))
label3.pack()
label3.place(x=225,y=150)
format=StringVar()

#Start the GUI application
root.mainloop()
