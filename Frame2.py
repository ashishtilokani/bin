#######This code is developed by Alok Singh Thakur, Prashast Bindal and Siddharth Bhatia#######Frame2

import wx
import wx.lib.buttons
import numpy as np
import os 
import cv2.cv as cv #Import functions from OpenCV
import cv2
from numpy import *
from PIL import Image #python imaging library
#from common import Sketcher
from collections import Counter 
from Tkinter import * #code for importing points or could do it in matplotlib-not able to install
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename
import tkMessageBox
import Image, ImageTk
import ImageDraw
import copy

global answerleft
global answerright
global flagimageleftname
global flagimagerightname
flagimageleftname=0
flagimagerightname=0
global root
global rootflag ## to generate new root when back clicked and manual clicked again
rootflag=0
#root = Tk() #use this only once not every time. else canvas not made. root destroy will destroy it

global image_l
global image_r
global image_l1
global image_r1

image_l1= 'scene_l.jpg' ## initialised photos
image_r1= 'scene_l.jpg'

global flagimageremove ##for removing duplicate image if size exceeds canvas size
flagimageremove=0


##global variables
ii = Image.open(image_l1)
global box1 ##from where copied
box1 = (0, 0, 0, 0)
global region #so that we can use it in the second canvas
region = ii.crop(box1)
global polygon ##first polygon
polygon = [(100,100),(200,200),(150,150),(300,300),(175,275)] #initialize polygon
global polygon2 ##second polygon
polygon2 = [(100,100),(200,200),(150,150),(300,300),(175,275)] #initialize polygon            
global im
im = Image.open(image_l1).convert("RGBA")
global im2
im2 = Image.open(image_l1).convert("RGBA")         
global imArray
imArray = np.asarray(im)
global imArray2
imArray2 = np.asarray(im2)        
global maskIm
global mask
global maskIm2
global mask2
maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0) ##shape 1 width and shape 0 height
maskIm2 = Image.new('L', (imArray2.shape[1], imArray2.shape[0]), 0) 
mask = np.array(maskIm)
mask2 = np.array(maskIm2)                    
        
global newImArray
newImArray = np.empty(imArray.shape,dtype='uint8')            
newImArray[:,:,:3] = imArray[:,:,:3]
newImArray[:,:,3] = mask*255
    

global newIm
newIm = Image.fromarray(newImArray, "RGBA")

global i            
global a
a=0
global b
b=0
global flagleft ##to see if left image changed. then use answerleft from now on
flagleft=0
global flagright ##to see if rightimage changed. then use answerright from now on
flagright=0
global minh1,minh2,minw1,minw2,maxh1,maxh2,maxw1,maxw2 ## to reduce the polygon checking..A difficult logic to think!
maxh1=0
maxw1=0
minh2=648
minw2=968
maxh2=0
maxw2=0
minw1=968
minh1=648

global flagpolygon ##flag to keep on using the same polygon for pasting
flagpolygon=1
polygon = [(100,100),(200,200),(150,150),(300,300),(175,275)] #initialize polygon
global flagnewpolygon ###for new polygon
flagnewpolygon=0
global flag ##in filling
flag=np.array(maskIm)
global flagescape ##case if multiple escapes are pressed
flagescape=1
global flagdestroycanvas ##to destroy canvas after made first time. so that image loaded in first canvas only.
flagdestroycanvas=0
global flagnew ##used for canvas to return if n is pressed..very difficult error to counter!!
flagnew=0
global flagpop
flagpop=0
global flagq ## flag for quit in canvas
flagq=0
global width1
width1=0
global flagZoom
flagZoom=1

def create(parent):
    global frame2
    frame2 = Frame2(parent)
    return frame2

[wxID_FRAME2, wxID_FRAME2BUTTON1, wxID_FRAME2PANEL1, wxID_FRAME2STATICTEXT1, 
 wxID_FRAME2TOGGLEBUTTON1, wxID_FRAME2TOGGLEBUTTON2, wxID_FRAME2TOGGLEBUTTON4, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Frame2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='Frame2', parent=prnt,
              pos=wx.Point(900, 144), size=wx.Size(400, 485),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame2')
        self.SetClientSize(wx.Size(384, 447))

        self.panel1 = wx.Panel(id=wxID_FRAME2PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 447),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME2STATICTEXT1,
              label=u'Masking', name='staticText1', parent=self.panel1,
              pos=wx.Point(136, 24), size=wx.Size(96, 33), style=0)
        self.staticText1.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.toggleButton1 = wx.ToggleButton(id=wxID_FRAME2TOGGLEBUTTON1,
              label=u'Manual', name='toggleButton1', parent=self.panel1,
              pos=wx.Point(32, 184), size=wx.Size(120, 48), style=0)
        self.toggleButton1.SetValue(False)
        self.toggleButton1.Enable(False)
        self.toggleButton1.Bind(wx.EVT_TOGGLEBUTTON,
              self.OnToggleButton1Togglebutton, id=wxID_FRAME2TOGGLEBUTTON1)

        self.toggleButton2 = wx.ToggleButton(id=wxID_FRAME2TOGGLEBUTTON2,
              label=u'Automatic', name='toggleButton2', parent=self.panel1,
              pos=wx.Point(32, 256), size=wx.Size(120, 48), style=0)
        self.toggleButton2.SetValue(False)
        self.toggleButton2.Enable(False)
        self.toggleButton2.Bind(wx.EVT_TOGGLEBUTTON,
              self.OnToggleButton2Togglebutton, id=wxID_FRAME2TOGGLEBUTTON2)

        

        self.toggleButton4 = wx.ToggleButton(id=wxID_FRAME2TOGGLEBUTTON4,
              label=u'Choose Image To Mask From', name='toggleButton4', parent=self.panel1,
              pos=wx.Point(90, 112), size=wx.Size(180, 47), style=0)
        self.toggleButton4.SetValue(False)
        self.toggleButton4.Bind(wx.EVT_TOGGLEBUTTON,
              self.OnToggleButton4Togglebutton, id=wxID_FRAME2TOGGLEBUTTON4)

        self.button1 = wx.Button(id=wxID_FRAME2BUTTON1, label=u'Quit',
              name='button1', parent=self.panel1, pos=wx.Point(216, 256),
              size=wx.Size(120, 48), style=0)
        self.button1.Enable(False)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME2BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)
    
    
    def OnButton1Button(self, event): ## quit button
        global flagremove
        global origleftheight
        global origleftwidth
        global origrightheight
        global origrightwidth
        global answerleft 
        global answerright
        if flagimageremove==0:
            imgl = Image.open(answerleft)
            imgl = imgl.resize((origleftwidth,origleftheight), Image.ANTIALIAS)
            imgl.save(answerleft)
            
            imgr = Image.open(answerright)
            imgr = imgr.resize((origrightwidth,origrightheight), Image.ANTIALIAS)
            imgr.save(answerright)
            
            #os.remove('imagel1.jpg')
            #os.remove('imager1.jpg')
        
        global rootflag
        
        if rootflag==0:
            root.destroy()

        self.Destroy()
        
        
    def OnToggleButton4Togglebutton(self, event):## choose images button
        #self.staticText1.SetLabel('Success')
                
        global answerleft
        global answerright
        global flagimageleftname
        global flagimagerightname
        flagimageleftname=0
        flagimagerightname=0

        global root
        global rootflag
        rootflag=0
        
        root = Tk()

        global image_l
        global image_r
        global image_l1
        global image_r1
        global properImage
        global zoomImage
        global flagimageremove 
        flagimageremove=0
        
        fmask = open('file_to_mask.txt','r')
        image_l = fmask.read()
        fmask.close()
        print image_l
        image_r = askopenfilename(parent=root, initialdir="C:/Users/Siddharth Bhatia/Desktop/IIRS/Pics",title='Select Image To Mask From')
        image_l1= 'imagel1.jpg'
        image_r1= 'imager1.jpg'
        answerleft= 'imagel2.jpg'
        answerright= 'imager2.jpg'

        #image_l1=copy.deepcopy(image_l)
        #image_r1=copy.copy(image_r)
        properLeftImage = Image.open(image_l)
        zoomLeftImage = properLeftImage.copy()
        zoomLeftImage.save(image_l1)
        properRightImage = Image.open(image_r)
        zoomRightImage = properRightImage.copy()
        zoomRightImage.save(image_r1)
        
        left  = cv.LoadImage(image_l1,cv.CV_LOAD_IMAGE_GRAYSCALE)
        right = cv.LoadImage(image_r1,cv.CV_LOAD_IMAGE_GRAYSCALE)
        global width1
        global origleftwidth
        global origleftheight
        global origrightwidth
        global origrightheight
        global currentleftheight
        global currentleftwidth
        global currentrightheight
        global currentrightwidth
        global currentleftheight_for_zoom
        global currentleftwidth_for_zoom
        global currentrightheight_for_zoom
        global currentrightwidth_for_zoom
        origleftwidth=left.width
        origleftheight=left.height
        origrightwidth=right.width
        origrightheight=right.height
        currentleftwidth=left.width
        currentleftheight=left.height
        currentrightwidth=right.width
        currentrightheight=right.height
        currentleftwidth_for_zoom=left.width
        currentleftheight_for_zoom=left.height
        currentrightwidth_for_zoom=right.width
        currentrightheight_for_zoom=right.height

        if(left.width>968 or left.height>648):
            flagimageremove=0
            imgl = Image.open(image_l)
            imgl = imgl.resize((968,648), Image.ANTIALIAS)
            imgl.save(image_l1)
            currentleftwidth=968
            currentleftheight=648
            width1=968/100

        if(right.width>968 or right.height>648):
            flagimageremove=0
            imgr = Image.open(image_r)
            imgr = imgr.resize((968,648), Image.ANTIALIAS)
            imgr.save(image_r1)
            currentrightwidth=968
            currentrightheight=648
            width1=968/100

        ##global variables
        
        self.toggleButton1.Enable(True)
        self.toggleButton2.Enable(True)
        self.button1.Enable(True)
            
   
    def OnToggleButton1Togglebutton(self, event): ## manual button

                
        global answerleft
        global answerright
        global flagimageleftname
        global flagimagerightname
        global flagq
        flagq=0

        global root
        global rootflag
        if rootflag==1:
            root = Tk()
                         
            
        self.Show(False)
        #Boa:Frame:Frame3

        global box1 
        global region
        global polygon
        global im
        global imArray
        global maskIm
        global mask
        global newImArray
        global newIm
        global i            
        global a
        global b
        global flagleft
        global flagright
        global minh1,minh2,minw1,minw2,maxh1,maxh2,maxw1,maxw2
        global flagpolygon
        global flagnewpolygon
        global flagdestroycanvas
        global image_l
        global image_r
        global image_l1
        global image_r1
        


        global flag
        global flagescape
        global flagnew

        ##global variables
        ii = Image.open(image_l1)
        global box1
        box1 = (0, 0, 0, 0)
        global region
        region = ii.crop(box1)
        global polygon
        polygon = [(100,100),(200,200),(150,150),(300,300),(175,275)]
        global polygon2
        polygon2 = [(100,100),(200,200),(150,150),(300,300),(175,275)]
        global im
        global im2
        global imArray
        global imArray2
        global maskIm
        global mask
        global maskIm2
        global mask2
        im = Image.open(image_l1).convert("RGBA")
        im2 = Image.open(image_l1).convert("RGBA")         
        imArray = np.asarray(im)
        imArray2 = np.asarray(im2)        
        maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0) ##shape 1 width and shape 0 height
        maskIm2 = Image.new('L', (imArray2.shape[1], imArray2.shape[0]), 0) 
        mask = np.array(maskIm)
        mask2 = np.array(maskIm2)                    
            
        global newImArray
        newImArray = np.empty(imArray.shape,dtype='uint8')            
        newImArray[:,:,:3] = imArray[:,:,:3]
        newImArray[:,:,3] = mask*255
        

        global newIm
        newIm = Image.fromarray(newImArray, "RGBA")
        
        global i            
        global a
        a=0
        global b
        b=0
        global flagleft
        #flagleft=0 ## because we need masked images for manual and automatic
        global flagright
        #flagright=0
        global minh1,minh2,minw1,minw2,maxh1,maxh2,maxw1,maxw2
        maxh1=0
        maxw1=0
        minh2=648
        minw2=968
        maxh2=0
        maxw2=0
        minw1=968
        minh1=648

        global flagpolygon
        flagpolygon=1
        polygon = [(100,100),(200,200),(150,150),(300,300),(175,275)]
        global flagnewpolygon
        flagnewpolygon=0
        global flag
        flag=np.array(maskIm)
        global flagescape
        flagescape=1
        global flagdestroycanvas
        flagdestroycanvas=0
        global flagnew
        flagnew=0
        
        

        def create(parent):
            return Frame3(parent)


        [wxID_FRAME3, wxID_FRAME3PANEL1, wxID_FRAME3STATICTEXT1, 
         wxID_FRAME3TOGGLEBUTTON1, wxID_FRAME3TOGGLEBUTTON2, wxID_FRAME3TOGGLEBUTTON3, 
         wxID_FRAME3TOGGLEBUTTON4, wxID_FRAME3TOGGLEBUTTON5, wxID_FRAME3TOGGLEBUTTON6, 
         wxID_FRAME3TOGGLEBUTTON7, 
        ] = [wx.NewId() for _init_ctrls in range(10)]
        
        frame2hold=self

        class Frame3(wx.Frame):
            #Frame2n=create(None)
            def _init_ctrls(self, prnt):
                # generated method, don't edit
                wx.Frame.__init__(self, id=wxID_FRAME3, name='Frame3', parent=prnt,
                      pos=wx.Point(900, 144), size=wx.Size(400, 485),
                      style=wx.DEFAULT_FRAME_STYLE, title='Frame3')
                self.SetClientSize(wx.Size(384, 447))

                self.panel1 = wx.Panel(id=wxID_FRAME3PANEL1, name='panel1', parent=self,
                      pos=wx.Point(0, 0), size=wx.Size(384, 447),
                      style=wx.TAB_TRAVERSAL)

                self.toggleButton3 = wx.ToggleButton(id=wxID_FRAME3TOGGLEBUTTON3,
                      label=u'Begin Masking', name='toggleButton3', parent=self.panel1,
                      pos=wx.Point(20, 248), size=wx.Size(140, 48), style=0)
                self.toggleButton3.SetValue(False)
                self.toggleButton3.Bind(wx.EVT_TOGGLEBUTTON,
                      self.OnToggleButton3Togglebutton, id=wxID_FRAME3TOGGLEBUTTON3)


                self.toggleButton5 = wx.ToggleButton(id=wxID_FRAME3TOGGLEBUTTON5,
                      label=u'Back', name='toggleButton5', parent=self.panel1,
                      pos=wx.Point(208, 152), size=wx.Size(112, 48), style=0)
                self.toggleButton5.SetValue(False)
                self.toggleButton5.Bind(wx.EVT_TOGGLEBUTTON,
                      self.OnToggleButton5Togglebutton, id=wxID_FRAME3TOGGLEBUTTON5)

                
                self.toggleButton6 = wx.ToggleButton(id=wxID_FRAME3TOGGLEBUTTON6,
                      label=u'Quit', name='toggleButton6', parent=self.panel1,
                      pos=wx.Point(208, 248), size=wx.Size(112, 48), style=0)
                self.toggleButton6.SetValue(False)
                self.toggleButton6.SetBackgroundColour(wx.Colour(255, 128, 128))
                self.toggleButton6.Bind(wx.EVT_TOGGLEBUTTON,
                      self.OnToggleButton6Togglebutton, id=wxID_FRAME3TOGGLEBUTTON6)

                self.staticText1 = wx.StaticText(id=wxID_FRAME3STATICTEXT1,
                      label=u'Masking', name='staticText1', parent=self.panel1,
                      pos=wx.Point(136, 24), size=wx.Size(75, 25), style=0)
                self.staticText1.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL,
                      False, u'Tahoma'))

            def __init__(self, parent):
                self._init_ctrls(parent)


            def OnToggleButton3Togglebutton(self, event):
                

                self.toggleButton3.Enable(False)
                self.toggleButton5.Enable(False)
                self.toggleButton6.Enable(False)
                
                global answerleft
                global answerright
                global flagimageleftname
                global flagimagerightname

                global root
                global box1 
                global region
                global polygon
                global im
                global imArray
                global maskIm
                global mask
                global newImArray
                global newIm
                global i            
                global a
                global b
                global flagleft
                global flagright
                global minh1,minh2,minw1,minw2,maxh1,maxh2,maxw1,maxw2
                global flagpolygon
                global flagnewpolygon
                global flagdestroycanvas
                global image_l
                global image_r
                global image_l1
                global image_r1
                global flag
                global flagescape
                global flagnew
                global flagq
                global image_to_mask
                global image_to_mask_from
                global photoImg2
                global photoImg
                flagq=0

                def zoom_left(self):
                    b = sliderLeft.get()
                    global photoImg2
                    global image_l
                    global image_to_mask
                    global flagZoom
                    print b
                    global currentleftwidth
                    global currentleftheight
                    global flagimageleftname
                    if flagZoom==0:
                        if flagimageleftname==1:
                            imgl = Image.open(answerleft,mode='r')
                        else:
                            imgl = Image.open(image_l,mode='r')
                        if b>=100:
                            imgl = imgl.resize((currentleftwidth*b/100,currentleftheight*b/100),Image.BILINEAR)
                        else:
                            imgl = imgl.resize((currentleftwidth*b/100,currentleftheight*b/100),Image.ANTIALIAS)
                        imgl.save(image_l1)
                        photoImg2 = ImageTk.PhotoImage(imgl)
                        canvas2.itemconfigure(image_to_mask, image=photoImg2)
                        canvas2.config(scrollregion=canvas2.bbox(ALL))
                    flagZoom=0

                def zoom_right(self):
                    b = sliderRight.get()
                    global photoImg
                    global image_to_mask_from
                    global image_l
                    global image_r
                    global flagZoom
                    print b
                    global currentrightwidth
                    global currentrightheight
                    if flagZoom==0:
                        imgr = Image.open(image_r,mode='r')
                        if b>=100:
                            imgr = imgr.resize((currentrightwidth*b/100,currentrightheight*b/100),Image.BILINEAR)
                        else:
                            imgr = imgr.resize((currentrightwidth*b/100,currentrightheight*b/100),Image.ANTIALIAS)
                        imgr.save(image_r1)
                        photoImg = ImageTk.PhotoImage(imgr)
                        canvas.itemconfigure(image_to_mask_from, image=photoImg)
                        canvas.config(scrollregion=canvas.bbox(ALL))
                    flagZoom=0

                def create_polygon():
                    global flagpolygon
                    global flagnewpolygon
                    global polygon
                    flagpolygon=1
                    flagnewpolygon=2
                    polygon = [(100,100),(200,200),(150,150),(300,300),(175,275)]
                    root.quit()
                    global flagnew
                    flagnew=1
                    canvas.delete("line")

                def begin_masking():
                    global flagpolygon
                    global flagnewpolygon
                    global polygon
                    if(flagpolygon==0):
                        polygon.pop(4)
                        polygon.pop(3)
                        polygon.pop(2)
                        polygon.pop(1)
                        polygon.pop(0)
                        flagpolygon=2 ## equate to 2 so that initial polygon removed only once from the polygon list.not equal to 0 or 1
                        flagnewpolygon=1

                        global flagescape
                        if flagescape==1:
                            flagescape=0
                            root.quit()

                def quit_masking():
                    self.toggleButton5.Enable(True)
                    self.toggleButton6.Enable(True)

                    global flagq
                    flagq=1
                                    
                    canvas.destroy()
                    frame.destroy()
                    global rootflag
                    rootflag=1
                    root.destroy()

                def changeRightImage():## choose images button
        #self.staticText1.SetLabel('Success')
                
                    global answerleft
                    global flagimageleftname
                    flagimageleftname=0
                    global flagRight
                    flagRight=0
                    global flagleft
                    flagleft=0
                    global flagZoom
                    flagZoom=1

                    global image_to_mask
                    global photoImg2
                    global image_l
                    global image_l1
                    global properImage
                    global zoomImage
                    global flagimageremove 
                    flagimageremove=0
        
                    image_l = askopenfilename(parent=root, initialdir="C:/Users/Siddharth Bhatia/Desktop/IIRS/Pics",title='Select Image To Mask From')
                    image_l1= 'imagel1.jpg'
                    answerleft= 'imagel2.jpg'

                    properLeftImage = Image.open(image_l)
                    zoomLeftImage = properLeftImage.copy()
                    zoomLeftImage.save(image_l1)
        
                    left  = cv.LoadImage(image_l1,cv.CV_LOAD_IMAGE_GRAYSCALE)
                    global width1
                    global origleftwidth
                    global origleftheight
                    global currentleftheight
                    global currentleftwidth
                    global currentleftheight_for_zoom
                    global currentleftwidth_for_zoom
                    origleftwidth=left.width
                    origleftheight=left.height
                    currentleftwidth=left.width
                    currentleftheight=left.height
                    currentleftwidth_for_zoom=left.width
                    currentleftheight_for_zoom=left.height

                    if(left.width>968 or left.height>648):
                        flagimageremove=0
                        imgl = Image.open(image_l)
                        imgl = imgl.resize((968,648), Image.ANTIALIAS)
                        imgl.save(image_l1)
                        currentleftwidth=968
                        currentleftheight=648
                        width1=968/100

                    img2 = Image.open(image_l1)
                    photoImg2 = ImageTk.PhotoImage(img2)
                    canvas2.itemconfigure(image_to_mask, image=photoImg2)
                    canvas2.config(scrollregion=canvas2.bbox(ALL))

                def changeLeftImage():## choose images button
                #self.staticText1.SetLabel('Success')
                
                    global answerright
                    global flagimagerightname
                    flagimagerightname=0
                    global flagLeft
                    flagLeft=0
                    global flagZoom
                    global flagleft
                    flagleft=0

                    global image_to_mask_from
                    global photoImg
                    global image_r
                    global image_r1
                    global properImage
                    global zoomImage
                    global flagimageremove 
                    flagimageremove=0
        
                    image_r = askopenfilename(parent=root, initialdir="C:/Users/Siddharth Bhatia/Desktop/IIRS/Pics",title='Select Image To Mask From')
                    image_r1= 'imager1.jpg'
                    answerright= 'imager2.jpg'

                    properRightImage = Image.open(image_r)
                    zoomRightImage = properRightImage.copy()
                    zoomRightImage.save(image_r1)
        
                    right = cv.LoadImage(image_r1,cv.CV_LOAD_IMAGE_GRAYSCALE)
                    global width1
                    global origrightwidth
                    global origrightheight
                    global currentrightheight
                    global currentrightwidth
                    global currentrightheight_for_zoom
                    global currentrightwidth_for_zoom
                    origrightwidth=right.width
                    origrightheight=right.height
                    currentrightwidth=right.width
                    currentrightheight=right.height
                    currentrightwidth_for_zoom=right.width
                    currentrightheight_for_zoom=right.height

                    if(right.width>968 or right.height>648):
                        flagimageremove=0
                        imgr = Image.open(image_r)
                        imgr = imgr.resize((968,648), Image.ANTIALIAS)
                        imgr.save(image_r1)
                        currentrightwidth=968
                        currentrightheight=648
                        width1=968/100
                    img = Image.open(image_r1)
                    photoImg = ImageTk.PhotoImage(img)
                    canvas.itemconfigure(image_to_mask_from, image=photoImg)
                    canvas.config(scrollregion=canvas.bbox(ALL))

                def change_mode():
                    quit_masking()
                    global frame3
                    frame3.OnToggleButton6Togglebutton(event)

                frame = Frame(root, bd=2, relief=SUNKEN)
                leftFrame = Frame(frame,bd=0)
                topFrame = Frame(frame,bd=0)
                rightFrame = Frame(frame,bd=0)
                topFrame.pack(side=TOP,fill=BOTH)
                leftFrame.pack(side=LEFT,fill=BOTH,expand=TRUE)
                rightFrame.pack(side=LEFT,fill=BOTH,expand=TRUE)
                xscroll = Scrollbar(leftFrame, orient=HORIZONTAL)
                xscroll.pack(side=BOTTOM,fill=X)
                yscroll = Scrollbar(leftFrame,orient=VERTICAL)
                yscroll.pack(side=RIGHT, fill=Y)
                canvas = Canvas(leftFrame, bd=0,xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
                canvas.pack(side=LEFT,expand=TRUE,fill=BOTH)
                xscroll.config(command=canvas.xview)
                yscroll.config(command=canvas.yview)

                xscroll2 = Scrollbar(rightFrame, orient=HORIZONTAL)
                xscroll2.pack(side=BOTTOM,fill=X)
                yscroll2 = Scrollbar(rightFrame,orient=VERTICAL)
                yscroll2.pack(side=RIGHT, fill=Y)
                canvas2 = Canvas(rightFrame, bd=0,xscrollcommand=xscroll2.set, yscrollcommand=yscroll2.set)
                xscroll2.config(command=canvas2.xview)
                yscroll2.config(command=canvas2.yview)
                canvas2.pack(side=LEFT,expand=TRUE,fill=BOTH)

                sliderLeft = Scale(topFrame,from_=25,to=200,orient=HORIZONTAL,command=zoom_left,label="Zoom Right Image")
                sliderRight = Scale(topFrame,from_=25,to=200,orient=HORIZONTAL,command=zoom_right,label="Zoom Left Image")
                sliderRight.pack(side=LEFT)
                sliderLeft.pack(side=RIGHT)
                if flagZoom==1:
                    sliderLeft.set(100)
                    sliderRight.set(100)

                bnewPolygon = Button(topFrame,text="Create New Polygon",command=create_polygon)
                bnewPolygon.pack(side=LEFT)
                bmask = Button(topFrame,text="Begin Masking",command=begin_masking)
                bmask.pack(side=LEFT)
                bquit = Button(topFrame,text="Quit",command=quit_masking)
                bquit.pack(side=LEFT)

                bchangeRightImage = Button(topFrame,text="Change Right Image",command=changeRightImage)
                bchangeRightImage.pack(side=RIGHT)
                bchangeLeftImage = Button(topFrame,text="Change Left Image",command=changeLeftImage)
                bchangeLeftImage.pack(side=RIGHT)
                bchangeMode = Button(topFrame,text="Change Mode",command=change_mode)
                bchangeMode.pack(side=RIGHT)

                frame.pack(fill=BOTH,expand=TRUE)

                img = Image.open(image_r1)
                photoImg = ImageTk.PhotoImage(img)
                image_to_mask_from = canvas.create_image(0,0,image=photoImg,anchor="nw")
                canvas.config(scrollregion=canvas.bbox(ALL))

                img2 = Image.open(image_l1)
                photoImg2 = ImageTk.PhotoImage(img2)
                image_to_mask = canvas2.create_image(0,0,image=photoImg2,anchor="nw")
                canvas2.config(scrollregion=canvas2.bbox(ALL))
                    
                while True:
                    if flagdestroycanvas==1:
                        flagdestroycanvas=0
                        canvas.destroy()
                        frame.destroy()

                    if flagleft==1:
                            #image_l1='answerleft.jpg'
                        imgl = Image.open(answerleft)
                        imgl.save(image_l1)
                    
                    if flagnewpolygon==0 or flagnewpolygon==2:
                            #img = ImageTk.PhotoImage(Image.open(image_l1))
                            
                        img = Image.open(image_r1)
                            #img = ImageTk.PhotoImage(Image.open(image_r1))
                            
                    #if flagnewpolygon==1:
                    img2 = Image.open(image_l1)
                            #img = ImageTk.PhotoImage(Image.open(image_l1))
                    
                    #if __name__ == "__main__":

                       #function to be called when mouse is clicked
                        
                    while True:
                        
                        if flagnew==1:
                            flagnew=0
                            root.quit()
                    
                        global flagescape
                        flagescape=1
                        
                                                   
                        i=1
                        
                        def printcoords(event):
                            #outputting x and y coords to console
                            
                            event.x = int(canvas.canvasx(event.x)) ## canvas.canvasx reqd for absolute coordinates on the canvas with scrolling..difficult to find!!
                            event.y = int(canvas.canvasy(event.y))
                            
                            #print (event.x,event.y) ## returns integer values only
                            global minw1,minh1,maxw1,maxh1

                            
                            value = (event.x,event.y)
                            if event.x<minw1:
                                minw1=event.x
                            if event.y<minh1:
                                minh1=event.y
                            if event.x>maxw1:
                                maxw1=event.x
                            if event.y>maxh1:
                                maxh1=event.y
                            
                            global polygon
                            
                            polygon.append(value)
                            global i
                            global a
                            global b
                            global width1
                            if i>1:
                                canvas.create_line(a,b,event.x,event.y,fill="red",width=1,tag="line") ###creates line if more than 1 point
                                
                            a=event.x
                            b=event.y
                            i=i+1
                            global flagpolygon
                            flagpolygon=0
                            
                        #mouseclick event
                        if flagpolygon==1: #to get new polygon only when starts again
                            canvas.bind("<Button 1>",printcoords)
                            
                        break                    ##code runs after first time when we break. imp line.
                        
                    root.mainloop() #loop will continue but quit inside will make it move outside

                    #if __name__ == "__main__":

                    if flagleft==1:
                            #image_l1='answerleft.jpg'
                        imgl = Image.open(answerleft)
                        imgl.save(image_l1)

                    img2 = Image.open(image_l1)
                        #img = ImageTk.PhotoImage(Image.open(image_l1))

                    if flagq==0:
                        photoImg2 = ImageTk.PhotoImage(img2)
                        canvas2.itemconfigure(image_to_mask, image=photoImg2)
                        canvas2.config(scrollregion=canvas2.bbox(ALL))
                    
                    def point_inside_polygon(x,y,poly): ##first takes width, then height
                        """Deciding if a LaserPoint is inside (True, False otherwise) a polygon,
                        where poly is a list of pairs (x,y) containing the coordinates
                        of the polygon's vertices."""
                        n = len(poly)
                        if n <= 2:
                            raise ValueError("poly has only %s vertice(s)" % (n))
                        inside = False
                        p1x,p1y = poly[0]
                        for i in xrange(n+1):
                            p2x,p2y = poly[i % n]
                            if y > min(p1y,p2y):
                                if y <= max(p1y,p2y):
                                    if x <= max(p1x,p2x):
                                        if p1y != p2y:
                                            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                                        if p1x == p2x or x <= xinters:
                                            inside = not inside
                            p1x,p1y = p2x,p2y
                        return inside
                                
                    # read image as RGB and add alpha (transparency)    
                    #global im
                    
                    im = Image.open(image_r1).convert("RGBA")
                     
                    # convert to numpy (for convenience)
                    #global imArray
                    imArray = np.asarray(im)
                
                    maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
                    ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
                    mask = np.array(maskIm)
                    for i in range(minh1,maxh1):## i  in height range
                        for j in range(minw1,maxw1):
                            if point_inside_polygon(j,i,polygon): ##first width, then height-imp.
                                mask[i,j]=1
                            else:
                                mask[i,j]=0

                    # assemble new image (uint8: 0-255)
                    newImArray = np.empty(imArray.shape,dtype='uint8')
                    
                    # colors (three first columns, RGB)
                    newImArray[:,:,:3] = imArray[:,:,:3]
                    
                    # transparency (4th column)
                    newImArray[:,:,3] = mask*255
                    
                    # back to Image from numpy
                    #global newIm
                    newIm = Image.fromarray(newImArray, "RGBA")
                    newIm.save("polygon.jpg")

                
                    def printcoords2(event):
                            #outputting x and y coords to console

                        global answerleft
                        global answerright
                        global flagimageleftname
                        global flagimagerightname

                        
                        
                        event.x = int(canvas2.canvasx(event.x))
                        event.y = int(canvas2.canvasy(event.y))
                        #print (event.x,event.y) # new point coordinates



                        io = Image.open(image_l1).convert("RGBA")
                        
                        dist1=event.x-polygon[0][0] ##dist. along width
                        
                        dist2=event.y-polygon[0][1] ##dist. along height
                        
                        newIm = Image.open("polygon.jpg").convert("RGBA")

                        global minw1,minh1,maxw1,maxh1
                        for i in range(minh1, maxh1):
                            for j in range(minw1, maxw1):
                                   if(mask[i,j]==1):
                                    x,y,w,h=(j,i,1,1) ##box first width coordinate, then height coordinate
                                    box1=(x,y,x+w,y+h)
                                    box2=(x+dist1,y+dist2,x+dist1+w,y+dist2+h)
                                    region=newIm.crop(box1)
                                    io.paste(region,box2)

                        global flagleft
                        global flagright
                        flagleft=1
                        #io.save(".jpg") #final image
                        
                        if flagimageleftname==0:
                            flagimageleftname=1
                            msg = wx.MessageDialog(None,'Please save the image name with .jpg extension in window to appear')
                            msg.ShowModal()
                            answerleft=asksaveasfilename(parent=root, initialdir="C:/Users/Siddharth Bhatia/Desktop/",title='Save Masked Image')
                        io.save(answerleft) #final image                        
                            
                        root.quit()
                        
                        #mouseclick event
                    if flagq==0:
                        canvas2.bind("<Button 1>",printcoords2)
                    
                    flagescape=0
                    if flagnew==1:
                        root.quit()
                                                 
                    if flagnew==0:
                        root.mainloop()

                    if flagq==1:
                        break
                    
                    #flagdestroycanvas=1
                    
                          
                event.Skip()
                                
                
            def OnToggleButton5Togglebutton(self, event):
                self.Destroy()
                #self.Show(False)
                global rootflag
                global flagq
                if flagq==1:
                    rootflag=1
                else:
                    rootflag=0
                
                
                
                frame2hold.Show(True)
                
            def OnToggleButton6Togglebutton(self, event):
                global flagremove
                global origleftheight
                global origleftwidth
                global origrightheight
                global origrightwidth
                global answerleft 
                global answerright
                if flagimageremove==0:
                    imgl = Image.open(answerleft)
                    imgl = imgl.resize((origleftwidth,origleftheight), Image.ANTIALIAS)
                    imgl.save(answerleft)
                    
                    imgr = Image.open(answerright)
                    imgr = imgr.resize((origrightwidth,origrightheight), Image.ANTIALIAS)
                    imgr.save(answerright)
                    
                    #os.remove('imagel1.jpg')
                    #os.remove('imager1.jpg')
                    
                #frame2hold.Destroy()
                global rootflag
                
                
                if rootflag==0:
                    root.destroy()

                self.Destroy()
                frame2hold.Show(True)

        global frame3       
        frame3=create(None)
        frame3.Show(True)



                        
    def OnToggleButton2Togglebutton(self, event):
        self.Show(False)
        #Boa:Frame:Frame3


        global answerleft
        global answerright
        global flagimageleftname
        global flagimagerightname

        global root
        global rootflag
        if rootflag==1:
            root = Tk()
            
        #self.Show(False)
        #Boa:Frame:Frame3

        global box1 
        global region
        global polygon
        global polygon2
        global im
        global imArray
        global maskIm
        global mask
        global newImArray
        global newIm
        global i            
        global a
        global b
        global flagleft
        global flagright
        global minh1,minh2,minw1,minw2,maxh1,maxh2,maxw1,maxw2
        global flagpolygon
        global flagnewpolygon
        global flagdestroycanvas
        global image_l
        global image_r
        global image_l1
        global image_r1
        
        global flag
        global flagescape
        global flagnew

        ##global variables
        ii = Image.open(image_l1)
        global box1
        box1 = (0, 0, 0, 0)
        global region
        region = ii.crop(box1)
        global polygon
        polygon = [(100,100),(200,200),(150,150),(300,300),(175,275)]
        global polygon2
        polygon2 = [(100,100),(200,200),(150,150),(300,300),(175,275)]
        global im
        im = Image.open(image_l1).convert("RGBA")
        global im2
        im2 = Image.open(image_l1).convert("RGBA")         
        global imArray
        imArray = np.asarray(im)
        global imArray2
        imArray2 = np.asarray(im2)        
        global maskIm
        global mask
        global maskIm2
        global mask2
        maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0) ##shape 1 width and shape 0 height
        maskIm2 = Image.new('L', (imArray2.shape[1], imArray2.shape[0]), 0) 
        mask = np.array(maskIm)
        mask2 = np.array(maskIm2)                    
            
        global newImArray
        newImArray = np.empty(imArray.shape,dtype='uint8')            
        newImArray[:,:,:3] = imArray[:,:,:3]
        newImArray[:,:,3] = mask*255
        

        global newIm
        newIm = Image.fromarray(newImArray, "RGBA")
        
        global i            
        global a
        a=0
        global b
        b=0
        global flagleft
        #flagleft=0
        global flagright
        #flagright=0
        global minh1,minh2,minw1,minw2,maxh1,maxh2,maxw1,maxw2
        maxh1=0
        maxw1=0
        minh2=648
        minw2=968
        maxh2=0
        maxw2=0
        minw1=968
        minh1=648

        global flagpolygon
        flagpolygon=1
        polygon = [(100,100),(200,200),(150,150),(300,300),(175,275)]
        global flagnewpolygon
        flagnewpolygon=0
        global flag
        flag=np.array(maskIm)
        global flagescape
        flagescape=1
        global flagdestroycanvas
        flagdestroycanvas=0
        global flagnew
        flagnew=0
        
        def create(parent):
            return Frame4(parent)

        [wxID_FRAME4, wxID_FRAME4PANEL1, wxID_FRAME4STATICTEXT1, 
         wxID_FRAME4TOGGLEBUTTON1, wxID_FRAME4TOGGLEBUTTON2, wxID_FRAME4TOGGLEBUTTON3, 
         wxID_FRAME4TOGGLEBUTTON4, wxID_FRAME4TOGGLEBUTTON5, wxID_FRAME4TOGGLEBUTTON6, 
         wxID_FRAME4TOGGLEBUTTON7, 
        ] = [wx.NewId() for _init_ctrls in range(10)]
        
        frame2hold=self

        class Frame4(wx.Frame):
            #Frame2n=create(None)
            def _init_ctrls(self, prnt):
                # generated method, don't edit
                wx.Frame.__init__(self, id=wxID_FRAME4, name='', parent=prnt,
                      pos=wx.Point(900, 144), size=wx.Size(400, 485),
                      style=wx.DEFAULT_FRAME_STYLE, title='Frame4')
                self.SetClientSize(wx.Size(384, 447))

                self.panel1 = wx.Panel(id=wxID_FRAME4PANEL1, name='panel1', parent=self,
                      pos=wx.Point(0, 0), size=wx.Size(384, 447),
                      style=wx.TAB_TRAVERSAL)
                

                self.toggleButton3 = wx.ToggleButton(id=wxID_FRAME4TOGGLEBUTTON3,
                      label=u'Begin Masking', name='toggleButton3', parent=self.panel1,
                      pos=wx.Point(20, 248), size=wx.Size(140, 48), style=0)
                self.toggleButton3.SetValue(False)
                self.toggleButton3.Bind(wx.EVT_TOGGLEBUTTON,
                      self.OnToggleButton3Togglebutton, id=wxID_FRAME4TOGGLEBUTTON3)

 

                self.toggleButton5 = wx.ToggleButton(id=wxID_FRAME4TOGGLEBUTTON5,
                      label=u'Back', name='toggleButton5', parent=self.panel1,
                      pos=wx.Point(208, 152), size=wx.Size(112, 48), style=0)
                self.toggleButton5.SetValue(False)
                self.toggleButton5.Bind(wx.EVT_TOGGLEBUTTON,
                      self.OnToggleButton5Togglebutton, id=wxID_FRAME4TOGGLEBUTTON5)

                
                self.toggleButton6 = wx.ToggleButton(id=wxID_FRAME4TOGGLEBUTTON6,
                      label=u'Quit', name='toggleButton6', parent=self.panel1,
                      pos=wx.Point(208, 248), size=wx.Size(112, 48), style=0)
                self.toggleButton6.SetValue(False)
                self.toggleButton6.SetBackgroundColour(wx.Colour(255, 128, 128))
                self.toggleButton6.Bind(wx.EVT_TOGGLEBUTTON,
                      self.OnToggleButton6Togglebutton, id=wxID_FRAME4TOGGLEBUTTON6)


                self.staticText1 = wx.StaticText(id=wxID_FRAME4STATICTEXT1,
                      label=u'Masking', name='staticText1', parent=self.panel1,
                      pos=wx.Point(136, 24), size=wx.Size(75, 25), style=0)
                self.staticText1.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL,
                      False, u'Tahoma'))

            def __init__(self, parent):
                self._init_ctrls(parent)


            def OnToggleButton3Togglebutton(self, event):
                self.toggleButton3.Enable(False)
                self.toggleButton5.Enable(False)
                self.toggleButton6.Enable(False)

                global answerleft
                global answerright
                global flagimageleftname
                global flagimagerightname

                global root
                global box1 
                global region
                global polygon
                global polygon2
                global im
                global imArray
                global maskIm
                global mask
                global newImArray
                global newIm
                global i            
                global a
                global b
                global flagleft
                global flagright
                global minh1,minh2,minw1,minw2,maxh1,maxh2,maxw1,maxw2
                global flagpolygon
                global flagnewpolygon
                global flagdestroycanvas
                global image_l
                global image_r
                global image_l1
                global image_r1
                global flag
                global flagescape
                global flagnew
                global flagq
                flagq=0

                global im2
                global imArray2
                global maskIm2
                global mask2
                global image_to_mask
                global image_to_mask_from
                global photoImg2
                
                def zoom_left(self):
                    b = sliderLeft.get()
                    global photoImg2
                    global image_l
                    global image_to_mask
                    global flagZoom
                    print b
                    global currentleftwidth
                    global currentleftheight
                    global flagimageleftname
                    global currentleftwidth_for_zoom
                    global currentleftheight_for_zoom
                    global minh1,minh2,minw1,minw2,maxh1,maxh2,maxw1,maxw2
                    if flagZoom==0:
                        if flagimageleftname==1:
                            imgl = Image.open(answerleft,mode='r')
                        else:
                            imgl = Image.open(image_l,mode='r')
                        if b>=100:
                            imgl = imgl.resize((currentleftwidth*b/100,currentleftheight*b/100),Image.BILINEAR)
                            currentleftwidth_for_zoom = currentleftwidth*b/100
                            currentleftheight_for_zoom = currentleftheight*b/100
                            minh2=currentleftheight_for_zoom
                            minw2=currentleftwidth_for_zoom
                        else:
                            imgl = imgl.resize((currentleftwidth*b/100,currentleftheight*b/100),Image.ANTIALIAS)
                            currentleftwidth_for_zoom = currentleftwidth*b/100
                            currentleftheight_for_zoom = currentleftheight*b/100
                            minh2=currentleftheight_for_zoom
                            minw2=currentleftwidth_for_zoom
                        imgl.save(image_l1)
                        photoImg2 = ImageTk.PhotoImage(imgl)
                        canvas2.itemconfigure(image_to_mask, image=photoImg2)
                        canvas2.config(scrollregion=canvas2.bbox(ALL))
                    flagZoom=0

                def zoom_right(self):
                    b = sliderRight.get()
                    global photoImg
                    global image_to_mask_from
                    global image_l
                    global image_r
                    global flagZoom
                    print b
                    global currentrightwidth
                    global currentrightheight
                    global currentrightwidth_for_zoom
                    global currentrightheight_for_zoom
                    global minh1,minh2,minw1,minw2,maxh1,maxh2,maxw1,maxw2
                    if flagZoom==0:
                        imgr = Image.open(image_r,mode='r')
                        if b>=100:
                            imgr = imgr.resize((currentrightwidth*b/100,currentrightheight*b/100),Image.BILINEAR)
                            currentrightwidth_for_zoom = currentrightwidth*b/100
                            currentrightheight_for_zoom = currentrightheight*b/100
                            minh1=currentrightheight_for_zoom
                            minw1=currentrightwidth_for_zoom
                        else:
                            imgr = imgr.resize((currentrightwidth*b/100,currentrightheight*b/100),Image.ANTIALIAS)
                            currentrightwidth_for_zoom = currentrightwidth*b/100
                            currentrightheight_for_zoom = currentrightheight*b/100
                            minh1=currentrightheight_for_zoom
                            minw1=currentrightwidth_for_zoom
                        imgr.save(image_r1)
                        photoImg = ImageTk.PhotoImage(imgr)
                        canvas.itemconfigure(image_to_mask_from, image=photoImg)
                        canvas.config(scrollregion=canvas.bbox(ALL))
                    flagZoom=0

                def create_polygon():
                    global flagpolygon
                    global flagnewpolygon
                    global polygon
                    global flagRectangle
                    flagpolygon=1
                    flagnewpolygon=2
                    polygon = [(100,100),(200,200),(150,150),(300,300),(175,275)]
                    root.quit()
                    global flagnew
                    flagnew=1
                    canvas.delete("line")
                    canvas2.delete("line")
                    flagRectangle=1

                def select_polygon():
                    global flagpolygon
                    global flagnewpolygon
                    global polygon
                    if(flagpolygon==0):
                        '''polygon.pop(4)
                        polygon.pop(3)
                        polygon.pop(2)
                        polygon.pop(1)
                        polygon.pop(0)'''
                        flagpolygon=2 ## equate to 2 so that initial polygon removed only once from the polygon list.not equal to 0 or 1
                        flagnewpolygon=1

                    global flagescape
                    if flagescape==1:
                        flagescape=0
                        root.quit()
                    global flagRightPolygon
                    flagRightPolygon=1

                def quit_masking():
                    self.toggleButton5.Enable(True)
                    self.toggleButton6.Enable(True)

                    global flagq
                    flagq=1
                                    
                    canvas.destroy()
                    frame.destroy()
                    global rootflag
                    rootflag=1
                    root.destroy()

                def save():
                    global io2
                    if flagleft==1:
                        io2.save(image_l1)

                def begin_masking():
                    global image_l
                    global answerleft
                    global answerright
                    global flagimageleftname
                    global flagimagerightname

                    global flagpolygon
                    global flagnewpolygon
                    global polygon
                    global flagescape
                    global polygon2
                    global rectangle
                            
                    polygon2.pop(4)
                    polygon2.pop(3)
                    polygon2.pop(2)
                    polygon2.pop(1)
                    polygon2.pop(0)
                    global flagpop
                    flagpop = 0
                                                                
                    # read image as RGB and add alpha (transparency)
                    global im2
                                
                    im2 = Image.open(image_l1).convert("RGBA")
                                 
                    # convert to numpy (for convenience)
                    global imArray2
                    imArray2 = np.asarray(im2)
                            
                    # create mask
                    global maskIm2
                    global mask2
                    global flag
                    global currentleftheight_for_zoom
                    global currentleftwidth_for_zoom
                    maskIm2 = Image.new('L', (imArray2.shape[1], imArray2.shape[0]), 0)
                    ImageDraw.Draw(maskIm2).polygon(polygon2, outline=1, fill=1)
                    mask2 = np.array(maskIm2)
                    flag = np.array(maskIm2)
                    global minh2,minw2,maxh2,maxw2
                    #print minh2,minw2,maxh2,maxw2
                    for i in range(minh2,maxh2):
                        for j in range(minw2,maxw2):
                            if point_inside_polygon(j,i,polygon2):
                                mask2[i,j]=1 ### where mask is 1 there flag is 0
                                flag[i,j]=0
                            else:
                                mask2[i,j]=0
                                flag[i,j]=1

                    # back to Image from numpy
                    global io2            
                    io2 = Image.open(image_l1).convert("RGBA")
                                
                    global mask
                    #      global mask2
                    #       global flag
                    global newIm
                    global region
                    global photoImg2
                    global image_to_mask

                    global minw1,minh1,maxw1,maxh1
                        
                    for i in range(minh2, maxh2): ###loop to check for point in second image i.e. canvas 2
                        #print i
                        for j in range(minw2, maxw2):  ###loop to check for point in second image i.e. canvas 2
                                        
                            if mask2[i,j]==1 and flag[i,j]==0:###if the point is in polygon 2 and it is not already pasted then go in. if pasted flag becomes 1

                                dist1=maxw1-minw1 ##distance from initial point of polygon--width dist
                                dist2=maxh1-minh1 ##height dist
                                if  (j+dist1)<currentleftwidth_for_zoom and (i+dist2)<currentleftheight_for_zoom:            
                                    if flag[i+dist2,j+dist1]==0 and mask2[i+dist2,j+dist1]==1 and flag[i,j]==0 and mask2[i,j]==1 and flag[i+dist2,j]==0 and mask2[i+dist2,j]==1 and flag[i,j+dist1]==0 and mask2[i,j+dist1]==1: ###to check if this point is inside polygon 1 and the point to be masked (pasted upon) is inside the polygon 2. If outside then flag already 1 and if pasted on this then also flag 1.So goes only for points which are inside and not pasted (second if condition)
                                        #x,y=(j,i)
                                        box1=(minw1,minh1,maxw1,maxh1)
                                        box2=(j,i,j+dist1,i+dist2)
                                        region=newIm.crop(box1)
                                        io2.paste(region,box2)
                                        #flag[i+dist2,j+dist1]=1 ###flag changed to 1 so that not pasted again

                                if  (j-dist1)>currentleftwidth_for_zoom and (i-dist2)>currentleftheight_for_zoom:            
                                    if flag[i-dist2,j-dist1]==0 and mask2[i-dist2,j-dist1]==1 and flag[i,j]==0 and mask2[i-dist2,j]==1 and flag[i-dist2,j]==0 and mask2[i-dist2,j]==1 and flag[i,j-dist1]==0 and mask2[i,j-dist1]==1: ###to check if this point is inside polygon 1 and the point to be masked (pasted upon) is inside the polygon 2. If outside then flag already 1 and if pasted on this then also flag 1.So goes only for points which are inside and not pasted (second if condition)
                                        #x,y=(j,i)
                                        box1=(minw1,minh1,maxw1,maxh1)
                                        box2=(j,i,j-dist1,i-dist2)
                                        region=newIm.crop(box1)
                                        io2.paste(region,box2)
                                        #flag[i-dist2,j-dist1]=1 ###flag changed to 1 so that not pasted again

                                if  (j-dist1)>currentleftwidth_for_zoom and (i+dist2)<currentleftheight_for_zoom:            
                                    if flag[i+dist2,j-dist1]==0 and mask2[i+dist2,j-dist1]==1 and flag[i,j]==0 and mask2[i,j]==1 and flag[i+dist2,j]==0 and mask2[i+dist2,j]==1 and flag[i,j-dist1]==0 and mask2[i,j-dist1]==1: ###to check if this point is inside polygon 1 and the point to be masked (pasted upon) is inside the polygon 2. If outside then flag already 1 and if pasted on this then also flag 1.So goes only for points which are inside and not pasted (second if condition)
                                        #x,y=(j,i)
                                        box1=(minw1,minh1,maxw1,maxh1)
                                        box2=(j,i,j-dist1,i+dist2)
                                        region=newIm.crop(box1)
                                        io2.paste(region,box2)
                                        #flag[i+dist2,j-dist1]=1 ###flag changed to 1 so that not pasted again

                                if  (j+dist1)<currentleftwidth_for_zoom and (i-dist2)>currentleftheight_for_zoom:            
                                    if flag[i-dist2,j+dist1]==0 and mask2[i-dist2,j+dist1]==1 and flag[i,j]==0 and mask2[i,j]==1 and flag[i-dist2,j]==0 and mask2[i-dist2,j]==1 and flag[i,j+dist1]==0 and mask2[i,j+dist1]==1: ###to check if this point is inside polygon 1 and the point to be masked (pasted upon) is inside the polygon 2. If outside then flag already 1 and if pasted on this then also flag 1.So goes only for points which are inside and not pasted (second if condition)
                                        #x,y=(j,i)
                                        box1=(minw1,minh1,maxw1,maxh1)
                                        box2=(j,i,j+dist1,i-dist2)
                                        region=newIm.crop(box1)
                                        io2.paste(region,box2)
                                        #flag[i-dist2,j+dist1]=1 ###flag changed to 1 so that not pasted again

                    photoImg2 = ImageTk.PhotoImage(io2)
                    canvas2.itemconfigure(image_to_mask, image=photoImg2)
                    canvas2.config(scrollregion=canvas2.bbox(ALL))                             

                    global flagleft
                    global flagright
                    global answerleft
                    global answerright
                    global flagimageleftname
                    global flagimagerightname
                                
                    flagleft=1
                    if flagimageleftname==0:
                        flagimageleftname=1
                        msg = wx.MessageDialog(None,'Please save the image name with .jpg extension in window to appear')
                        msg.ShowModal()
                        answerleft=asksaveasfilename(parent=root, initialdir="C:/Users/Siddharth Bhatia/Desktop/",title='Save as..')
                    io2.save(answerleft) #final image
                    #image_l = answerleft

                    #io2.save("answerleft.jpg") #final image

                                                                                                       
                    #io2.show() #to show the output image. had to change image show code in PIL library
                                
                    flagescape=0
                                    
                def change_mode():
                    quit_masking()
                    global frame4
                    frame4.OnToggleButton6Togglebutton(event)

                def changeRightImage():## choose images button
        #self.staticText1.SetLabel('Success')
                
                    global answerleft
                    global flagimageleftname
                    flagimageleftname=0
                    global flagRight
                    flagRight=0
                    global flagleft
                    flagleft=0
                    global flagZoom
                    flagZoom=1

                    global image_to_mask
                    global photoImg2
                    global image_l
                    global image_l1
                    global properImage
                    global zoomImage
                    global flagimageremove 
                    flagimageremove=0
        
                    image_l = askopenfilename(parent=root, initialdir="C:/Users/Siddharth Bhatia/Desktop/IIRS/Pics",title='Select Image To Mask From')
                    image_l1= 'imagel1.jpg'
                    answerleft= 'imagel2.jpg'

                    properLeftImage = Image.open(image_l)
                    zoomLeftImage = properLeftImage.copy()
                    zoomLeftImage.save(image_l1)
        
                    left  = cv.LoadImage(image_l1,cv.CV_LOAD_IMAGE_GRAYSCALE)
                    global width1
                    global origleftwidth
                    global origleftheight
                    global currentleftheight
                    global currentleftwidth
                    global currentleftheight_for_zoom
                    global currentleftwidth_for_zoom
                    origleftwidth=left.width
                    origleftheight=left.height
                    currentleftwidth=left.width
                    currentleftheight=left.height
                    currentleftwidth_for_zoom=left.width
                    currentleftheight_for_zoom=left.height

                    if(left.width>968 or left.height>648):
                        flagimageremove=0
                        imgl = Image.open(image_l)
                        imgl = imgl.resize((968,648), Image.ANTIALIAS)
                        imgl.save(image_l1)
                        currentleftwidth=968
                        currentleftheight=648
                        width1=968/100

                    img2 = Image.open(image_l1)
                    photoImg2 = ImageTk.PhotoImage(img2)
                    canvas2.itemconfigure(image_to_mask, image=photoImg2)
                    canvas2.config(scrollregion=canvas2.bbox(ALL))

                def changeLeftImage():## choose images button
                #self.staticText1.SetLabel('Success')
                
                    global answerright
                    global flagimagerightname
                    flagimagerightname=0
                    global flagLeft
                    flagLeft=0
                    global flagZoom
                    global flagleft
                    flagleft=0

                    global image_to_mask_from
                    global photoImg
                    global image_r
                    global image_r1
                    global properImage
                    global zoomImage
                    global flagimageremove 
                    flagimageremove=0
        
                    image_r = askopenfilename(parent=root, initialdir="C:/Users/Siddharth Bhatia/Desktop/IIRS/Pics",title='Select Image To Mask From')
                    image_r1= 'imager1.jpg'
                    answerright= 'imager2.jpg'

                    properRightImage = Image.open(image_r)
                    zoomRightImage = properRightImage.copy()
                    zoomRightImage.save(image_r1)
        
                    right = cv.LoadImage(image_r1,cv.CV_LOAD_IMAGE_GRAYSCALE)
                    global width1
                    global origrightwidth
                    global origrightheight
                    global currentrightheight
                    global currentrightwidth
                    global currentrightheight_for_zoom
                    global currentrightwidth_for_zoom
                    origrightwidth=right.width
                    origrightheight=right.height
                    currentrightwidth=right.width
                    currentrightheight=right.height
                    currentrightwidth_for_zoom=right.width
                    currentrightheight_for_zoom=right.height

                    if(right.width>968 or right.height>648):
                        flagimageremove=0
                        imgr = Image.open(image_r)
                        imgr = imgr.resize((968,648), Image.ANTIALIAS)
                        imgr.save(image_r1)
                        currentrightwidth=968
                        currentrightheight=648
                        width1=968/100
                    img = Image.open(image_r1)
                    photoImg = ImageTk.PhotoImage(img)
                    canvas.itemconfigure(image_to_mask_from, image=photoImg)
                    canvas.config(scrollregion=canvas.bbox(ALL))

                frame = Frame(root, bd=2, relief=SUNKEN)
                leftFrame = Frame(frame,bd=0)
                topFrame = Frame(frame,bd=0)
                rightFrame = Frame(frame,bd=0)
                topFrame.pack(side=TOP,fill=BOTH)
                leftFrame.pack(side=LEFT,fill=BOTH,expand=TRUE)
                rightFrame.pack(side=LEFT,fill=BOTH,expand=TRUE)
                xscroll = Scrollbar(leftFrame, orient=HORIZONTAL)
                xscroll.pack(side=BOTTOM,fill=X)
                yscroll = Scrollbar(leftFrame,orient=VERTICAL)
                yscroll.pack(side=RIGHT, fill=Y)
                canvas = Canvas(leftFrame, bd=0,xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
                canvas.pack(side=LEFT,expand=TRUE,fill=BOTH)
                xscroll.config(command=canvas.xview)
                yscroll.config(command=canvas.yview)

                xscroll2 = Scrollbar(rightFrame, orient=HORIZONTAL)
                xscroll2.pack(side=BOTTOM,fill=X)
                yscroll2 = Scrollbar(rightFrame,orient=VERTICAL)
                yscroll2.pack(side=RIGHT, fill=Y)
                canvas2 = Canvas(rightFrame, bd=0,xscrollcommand=xscroll2.set, yscrollcommand=yscroll2.set)
                xscroll2.config(command=canvas2.xview)
                yscroll2.config(command=canvas2.yview)
                canvas2.pack(side=LEFT,expand=TRUE,fill=BOTH)

                sliderLeft = Scale(topFrame,from_=25,to=200,orient=HORIZONTAL,command=zoom_left,label="Zoom Right Image")
                sliderRight = Scale(topFrame,from_=25,to=200,orient=HORIZONTAL,command=zoom_right,label="Zoom Left Image")
                sliderRight.pack(side=LEFT)
                sliderLeft.pack(side=RIGHT)
                if flagZoom==1:
                    sliderLeft.set(100)
                    sliderRight.set(100)

                bnewPolygon = Button(topFrame,text="Create Rectangle",command=create_polygon)
                bnewPolygon.pack(side=LEFT)
                bselectPolygon = Button(topFrame,text="Select Right Polygon",command=select_polygon)
                bselectPolygon.pack(side=LEFT)
                bmask = Button(topFrame,text="Begin Automatic Masking",command=begin_masking)
                bmask.pack(side=LEFT)
                bsave = Button(topFrame,text="Save",command=save)
                bsave.pack(side=LEFT)
                bquit = Button(topFrame,text="Quit",command=quit_masking)
                bquit.pack(side=LEFT)

                frame.pack(fill=BOTH,expand=TRUE)

                bchangeRightImage = Button(topFrame,text="Change Right Image",command=changeRightImage)
                bchangeRightImage.pack(side=RIGHT)
                bchangeLeftImage = Button(topFrame,text="Change Left Image",command=changeLeftImage)
                bchangeLeftImage.pack(side=RIGHT)
                bchangeMode = Button(topFrame,text="Change Mode",command=change_mode)
                bchangeMode.pack(side=RIGHT)

                img = Image.open(image_r1)
                photoImg = ImageTk.PhotoImage(img)
                image_to_mask_from = canvas.create_image(0,0,image=photoImg,anchor="nw")
                canvas.config(scrollregion=canvas.bbox(ALL))

                img2 = Image.open(image_l1)
                photoImg2 = ImageTk.PhotoImage(img2)
                image_to_mask = canvas2.create_image(0,0,image=photoImg2,anchor="nw")
                canvas2.config(scrollregion=canvas.bbox(ALL))
                    
                while True:
                    if flagdestroycanvas==1:
                        flagdestroycanvas=0
                        canvas.destroy()
                        frame.destroy()

                    if flagleft==1:
                            #image_l1='answerleft.jpg'
                        imgl = Image.open(answerleft)
                        imgl.save(image_l1)
                    
                    if flagnewpolygon==0 or flagnewpolygon==2:
                            #img = ImageTk.PhotoImage(Image.open(image_l1))
                            
                        img = Image.open(image_r1)
                            #img = ImageTk.PhotoImage(Image.open(image_r1))
                            
                    #if flagnewpolygon==1:
                    img2 = Image.open(image_l1)
                            #img = ImageTk.PhotoImage(Image.open(image_l1))
                    
                    #if __name__ == "__main__":

                       #function to be called when mouse is clicked
                    while True:
                        
                        if flagnew==1:
                            flagnew=0
                            root.quit()
                    
                        global flagescape
                        flagescape=1
                                                                          
                        def printcoords(event):
                            #outputting x and y coords to console
                            global flagRectangle
                            event.x = int(canvas.canvasx(event.x)) ## canvas.canvasx reqd for absolute coordinates on the canvas with scrolling..difficult to find!!
                            event.y = int(canvas.canvasy(event.y))
                            
                            #print (event.x,event.y) ## returns integer values only
                            global minw1,minh1,maxw1,maxh1

                            if flagRectangle==1:
                                minw1,minh1 = (event.x,event.y)
                                maxw1,maxh1 = (event.x,event.y)
                            if event.x<minw1:
                                minw1=event.x
                            if event.y<minh1:
                                minh1=event.y
                            if event.x>maxw1:
                                maxw1=event.x
                            if event.y>maxh1:
                                maxh1=event.y
                            
                            global rectangle
                            global a
                            global b
                            global width1
                            if flagRectangle>1:
                                #canvas.create_line(a,b,event.x,event.y,fill="red",width=1,tag="line") ###creates line if more than 1 point
                                rectangle = canvas.create_rectangle(minw1,minh1,maxw1,maxh1,fill="red",width=1,tag="line")
                            a=event.x
                            b=event.y
                            flagRectangle+=1
                            global flagpolygon
                            flagpolygon=0
                            
                        #mouseclick event
                        if flagpolygon==1: #to get new polygon only when starts again
                            canvas.bind("<Button 1>",printcoords)
                            
                        break                    ##code runs after first time when we break. imp line.
                        
                    root.mainloop() #loop will continue but quit inside will make it move outside

                    #if __name__ == "__main__":

                    if flagleft==1:
                            #image_l1='answerleft.jpg'
                        imgl = Image.open(answerleft)
                        imgl.save(image_l1)

                    img = Image.open(image_l1)
                        #img = ImageTk.PhotoImage(Image.open(image_l1))

                    if flagq==0:
                        img2=Image.open(image_l1)
                        photoImg2 = ImageTk.PhotoImage(img2)
                        canvas2.itemconfigure(image_to_mask, image=photoImg2)
                        canvas2.config(scrollregion=canvas2.bbox(ALL))
                    
                    def point_inside_polygon(x,y,poly): ##first takes width, then height
                        """Deciding if a LaserPoint is inside (True, False otherwise) a polygon,
                        where poly is a list of pairs (x,y) containing the coordinates
                        of the polygon's vertices."""
                        n = len(poly)
                        if n <= 2:
                            raise ValueError("poly has only %s vertice(s)" % (n))
                        inside = False
                        p1x,p1y = poly[0]
                        for i in xrange(n+1):
                            p2x,p2y = poly[i % n]
                            if y > min(p1y,p2y):
                                if y <= max(p1y,p2y):
                                    if x <= max(p1x,p2x):
                                        if p1y != p2y:
                                            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                                        if p1x == p2x or x <= xinters:
                                            inside = not inside
                            p1x,p1y = p2x,p2y
                        return inside

                                
                    # read image as RGB and add alpha (transparency)    
                    #global im
                    
                    im = Image.open(image_r1).convert("RGBA")
                     
                    # convert to numpy (for convenience)
                    #global imArray
                    imArray = np.asarray(im)
                
                    maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
                    ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
                    mask = np.array(maskIm)
                    '''for i in range(minh1,maxh1):## i  in height range
                        for j in range(minw1,maxw1):
                            if point_inside_polygon(j,i,polygon): ##first width, then height-imp.
                                mask[i,j]=1
                            else:
                                mask[i,j]=0'''

                    # assemble new image (uint8: 0-255)
                    newImArray = np.empty(imArray.shape,dtype='uint8')
                    
                    # colors (three first columns, RGB)
                    newImArray[:,:,:3] = imArray[:,:,:3]
                    
                    # transparency (4th column)
                    newImArray[:,:,3] = mask*255
                    
                    # back to Image from numpy
                    #global newIm
                    newIm = Image.fromarray(newImArray, "RGBA")
                    newIm.save("polygon.jpg")
                
                    global polygon2
                    
                    polygon2 = [(100,100),(200,200),(150,150),(300,300),(175,275)] #initialize polygon

                    i = 1
                    while True:

                        global flagpop
                        if flagpop==0:
                            polygon2 = [(100,100),(200,200),(150,150),(300,300),(175,275)]
                        
                        def printcoords3(event):
                            #outputting x and y coords to console
                                
                            event.x = int(canvas2.canvasx(event.x))
                            event.y = int(canvas2.canvasy(event.y))
                            #print (event.x,event.y) # returns integer values only
                            #event.x = math.floor(event.x)  returns value as 120.0 which is float cannot use in io.paste. it needs integer

                            global minw2,minh2,maxw2,maxh2
                            global flagRightPolygon

                            if flagRightPolygon==1:
                                maxh1=0
                                maxw1=0
                                minh2=648                   
                                minw2=968
                                maxh2=0
                                maxw2=0
                                minw1=968
                                minh1=648
                        
                            value = (event.x,event.y)
                            if event.x<minw2:
                                minw2=event.x
                            if event.y<minh2:
                                minh2=event.y
                            if event.x>maxw2:
                                maxw2=event.x
                            if event.y>maxh2:
                                maxh2=event.y
                            
                            global polygon2

                            polygon2.append(value)
                            global i
                            global a
                            global b
                            global width1
                            if flagRightPolygon>1:
                                canvas2.create_line(a,b,event.x,event.y,fill="red",width=1,tag="line")
                            a=event.x
                            b=event.y
                            flagRightPolygon+=1
                            global flagpop
                            flagpop=1
                            
                        #mouseclick event
                        
                        
                        if flagq==0:
                            canvas2.bind("<Button 1>",printcoords3) #go to function when clicked
                        
                        flagescape=0
                        #flagdestroycanvas=1  
                        if flagnew==1:
                            polygon = [(100,100),(200,200),(150,150),(300,300),(175,275)]
                            flagescape=1
                            
                            flagnew=0
                            break

                        if flagq==1:
                            break

                                      
                        if flagnew==0:
                            root.mainloop()

                    if flagq==1:
                        break
                event.Skip()



                
            def OnToggleButton5Togglebutton(self, event):
                
                self.Destroy()
                #self.Show(False)
                global rootflag
                global flagq
                if flagq==1:
                    rootflag=1
                else:
                    rootflag=0
                
                
                
                frame2hold.Show(True)
                
            def OnToggleButton6Togglebutton(self, event):
                

                global flagremove
                global origleftheight
                global origleftwidth
                global origrightheight
                global origrightwidth
                global answerleft 
                global answerright
                if flagimageremove==0:
                    imgl = Image.open(answerleft)
                    imgl = imgl.resize((origleftwidth,origleftheight), Image.ANTIALIAS)
                    imgl.save(answerleft)
                    
                    imgr = Image.open(answerright)
                    imgr = imgr.resize((origrightwidth,origrightheight), Image.ANTIALIAS)
                    imgr.save(answerright)
                    
                    #os.remove('imagel1.jpg')
                    #os.remove('imager1.jpg')
                    
                #frame2hold.Destroy()
                global rootflag
                
                
                if rootflag==0:
                    root.destroy()

                self.Destroy()
                frame2hold.Show(True)
                
        global frame4
        frame4=create(None)
        frame4.Show(True)

        

#############################################################################
#Contact siddharthbhatia2003@gmail.com or aloksingh.thakur009@gmail.com for any doubts
