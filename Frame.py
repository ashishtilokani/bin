#Boa:Frame:homeFrame

import threading
from PIL.ExifTags import TAGS
import wx
import cStringIO
import shutil
import tkFileDialog
import time
import wx.richtext
import wx.lib.filebrowsebutton
import os
import zipfile
import loadKML
from Tkinter import *
import time
import Dialog
import loadproject
import subprocess
from PIL import Image
import sys
import getopt
import sqlite3
from glob import glob
import RunBundler
import name
import gps
import RunPMVS
import thread
import run_calib
import canny_main
import addPlacemark_new
import database_enter
import foot_manual
import DemoDatabase
import Utm_height
import RunCMVS
import name
import gps

wrk_drr="C:\\3d-Model\\bin"
draw_flag=0
flagbrowse=True
flagshow=True
path = ""
projName2 = ""
proceed_flag=0
calib_flag=0
gauge_value=0

def create(parent):
    return homeFrame(parent)

[wxID_HOMEFRAME, wxID_HOMEFRAMEABORT, wxID_HOMEFRAMEALLTOGETHER, wxID_HOMEFRAMEATTBLISTBOX, 
 wxID_HOMEFRAMEBITMAPBUTTON1, wxID_HOMEFRAMEBITMAPBUTTON2, 
 wxID_HOMEFRAMEBITMAPBUTTON3, wxID_HOMEFRAMEBITMAPBUTTON4, 
 wxID_HOMEFRAMEBITMAPBUTTON5, wxID_HOMEFRAMEBROWSEFILES, wxID_HOMEFRAMEBROWSE_SAVECALIB, wxID_HOMEFRAMELOADCALIB,wxID_HOMEFRAMEBUTTON1, wxID_HOMEFRAMEBUTTON2,wxID_HOMEFRAMEBUTTON3,wxID_HOMEFRAMEBROWSE_CALIB,
 wxID_HOMEFRAMEBUTTON4, wxID_HOMEFRAMEBUTTON5, wxID_HOMEFRAMEBUTTON6,wxID_HOMEFRAMECALIBRATION, 
 wxID_HOMEFRAMECALIB_GAUGE, wxID_HOMEFRAMECANNY, wxID_HOMEFRAMECHANGE, 
 wxID_HOMEFRAMECOMBO_BOX_SENSE, wxID_HOMEFRAMECONTOUR, wxID_HOMEFRAMECROP, 
 wxID_HOMEFRAMEDIRBROWSEBUTTON1, wxID_HOMEFRAMEDIRBROWSEBUTTON2, 
 wxID_HOMEFRAMEDIRBROWSEBUTTON3, wxID_HOMEFRAMEDIRBROWSEBUTTON4, 
 wxID_HOMEFRAMEDRAWBUILD, wxID_HOMEFRAMEFILEBROWSEBUTTON1, 
 wxID_HOMEFRAMEFINISH, wxID_HOMEFRAMEFOOTPRINTEX, wxID_HOMEFRAMELOADKML, wxID_HOMEFRAMEFOOTPROCESS, 
 wxID_HOMEFRAMEFOOTPROCESSGAUGE, wxID_HOMEFRAMEHEIGHT, wxID_HOMEFRAMELISTBOX1, 
 wxID_HOMEFRAMEMASKINGTEXT, wxID_HOMEFRAMEMASK_BUTTON, wxID_HOMEFRAMESENSORTEXT,wxID_TIMETAKEN, 
 wxID_HOMEFRAMENEWBUILDING, wxID_HOMEFRAMENOTEBOOK1, wxID_HOMEFRAMENOT_FOUND, 
 wxID_HOMEFRAMEONEBYONE, wxID_HOMEFRAMEOPENPOINTCLOUD, wxID_HOMEFRAMEPANEL1, 
 wxID_HOMEFRAMEPANEL2, wxID_HOMEFRAMEPANEL3, wxID_HOMEFRAMEPANEL4, 
 wxID_HOMEFRAMEPANEL5, wxID_HOMEFRAMEPANEL6,wxID_HOMEFRAMEPLACEMARK, wxID_HOMEFRAMEPROCEED, wxID_OVERLAPCOMBOBOX,
 wxID_HOMEFRAMERESULT, wxID_HOMEFRAMESAVECALIB,wxID_HOMEFRAMERICHTEXTCTRL1, 
 wxID_HOMEFRAMERICHTEXTCTRL2, wxID_HOMEFRAMESEGMENT, wxID_CALCNUMPHOTOS,
 wxID_HOMEFRAMESEGMENTATION, wxID_HOMEFRAMESENSE, wxID_HOMEFRAMEPANEL7, wxID_PATHLENGTH, wxID_CAMERADIST , wxID_BUTTONFPGOOGLE,
 wxID_HOMEFRAMESHOW, wxID_HOMEFRAMESTATICTEXT1,wxID_HOMEFRAMESTATICTEXT2,wxID_HOMEFRAMESTATICTEXT3,wxID_ADDCAMERATEXT,
 wxID_HOMEFRAMESTATICTEXT4, wxID_HOMEFRAMESTATUSBAR, wxID_HOMEFRAMETEXTCTRL1, wxID_HOMEFRAMETEXTCTRL2, wxID_HOMEFRAMEABOUTABOUTAPP, wxID_HOMEFRAMEFILELOADPROJ,
 wxID_HOMEFRAMEVISUALISEGAUGE, wxID_HOMEFRAMEVISUALISEGE, wxID_HOMEFRAMECAMERATEXT,wxID_HOMEFRAMEADDNEWCAMERA, wxID_EXISTING , wxID_NEW, wxID_SAVEQUERYRESULTS
] = [wx.NewId() for _init_ctrls in range(87)]

[wxID_HOMEFRAMEABOUT, wxID_HOMEFRAMEHELPHELP, 
] = [wx.NewId() for _init_coll_Help_Items in range(2)]

[wxID_HOMEFRAMEFILEEXIT, PROJ, wxID_HOMEFRAMEFILENEW, 
] = [wx.NewId() for _init_coll_File_Items in range(3)]

[wxID_HOMEFRAMETIMER] = [wx.NewId() for _init_utils in range(1)]

current="NIL"

class homeFrame(wx.Frame):

    def _init_coll_MenuBar_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.File, title='&File')
        parent.Append(menu=self.Help, title='&Help')
        parent.Append(menu=self.About, title='&About')

    def _init_coll_File_Items(self, parent):
        # generated method, don't edit

        parent.Append(help="\tPRSD, Indian Institute Of Remote Sensing", id=wxID_HOMEFRAMEFILENEW,
              kind=wx.ITEM_NORMAL, text='&New Project')
        parent.Append(help="\tPRSD, Indian Institute Of Remote Sensing", id=wxID_HOMEFRAMEFILELOADPROJ,
              kind=wx.ITEM_NORMAL, text='&Load Project')
        parent.Append(help="\tPRSD, Indian Institute Of Remote Sensing", id=wxID_HOMEFRAMEFILEEXIT,
              kind=wx.ITEM_NORMAL, text='&Exit')
        self.Bind(wx.EVT_MENU, self.OnFileNewMenu, id=wxID_HOMEFRAMEFILENEW)
        self.Bind(wx.EVT_MENU, self.OnFileExitMenu, id=wxID_HOMEFRAMEFILEEXIT)
        self.Bind(wx.EVT_MENU, self.OnFileLoadprojMenu,
              id=wxID_HOMEFRAMEFILELOADPROJ)

    def _init_coll_Help_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'App Help', id=wxID_HOMEFRAMEHELPHELP,
              kind=wx.ITEM_NORMAL, text='&Help')
        #parent.Append(help=u'About App', id=wxID_HOMEFRAMEHELPABOUT,
              #kind=wx.ITEM_NORMAL, text='&About')
        self.Bind(wx.EVT_MENU, self.OnHelpHelpMenu, id=wxID_HOMEFRAMEHELPHELP)
        #self.Bind(wx.EVT_MENU, self.OnHelpAboutMenu, id=wxID_HOMEFRAMEHELPABOUT)

    def _init_coll_About_Items(self, parent):
        parent.Append(help=u'About App', id=wxID_HOMEFRAMEABOUTABOUTAPP,
              kind=wx.ITEM_NORMAL, text='&About 3-D Street View v.1.1(alpha)')
        self.Bind(wx.EVT_MENU, self.OnAboutAboutAppMenu, id=wxID_HOMEFRAMEABOUTABOUTAPP)

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=True,
              text=u'Camera Calibration')
        parent.AddPage(imageId=-1, page=self.panel7, select=False,
              text=u'Field Planning')
        parent.AddPage(imageId=-1, page=self.panel2, select=False,
              text=u'Point Cloud Generation')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text=u'Segmentation and Masking')
        parent.AddPage(imageId=-1, page=self.panel4, select=False,
              text=u'Height Extraction')
        parent.AddPage(imageId=-1, page=self.panel5, select=False,
              text=u'3D Model Generation')
        parent.AddPage(imageId=-1, page=self.panel6, select=False,
              text=u'Query Processing')

    def _init_coll_StatusBar_Fields(self, parent):
        bmp1 = wx.Image(r'C:\3d-Model\bin\IIRS_LOGO.jpg',wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        #bmp2 = wx.Image('isro.jpg',wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        def scale_bitmap(bitmap, width, height):
            image = wx.ImageFromBitmap(bitmap)
            image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
            result = wx.BitmapFromImage(image)
            return result

        #bmp1 = scale_bitmap(bmp1, 25, 25)
        bmp2 = scale_bitmap(bmp1, 60,25)
        #bm1=wx.StaticBitmap(parent , 0 , bmp1,(0,0))
        bm2=wx.StaticBitmap(parent , 0 , bmp2,(0,0))
        bmp1 = wx.Image(r'C:\3d-Model\bin\isro.jpg',wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        bmp2 = scale_bitmap(bmp1, 60,25)
        bm2 = wx.StaticBitmap(parent , 0 , bmp2,(860,0))

    def _init_utils(self):
        # generated method, don't edit
        self.File = wx.Menu(title=u'')

        self.Help = wx.Menu(title=u'')
        self.About = wx.Menu(title=u'')

        self.MenuBar = wx.MenuBar()
        self.MenuBar.SetClientSize(wx.Size(196353888, 503523728))

        self.timer = wx.Timer(id=wxID_HOMEFRAMETIMER, owner=self)
        self.Bind(wx.EVT_TIMER, self.OnTimerTimer, id=wxID_HOMEFRAMETIMER)

        self._init_coll_File_Items(self.File)
        self._init_coll_Help_Items(self.Help)
        self._init_coll_About_Items(self.About)
        self._init_coll_MenuBar_Menus(self.MenuBar)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_HOMEFRAME, name=u'homeFrame',
              parent=prnt, pos=wx.Point(238, 252), size=wx.Size(930, 640),
              style=wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER^wx.MAXIMIZE_BOX,
              title=u'Welcome to 3-D Street View v1.1(alpha)')
        self._init_utils()
        self.SetClientSize(wx.Size(920, 601))
        self.SetMenuBar(self.MenuBar)
        self.Center(wx.BOTH)

        self.StatusBar = wx.StatusBar(id=wxID_HOMEFRAMESTATUSBAR,
              name=u'StatusBar', parent=self, style=0)
        self.StatusBar.SetToolTipString(u'StatusBar')
        
        self._init_coll_StatusBar_Fields(self.StatusBar)
        self.SetStatusBar(self.StatusBar)
        self.StatusBar.SetStatusText("\tPRSD, Indian Institute Of Remote Sensing")
        
        self.notebook1 = wx.Notebook(id=wxID_HOMEFRAMENOTEBOOK1, parent=self,size=(920, 601))
        self.notebook1.Show(False)
        
        ################################################### panel1 begin here (CAMERA CALIBRATION) ################################################

        # this panel contains all elements of camera calibration screen ##
        self.panel1 = wx.Panel(id=wxID_HOMEFRAMEPANEL1,parent=self.notebook1,style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour('WHITE')

        self.vbox1 = wx.BoxSizer(wx.VERTICAL)

        ## PANEL 11 begins here # this panel contains 'Select Camera and Directory' and 'Add New Camera' ##

        
        self.panel11=wx.Panel(self.panel1,-1)

        self.hbox11=wx.BoxSizer(wx.HORIZONTAL)

        self.sizer11 = wx.StaticBoxSizer(wx.StaticBox(self.panel11, -1, 'Select Camera and Directory'), orient=wx.VERTICAL)

         #selecting camera from drop down ##
        f=open(r"C:\3d-Model\bin\camera_calibration\camera_database.txt",'r')
        file1=f.readlines()
        
        self.combo_box_sense = wx.ComboBox(choices=file1,id=wxID_HOMEFRAMECOMBO_BOX_SENSE,parent=self.panel11,size=(235,25))

        ##The Button for selecting directory of chessboard images##
        self.browse_calib = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',dialogTitle='', id=wxID_HOMEFRAMEBROWSE_CALIB,labelText='', newDirectory=False,parent=self.panel11, pos=wx.Point(268, 137), size=wx.Size(235, 25),startDirectory='.', style=wx.TAB_TRAVERSAL,toolTip='Type directory name or browse to select')

        ##The Button which shows result##
        self.result = wx.Button(id=wxID_HOMEFRAMERESULT,label=u'Calculate Camera Parameters', name=u'result', parent=self.panel11,size=(400,30))
        self.result.Bind(wx.EVT_BUTTON, self.OnResultButton,id=wxID_HOMEFRAMERESULT)

        ##The progress bar(gauge) for calibration ##
        self.calib_gauge = wx.Gauge(id=wxID_HOMEFRAMECALIB_GAUGE, parent=self.panel11,range=100,size=(400,30))
        
        self.grid11 = wx.FlexGridSizer(3, 2,15,0)

        self.grid11.AddMany([(wx.StaticText(self.panel11, -1, 'Camera Name:'),1,wx.ALL|wx.EXPAND,5),(self.combo_box_sense,1,wx.ALL|wx.EXPAND,5),
                             (wx.StaticText(self.panel11, -1, 'Directory for chessboard images:'),1,wx.ALL|wx.EXPAND,5),(self.browse_calib,1,wx.ALL|wx.EXPAND,5),
                              (-1,45),(-1,45)
                             ])

        self.grid13=wx.GridSizer(2,1,15,0)

        self.grid13.AddMany([(self.calib_gauge,wx.ALL|wx.EXPAND,5),(self.result,wx.ALL|wx.EXPAND,5)])
        
        self.sizer11.Add(self.grid11)

        self.sizer11.Add(self.grid13)

        self.hbox11.Add(self.sizer11,1,wx.ALL|wx.EXPAND, 10)

        self.sizer12 = wx.StaticBoxSizer(wx.StaticBox(self.panel11, -1, 'Add New Camera'), orient=wx.VERTICAL)

        self.grid12 = wx.GridSizer(2, 2,15,0)
        
        ## Add new camera text field ##
        self.addCameraText = wx.TextCtrl(id=wxID_ADDCAMERATEXT, parent=self.panel11,size=(200,25))
        self.addCameraText.SetEditable(True)

        ##Sensor width##
        self.sense = wx.TextCtrl(id=wxID_HOMEFRAMESENSE, parent=self.panel11,size=(200,25))
        self.sense.SetEditable(True)
        
        ##the button for adding camera to database ##
        self.addNewCamera = wx.Button(id=wxID_HOMEFRAMEADDNEWCAMERA,label=u'Add New Camera', parent=self.panel11,size=(250,30))
        self.addNewCamera.Bind(wx.EVT_BUTTON, self.OnAddNewCamera,id=wxID_HOMEFRAMEADDNEWCAMERA)

        self.grid12.AddMany([ (wx.StaticText(self.panel11, -1, 'Camera Name:'),1,wx.ALL|wx.EXPAND,5),(self.addCameraText,1,wx.ALL|wx.EXPAND,5),
                              (wx.StaticText(self.panel11, -1, 'Sensor Width:'),1,wx.ALL|wx.EXPAND,5),(self.sense,1,wx.ALL|wx.EXPAND,5)
                              ])

        self.sizer12.AddMany([self.grid12,(-1,100),(self.addNewCamera,1,wx.ALL|wx.EXPAND,5)])
        
        self.hbox11.Add(self.sizer12,1,wx.ALL|wx.EXPAND,10)

        self.panel11.SetSizer(self.hbox11)

        self.vbox1.Add(self.panel11,1,wx.ALL|wx.EXPAND,10)

        self.panel12=wx.Panel(self.panel1,-1)

        self.sizer13 = wx.StaticBoxSizer(wx.StaticBox(self.panel12, -1, 'Camera Parameters'), orient=wx.HORIZONTAL)

        ##The output screen##
        self.richTextCtrl2 = wx.richtext.RichTextCtrl(id=wxID_HOMEFRAMERICHTEXTCTRL2,parent=self.panel12, style=wx.richtext.RE_MULTILINE)
        self.richTextCtrl2.SetEditable(False)
        self.richTextCtrl2.Enable(False)

        ##The Button which saves result##
        self.save_calib = wx.Button(id=wxID_HOMEFRAMESAVECALIB,label=u'Save Camera Parameters', parent=self.panel12,size=wx.Size(200,25))
        self.save_calib.Enable(False)
        self.save_calib.Bind(wx.EVT_BUTTON, self.OnSaveCalib,id=wxID_HOMEFRAMESAVECALIB)

        ##the button which loads result##
        self.load_calib=wx.Button(id=wxID_HOMEFRAMELOADCALIB,label=u'Load Camera Parameters', parent=self.panel12,size=wx.Size(200,25))
        self.load_calib.Bind(wx.EVT_BUTTON, self.OnLoadCalib,id=wxID_HOMEFRAMELOADCALIB)

        self.hbox12=wx.BoxSizer(wx.VERTICAL)

        self.hbox12.AddMany([(self.load_calib,1,wx.ALL|wx.EXPAND,5),(self.save_calib,1,wx.ALL|wx.EXPAND,5)])

        self.sizer13.AddMany([(self.richTextCtrl2,1,wx.ALL|wx.EXPAND,5),(self.hbox12,1,wx.ALL|wx.EXPAND,5)])

        self.panel12.SetSizer(self.sizer13)

        self.vbox1.Add(self.panel12,1,wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND,20)
        
        self.panel1.SetSizer(self.vbox1)

        ################################# PANEL 1 ends here ######################################################################


        ################################## PANEL2 begins here ######################################################################
        
        self.panel2 = wx.Panel(id=wxID_HOMEFRAMEPANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(912, 532),
              style=wx.TAB_TRAVERSAL)

        self.vbox2=wx.BoxSizer(wx.VERTICAL)

        self.panel21=wx.Panel(self.panel2,-1)

        self.hbox12=wx.BoxSizer(wx.HORIZONTAL)

        self.sizer21 = wx.StaticBoxSizer(wx.StaticBox(self.panel21, -1, 'Step 1 : Generate Sparse Point Cloud'),
                                         orient=wx.VERTICAL)
        
        self.dirBrowseButton2 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_HOMEFRAMEDIRBROWSEBUTTON2,
              labelText=u'Select directory for photos', newDirectory=False,
              parent=self.panel21,
              startDirectory='.', style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')

        self.button3 = wx.Button(id=wxID_HOMEFRAMEBUTTON3,
              label=u'Generate Point Cloud', name='button3', parent=self.panel21)
        
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_HOMEFRAMEBUTTON3)

        self.sizer21.AddMany([(self.dirBrowseButton2,1,wx.ALL|wx.EXPAND,5),(-1,100),
                         (self.button3,1,wx.ALL|wx.EXPAND,5)])

        self.sizer22=wx.StaticBoxSizer(wx.StaticBox(self.panel21,-1,'Step 2 : Densify Point Cloud'),orient=wx.wx.VERTICAL)

        self.textCtrl1 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_HOMEFRAMETEXTCTRL1,
              labelText=u'Sparse Point Cloud Path:', newDirectory=False,
              parent=self.panel21,
              startDirectory='.', style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')

        self.button4 = wx.Button(id=wxID_HOMEFRAMEBUTTON4, label=u'Densify Point Cloud',
              name='button4', parent=self.panel21)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_HOMEFRAMEBUTTON4)
        
        self.sizer22.AddMany([(self.textCtrl1,1,wx.ALL|wx.EXPAND,5),(-1,100),(self.button4,1,wx.ALL|wx.EXPAND,5)])

        self.hbox21=wx.BoxSizer(wx.HORIZONTAL)
        
        self.hbox21.AddMany([(self.sizer21,1,wx.ALL|wx.EXPAND, 10),(self.sizer22,1,wx.ALL|wx.EXPAND, 10)])
        
        self.panel21.SetSizer(self.hbox21)

        self.panel22=wx.Panel(self.panel2,-1)

        self.hbox22=wx.BoxSizer(wx.HORIZONTAL)

        self.sizer23=wx.StaticBoxSizer(wx.StaticBox(self.panel22,-1,'Step 3 : Georeference Point Cloud'),orient=wx.VERTICAL)
        
        self.button1 = wx.Button(id=wxID_HOMEFRAMEBUTTON1,
              label=u'Proceed to georef',
              parent=self.panel22,size=wx.Size(385,100) )
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_HOMEFRAMEBUTTON1)

        grid21=wx.GridSizer(2,1)

        grid21.AddMany([(-1,100),(self.button1,1,wx.ALL|wx.EXPAND,5)])
        
        self.sizer23.Add(grid21)

        self.sizer24=wx.StaticBoxSizer(wx.StaticBox(self.panel22,-1,''),orient=wx.VERTICAL)

        self.hbox22.AddMany([(self.sizer23,1,wx.ALL|wx.EXPAND, 10),(self.sizer24,1,wx.ALL|wx.EXPAND, 10)])
        
        self.panel22.SetSizer(self.hbox22)

        self.vbox2.AddMany([(self.panel21,1,wx.ALL|wx.EXPAND,10),(self.panel22,1,wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND,20)])

        self.panel2.SetSizer(self.vbox2)
        ########################################### PANEL2 ends here ###################################################

        self.panel3 = wx.Panel(id=wxID_HOMEFRAMEPANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(912, 532),
              style=wx.TAB_TRAVERSAL)

        self.panel4 = wx.Panel(id=wxID_HOMEFRAMEPANEL4, name='panel4',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(912, 532),
              style=wx.TAB_TRAVERSAL)

        self.panel5 = wx.Panel(id=wxID_HOMEFRAMEPANEL5, name='panel5',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(912, 532),
              style=wx.TAB_TRAVERSAL)

        self.newBuilding = wx.Button(id=wxID_HOMEFRAMENEWBUILDING,
              label=u'Add New Building', name=u'newBuilding',
              parent=self.panel5, pos=wx.Point(32, 32), size=wx.Size(168, 48),
              style=0)
        self.newBuilding.Bind(wx.EVT_BUTTON, self.OnNewBuildingButton,
              id=wxID_HOMEFRAMENEWBUILDING)

        self.FootprintEx = wx.Button(id=wxID_HOMEFRAMEFOOTPRINTEX,
              label=u'Footprint Extraction', name=u'FootprintEx',
              parent=self.panel5, pos=wx.Point(288, 80), size=wx.Size(160, 48),
              style=0)
        self.FootprintEx.Enable(False)
        self.FootprintEx.Bind(wx.EVT_BUTTON, self.OnFootprintExButton,
              id=wxID_HOMEFRAMEFOOTPRINTEX)

        self.LoadKML = wx.Button(id=wxID_HOMEFRAMELOADKML,
              label=u'Load KML Files', name=u'LoadKML',
              parent=self.panel5, pos=wx.Point(480, 80), size=wx.Size(160, 48),
              style=0)
        self.LoadKML.Enable(False)
        self.LoadKML.Bind(wx.EVT_BUTTON, self.OnLoadKML,
              id=wxID_HOMEFRAMELOADKML)

        self.footprocess = wx.Button(id=wxID_HOMEFRAMEFOOTPROCESS,
              label=u'Footprint Processing', name=u'footprocess',
              parent=self.panel5, pos=wx.Point(296, 320), size=wx.Size(160, 48),
              style=0)
        self.footprocess.Enable(False)
        self.footprocess.Bind(wx.EVT_BUTTON, self.OnFootprocessButton,
              id=wxID_HOMEFRAMEFOOTPROCESS)

        self.drawbuild = wx.Button(id=wxID_HOMEFRAMEDRAWBUILD,
              label=u'Construct Building(s)', name=u'drawbuild',
              parent=self.panel5, pos=wx.Point(296, 400), size=wx.Size(160, 48),
              style=0)
        self.drawbuild.Enable(False)
        self.drawbuild.Bind(wx.EVT_BUTTON, self.OnDrawbuildButton,
              id=wxID_HOMEFRAMEDRAWBUILD)

        self.visualiseGE = wx.Button(id=wxID_HOMEFRAMEVISUALISEGE,
              label=u'Visualise on Geo Portal', name=u'visualiseGE',
              parent=self.panel5, pos=wx.Point(296, 480), size=wx.Size(160, 50),
              style=0)
        self.visualiseGE.Enable(True)
        self.visualiseGE.Bind(wx.EVT_BUTTON, self.OnVisualiseGEButton,
              id=wxID_HOMEFRAMEVISUALISEGE)

        self.oneBYone = wx.RadioButton(id=wxID_HOMEFRAMEONEBYONE,
              label=u': Draw Buildings One by One', name=u'oneBYone',
              parent=self.panel5, pos=wx.Point(288, 160), size=wx.Size(224, 13),
              style=0)
        self.oneBYone.SetValue(False)
        self.oneBYone.Enable(False)
        self.oneBYone.Bind(wx.EVT_RADIOBUTTON, self.OnOneBYoneRadiobutton,
              id=wxID_HOMEFRAMEONEBYONE)

        self.allTogether = wx.RadioButton(id=wxID_HOMEFRAMEALLTOGETHER,
              label=u': Draw All Buildings Together', name=u'allTogether',
              parent=self.panel5, pos=wx.Point(288, 192), size=wx.Size(224, 13),
              style=0)
        self.allTogether.SetValue(False)
        self.allTogether.Enable(False)
        self.allTogether.Bind(wx.EVT_RADIOBUTTON, self.OnAllTogetherRadiobutton,
              id=wxID_HOMEFRAMEALLTOGETHER)

        self.footprocessgauge = wx.Gauge(id=wxID_HOMEFRAMEFOOTPROCESSGAUGE,
              name=u'footprocessgauge', parent=self.panel5, pos=wx.Point(480,
              328), range=100, size=wx.Size(256, 28), style=wx.GA_HORIZONTAL)
        self.footprocessgauge.Enable(False)

        self.visualisegauge = wx.Gauge(id=wxID_HOMEFRAMEVISUALISEGAUGE,
              name=u'visualisegauge', parent=self.panel5, pos=wx.Point(480,
              488), range=100, size=wx.Size(264, 28), style=wx.GA_HORIZONTAL)
        self.visualisegauge.Enable(False)

        self.dirBrowseButton1 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_HOMEFRAMEDIRBROWSEBUTTON1,
              labelText='Select a directory:', newDirectory=False,
              parent=self.panel5, pos=wx.Point(285, 232), size=wx.Size(440, 48),
              startDirectory=u'C:\\3d-Model\\projects',
              toolTip='Type directory name or browse to select')
           
        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_HOMEFRAMERICHTEXTCTRL1,
              parent=self.panel5, pos=wx.Point(24, 152), size=wx.Size(184, 384),
              style=wx.richtext.RE_MULTILINE, value=u'Progress Updates....')
        self.richTextCtrl1.SetEditable(False)
        self.richTextCtrl1.SetLabel(u'richText')
        self.richTextCtrl1.SetInsertionPoint(0)

        self.browsefiles = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Browse',
              dialogTitle='Choose a file', fileMask='*.*',
              id=wxID_HOMEFRAMEBROWSEFILES, initialValue='',
              labelText=u'Select Picture', parent=self.panel3, pos=wx.Point(44,
              70), size=wx.Size(296, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')
        self.browsefiles.Enable()
        self.browsefiles.SetName(u'browsefiles')
        self.browsefiles.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.show = wx.Button(id=wxID_HOMEFRAMESHOW, label=u'Show Image',
              name=u'show', parent=self.panel3, pos=wx.Point(59, 130),
              size=wx.Size(270, 40), style=0)
        self.show.Enable(True)
        #self.show.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.show.Bind(wx.EVT_BUTTON, self.OnShowButton, id=wxID_HOMEFRAMESHOW)

        self.proceed = wx.Button(id=wxID_HOMEFRAMEPROCEED,
              label=u'Proceed To Segmentation', name=u'proceed', parent=self.panel3,
              pos=wx.Point(59, 250), size=wx.Size(270, 40), style=0)
        self.proceed.Enable(True)
       # self.proceed.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.proceed.Bind(wx.EVT_BUTTON, self.OnProceedButton  ,
              id=wxID_HOMEFRAMEPROCEED)

        self.abort = wx.Button(id=wxID_HOMEFRAMEABORT, label=u'Abort',
              name=u'abort', parent=self.panel3, pos=wx.Point(568, 488),
              size=wx.Size(128, 31), style=0)
        self.abort.Enable(False)
        self.abort.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.abort.Bind(wx.EVT_BUTTON, self.OnAbortButton,
              id=wxID_HOMEFRAMEABORT)

        self.finish = wx.Button(id=wxID_HOMEFRAMEFINISH, label=u'Finish!',
              name=u'finish', parent=self.panel3, pos=wx.Point(750, 488),
              size=wx.Size(128, 31), style=0)
        self.finish.Enable(False)
        self.finish.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.finish.Bind(wx.EVT_BUTTON, self.OnFinishButton,
              id=wxID_HOMEFRAMEFINISH)

        self.canny = wx.BitmapButton(bitmap=wx.Image("C:\\3d-Model\\bin\\segmentation_files\\progress_images\\Cannyedge_r.png",
              wx.BITMAP_TYPE_ANY).ConvertToBitmap(), id=wxID_HOMEFRAMECANNY,
              name=u'canny', parent=self.panel3, pos=wx.Point(6, 344),
              size=wx.Size(212, 87), style=wx.BU_AUTODRAW)

        self.contour = wx.BitmapButton(bitmap=wx.Image("C:\\3d-Model\\bin\\segmentation_files\\progress_images\\contour_r.png",
              wx.BITMAP_TYPE_ANY).ConvertToBitmap(), id=wxID_HOMEFRAMECONTOUR,
              name=u'contour', parent=self.panel3, pos=wx.Point(231, 344),
              size=wx.Size(212, 87), style=wx.BU_AUTODRAW)

        self.segment = wx.BitmapButton(bitmap=wx.Image("C:\\3d-Model\\bin\\segmentation_files\\progress_images\\segment_r.png",
              wx.BITMAP_TYPE_ANY).ConvertToBitmap(), id=wxID_HOMEFRAMESEGMENT,
              name=u'segment', parent=self.panel3, pos=wx.Point(463, 343),
              size=wx.Size(212, 87), style=wx.BU_AUTODRAW)

        self.crop = wx.BitmapButton(bitmap=wx.Image("C:\\3d-Model\\bin\\segmentation_files\\progress_images\\image_r.png",
              wx.BITMAP_TYPE_ANY).ConvertToBitmap(), id=wxID_HOMEFRAMECROP,
              name=u'crop', parent=self.panel3, pos=wx.Point(685, 344),
              size=wx.Size(212, 87), style=wx.BU_AUTODRAW)

        self.mask_button = wx.Button(id=wxID_HOMEFRAMEMASK_BUTTON,
              label=u'Click this button if you want to mask this photo', name=u'mask_button', parent=self.panel3,
              pos=wx.Point(59, 190), size=wx.Size(270, 40), style=0)
        #self.mask_button.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.mask_button.Enable(True)
        self.mask_button.Bind(wx.EVT_BUTTON, self.OnMask_buttonButton,
              id=wxID_HOMEFRAMEMASK_BUTTON)

        #self.maskingText = wx.StaticText(id=wxID_HOMEFRAMEMASKINGTEXT,label=u'Click the button if you want to mask this photo',
         #     name=u'maskingText', parent=self.panel3, pos=wx.Point(91, 200),
          #    size=wx.Size(224, 13), style=0)

        
        self.fileBrowseButton1 = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Browse',
              dialogTitle='Choose a file', fileMask='*.*',
              id=wxID_HOMEFRAMEFILEBROWSEBUTTON1, initialValue='',
              labelText=u'Select Point Cloud File', parent=self.panel4,
              pos=wx.Point(232, 72), size=wx.Size(432, 48), startDirectory=current,
              style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')
        self.fileBrowseButton1.SetValue(current)

        self.dirBrowseButton4 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_HOMEFRAMEDIRBROWSEBUTTON4,
              labelText=u'Select Directory for Coordinates:',
              newDirectory=False, parent=self.panel4, pos=wx.Point(232, 168),
              size=wx.Size(432, 48), startDirectory=current, style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton4.Show(False)

        self.OpenPointCloud = wx.Button(id=wxID_HOMEFRAMEOPENPOINTCLOUD,
              label=u'Open Point Cloud', name=u'OpenPointCloud',
              parent=self.panel4, pos=wx.Point(392, 248), size=wx.Size(128, 48),
              style=0)
        self.OpenPointCloud.Bind(wx.EVT_BUTTON, self.OnOpenPointCloudButton,
              id=wxID_HOMEFRAMEOPENPOINTCLOUD)

        self.Height = wx.Button(id=wxID_HOMEFRAMEHEIGHT,
              label=u'Extract Height', name=u'Height', parent=self.panel4,
              pos=wx.Point(400, 312), size=wx.Size(120, 40), style=0)
        self.Height.Show(False)
        self.Height.Bind(wx.EVT_BUTTON, self.OnHeightButton,
              id=wxID_HOMEFRAMEHEIGHT)

        self.bitmapButton4 = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_HOMEFRAMEBITMAPBUTTON4, name='bitmapButton4',
              parent=self.panel4, pos=wx.Point(152, 368), size=wx.Size(212, 87),
              style=wx.BU_AUTODRAW)
        self.bitmapButton4.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/pickpoints_r.png',
              wx.BITMAP_TYPE_PNG))

        self.bitmapButton5 = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_HOMEFRAMEBITMAPBUTTON5, name='bitmapButton5',
              parent=self.panel4, pos=wx.Point(544, 368), size=wx.Size(212, 87),
              style=wx.BU_AUTODRAW)
        self.bitmapButton5.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/extractht_r.png',
              wx.BITMAP_TYPE_PNG))

        self.placemark = wx.Button(id=wxID_HOMEFRAMEPLACEMARK,
              label=u'Apply Placemarks + \nEnter the values in Database', name=u'placemark', parent=self.panel5,
              pos=wx.Point(496, 400), size=wx.Size(128, 40), style=0)
        self.placemark.Bind(wx.EVT_BUTTON, self.OnPlacemarkButton,
              id=wxID_HOMEFRAMEPLACEMARK)
        
        self.panel6 = wx.Panel(id=wxID_HOMEFRAMEPANEL6, name='panel6',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(912, 532),
              style=wx.TAB_TRAVERSAL)
        self.panel6.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.textCtrl2 = wx.TextCtrl(id=wxID_HOMEFRAMETEXTCTRL2,
              name='textCtrl2', parent=self.panel6, pos=wx.Point(336, 96),
              size=wx.Size(416, 40), style=0)

        self.staticText1 = wx.StaticText(id=wxID_HOMEFRAMESTATICTEXT1,
              label=u'Enter Query:', name='staticText1', parent=self.panel6,
              pos=wx.Point(168, 104), size=wx.Size(136, 29), style=0)
        self.staticText1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False))

        self.staticText2 = wx.StaticText(id=wxID_HOMEFRAMESTATICTEXT2,
              label=u'Result:', name='staticText2', parent=self.panel6,
              pos=wx.Point(176, 256), size=wx.Size(83, 33), style=0)
        self.staticText2.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False))

       #submit button of query
        self.button2 = wx.Button(id=wxID_HOMEFRAMEBUTTON2, label=u'Submit Query',
              name='button2', parent=self.panel6, pos=wx.Point(400, 176),
              size=wx.Size(120, 32), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_HOMEFRAMEBUTTON2)

        self.saveQueryResults=wx.Button(id=wxID_SAVEQUERYRESULTS, label=u'Save Query Results',
               parent=self.panel6, pos=wx.Point(400, 450),
              size=wx.Size(120, 32), style=0)
        self.saveQueryResults.Bind(wx.EVT_BUTTON, self.onSaveQueryResults,
              id=wxID_SAVEQUERYRESULTS)

        #this is the output box for queries
        self.listBox1 = wx.ListBox(choices=[], id=wxID_HOMEFRAMELISTBOX1,
              name='listBox1', parent=self.panel6, pos=wx.Point(336, 232),
              size=wx.Size(448, 184), style=0)

        #list of attributes are displayed here
        self.attbListBox = wx.ListBox(choices=[], id=wxID_HOMEFRAMEATTBLISTBOX,
              name=u'attbListBox', parent=self.panel6, pos=wx.Point(8, 96),
              size=wx.Size(144, 328), style=0)

        self.button6 = wx.Button(id=wxID_HOMEFRAMEBUTTON6,
              label=u'Load Attributes', name='button6', parent=self.panel6,
              pos=wx.Point(16, 448), size=wx.Size(136, 31), style=0)
        self.button6.Bind(wx.EVT_BUTTON, self.OnButton6Button,
              id=wxID_HOMEFRAMEBUTTON6)

        self.staticText3 = wx.StaticText(id=wxID_HOMEFRAMESTATICTEXT3,
              label=u'The following Listbox shows the names\nof the columns/attributes in the database\nfor query processing.',
              name='staticText3', parent=self.panel6, pos=wx.Point(8, 40),
              size=wx.Size(200, 39), style=0)
        self.staticText3.SetBackgroundColour(wx.Colour(255, 255, 128))

        self.staticText4 = wx.StaticText(id=wxID_HOMEFRAMESTATICTEXT4,
              label=u"eg: name = 'build1_1' and area > 50", name='staticText4',
              parent=self.panel6, pos=wx.Point(576, 144), size=wx.Size(176, 13),
              style=0)
        self.staticText4.SetBackgroundColour(wx.Colour(255, 255, 128))

        self.panel7 = wx.Panel(id=wxID_HOMEFRAMEPANEL7,parent=self.notebook1,style=wx.TAB_TRAVERSAL)
        self.panel7.SetBackgroundColour('WHITE')

        self.vbox7=wx.BoxSizer(wx.VERTICAL)
        self.sizer71=wx.StaticBoxSizer(wx.StaticBox(self.panel7,-1,'Input'),orient=wx.wx.VERTICAL)

        self.buttonfpgoogle=wx.Button( id=wxID_BUTTONFPGOOGLE, label=u'Open Google Earth', parent=self.panel7 )
        self.buttonfpgoogle.Bind( wx.EVT_BUTTON, self.OnFootprintExButton,id=wxID_BUTTONFPGOOGLE )

        self.timeTaken=wx.TextCtrl(id=wxID_TIMETAKEN,  parent=self.panel7,value='1')

        self.calcnumphotos=wx.Button( id=wxID_CALCNUMPHOTOS, label=u'Calculate', parent=self.panel7 )
        self.calcnumphotos.Bind( wx.EVT_BUTTON, self.OnCalcNumPhotos,id=wxID_CALCNUMPHOTOS )
        grid71=wx.GridSizer(3,2,15,0);
        
        self.pathLength = wx.TextCtrl(id=wxID_PATHLENGTH, parent=self.panel7)
        self.cameraDist = wx.TextCtrl(id=wxID_CAMERADIST, parent=self.panel7)

        self.overlapcombobox = wx.ComboBox(choices=['60','70','80','90'],id=wxID_OVERLAPCOMBOBOX,parent=self.panel7)
        
        grid71.AddMany([ (wx.StaticText(id=-1, parent=self.panel7, label=u'Length of path(metres)'),1,wx.ALL|wx.EXPAND,10), (self.pathLength,1,wx.ALL|wx.EXPAND,10),
                        (wx.StaticText(id=-1, parent=self.panel7, label=u'Distance from building(metres)') ,1,wx.ALL|wx.EXPAND ,10)
                             ,(self.cameraDist,1,wx.ALL|wx.EXPAND,10), (wx.StaticText(id=-1, parent=self.panel7, label=u'Percentage overlap of photos') ,1,wx.ALL|wx.EXPAND ,10),
                           (self.overlapcombobox,1,wx.ALL|wx.EXPAND,10),
                         (wx.StaticText(id=-1, parent=self.panel7, label=u'Approximate time for one photo(seconds):'),1,wx.ALL|wx.EXPAND ,10),
                          (self.timeTaken,1,wx.ALL|wx.EXPAND,10) ]);

        grid72=wx.GridSizer(2,2,15,0);

        self.outputnumber=wx.TextCtrl(id=-1, parent=self.panel7 )
        self.outputnumber.SetEditable(False)
        
        self.outputtime=wx.TextCtrl(id=-1, parent=self.panel7 )
        self.outputtime.SetEditable(False)
        
        self.sizer72=wx.StaticBoxSizer(wx.StaticBox(self.panel7,-1,'Output'),orient=wx.wx.VERTICAL)

        grid72.AddMany( [(wx.StaticText(id=-1, parent=self.panel7, label=u'Number of photos required'),1,wx.ALL|wx.EXPAND,10) , (self.outputnumber,1,wx.ALL|wx.EXPAND,10)
                         , (wx.StaticText(id=-1, parent=self.panel7, label=u'Approximate time required'),1,wx.ALL|wx.EXPAND,10), (self.outputtime,1,wx.ALL|wx.EXPAND,10) ])

        self.sizer71.AddMany([ self.buttonfpgoogle , grid71 , self.calcnumphotos]);

        self.sizer72.Add(grid72)

        self.vbox7.AddMany([(self.sizer71,1,wx.ALL|wx.EXPAND,15),(self.sizer72,1,wx.ALL|wx.EXPAND,15)]);
        
        self.panel7.SetSizer(self.vbox7);
        
        self._init_coll_notebook1_Pages(self.notebook1)  

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnCalcNumPhotos(self,event):
        f=open(r'C:\3d-Model\bin\camera_calibration\calib_temp.txt','r')

        for i in range(2):
            a=f.readline()
        try:
            b=a.split(' ')
            ccd=float(b[3])
        except:
            wx.MessageBox("Sensor width could not be obtained. Make sure to calculate or load camera parameters before proceeding further.")

        for i in range(7):
            a=f.readline()

        try:
            b=a.split(' ')
            focalLength=float(b[3])
        except:
            wx.MessageBox("Focal length could not be obtained. Make sure to calculate or load camera parameters before proceeding further.")

        if self.pathLength.GetValue()==0 or self.cameraDist.GetValue()==0:
            wx.MessageBox('Path Length and Distance from building should be positive','Error')
        numerator=  (float(self.pathLength.GetValue())*focalLength)/( ccd*float(self.cameraDist.GetValue()) )
        denominator=(1-float(self.overlapcombobox.GetValue())/100)
        if (numerator-1)/denominator >= 0:
            number=float( (numerator-1)/denominator+1 )
            self.outputnumber.SetValue( str(int(number)) )
            time=int(float(self.timeTaken.GetValue())*float(number))
            hours=int(time/3600)
            minutes=int( (time-hours*3600)/60 )
            seconds=int( time-minutes*60-hours*3600 )
            self.outputtime.SetValue( str(hours)+"h:"+str(minutes)+"m:"+str(seconds)+"s" )
        else:
            self.outputnumber.SetValue(str(1))
        event.Skip()
        
    def unzip(self,path):
        self.visualisegauge.Enable(True)
        os.chdir(path)
        filenames = []
        totalLength=0
        for files in os.listdir("."):
            if files.endswith(".kmz"):
                totalLength +=1
        self.visualisegauge.SetValue(0)       
        self.visualisegauge.SetRange(totalLength)
        count = 0
        for files in os.listdir("."):
            if files.endswith(".kmz"):
                fh = open(files,'rb')
                z = zipfile.ZipFile(fh)
                count += 1
                for name in z.namelist():
                    outpath = path +'\\' + fh.name[:-4]
                    z.extract(name,outpath)
                self.visualisegauge.SetValue(count)
                fh.close()

    def OnHelpHelpMenu(self, event):
        os.chdir(r'C:\3d-Model\docs')
        os.system('COMPLETE_DOCUMENTATION.pdf')

    def OnAboutAboutAppMenu(self, event):
        description = """3-D Street View is an advanced application for generating 3-D Street image which is open source.
        Features include Camera Calibration,Segmentation, masking, Point Cloud generation and Google earth based 3-D Model generation.
        """
        info = wx.AboutDialogInfo()
        info.SetName('3-D Street View')
        info.SetVersion('1.1')
        info.SetDescription(description)
        info.SetCopyright('(C) 2014 IIRS')
        info.AddDeveloper('BITS PILANI')
        wx.AboutBox(info)
        
    def choice(self):
        f=open(r"C:\3d-Model\bin\camera_calibration\camera_database.txt",'r')
        file=f.readlines()
        return file

    def OnFileNewMenu(self, event):
        global current
        global projName2
        fd=Dialog.create(self)
        fd.ShowModal()
        path,projName2 = Dialog.Dialog1.GetValues()
        try:
            os.mkdir(path+"\\"+projName2)
            os.mkdir(path+"\\"+projName2+"\\"+"input")
            os.mkdir(path+"\\"+projName2+"\\"+"output")
            os.chdir(wrk_drr)
            namefile = open(r'C:\\3d-Model\\bin\\curr_proj.txt','w')
            current=str(path)+"\\"+str(projName2)
            namefile.write(current)
            namefile.close()
            DemoDatabase.run()
            print "Database Made"
            print "add column"
            os.system(r"C:\3d-Model\bin\App4.py")
            try:
                self.StatusBar.SetStatusText('\tPROJECT:  '+ (current.split("\\"))[3] , 0)
            except:
                pass
            self.notebook1.Show(True)
        except:
            if current=="NIL":
                self.StatusBar.SetStatusText("\tPRSD, Indian Institute Of Remote Sensing")
            else:
                self.StatusBar.SetStatusText('\tPROJECT:  '+ (current.split("\\"))[3] , 0)
            wx.MessageBox('No project created!','Warning')
        ##############
        fd.Destroy()

    def OnFileExitMenu(self, event):
        self.Close()
        event.Skip()
        
    def OnVisualiseGEButton(self, event):
        global path
        global projName2
        global current
        #path,projName2 = Dialog.Dialog1.GetValues()
        wildcard = "kmz (*.kmz)|*.kmz|"\
           "All files (*.*)|*.*"
##############################################################################################################
        pth = current
        dlg = wx.FileDialog(
            self, message="Choose a file",
            #defaultDir=r"C:\pSApp\output", 
            defaultDir=pth+"\\output",  
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        # Show the dialog and retrieve the user response. If it is the OK response, 
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
        # This returns a Python list of files that were selected.
            paths = dlg.GetPaths()
        
        spaceLength = len(paths)
        
        #path = r'C:\pSApp\output'#####################################################   put project name here
        self.unzip(pth+"\\output")
        
        pathStr = ""
        for i in range(spaceLength):
            paths[i] = (paths[i])[:-4]
            pathStr += " "
            pathStr += paths[i] + '\\doc.kml'
        pathStr += ' '+pth+'\\output\\Placemark.kml'
        root = Tk()
        root.withdraw()
        filename = tkFileDialog.askopenfilename(parent=root,defaultextension=".exe",title="Open Google Earth",
                                                filetypes=[("Application","*.exe")])
        os.startfile(filename + ' ' + pathStr)
        #subprocess.Popen(['python '+filename+' '+ pathStr],shell=TRUE,executable="/bin/bash")

        event.Skip()

    def OnNewBuildingButton(self, event):
        self.allTogether.Enable(True)
        self.oneBYone.Enable(True)
        self.FootprintEx.Enable(True)
        self.LoadKML.Enable(True)
        event.Skip()

    def OnFootprintExButton(self, event):
        root = Tk()
        root.withdraw()
        filename = tkFileDialog.askopenfilename(parent=root,defaultextension=".exe",title="Open Google Earth")
        os.startfile(filename)
        event.Skip()


    def OnLoadKML(self, event):
        global current
        fd=loadKML.create(self)
        fd.ShowModal()
        current=fd.GetVal()
        if os.path.isdir(current):
            print current
        else:
            wx.MessageBox("Invalid Project Name","Error")
              
        fd.Destroy()

    def OnFootprocessButton(self, event):           ###########put error check ie if user puts 1 dir for footex and does other thing
        global wrk_drr
        self.footprocessgauge.Enable(True)       
        str = self.dirBrowseButton1.GetValue()
        flag = True
        if(len(str) != 0):
##            num = len(wrk_drr)#os.getcwd())
##            if((os.getcwd()[num-12:num]=='3d-modelling')!=True):
##                os.chdir(os.getcwd()+'\\3d-modelling')
##            dr = os.getcwd()
            os.chdir("C:\\3d-Model\\bin\\3d-modelling")
            fw = open('temp.txt','w')
            str = str.replace("\\", "\\\\" )
            fw.write(str)
            fw.close()
            flag = True
        else:
            box=wx.MessageDialog(None,'Please specify the folder','Warning',wx.OK)
            answer = box.ShowModal()
            box.Destroy()
            flag = False
        
        if(self.oneBYone.GetValue()==True and flag):
            tot_range=1
            t_old=0.0
            t_new=0.0
            self.footprocessgauge.SetValue(0)       
            self.footprocessgauge.SetRange(tot_range)
            
            #os.chdir(r'C:\pSApp\tempFiles')
            os.chdir(wrk_drr+'\\3d-modelling')
            f=open("temp.txt")
            line_count=0
    
            for line in f:
                line_count=line_count+1
                if(line_count==1):
                    l=line
                    for files in os.listdir(l):
                        if files.endswith(".kml"):
                            f_name=files                    
                    t_old=os.path.getmtime(l+'\\\\'+f_name)
                    break
                
            #os.chdir(r'C:\pSApp\execute')
            os.chdir(wrk_drr+'\\3d-modelling')
            thread.start_new_thread(foot_manual.run,('',))
            
            t_new=os.path.getmtime(l+'\\\\'+f_name)
            if(t_old==t_new): 
                self.footprocessgauge.SetValue(1)       
            
        if(self.allTogether.GetValue()==True and flag):
            tot_range=0
            t_old=0.0
            t_new=0.0
            self.footprocessgauge.SetValue(0)    
                
            #os.chdir(r'C:\pSApp\tempFiles')
            os.chdir(wrk_drr+'\\3d-modelling')
            f=open("temp.txt")
            line_count=0
    
            for line in f:
                line_count=line_count+1
                if(line_count==1):
                    l=line
                    x=os.listdir(l)
                    iterator=len(os.listdir(l))
                    for i in range(iterator):
                        for files in os.listdir(l+'\\\\'+x[i]):                 
                            if files.endswith(".kml"):
                                tot_range+=1
                    break
                    
            self.footprocessgauge.SetRange(tot_range)

            iterator=len(os.listdir(l))
            for i in range(iterator):
                for files in os.listdir(l+'\\\\'+x[i]):                 
                    if files.endswith(".kml"):
                        f_name=files
                       
                        #os.chdir(r'C:\pSApp\tempFiles')
                        os.chdir(wrk_drr+'\\3d-modelling')
                        fw = open('temp.txt','w')
                        fw.write(l+'\\\\'+x[i])
                        fw.close()
                        
                        t_old=os.path.getmtime(l+'\\\\'+x[i]+'\\\\'+f_name)
                        #os.chdir(r'C:\pSApp\execute')
                        os.chdir(wrk_drr+'\\3d-modelling')
                        subprocess.Popen(['python','foot_manual.py'])
                        #os.system('foot_manual.py')
                        t_new=os.path.getmtime(l+'\\\\'+x[i]+'\\\\'+f_name)
                if(t_old<=t_new):
                    self.footprocessgauge.SetValue(i+1)
        event.Skip()

    def OnDrawbuildButton(self, event):
        self.timer.Start(10,False)
        global draw_flag
        draw_flag=1
        str = self.dirBrowseButton1.GetValue()
        flag = True
        if(len(str) != 0):
            os.chdir(wrk_drr+'\\3d-modelling')           
            fw = open('temp.txt','w')
            str = str.replace("\\", "\\\\" )
            fw.write(str)
            fw.close()
            #os.chdir(dr)
            #os.chdir(r"C:\Program Files (x86)\Google\Google SketchUp 8")
            #os.system("SketchUp.exe")
            #subprocess.call("SketchUp.exe")
            os.chdir('.\..\..\\resources\\Google SketchUp 8')
            os.startfile("SketchUp.exe")
            
        else:
            box=wx.MessageDialog(None,'Please specify the folder','Warning',wx.OK)
            answer = box.ShowModal()
            box.Destroy()
        event.Skip()

    def OnOneBYoneRadiobutton(self, event):
        self.drawbuild.Enable(True)
        self.footprocess.Enable(True)
        event.Skip()

    def OnAllTogetherRadiobutton(self, event):
        self.drawbuild.Enable(True)
        self.footprocess.Enable(True)
        event.Skip()

    def OnTimerTimer(self, event):
        global draw_flag
        global proceed_flag
        global calib_flag
        if (draw_flag==1):
            
            os.chdir(wrk_drr+"\\3d-modelling")###############change
            progressFile = open('temp_for_display.txt','r')
            self.richTextCtrl1.SetValue(progressFile.read())
##################################################################################################            
        if(proceed_flag==1):
            with open("C:\\3d-Model\\bin\\segmentation_files\\progress.txt","r") as f:
                #Read whole file into data
                code = f.read()
            if code!="":
                print "\nupdated: ",
                print time.ctime()
                print code
                with open("C:\\3d-Model\\bin\\segmentation_files\\progress.txt","w") as f:
                    f.write("")
            if code=="canny":
                self.canny.SetBitmapLabel(self.canny_image)
            elif code=="contour":
                self.canny.SetBitmapLabel(self.canny_image)
                self.contour.SetBitmapLabel(self.contour_image)
            elif code=="segment":
                self.canny.SetBitmapLabel(self.canny_image)
                self.contour.SetBitmapLabel(self.contour_image)
                self.segment.SetBitmapLabel(self.segment_image)
            elif code=="crop":
                self.crop.SetBitmapLabel(self.crop_image)
                self.finish.Enable(True)
                self.timer.Stop()
                proceed_flag=0
            self.Update()

        if calib_flag==1:
            self.calib_gauge.Enable(True)
            #value stores the number of files
            with open("C:\\3d-Model\\bin\\camera_calibration\\value.txt","r") as f:
                self.calib_gauge.SetValue(int(f.read()))
            #if finish.txt has finish in it, then calibration is finished
            with open("C:\\3d-Model\\bin\\camera_calibration\\finish.txt","r") as f:
                code = f.read()
            if code=="finish":
                print "finish calibration"
                with open('C:\\3d-Model\\bin\\camera_calibration\\finish.txt', 'w') as myFile:
                    myFile.write("")
                with open('C:\\3d-Model\\bin\\camera_calibration\\value.txt', 'w') as myFile:
                    myFile.write("0")
                self.timer.Stop()
                calib_flag=0
                self.save_calib.Enable(True)
                progressFile = open(r'C:\3d-Model\bin\camera_calibration\calib_temp.txt','r')
                self.richTextCtrl2.SetValue(progressFile.read())
            elif code=="failed":
                print "calibration failed"
                with open('C:\\3d-Model\\bin\\camera_calibration\\finish.txt', 'w') as myFile:
                    myFile.write("")
                with open('C:\\3d-Model\\bin\\camera_calibration\\value.txt', 'w') as myFile:
                    myFile.write("0")
                self.timer.Stop()
                calib_flag=0
                wx.MessageBox("No chessboard images found in the specified directory.","Calibration Failed")
            self.result.Enable(True)
        event.Skip()
###os.path.getmtime(r'c:\pSApp\tempFiles\temp_for_display.txt')

###Segmentation Panel
    def _getExif(self, photoHandle):
        exif = {}
        info = photoHandle._getexif()
        if info:
            for attr, value in info.items():
                decodedAttr = TAGS.get(attr, attr)
                if decodedAttr in exifAttrs: exif[decodedAttr] = value
        if 'FocalLength' in exif: exif['FocalLength'] = float(exif['FocalLength'][0])/float(exif['FocalLength'][1])
        return exif
    
    def Image_init(self):
        canny_image = r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\Cannyedge_g.png"
        self.canny_image = wx.Bitmap(canny_image)
        contour_image= r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\contour_g.png"
        self.contour_image = wx.Bitmap(contour_image)
        segment_image = r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\segment_g.png"
        self.segment_image = wx.Bitmap(segment_image)
        crop_image = r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\image_g.png"
        self.crop_image = wx.Bitmap(crop_image)
        canny_image_r = r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\Cannyedge_r.png"
        self.canny_image_r = wx.Bitmap(canny_image_r)
        contour_image_r= r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\contour_r.png"
        self.contour_image_r = wx.Bitmap(contour_image_r)
        segment_image_r = r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\segment_r.png"
        self.segment_image_r = wx.Bitmap(segment_image_r)
        crop_image_r = r"C:\\3d-Model\\bin\\segmentation_files\\progress_images\\image_r.png"
        self.crop_image_r = wx.Bitmap(crop_image_r)
        
        #self.timer = wx.Timer(self)
        #self.Bind(wx.EVT_TIMER, self.update, self.timer)
        

    def OnSegmentationButton(self, event):
        self.browsefiles.Enable(flagbrowse)
        self.show.Enable(flagshow)
        self.Image_init()
        event.Skip()

    def OnShowButton(self, event):
        try:
            image_file = self.browsefiles.GetValue()
            with open('C:\\3d-Model\\bin\\segmentation_files\\path.txt', 'w') as myFile:
                myFile.write(image_file)
            img_org = Image.open(image_file)
            # get the size of the original image
            width_org, height_org = img_org.size
            # set the resizing factor so the aspect ratio can be retained
            # factor > 1.0 increases size
            # factor < 1.0 decreases size
            factor = .10
            width = int(width_org * factor)
            height = int(height_org * factor)
            # best down-sizing filter
            img_anti = img_org.resize((width, height), Image.ANTIALIAS)
            # split image filename into name and extension
            name, ext = os.path.splitext(image_file)
            # create a new file name for saving the result
            new_image_file = "C:\\3d-Model\\bin\\segmentation_files\\pic_resize.jpg"
            img_anti.save(new_image_file)
            #print("resized file saved as %s" % new_image_file)
            bmp = wx.Image(new_image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            width = bmp.GetWidth()
            height = bmp.GetHeight()
            # show the bitmap, you need to set size, image's upper
            # left corner anchors at panel coordinates (5, 5)
            wx.StaticBitmap(self.panel3, -1, bmp, pos=(450,20), size=(width, height))
           # self.change.Enable(True)
        except:
            wx.MessageBox("Please specify a valid image.","Error displaying image")
        event.Skip()

    def OnChangeButton(self, event):
        self.browsefiles.Enable(False)
        self.show.Enable(False)
        self.change.Enable(False)
        self.mask_button.Enable(False)
        self.proceed.Enable(False)
        event.Skip()

    def OnProceedButton(self, event):
        try:
            image_file = self.browsefiles.GetValue()
            with open('C:\\3d-Model\\bin\\segmentation_files\\path.txt', 'w') as myFile:
                myFile.write(image_file)
            img_org = Image.open(image_file)
            # get the size of the original image
            width_org, height_org = img_org.size
            # set the resizing factor so the aspect ratio can be retained
            # factor > 1.0 increases size
            # factor < 1.0 decreases size
            factor = .10
            width = int(width_org * factor)
            height = int(height_org * factor)
            # best down-sizing filter
            img_anti = img_org.resize((width, height), Image.ANTIALIAS)
            # split image filename into name and extension
            name, ext = os.path.splitext(image_file)
            # create a new file name for saving the result
            new_image_file = "C:\\3d-Model\\bin\\segmentation_files\\pic_resize.jpg"
            img_anti.save(new_image_file)
            #print("resized file saved as %s" % new_image_file)
            bmp = wx.Image(new_image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            width = bmp.GetWidth()
            height = bmp.GetHeight()
            # show the bitmap, you need to set size, image's upper
            # left corner anchors at panel coordinates (5, 5)
            wx.StaticBitmap(self.panel3, -1, bmp, pos=(450,20), size=(width, height))
            # self.change.Enable(True)
            global proceed_flag
            proceed_flag=1
            self.Image_init()
            self.timer.Start(1000,False)
            canny_main.run()
            self.abort.Enable(True)
        except:
            wx.MessageBox("Please specify a valid image.","Error displaying image")
        event.Skip()

    def OnAbortButton(self, event):
        self.Close()
        event.Skip()

    def OnFinishButton(self, event):
        self.abort.Enable(False)
        #self.browsefiles.Enable(False)
        #self.show.Enable(False)
        #self.proceed.Enable(False)
        #self.mask_button.Enable(False)
        self.canny.SetBitmapLabel(self.canny_image_r)
        self.Update()

        self.contour.SetBitmapLabel(self.contour_image_r)
        self.Update()

        self.segment.SetBitmapLabel(self.segment_image_r)
        self.Update()

        self.crop.SetBitmapLabel(self.crop_image_r)
        self.Update()
        self.finish.Enable(False)
        self.proceed.Enable(True)
        event.Skip()

    def OnMask_buttonButton(self, event):
        box = wx.MessageDialog(None,"Do you want to do masking ?","Warning",wx.YES_NO)
        answer = box.ShowModal()
        box.Destroy()
        if answer == wx.ID_YES:
            #os.chdir(r"C:\3d-Model\bin\masking")
            with open("file_to_mask.txt",'w') as f:
                f.write(self.browsefiles.GetValue())
            subprocess.Popen(['python',r"C:\3d-Model\bin\App2.py"])
            wx.MessageBox("Please specify the path of the masked image.","Reminder")
            self.browsefiles.SetFocus()
            #pid = subprocess.Popen([sys.executable, "C:\\3d-Model\\bin\\masking\\App2.py"])
        #event.Skip()

    def OnButton1Button(self, event):
        path=r'C:\3d-Model\resources'
        full_path=path+r'\sfm_georef_2.3.exe'
        #os.system(full_path)
        #pid = subprocess.Popen([ sys.executable,full_path ])
        os.startfile(full_path)
                    
    def OnButton3Button(self, event):
        global current
        bundlerPath=""
        photoPath=self.dirBrowseButton2.GetValue()
        if not(os.path.isdir(photoPath)):
            wx.MessageBox('Invalid path. Enter the correct path','Warning')
        else:
            newPhotoPath="C:/3d-Model/bin/point_cloud/temp/"
            p=os.listdir(newPhotoPath)
            for i in p:
                os.remove(newPhotoPath+i)
            f=os.listdir(photoPath)
            for i in f:
                a=i.split('.')
                flag=0
                try:
                    Image.open(os.path.join(photoPath,i))
                except:
                    flag=1
                if (a[len(a)-1]=="jpg" or a[len(a)-1]=="JPG")and flag==0:
                    shutil.copy(os.path.join(photoPath,i),r"C:/3d-Model/bin/point_cloud/temp/")
            newPhotoPath="C:/3d-Model/bin/point_cloud/temp/"
            pid = subprocess.call(["python",r'C:/3d-Model/bin/gps.py',newPhotoPath ,os.path.join(current,"coordinates.txt")])# photo directory along with coordinates is passed to it
            a=[newPhotoPath,os.path.join(current,"coordinates.txt")]
            gps.run(a)
            pid = subprocess.Popen(['python', r"C:/3d-Model/bin/name.py ", newPhotoPath])
            a=[newPhotoPath]
            name.run(a)
            a=[bundlerPath , "--photos=" + newPhotoPath]
            thread.start_new_thread(RunBundler.run,(a,))
            self.textCtrl1.SetValue(os.path.join(current,"PointCloud"))

    def OnButton4Button(self, event):
        bundlerOutputPath=self.textCtrl1.GetValue()
        if not (os.path.isdir(bundlerOutputPath)):
            wx.MessageBox('Invalid path. Enter the correct path','Warning')
        else:
            a=['--bundlerOutputPath='+bundlerOutputPath]
            thread.start_new_thread( RunPMVS.run,(a,) )
            #c = subprocess.Popen(['python',pmvsPath,'--bundlerOutputPath='+bundlerOutputPath],creationflags = subprocess.CREATE_NEW_CONSOLE)
            
    def OnButton6Button(self, event):
        self.attbListBox.Clear()
        global current
        path = current
        os.chdir(path)
        f = open('column.txt','r')
        names = f.readlines()
        f.close()
        
        self.attbListBox.Append('name(string)')
        self.attbListBox.Append('latitude(string)')
        self.attbListBox.Append('longitude(string)')
        self.attbListBox.Append('alititude(float)')
        
        for i in range(len(names)):
            self.attbListBox.Append(names[i][:-1] )
        event.Skip()

    def OnOpenPointCloudButton(self, event):
        global current
        path = current
        str1 = r'\input'
        os.system('start explorer.exe '+path+str1)
        #os.chdir(r'C:\3d-Model\resources\CloudCompare')
        path2 = self.fileBrowseButton1.GetValue()
        os.startfile(path2)
        #os.system(path2)
        self.bitmapButton4.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/pickpoints_g.png',
              wx.BITMAP_TYPE_PNG))
        self.OpenPointCloud.Show(False)
        self.Height.Show(True)
        self.dirBrowseButton4.Show(True)
        self.fileBrowseButton1.Show(False)
        event.Skip()

    def OnHeightButton(self, event):
        paths=self.dirBrowseButton4.GetValue()
        global current
        path = current
        str1 = r'\input'
        a=[paths,path+str1]
        thread.start_new_thread( Utm_height.run , (a,) )
   
        self.bitmapButton5.SetBitmapLabel(wx.Bitmap(u'C:/3d-Model/bin/point_cloud/progress_images/extractht_g.png',
              wx.BITMAP_TYPE_PNG))
##################camera calibration
     # if self.RepresentsInt(self.sense.GetValue())==False :
           # wx.MessageBox('Sensor width should be a floating point number', 'Error')

    def OnResultButton(self, event):
        with open(r'C:\3d-Model\bin\camera_calibration\sensor_value.txt', 'w') as myFile:
            myFile.write(str(self.combo_box_sense.GetValue()))
        global calib_flag
        if calib_flag==0:
            path_calib = self.browse_calib.GetValue()
            print path_calib
            with open('C:\\3d-Model\\bin\\camera_calibration\\path.txt', 'w') as myFile:
                 myFile.write(path_calib)

            f = open("C:\\3d-Model\\bin\\camera_calibration\\path.txt","r")
                #Read whole file into data
            path=f.read()+ "\\*.jpg"

            args, img_mask = getopt.getopt(sys.argv[1:], '', ['save=', 'debug=', 'square_size='])
            args = dict(args)
            try: img_mask = img_mask[0]
            except: img_mask = path
            img_names = glob(img_mask)
            calib_flag=1
            value_calib=len(img_names)
            print value_calib
            self.richTextCtrl2.SetValue("Camera Parameters...")
            self.calib_gauge.SetRange(int(value_calib))
            self.timer.Start(500,False)
            self.save_calib.Enable(False)
            thread.start_new_thread( run_calib.run,('',))
        event.Skip()

    def OnCalibrationButton(self, event):
        self.browse_calib.Enable(True)
        self.result.Enable(True)
        event.Skip()
####################
        
    def OnFileLoadprojMenu(self, event):
        global current
        fd=loadproject.create(self)
        fd.ShowModal()
        current=fd.GetValues()
        if os.path.isdir(current):
            namefile = open(r'C:\\3d-Model\\bin\\curr_proj.txt','w')
            namefile.write(str(current))
            namefile.close()
            self.notebook1.Show()
            self.fileBrowseButton1.SetValue(current)
            self.dirBrowseButton4.SetValue(current)
            try:
                self.StatusBar.SetStatusText('\tPROJECT:  '+ (current.split("\\"))[3] )
            except:
                pass
        else:
            wx.MessageBox("Project Could Not Be Loaded","Error")
            if current=="NIL":
                self.StatusBar.SetStatusText("\tPRSD, Indian Institute Of Remote Sensing")   
            else:
                try:
                    self.StatusBar.SetStatusText('\tPROJECT:  '+ (current.split("\\"))[3] )     
                except:
                    pass
            fd.Destroy()
    
    def OnPlacemarkButton(self, event):
        addPlacemark_new.main()
        print "\n\n\nEntering values in the database.. Please Wait\n"
        database_enter.run()
        print "\n All values have been added please move to the query section"
        event.Skip()

    def OnCheckListBox1Checklistbox(self, event):
        event.Skip()

    def OnCheckListBox1Listbox(self, event):
        event.Skip()

    def OnButton2Button(self, event):
        global current
        path = current
        os.chdir(path)
        f = open('column.txt','r')
        names = f.readlines()
        f.close()
        attributesList=[]
        attributesList.append('name')
        attributesList.append('latitude')
        attributesList.append('longitude')
        attributesList.append('alititude')
        
        for i in range(len(names)):
            attributesList.append(names[i][:-1] )
            
        self.listBox1.Clear() #output screen cleared
        q=self.textCtrl2.GetValue()  #stores input query
        
        os.chdir(path)
        pathData = path.split('\\')
        index=len(pathData)-1
        databaseName = pathData[index] + '.db'
        conn = sqlite3.connect(databaseName)
        dbcursor = conn.cursor()
        
        result=dbcursor.execute("SELECT * FROM information where "+q)
        
        count=0
        
        for row in result:
            count+=1
            
        self.listBox1.Append("Number of results " + " where "  + str(q) + " = " + str(count))
        self.listBox1.Append(" ")

        result=dbcursor.execute("SELECT * FROM information where "+q)
        
        for row in result:
            for i in range(len(row)):
                self.listBox1.Append(str(attributesList[i]) + " : " +str(str(row[i]).strip('u\'')))
            self.listBox1.Append(" ")

    def OnCheckListBox1Checklistbox(self, event):
        event.Skip()

    def OnCheckListBox1Listbox(self, event):
        event.Skip()
        
    def OnSensorButtonButton(self, event):
        sensor_value = self.sense.GetValue()
        print sensor_value
        with open(r'C:\3d-Model\bin\camera_calibration\sensor_value.txt', 'w') as myFile:
            myFile.write(sensor_value)
        event.Skip()

    def RepresentsInt(self,s):
        try: 
            float(s)
        except ValueError:
            return False
        return True

    def OnSaveCalib(self,event):
        root = Tk()
        root.withdraw()
        global current
        filename = tkFileDialog.asksaveasfilename(parent=root,initialfile=(self.combo_box_sense.GetValue().split('-'))[0]+"(Camera Calibration Results)",initialdir=current,defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        print filename
        try:
            shutil.copyfile(r'C:\3d-Model\bin\camera_calibration\calib_temp.txt',filename);
            wx.MessageBox("Result stored in " + filename,"Success!")
        except:
            wx.MessageBox("File save unsuccesful. Please try again.","Error")
        event.Skip()

    def onSaveQueryResults(self,event):
        root = Tk()
        root.withdraw()
        global current
        filename = tkFileDialog.asksaveasfilename(parent=root,initialfile="QueryResults",initialdir=current,defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        print filename
        #try:
        with open(filename,'w') as f:
            strings=self.listBox1.GetStrings()
            for string in strings:
                f.write( str(string) + "\n" )
        #wx.MessageBox("Result stored in " + filename,"Success!")
        #except:
        #   wx.MessageBox("File save unsuccesful. Please try again.","Error")
        event.Skip()

    def OnLoadCalib(self,event):
        root = Tk()
        root.withdraw()
        filename = tkFileDialog.askopenfilename(parent=root,defaultextension=".txt",initialdir=current,filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        print filename
        try:
            with open(filename,'r') as f:
                a=f.read()
                self.richTextCtrl2.SetValue(a)
                with open(r'C:\3d-Model\bin\camera_calibration\calib_temp.txt','w') as f2:
                    f2.write(a)
        except:
            wx.MessageBox("File load unsuccesful. Please try again.","Error")
        event.Skip()
    
    def OnAddNewCamera(self,event):
        if self.RepresentsInt(self.sense.GetValue()) and self.addCameraText.GetValue().strip(' ')!='':
            with open(r'C:\3d-Model\bin\camera_calibration\camera_database.txt','a') as f:
                a=self.addCameraText.GetValue().strip(' ') + "-" + self.sense.GetValue().strip(' ') 
                f.write('\n'+a)
                print a + " added to database"
                self.combo_box_sense.Append(a)
                self.combo_box_sense.SetValue(a)
              #  wx.MessageBox("Camera Name: " + self.addCameraText.GetValue().strip(' ') + "\nSensor Width: " +  self.sense.GetValue().strip(' ') +
               #                  "\nadded to camera database" ,"Camera Added")
        else:
            wx.MessageBox("Enter valid camera name and sensor width","Error")
        event.Skip()

    def SetVal(self, event):
         state1 = str(self.rb1.GetValue())
         state2 = str(self.rb2.GetValue())
         state3 = str(self.rb3.GetValue())
         event.Skip()
