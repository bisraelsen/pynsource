import sys; sys.path.append("../lib")
from architecture_support import *

import wx
import wx.lib.mixins.inspection  # Ctrl-Alt-I 
import thread, time
import random

# GUI Form is auto generated by wxBuilder tool
from ViewWx import GuiFrame
       
# GUI Mediator inherits rather than wraps the viewComponent, in this case, due
# to the way wxBuilder sends us events - expecting us to override handlers

class MyFormMediator(GuiFrame):
    def __init__(self, parent):
        GuiFrame.__init__(self, parent)
        self.app = None
        self.observers = multicast()
        self.random = None        # inject
        
    def Boot(self):
        self._InitHyperlinks()

    def _InitHyperlinks(self):
        def seturl(obj):
            obj.SetURL(self.app.url_server + obj.GetLabel())
            obj.SetToolTip(wx.ToolTip(obj.GetLabel()))
        seturl(self.m_hyperlink1)
        seturl(self.m_hyperlink2)
        seturl(self.m_hyperlink3)
        seturl(self.m_hyperlink4)

    # Util

    def _FindClientData(self, control, clientData):
        """ Listboxes etc. don't support finding via clientData so I wrote this. """
        for i in range(0, self.m_listBox1.GetCount()):
            if self.m_listBox1.GetClientData(i) == clientData:
                return i
        return wx.NOT_FOUND

    def _RepairSelection(self, index):
        if self.m_listBox1.IsEmpty():
            return
        index = max(0, index-1)
        self.m_listBox1.SetSelection(index)
        
    # Threading
    
    def MainThreadMutexGuiEnter(self):
        wx.MutexGuiEnter()
    
    def MainThreadMutexGuiLeave(self):
        wx.MutexGuiLeave()
        
    # Gui Generated Events, override the handler here
    
    def OnClose(self, event):
        self.app.Shutdown()
        event.Skip() # so the standard code for closing is done

    def OnFileNew(self, event):
        self.observers.CMD_FILE_NEW()

    def OnLoadAll(self, event):
        self.observers.CMD_FILE_LOAD_ALL()

    def OnSaveAll(self, event):
        self.observers.CMD_FILE_SAVE_ALL()
        
    def OnAddThing(self, event):
        assert self.random
        info = str(self.random(0,99999)) + " " + self.inputFieldTxt.GetValue()
        self.observers.CMD_ADD_THING(info)

    def OnAddInfoToThing(self, event):
        if self.m_listBox1.IsEmpty():
            return
        index = self.m_listBox1.GetSelection()
        if index == wx.NOT_FOUND:
            return
        thing = self.m_listBox1.GetClientData(index) # see ItemContainer methods http://www.wxpython.org/docs/api/wx.ItemContainer-class.html
        self.observers.CMD_ADD_INFO_TO_THING(thing, "Z")

    def OnDeleteThing(self, event):
        if self.m_listBox1.IsEmpty():
            return
        index = self.m_listBox1.GetSelection()
        thing = self.m_listBox1.GetClientData(index) # see ItemContainer methods http://www.wxpython.org/docs/api/wx.ItemContainer-class.html
        self.observers.CMD_DELETE_THING(thing)

    def OnDumpModel(self, event):
        #self.m_textCtrlDump.Clear()
        self.m_textCtrlDump.AppendText(str(self.app.model) + "\n")

    # Non Gui Incoming Events
    
    def MODEL_CLEARED(self):
        self.m_listBox1.Clear()
        
    def MODEL_CHANGED(self, things):
        self.m_listBox1.Clear()
        for thing in things:
            self.m_listBox1.Append(str(thing), thing)

    def MODEL_THING_ADDED(self, thing, modelsize):
        print "MODEL_THING_ADDED"
        self.m_listBox1.Append(str(thing), thing)

    def MODEL_THING_UPDATE(self, thing):
        index = self._FindClientData(self.m_listBox1, thing)
        if index != wx.NOT_FOUND:
            self.m_listBox1.SetString(index, str(thing))  # Maybe .Set() does both at the same time?
            self.m_listBox1.SetClientData(index, thing)

    def MODEL_THING_DELETED(self, thing):
        print "MODEL_THING_DELETED"
        index = self._FindClientData(self.m_listBox1, thing)
        if index != wx.NOT_FOUND:
            self.m_listBox1.Delete(index)
            self._RepairSelection(index)        

    def MODEL_STATUS_LOAD_OR_SAVE_ALL(self, msg, success):
        self.m_statusBar1.SetStatusText("%(msg)s result: %(success)s" % vars())

class MyWxApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
    def OnInit(self):
        self.Init()  # initialize the inspection tool
        frame = MyFormMediator(parent=None)
        frame.Show()
        self.myframe = frame
        return True
