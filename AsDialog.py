import wx
import AsFunction
import wx.xrc
import wx.grid


class MyDialog1(wx.Dialog):

    def __init__(self, parent, Title, MessageValue):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=Title, pos=wx.DefaultPosition, size=wx.Size(300, 200),
                           style=wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer39 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel14 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer40 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl53 = wx.TextCtrl(self.m_panel14, wx.ID_ANY, MessageValue, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        bSizer40.Add(self.m_textCtrl53, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button19 = wx.Button(self.m_panel14, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer40.Add(self.m_button19, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel14.SetSizer(bSizer40)
        self.m_panel14.Layout()
        bSizer40.Fit(self.m_panel14)
        bSizer39.Add(self.m_panel14, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer39)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button19.Bind(wx.EVT_BUTTON, self.mbutton19)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def mbutton19(self, event):
        self.Destroy()


# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################



###########################################################################
## Class MyDialog2
###########################################################################

class MyDialog2(wx.Dialog):

    def __init__(self, parent, Title, Tips, Value):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=Title, pos=wx.DefaultPosition, size=wx.Size(300, 200),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer81 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel35 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer82 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl55 = wx.TextCtrl(self.m_panel35, wx.ID_ANY, Value, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        bSizer82.Add(self.m_textCtrl55, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText91 = wx.StaticText(self.m_panel35, wx.ID_ANY, Tips, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText91.Wrap(-1)
        bSizer82.Add(self.m_staticText91, 0, wx.RIGHT | wx.LEFT, 5)

        bSizer83 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button32 = wx.Button(self.m_panel35, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer83.Add(self.m_button32, 1, wx.ALL, 5)

        self.m_button33 = wx.Button(self.m_panel35, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer83.Add(self.m_button33, 1, wx.ALL, 5)

        bSizer82.Add(bSizer83, 0, wx.EXPAND, 5)

        self.m_panel35.SetSizer(bSizer82)
        self.m_panel35.Layout()
        bSizer82.Fit(self.m_panel35)
        bSizer81.Add(self.m_panel35, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer81)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button32.Bind(wx.EVT_BUTTON, self.button32)
        self.m_button33.Bind(wx.EVT_BUTTON, self.button33)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def button32(self, event):
        event.Skip()

    def button33(self, event):
        self.Destroy()


class MyDialog3(wx.Dialog):

    def __init__(self, parent, title, label, ctime, mtime, values):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition, size=wx.DefaultSize,
                           style=wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.STAY_ON_TOP)

        self.SetSizeHintsSz(wx.Size(800, 500), wx.DefaultSize)

        bSizer176 = wx.BoxSizer(wx.VERTICAL)

        bSizer177 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText144 = wx.StaticText(self, wx.ID_ANY, u"Label", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText144.Wrap(-1)
        bSizer177.Add(self.m_staticText144, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText145 = wx.StaticText(self, wx.ID_ANY, label, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText145.Wrap(-1)
        bSizer177.Add(self.m_staticText145, 1, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText146 = wx.StaticText(self, wx.ID_ANY, u"CTime", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText146.Wrap(-1)
        bSizer177.Add(self.m_staticText146, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText147 = wx.StaticText(self, wx.ID_ANY, ctime, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText147.Wrap(-1)
        bSizer177.Add(self.m_staticText147, 1, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText148 = wx.StaticText(self, wx.ID_ANY, u"MTime", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText148.Wrap(-1)
        bSizer177.Add(self.m_staticText148, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText149 = wx.StaticText(self, wx.ID_ANY, mtime, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText149.Wrap(-1)
        bSizer177.Add(self.m_staticText149, 1, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        bSizer176.Add(bSizer177, 0, wx.EXPAND, 5)

        bSizer178 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl100 = wx.TextCtrl(self, wx.ID_ANY, values, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_MULTILINE | wx.NO_BORDER)
        bSizer178.Add(self.m_textCtrl100, 1, wx.ALL | wx.EXPAND, 5)

        bSizer176.Add(bSizer178, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer176)
        self.Layout()
        bSizer176.Fit(self)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass



