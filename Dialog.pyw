#Boa:Dialog:Dialog1

import wx
import wx.lib.filebrowsebutton
import os

path = ""
projName1 = ""
flagCheck = False
def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1DIRBROWSEBUTTON1, wxID_DIALOG1NEWPROJ, 
 wxID_DIALOG1PROJNAME, 
] = [wx.NewId() for _init_ctrls in range(4)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(475, 261), size=wx.Size(506, 214),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'New Project')
        self.SetClientSize(wx.Size(490, 176))
        self.Enable(True)
        self.Show(False)
        self.SetWindowVariant(wx.WINDOW_VARIANT_NORMAL)

        self.dirBrowseButton1 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_DIALOG1DIRBROWSEBUTTON1,
              labelText=u'Select a directory for Project:', newDirectory=False,
              parent=self, pos=wx.Point(24, 64), size=wx.Size(448, 48),
              startDirectory=u'C:\\3d-Model\\projects', style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton1.SetValue(u'C:\\3d-Model\\projects')

        self.projName = wx.TextCtrl(id=wxID_DIALOG1PROJNAME, name=u'projName',
              parent=self, pos=wx.Point(175, 24), size=wx.Size(416, 21), style=0,
              value=u'Untitled')

        wx.StaticText(parent=self,id=-1,label='Project Name:',pos=wx.Point(30,24))

        self.newProj = wx.Button(id=wxID_DIALOG1NEWPROJ,
              label=u'Create Project', name=u'newProj', parent=self,
              pos=wx.Point(184, 120), size=wx.Size(96, 39), style=0)
        self.newProj.Bind(wx.EVT_BUTTON, self.OnNewProjButton,
              id=wxID_DIALOG1NEWPROJ)

    def __init__(self, parent):
        self._init_ctrls(parent)
    
    
    def OnNewProjButton(self, event):
        global path
        path=self.dirBrowseButton1.GetValue()
        if os.path.isdir(path):
            global projName1
            projName1 = self.projName.Value
            global flagCheck
            flagCheck = True
            self.Close()
        else:
            wx.MessageBox('Invalid Directory','Error')
        event.Skip()
    
    @staticmethod
    def GetValues():
        global flagCheck
        if flagCheck:            
            values = [path,projName1]
            flagCheck = False
            return values
        else:
            values = [None,None]
            return values
