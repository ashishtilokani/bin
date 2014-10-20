#Boa:Frame:Frame4

import wx
import sqlite3
import os

def create(parent):
    return Frame4(parent)

[wxID_FRAME4, wxID_FRAME4RADIOBUTTON1, wxID_FRAME4RADIOBUTTON2, wxID_FRAME4LISTBOX1,
 wxID_FRAME4TEXTCTRL1, wxID_FRAME4TOGGLEBUTTON1, wxID_FRAME4TOGGLEBUTTON2, 
 wxID_FRAME4TOGGLEBUTTON3 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame4(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME4, parent=prnt,
                          title="Enter columns names for database", size=wx.Size(400, 300),
                          style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.Center()

        self.panel1 = wx.Panel(name='panel1', parent=self, size=wx.Size(400, 300),
              style=wx.TAB_TRAVERSAL)

        vbox=wx.BoxSizer(wx.VERTICAL)
        
        grid1=wx.GridSizer(2,2,15,15)
       
        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME4TEXTCTRL1,
              parent=self.panel1,style=0)

        sizer21 = wx.StaticBoxSizer(wx.StaticBox(self.panel1, -1, u'Variable Type:',size = (100,100)))
        self.rb1 = wx.RadioButton(self.panel1, -1, 'Varchar', style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(self.panel1, -1, 'Real')                 
        sizer21.Add(self.rb1)
        sizer21.Add(self.rb2)

        grid1.AddMany([(wx.StaticText(label=u'Name:', id=-1, parent=self.panel1,
                      style=0),1,wx.EXPAND),(self.textCtrl1,1,wx.EXPAND)])
        grid1.Add(sizer21, 1, wx.CENTER)

        self.panel1.SetSizer(vbox)

        vbox2=wx.BoxSizer(wx.VERTICAL)

        grid2=wx.GridSizer(1,3,15,15)

        self.toggleButton1 = wx.ToggleButton(id=wxID_FRAME4TOGGLEBUTTON1,
              label=u'ADD', parent=self.panel1, style=0)
        self.toggleButton1.Bind(wx.EVT_TOGGLEBUTTON,
              self.OnToggleButton1Togglebutton, id=wxID_FRAME4TOGGLEBUTTON1)

        self.toggleButton2 = wx.ToggleButton(id=wxID_FRAME4TOGGLEBUTTON2,
              label=u'REMOVE', parent=self.panel1, style=0)
        self.toggleButton2.Bind(wx.EVT_TOGGLEBUTTON,
              self.OnToggleButton2Togglebutton, id=wxID_FRAME4TOGGLEBUTTON2)

        vbox2.AddMany([(self.toggleButton1,1,wx.EXPAND|wx.ALL,5),(self.toggleButton2,1,wx.ALL|wx.EXPAND,5)])
        
        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAME4LISTBOX1, parent=self.panel1, style=0)

        self.typeListBox = wx.ListBox(choices=[], parent=self.panel1, style=0)

        grid2.AddMany([(vbox2,1,wx.EXPAND),(self.listBox1,1,wx.EXPAND),(self.typeListBox,1,wx.EXPAND)])
        
        self.toggleButton3 = wx.ToggleButton(id=wxID_FRAME4TOGGLEBUTTON3,
              label=u'SUBMIT', parent=self.panel1, style=0)
        self.toggleButton3.Bind(wx.EVT_TOGGLEBUTTON,
              self.OnToggleButton3Togglebutton, id=wxID_FRAME4TOGGLEBUTTON3)

        vbox.AddMany([(grid1,4,wx.EXPAND|wx.ALL,10),(grid2,6,wx.EXPAND|wx.ALL,10),
                      (self.toggleButton3,3,wx.ALL|wx.EXPAND,10)])
        
    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnToggleButton1Togglebutton(self, event):
        s1=self.textCtrl1.GetValue()
        s2=''
        if s1==s2:
            wx.MessageBox('Please Enter Value and Type')
        else:
            self.listBox1.Append(self.textCtrl1.GetValue())
            if self.rb1.GetValue() == True:
                self.typeListBox.Append("Varchar")
            if self.rb2.GetValue() == True:
                self.typeListBox.Append("Real")

            self.textCtrl1.SetValue('')              

    def OnToggleButton2Togglebutton(self, event):
        if self.listBox1.GetCount()==0:
            wx.MessageBox('No Values to Remove')
        else:    
            value = self.listBox1.GetSelection()
            self.listBox1.Delete(self.listBox1.GetSelection())
            self.typeListBox.Delete(value)

    def OnToggleButton3Togglebutton(self, event):
        if self.listBox1.GetCount()==0:
            wx.MessageBox('Please Enter Values')
        
        else:
            j=0
            k=0
            flag=0
            for j in range(0,self.listBox1.GetCount()):
                for k in range(j+1,self.listBox1.GetCount()):
                    if self.listBox1.GetString(j)==self.listBox1.GetString(k):
                        wx.MessageBox('Same column names. Please enter again')
                        flag=1
                        
            for j in range(0,self.listBox1.GetCount()):
                if self.listBox1.GetString(j).lower()=='name':
                    wx.MessageBox('Do not enter name as an attribute(Column Name)')
                    flag=1
                elif self.listBox1.GetString(j).lower()=='latitude':
                    wx.MessageBox('Do not enter latitude as an attribute(Column Name)')
                    flag=1

                elif self.listBox1.GetString(j).lower()=='longitude':
                    wx.MessageBox('Do not enter longitude as an attribute(Column Name)')
                    flag=1

                elif self.listBox1.GetString(j).lower()=='altitude':
                    wx.MessageBox('Do not enter altitude as an attribute(Column Name)')
                    flag=1
                        
            if flag==0:
                with open(r'C:\3d-Model\bin\curr_proj.txt','r') as fw:
                    pathDir = fw.readline()
                    print pathDir
                    count=self.listBox1.GetCount()
                    projName=os.path.join(pathDir,"column.txt")
                    dataFile=os.path.join(pathDir,"dataType.txt")
                    paths = pathDir.split('\\')
                    index=len(paths)-1
                    
                    fw=open(projName,'w')
                    fd=open(dataFile,'w')

                    databaseFile=os.path.join(pathDir,paths[index] + '.db')
                    conn= sqlite3.connect(databaseFile)
                    cursor = conn.cursor()
                
                for i in range(count):
                    
                    fw.write(self.listBox1.GetString(i)+"\n")
                    print self.listBox1.GetString(i)
                    fd.write(self.typeListBox.GetString(i)+"\n")
                    print self.typeListBox.GetString(i)
                    cursor.execute('''ALTER TABLE information ADD COLUMN '''+self.listBox1.GetString(i)+' '+self.typeListBox.GetString(i))

                fw.close()
                fd.close()
                wx.MessageBox('Values Entered Successfully. Your Database has been created')
                self.Destroy()
                #wx.MessageBox('Same column names Or Connection to Database Server lost. Try again')
