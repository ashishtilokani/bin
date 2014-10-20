#Boa:Dialog:loaddialog

import wx
import wx.lib.filebrowsebutton
import os
import shutil

def create(parent):
    return loaddialog(parent)

[wxID_LOADDIALOG, wxID_LOADDIALOGLOADINGDIR, wxID_DIALOG1DIRBROWSEBUTTON1, wxID_DIALOG1NEWPROJ 
] = [wx.NewId() for _init_ctrls in range(4)]
 
class loaddialog(wx.Dialog):
   
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        
        wx.Dialog.__init__(self, id=wxID_LOADDIALOG, name=u'loaddialog',
              parent=prnt, pos=wx.Point(481, 284), size=wx.Size(473, 215),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Move KML file')
        self.SetClientSize(wx.Size(457, 177))
        

        self.loadingdir = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Browse',
              dialogTitle='Choose a File', fileMask='*.*', id=wxID_LOADDIALOGLOADINGDIR,
              labelText='Select directory of KML Files:', initialValue='', parent=self, 
              pos=wx.Point(30, 24), size=wx.Size(400, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')

        self.loadingdir.SetValue("Select File location")

        global s
        fopen = open(r'C:\3d-Model\bin\curr_proj.txt' , 'r')
        s= str(fopen.read())
        fopen.close()
        s = s+ "\\input\\"

        self.dirBrowseButton1 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_DIALOG1DIRBROWSEBUTTON1,
              labelText=u'Select destination folder:', newDirectory=False,
              parent=self, pos=wx.Point(24, 64), size=wx.Size(400, 48),
              startDirectory= s, style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton1.SetValue(s)

        self.movefile = wx.Button(id=wxID_DIALOG1NEWPROJ,
              label=u'Move Files', name=u'moveKML Files', parent=self,
              pos=wx.Point(184, 120), size=wx.Size(80, 39), style=0)
        self.movefile.Bind(wx.EVT_BUTTON, self.OnMoveFileButton,
              id=wxID_DIALOG1NEWPROJ)

    def __init__(self, parent):
        self._init_ctrls(parent)
        global projname
        projName = self.loadingdir.GetValue()

    def OnMoveFileButton(self, event):
        source=self.loadingdir.GetValue()
        destination=self.dirBrowseButton1.GetValue()
        if os.path.isdir(source):
            if source.endswith(".txt"):
                shutil.copy(source,destination)
            wx.MessageBox('Files copied to given location','Success')
            self.Close()
        else:
            wx.MessageBox('Invalid Directory','Error')

        event.Skip()
        

    def OnProjNameTextEnter(self, event):
        event.Skip()

    @staticmethod
    def GetVal():
        global projName            
        return projName 
    
