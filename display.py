from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import random
import math
import os
from random import randint
from array import *


def shufflepixels():
    global pixmap
    global canvaslist
    
    if not canvaslist:
        norectangle()
        return
    else:
        pass
        
    checktuple=canvaslist[0] #gets first tuple in canvaslist
    #loop through the coordinates specified by checktuple(x1,y1,x2,y2) and shuffle around
    test1=list(checktuple)
    x1=math.floor(test1[0]) #x1 coord
    y1=math.floor(test1[1]) #y1 coord
    x2=math.floor(test1[2]) #x2 coord
    y2=math.floor(test1[3]) #y2 coord
    
    xpixels=list()
    for i in range(x1, x2): #xcoords
        xpixels.append(i)
    
    ypixels=list()
    for i in range(y1, y2):#ycoords
        ypixels.append(i)
     
    random.shuffle(xpixels)
    random.shuffle(ypixels)
    
    xcounter=-1
    ycounter=0
    
    for i in range(x1, x2):
        xcounter=xcounter+1
        for j in range(y1, y2):
            if ycounter >= len(ypixels):
                break
            else:
                pixmap[i, j]=pixmap[xpixels[xcounter], ypixels[ycounter]]
                ycounter=ycounter+1
        ycounter=0 
          
    global photo
    photo=ImageTk.PhotoImage(img)
    canvas.create_image(0,0,anchor=NW,image=photo)
    canvas.update_idletasks()
    
    for i in range(len(canvaslist)): #reset canvaslist
        del canvaslist[i]

def shuffleyaxis():
    global pixmap
    global canvaslist
    
    if not canvaslist:
        norectangle()
        return
    else:
        pass

    checktuple=canvaslist[0] #gets first tuple in canvaslist
    #loop through the coordinates specified by checktuple(x1,y1,x2,y2) and shuffle around
    test1=list(checktuple)
    x1=math.floor(test1[0]) #x1 coord
    y1=math.floor(test1[1]) #y1 coord
    x2=math.floor(test1[2]) #x2 coord
    y2=math.floor(test1[3]) #y2 coord
    
    xpixels=list()
    for i in range(x1, x2): #xcoords
        xpixels.append(i)

    ypixels=list()
    for i in range(y1, y2):#ycoords
        ypixels.append(i)
    
    random.shuffle(xpixels)
    random.shuffle(ypixels)
 
    xcounter=-1
    ycounter=0
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            if ycounter >=len(ypixels):
                break
            else:
                pixmap[i, j]=pixmap[i, ypixels[ycounter]]
                ycounter=ycounter+1
        ycounter=0
        
    global photo
    photo=ImageTk.PhotoImage(img)
    canvas.create_image(0,0,anchor=NW,image=photo)
    canvas.update_idletasks()
    
    for i in range(len(canvaslist)): #reset canvaslist
        del canvaslist[i]

def shufflexaxis():
    global pixmap
    global canvaslist
    
    if not canvaslist:
        norectangle()
        return
    else:
        pass

    checktuple=canvaslist[0] #gets first tuple in canvaslist
    #loop through the coordinates specified by checktuple(x1,y1,x2,y2) and shuffle around
    test1=list(checktuple)
    x1=math.floor(test1[0]) #x1 coord
    y1=math.floor(test1[1]) #y1 coord
    x2=math.floor(test1[2]) #x2 coord
    y2=math.floor(test1[3]) #y2 coord
    xpixels=list()
    for i in range(x1, x2): #xcoords
        xpixels.append(i)
  
    ypixels=list()
    for i in range(y1, y2):#ycoords
        ypixels.append(i)
    
    random.shuffle(xpixels)
    random.shuffle(ypixels)
 
    xcounter=0
    ycounter=0
    for i in range(y1, y2):
        for j in range(x1, x2):
            if xcounter >= len(xpixels):
                break
            else:
                pixmap[j, i]=pixmap[xpixels[xcounter], i]
        
    global photo
    photo=ImageTk.PhotoImage(img)
    canvas.create_image(0,0,anchor=NW,image=photo)
    canvas.update_idletasks()
    
    for i in range(len(canvaslist)): #reset canvaslist
        del canvaslist[i]
        
def on_button_press(event):
    global canvaslist
    if sharedcount == -1:
        canvas.start_x=event.x
        canvas.start_y=event.y
        canvas.x=event.x
        canvas.y=event.y
        xcoord=xpixel.get()
        ycoord=ypixel.get()
        if (xcoord > width) or (xcoord < 1):
            return
        else:
            pass
        if (ycoord > height) or (ycoord < 1):
            return
        else:
            pass
        if not canvaslist: #if a rectangle already exists, do not allow further rectangles to be drawn
            canvas.create_rectangle(canvas.x,canvas.y,(canvas.x + xcoord),(canvas.y + ycoord),fill="",outline="blue")
            z=canvas.create_rectangle(canvas.x,canvas.y,(canvas.x + xcoord),(canvas.y + ycoord),fill="",outline="blue")
            canvaslist.append(canvas.coords(z)) #(x1,y1,x2,y2) tuple of each rectangle's coordinates
        else:
            pass
    else:
        pass
        
def on_move_press(event):
    curX,curY=(event.x,event.y)
    canvas.coords(canvas.start_x,canvas.start_y,curX,curY)
    
    
def saveimage():
    f=filedialog.asksaveasfilename()
    ext=os.path.splitext(f)
 
    if sharedcount == -1:
        if f == "":
            return
        else:
            pass
        
        try:
            img.save(f + ext[1])
        except KeyError:
            invalidext() #warn user that specified extension is invalid
    else:
        if f == "":
            return
        else:
            pass
        try:    
            newimg.save(f + ext[1])
        except KeyError:
            invalidext()

 
def nextimage():
    global sharedcount
    
    for i in range(len(canvaslist)): #fixes bug where you draw rectangle in original photo, switch to another photo and try to shuffle, then warps you back to the original
        del canvaslist[i]

    sharedcount=sharedcount+1

    if sharedcount > (varvalue - 1):
        sharedcount=sharedcount - 1
        return

    canvas.create_image(0,0,anchor=NW,image=photolist[sharedcount])

def previousimage():
    global sharedcount
    sharedcount=sharedcount - 1
    
    if sharedcount == -1:
        canvas.create_image(0,0,anchor=NW,image=photo)
        return
    elif sharedcount < -1:
        sharedcount=sharedcount + 1
        return
    else:
        canvas.create_image(0,0,anchor=NW,image=photolist[sharedcount])
    
def alert():
    alertmsg=Toplevel()
    alertmsg.title("")
    msg=Label(alertmsg, text="Error: Image exceeds screen dimensions")
    msg.pack()
    closebtn=Button(alertmsg, text="Close", command=alertmsg.destroy)
    closebtn.pack()
    alertmsg.wait_window(alertmsg)
    
def norectangle():
    norect=Toplevel()
    norect.title("")
    nomsg=Label(norect, text="There is nothing here to shuffle!")
    nomsg.pack()
    nobttn=Button(norect, text="OK", command=norect.destroy)
    nobttn.pack()
    norect.wait_window(norect)
    
def invalidext():
    inv=Toplevel()
    inv.title("")
    invmsg=Label(inv, text="Invalid extension!")
    invmsg.pack()
    invbttn=Button(inv, text="OK", command=inv.destroy)
    invbttn.pack()
    invmsg.focus_force()
    
def kill():
    os._exit(0) #kill program
    
def varcheck():
    vvalue=var.get()
    if (vvalue > 10) or (vvalue < 1):
        vmsg=Toplevel()
        vmsg.title("")
        vlabel=Label(vmsg, text="Value must be between 1-10")
        vlabel.pack()
        vmsg.focus_force()
        
    else:
        popup.destroy()
        
    
def nothing():
    pass
    
def shufflewidth():
    global mwidth
    random.shuffle(mwidth)
    
def shuffleheight():
    global mheight
    random.shuffle(mheight)
    

popup=Tk()
popup.title("")
iconimage=ImageTk.PhotoImage(file="images/logo.gif") 
popup.tk.call('wm', 'iconphoto', popup._w, iconimage)
popup.protocol('WM_DELETE_WINDOW', kill)
var=IntVar(popup)
var.set(1)
dismessage=Label(popup,text="Select number of variations")
dismessage.pack()
valuebox=Spinbox(popup,from_=1,to=10,textvariable=var)
valuebox.pack()
closepopup=Button(popup, text="OK",command=varcheck)
closepopup.pack()
popup.wait_window(popup)
root=Tk()
root.title("Pixel Shuffle")
iconimage=ImageTk.PhotoImage(file="images/logo.gif") #need again here else or else tkinter error gets raised
root.tk.call('wm', 'iconphoto', root._w, iconimage)
root.fileName=filedialog.askopenfilename(filetypes=(("JPG files","*.jpg"),("PNG files","*.png"),("BMP files","*.bmp"),("GIF files","*.gif"),("All image files","*.jpg;*.png;*.bmp;*.gif")))

if not root.fileName:
    kill() #kill program if there is no selection
else:
    pass

img=Image.open(root.fileName)
width,height=img.size
screenwidth=root.winfo_screenwidth()
screenheight=root.winfo_screenheight()

if width > screenwidth:
    alert()
    root.destroy()
elif height > screenheight:
    alert()
    root.destroy()
else:
    pass

shuffwindow=Toplevel()
shuffwindow.title("")
shuffwindow.tk.call('wm', 'iconphoto', shuffwindow._w, iconimage)
shuffwindow.protocol('WM_DELETE_WINDOW', nothing)
xpixel=IntVar(shuffwindow)
xpixel.set(1)
ypixel=IntVar(shuffwindow)
ypixel.set(1)
xmessage=Label(shuffwindow,text="Choose Pixel Width")
xmessage.pack()
xspinbox=Spinbox(shuffwindow,from_=1,to=width,textvariable=xpixel)
xspinbox.pack()
ymessage=Label(shuffwindow,text="Choose Pixel Height")
ymessage.pack()
yspinbox=Spinbox(shuffwindow,from_=1,to=height,textvariable=ypixel)
yspinbox.pack()

shuffbutton=Button(shuffwindow,text="Shuffle All",command=lambda: shufflepixels())
shuffbutton.pack()
shuffley=Button(shuffwindow, text="Shuffle Y Axis", command=lambda:shuffleyaxis())
shuffley.pack()
shufflex=Button(shuffwindow, text="Shuffle X Axis", command=lambda:shufflexaxis())
shufflex.pack()
canvas_width=width
canvas_height=height
canvaslist=list() #list containing the coordinates of each rectangle drawn onto canvas

photo=ImageTk.PhotoImage(img)
canvas=Canvas(root,width=canvas_width,height=canvas_height)
canvas.x=0
canvas.y=0

canvas.bind("<ButtonPress-1>", on_button_press)
canvas.pack()
canvas.create_image(0,0,anchor=NW,image=photo)

pixmap=img.load()
newimg=Image.new("RGB",(width,height))
newpixels=newimg.load()

widthlist=list()
heightlist=list()

for i in range (width):
    widthlist.append(i)

for i in range (height):
    heightlist.append(i)

photolist=list() #list of shuffled variations
varvalue=var.get()  #holds variation number as specified by user

masterwidth=list()
for i in range(varvalue):
    masterwidth.append(widthlist)
masterheight=list()
for i in range(varvalue):
    masterheight.append(heightlist)

for i in range (varvalue):

    randnum=randint(1,2)
   
    mwidth=masterwidth.pop()
    
    mheight=masterheight.pop()
    
    if randnum == 1:
        shufflewidth()
    
    elif randnum == 2:
        shuffleheight()
    

    for i in range(width):
        for j in range(height):
            newpixels[i, j]=pixmap[mwidth[i], mheight[j]]

    photolist.append(ImageTk.PhotoImage(newimg))    

global sharedcount
sharedcount=-1

bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)

previousbutton=Button(bottomframe,command=lambda: previousimage())
prevphoto=ImageTk.PhotoImage(file="images/left arrow.gif")
previousbutton.config(image=prevphoto, width="25", height="25")
previousbutton.pack(side=LEFT)

save=Button(bottomframe,command=lambda: saveimage())
savephoto=ImageTk.PhotoImage(file="images/savebutton.gif")
save.config(image=savephoto, width="25", height="25")
save.pack(side=LEFT)

nextbutton=Button(bottomframe,command=lambda: nextimage())
nextphoto=ImageTk.PhotoImage(file="images/right arrow.gif")
nextbutton.config(image=nextphoto, width="25", height="25")
nextbutton.pack(side=LEFT)

root.mainloop()
