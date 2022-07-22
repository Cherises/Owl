# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Administrator", pos=wx.DefaultPosition,
                          size=wx.Size(1000, 650), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.Size(-1, -1), wx.Size(-1, -1))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menu11 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem(self.m_menu11, wx.ID_ANY, u"Interface", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuItem1.SetBitmap(wx.NullBitmap)
        self.m_menu11.AppendItem(self.m_menuItem1)

        self.m_menuItem12 = wx.MenuItem(self.m_menu11, wx.ID_ANY, u"Sentence", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu11.AppendItem(self.m_menuItem12)

        self.m_menu1.AppendSubMenu(self.m_menu11, u"Refresh")

        self.m_menuItem2 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"CleanAll", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuItem2.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_WARNING, wx.ART_TOOLBAR))
        self.m_menu1.AppendItem(self.m_menuItem2)

        self.m_menuItem3 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"OpenPath", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuItem3.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_TOOLBAR))
        self.m_menu1.AppendItem(self.m_menuItem3)

        self.m_menuItem10 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Show Sentences", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuItem10.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FIND, wx.ART_TOOLBAR))
        self.m_menu1.AppendItem(self.m_menuItem10)

        self.m_menubar1.Append(self.m_menu1, u"Start")

        self.m_menu2 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuItem5.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR))
        self.m_menu2.AppendItem(self.m_menuItem5)

        self.m_menuItem6 = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuItem6.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_DELETE, wx.ART_TOOLBAR))
        self.m_menu2.AppendItem(self.m_menuItem6)

        self.m_menuItem4 = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuItem4.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR))
        self.m_menu2.AppendItem(self.m_menuItem4)

        self.m_menubar1.Append(self.m_menu2, u"Modify")

        self.m_menu3 = wx.Menu()
        self.m_menuItem7 = wx.MenuItem(self.m_menu3, wx.ID_ANY, u"Taskmgr", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu3.AppendItem(self.m_menuItem7)

        self.m_menuItem8 = wx.MenuItem(self.m_menu3, wx.ID_ANY, u"Cmd", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu3.AppendItem(self.m_menuItem8)

        self.m_menuItem9 = wx.MenuItem(self.m_menu3, wx.ID_ANY, u"Explorer", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu3.AppendItem(self.m_menuItem9)

        self.m_menubar1.Append(self.m_menu3, u"Windows")

        self.SetMenuBar(self.m_menubar1)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer1362 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1182 = wx.StaticText(self, wx.ID_ANY, u"你好，世界", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1182.Wrap(-1)
        self.m_staticText1182.SetFont(wx.Font(12, 70, 90, 90, False, "华文中宋"))

        bSizer1362.Add(self.m_staticText1182, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText1193 = wx.StaticText(self, wx.ID_ANY, u"2022-05-23 12:13:12", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1193.Wrap(-1)
        self.m_staticText1193.SetFont(wx.Font(12, 70, 90, 92, False, "宋体"))

        bSizer1362.Add(self.m_staticText1193, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer2.Add(bSizer1362, 1, wx.EXPAND, 5)

        bSizer1791 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1511 = wx.StaticText(self, wx.ID_ANY, u"内存总量", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1511.Wrap(-1)
        bSizer1791.Add(self.m_staticText1511, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText152 = wx.StaticText(self, wx.ID_ANY, u"16GB", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText152.Wrap(-1)
        bSizer1791.Add(self.m_staticText152, 1, wx.ALL, 5)

        self.m_staticText153 = wx.StaticText(self, wx.ID_ANY, u"可用量", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText153.Wrap(-1)
        bSizer1791.Add(self.m_staticText153, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText154 = wx.StaticText(self, wx.ID_ANY, u"12GB", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText154.Wrap(-1)
        bSizer1791.Add(self.m_staticText154, 1, wx.ALL, 5)

        self.m_staticText155 = wx.StaticText(self, wx.ID_ANY, u"使用量", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText155.Wrap(-1)
        bSizer1791.Add(self.m_staticText155, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText156 = wx.StaticText(self, wx.ID_ANY, u"4GB", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText156.Wrap(-1)
        bSizer1791.Add(self.m_staticText156, 1, wx.ALL, 5)

        self.m_staticText157 = wx.StaticText(self, wx.ID_ANY, u"使用百分比", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText157.Wrap(-1)
        bSizer1791.Add(self.m_staticText157, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText158 = wx.StaticText(self, wx.ID_ANY, u"30%", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText158.Wrap(-1)
        bSizer1791.Add(self.m_staticText158, 1, wx.ALL, 5)

        self.m_staticText159 = wx.StaticText(self, wx.ID_ANY, u"交换分区总量", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText159.Wrap(-1)
        bSizer1791.Add(self.m_staticText159, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText160 = wx.StaticText(self, wx.ID_ANY, u"16GB", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText160.Wrap(-1)
        bSizer1791.Add(self.m_staticText160, 1, wx.ALL, 5)

        self.m_staticText161 = wx.StaticText(self, wx.ID_ANY, u"使用量", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText161.Wrap(-1)
        bSizer1791.Add(self.m_staticText161, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText162 = wx.StaticText(self, wx.ID_ANY, u"1GB", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText162.Wrap(-1)
        bSizer1791.Add(self.m_staticText162, 1, wx.ALL, 5)

        self.m_staticText163 = wx.StaticText(self, wx.ID_ANY, u"空闲量", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText163.Wrap(-1)
        bSizer1791.Add(self.m_staticText163, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText164 = wx.StaticText(self, wx.ID_ANY, u"15GB", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText164.Wrap(-1)
        bSizer1791.Add(self.m_staticText164, 1, wx.ALL, 5)

        self.m_staticText165 = wx.StaticText(self, wx.ID_ANY, u"使用百分比", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText165.Wrap(-1)
        bSizer1791.Add(self.m_staticText165, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText166 = wx.StaticText(self, wx.ID_ANY, u"1%", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText166.Wrap(-1)
        bSizer1791.Add(self.m_staticText166, 1, wx.ALL, 5)

        bSizer2.Add(bSizer1791, 1, wx.EXPAND, 5)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel50 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer136 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer137 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel51 = wx.Panel(self.m_panel50, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer138 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer143 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText134 = wx.StaticText(self.m_panel51, wx.ID_ANY, u"Common statistics", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText134.Wrap(-1)
        bSizer143.Add(self.m_staticText134, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer139 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_grid2 = wx.grid.Grid(self.m_panel51, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid2.CreateGrid(26, 3)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(0, 0)

        # Columns
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelSize(30)
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelSize(80)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        bSizer139.Add(self.m_grid2, 1, wx.ALL, 5)

        bSizer143.Add(bSizer139, 1, wx.EXPAND, 5)

        self.m_staticText167 = wx.StaticText(self.m_panel51, wx.ID_ANY, u"Update time", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText167.Wrap(-1)
        bSizer143.Add(self.m_staticText167, 0, wx.ALL, 5)

        bSizer138.Add(bSizer143, 0, wx.EXPAND, 5)

        bSizer1373 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1192 = wx.StaticText(self.m_panel51, wx.ID_ANY, u"Last File", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1192.Wrap(-1)
        bSizer1373.Add(self.m_staticText1192, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_listCtrl4 = wx.ListCtrl(self.m_panel51, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.LC_REPORT | wx.NO_BORDER)
        bSizer1373.Add(self.m_listCtrl4, 1, wx.ALL | wx.EXPAND, 5)

        bSizer138.Add(bSizer1373, 1, wx.EXPAND, 5)

        self.m_panel51.SetSizer(bSizer138)
        self.m_panel51.Layout()
        bSizer138.Fit(self.m_panel51)
        bSizer137.Add(self.m_panel51, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel8 = wx.Panel(self.m_panel50, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText61 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"UpLoad to SQL", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        bSizer13.Add(self.m_staticText61, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer1383 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1372 = wx.BoxSizer(wx.VERTICAL)

        self.m_dirPicker1 = wx.DirPickerCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString, u"Select a folder",
                                             wx.DefaultPosition, wx.Size(-1, -1), wx.DIRP_DEFAULT_STYLE)
        bSizer1372.Add(self.m_dirPicker1, 0, wx.EXPAND | wx.ALL, 5)

        bSizer812 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText86 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Percentage:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText86.Wrap(-1)
        bSizer812.Add(self.m_staticText86, 0, wx.ALL, 5)

        self.m_staticText931 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"0.00000000000000000", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText931.Wrap(-1)
        bSizer812.Add(self.m_staticText931, 1, wx.TOP | wx.BOTTOM, 5)

        self.m_staticText168 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText168.Wrap(-1)
        bSizer812.Add(self.m_staticText168, 1, wx.ALL, 5)

        self.m_staticText82 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Total File:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText82.Wrap(-1)
        bSizer812.Add(self.m_staticText82, 0, wx.ALL, 5)

        self.m_staticText83 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"000000", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText83.Wrap(-1)
        bSizer812.Add(self.m_staticText83, 1, wx.TOP | wx.BOTTOM, 5)

        self.m_staticText174 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Persent File:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText174.Wrap(-1)
        bSizer812.Add(self.m_staticText174, 0, wx.ALL, 5)

        self.m_staticText101 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"000000", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText101.Wrap(-1)
        bSizer812.Add(self.m_staticText101, 1, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        bSizer1372.Add(bSizer812, 0, wx.EXPAND, 5)

        bSizer1383.Add(bSizer1372, 1, wx.EXPAND, 5)

        bSizer1392 = wx.BoxSizer(wx.VERTICAL)

        self.m_button2 = wx.Button(self.m_panel8, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1392.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button221 = wx.Button(self.m_panel8, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1392.Add(self.m_button221, 0, wx.ALL, 5)

        bSizer1383.Add(bSizer1392, 0, 0, 5)

        bSizer13.Add(bSizer1383, 1, wx.EXPAND, 5)

        bSizer811 = wx.BoxSizer(wx.VERTICAL)

        self.m_gauge2 = wx.Gauge(self.m_panel8, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size(400, -1), wx.GA_HORIZONTAL)
        self.m_gauge2.SetValue(0)
        bSizer811.Add(self.m_gauge2, 1, wx.ALL | wx.EXPAND, 5)

        bSizer13.Add(bSizer811, 0, wx.EXPAND, 5)

        self.m_panel8.SetSizer(bSizer13)
        self.m_panel8.Layout()
        bSizer13.Fit(self.m_panel8)
        bSizer137.Add(self.m_panel8, 0, wx.EXPAND | wx.ALL, 5)

        bSizer136.Add(bSizer137, 1, wx.EXPAND, 5)

        self.m_panel33 = wx.Panel(self.m_panel50, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer81 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText63 = wx.StaticText(self.m_panel33, wx.ID_ANY, u"File Infromation", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText63.Wrap(-1)
        bSizer81.Add(self.m_staticText63, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText97 = wx.StaticText(self.m_panel33, wx.ID_ANY, u"File Name", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText97.Wrap(-1)
        bSizer81.Add(self.m_staticText97, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl47 = wx.TextCtrl(self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0 | wx.NO_BORDER)
        bSizer81.Add(self.m_textCtrl47, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText95 = wx.StaticText(self.m_panel33, wx.ID_ANY, u"File Size", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText95.Wrap(-1)
        bSizer81.Add(self.m_staticText95, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl48 = wx.TextCtrl(self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0 | wx.NO_BORDER)
        bSizer81.Add(self.m_textCtrl48, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText96 = wx.StaticText(self.m_panel33, wx.ID_ANY, u"File Type", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText96.Wrap(-1)
        bSizer81.Add(self.m_staticText96, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl49 = wx.TextCtrl(self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0 | wx.NO_BORDER)
        bSizer81.Add(self.m_textCtrl49, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText90 = wx.StaticText(self.m_panel33, wx.ID_ANY, u"Creation time", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText90.Wrap(-1)
        bSizer81.Add(self.m_staticText90, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl50 = wx.TextCtrl(self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0 | wx.NO_BORDER)
        bSizer81.Add(self.m_textCtrl50, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText921 = wx.StaticText(self.m_panel33, wx.ID_ANY, u"Last visit time", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText921.Wrap(-1)
        bSizer81.Add(self.m_staticText921, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl51 = wx.TextCtrl(self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0 | wx.NO_BORDER)
        bSizer81.Add(self.m_textCtrl51, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText93 = wx.StaticText(self.m_panel33, wx.ID_ANY, u"Modified time", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText93.Wrap(-1)
        bSizer81.Add(self.m_staticText93, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl52 = wx.TextCtrl(self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0 | wx.NO_BORDER)
        bSizer81.Add(self.m_textCtrl52, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText98 = wx.StaticText(self.m_panel33, wx.ID_ANY, u"File Path", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText98.Wrap(-1)
        bSizer81.Add(self.m_staticText98, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl46 = wx.TextCtrl(self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        bSizer81.Add(self.m_textCtrl46, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        bSizer85 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText23 = wx.StaticText(self.m_panel33, wx.ID_ANY, u"List Limit", wx.DefaultPosition,
                                            wx.Size(-1, -1), 0)
        self.m_staticText23.Wrap(-1)
        bSizer85.Add(self.m_staticText23, 0,
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        m_comboBox11Choices = [u"1", u"2", u"4", u"8", u"16", u"32", u"64", u"128"]
        self.m_comboBox11 = wx.ComboBox(self.m_panel33, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox11Choices, 0)
        self.m_comboBox11.SetSelection(4)
        bSizer85.Add(self.m_comboBox11, 1, wx.ALL, 5)

        bSizer81.Add(bSizer85, 0, wx.EXPAND, 5)

        self.m_panel33.SetSizer(bSizer81)
        self.m_panel33.Layout()
        bSizer81.Fit(self.m_panel33)
        bSizer136.Add(self.m_panel33, 0, wx.EXPAND | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        self.m_panel50.SetSizer(bSizer136)
        self.m_panel50.Layout()
        bSizer136.Fit(self.m_panel50)
        self.m_notebook1.AddPage(self.m_panel50, u"Statistics", False)
        self.m_panel49 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer1331 = wx.BoxSizer(wx.VERTICAL)

        bSizer134 = wx.BoxSizer(wx.VERTICAL)

        self.m_listCtrl2 = wx.ListCtrl(self.m_panel49, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.LC_REPORT | wx.NO_BORDER)
        bSizer134.Add(self.m_listCtrl2, 1, wx.EXPAND | wx.ALL, 5)

        self.m_listCtrl6 = wx.ListCtrl(self.m_panel49, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.LC_REPORT | wx.NO_BORDER)
        bSizer134.Add(self.m_listCtrl6, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        bSizer1331.Add(bSizer134, 1, wx.EXPAND, 5)

        bSizer173 = wx.BoxSizer(wx.VERTICAL)

        bSizer1331.Add(bSizer173, 1, wx.EXPAND, 5)

        bSizer135 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText137 = wx.StaticText(self.m_panel49, wx.ID_ANY, u"Super Search", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText137.Wrap(-1)
        self.m_staticText137.SetFont(wx.Font(20, 70, 90, 92, False, wx.EmptyString))

        bSizer135.Add(self.m_staticText137, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl75 = wx.TextCtrl(self.m_panel49, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                        0)
        self.m_textCtrl75.SetFont(wx.Font(14, 70, 90, 92, False, "宋体"))

        bSizer135.Add(self.m_textCtrl75, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1331.Add(bSizer135, 0, wx.EXPAND, 5)

        bSizer147 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText138 = wx.StaticText(self.m_panel49, wx.ID_ANY, u"List Limit", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText138.Wrap(-1)
        bSizer147.Add(self.m_staticText138, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        m_comboBox1Choices = [u"1", u"2", u"4", u"8", u"16", u"32", u"64", u"128"]
        self.m_comboBox1 = wx.ComboBox(self.m_panel49, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize,
                                       m_comboBox1Choices, 0)
        self.m_comboBox1.SetSelection(3)
        bSizer147.Add(self.m_comboBox1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText150 = wx.StaticText(self.m_panel49, wx.ID_ANY, u"File Path", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText150.Wrap(-1)
        bSizer147.Add(self.m_staticText150, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl77 = wx.TextCtrl(self.m_panel49, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0 | wx.NO_BORDER)
        bSizer147.Add(self.m_textCtrl77, 1, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        bSizer1331.Add(bSizer147, 0, wx.EXPAND, 5)

        self.m_panel49.SetSizer(bSizer1331)
        self.m_panel49.Layout()
        bSizer1331.Fit(self.m_panel49)
        self.m_notebook1.AddPage(self.m_panel49, u"Search", False)
        self.m_panel43 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer180 = wx.BoxSizer(wx.VERTICAL)

        self.m_listbook4 = wx.Listbook(self.m_panel43, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT)
        self.m_panel442 = wx.Panel(self.m_listbook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer181 = wx.BoxSizer(wx.VERTICAL)

        bSizer186 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer182 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1681 = wx.StaticText(self.m_panel442, wx.ID_ANY, u"收件人：", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.m_staticText1681.Wrap(-1)
        bSizer182.Add(self.m_staticText1681, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText169 = wx.StaticText(self.m_panel442, wx.ID_ANY, u"主    题：", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText169.Wrap(-1)
        bSizer182.Add(self.m_staticText169, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        bSizer186.Add(bSizer182, 0, wx.EXPAND, 5)

        bSizer183 = wx.BoxSizer(wx.VERTICAL)

        m_comboBox3Choices = [u"zhaozhinet@163.com", u"cherisenet@163.com", u"zhaozhinet@gmail.com"]
        self.m_comboBox3 = wx.ComboBox(self.m_panel442, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       m_comboBox3Choices, 0)
        bSizer183.Add(self.m_comboBox3, 0, wx.EXPAND, 5)

        self.m_textCtrl101 = wx.TextCtrl(self.m_panel442, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         0)
        bSizer183.Add(self.m_textCtrl101, 0, wx.EXPAND | wx.TOP, 5)

        bSizer186.Add(bSizer183, 1, wx.EXPAND, 5)

        bSizer181.Add(bSizer186, 0, wx.EXPAND, 5)

        bSizer184 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText170 = wx.StaticText(self.m_panel442, wx.ID_ANY, u"内容：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText170.Wrap(-1)
        bSizer184.Add(self.m_staticText170, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl102 = wx.TextCtrl(self.m_panel442, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_MULTILINE)
        bSizer184.Add(self.m_textCtrl102, 1, wx.ALL | wx.EXPAND, 5)

        bSizer181.Add(bSizer184, 1, wx.EXPAND, 5)

        bSizer185 = wx.BoxSizer(wx.VERTICAL)

        self.m_button28 = wx.Button(self.m_panel442, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer185.Add(self.m_button28, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer181.Add(bSizer185, 0, wx.EXPAND, 5)

        self.m_panel442.SetSizer(bSizer181)
        self.m_panel442.Layout()
        bSizer181.Fit(self.m_panel442)
        self.m_listbook4.AddPage(self.m_panel442, u"SendMail", False)
        self.m_panel451 = wx.Panel(self.m_listbook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer187 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl1021 = wx.TextCtrl(self.m_panel451, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.DefaultSize, wx.TE_MULTILINE | wx.NO_BORDER)
        bSizer187.Add(self.m_textCtrl1021, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        bSizer1633 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1382 = wx.StaticText(self.m_panel451, wx.ID_ANY, u"Client", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.m_staticText1382.Wrap(-1)
        bSizer1633.Add(self.m_staticText1382, 0, wx.ALL, 5)

        self.m_textCtrl811 = wx.TextCtrl(self.m_panel451, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         0 | wx.NO_BORDER)
        self.m_textCtrl811.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        bSizer1633.Add(self.m_textCtrl811, 1, wx.RIGHT | wx.LEFT, 5)

        bSizer187.Add(bSizer1633, 0, wx.EXPAND, 5)

        bSizer1621 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1361 = wx.StaticText(self.m_panel451, wx.ID_ANY, u"IP", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1361.Wrap(-1)
        bSizer1621.Add(self.m_staticText1361, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.m_textCtrl821 = wx.TextCtrl(self.m_panel451, wx.ID_ANY, u"127.0.0.1", wx.DefaultPosition, wx.DefaultSize,
                                         0)
        bSizer1621.Add(self.m_textCtrl821, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText1372 = wx.StaticText(self.m_panel451, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.m_staticText1372.Wrap(-1)
        bSizer1621.Add(self.m_staticText1372, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.m_textCtrl831 = wx.TextCtrl(self.m_panel451, wx.ID_ANY, u"9574", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1621.Add(self.m_textCtrl831, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button29 = wx.Button(self.m_panel451, wx.ID_ANY, u"Link", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1621.Add(self.m_button29, 0, wx.ALL, 5)

        self.m_button311 = wx.Button(self.m_panel451, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1621.Add(self.m_button311, 0, wx.ALL, 5)

        bSizer187.Add(bSizer1621, 0, 0, 5)

        self.m_panel451.SetSizer(bSizer187)
        self.m_panel451.Layout()
        bSizer187.Fit(self.m_panel451)
        self.m_listbook4.AddPage(self.m_panel451, u"Server", True)
        self.m_panel461 = wx.Panel(self.m_listbook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer188 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer189 = wx.BoxSizer(wx.VERTICAL)

        self.m_listCtrl7 = wx.ListCtrl(self.m_panel461, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer189.Add(self.m_listCtrl7, 1, wx.ALL | wx.EXPAND, 5)

        bSizer191 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button31 = wx.Button(self.m_panel461, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer191.Add(self.m_button31, 0, wx.ALL, 5)

        self.m_button331 = wx.Button(self.m_panel461, wx.ID_ANY, u"加入", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer191.Add(self.m_button331, 0, wx.ALL, 5)

        self.m_button341 = wx.Button(self.m_panel461, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer191.Add(self.m_button341, 0, wx.ALL, 5)

        bSizer189.Add(bSizer191, 0, wx.EXPAND, 5)

        bSizer188.Add(bSizer189, 1, wx.EXPAND, 5)

        bSizer190 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl106 = wx.TextCtrl(self.m_panel461, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         0)
        bSizer190.Add(self.m_textCtrl106, 0, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl103 = wx.TextCtrl(self.m_panel461, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_MULTILINE)
        self.m_textCtrl103.SetFont(wx.Font(18, 70, 90, 90, False, "宋体"))

        bSizer190.Add(self.m_textCtrl103, 1, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText171 = wx.StaticText(self.m_panel461, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText171.Wrap(-1)
        bSizer190.Add(self.m_staticText171, 0, wx.ALL, 5)

        self.m_textCtrl105 = wx.TextCtrl(self.m_panel461, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer190.Add(self.m_textCtrl105, 0, wx.ALL, 5)

        self.m_checkBox7 = wx.CheckBox(self.m_panel461, wx.ID_ANY, u"Specil", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer190.Add(self.m_checkBox7, 0, wx.ALL, 5)

        self.m_textCtrl104 = wx.TextCtrl(self.m_panel461, wx.ID_ANY, u"!@#$%^&*", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer190.Add(self.m_textCtrl104, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button301 = wx.Button(self.m_panel461, wx.ID_ANY, u"生成密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button301.SetDefault()
        bSizer190.Add(self.m_button301, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button32 = wx.Button(self.m_panel461, wx.ID_ANY, u"随机生成5个", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer190.Add(self.m_button32, 0, wx.ALL, 5)

        bSizer188.Add(bSizer190, 1, wx.EXPAND, 5)

        self.m_panel461.SetSizer(bSizer188)
        self.m_panel461.Layout()
        bSizer188.Fit(self.m_panel461)
        self.m_listbook4.AddPage(self.m_panel461, u"Password", False)
        self.m_panel471 = wx.Panel(self.m_listbook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer131 = wx.BoxSizer(wx.VERTICAL)

        self.m_listCtrl3 = wx.ListCtrl(self.m_panel471, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer131.Add(self.m_listCtrl3, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1321 = wx.BoxSizer(wx.VERTICAL)

        bSizer1332 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1341 = wx.BoxSizer(wx.VERTICAL)

        bSizer1632 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1141 = wx.StaticText(self.m_panel471, wx.ID_ANY, u"计划", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1141.Wrap(-1)
        bSizer1632.Add(self.m_staticText1141, 0, wx.TOP | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl711 = wx.TextCtrl(self.m_panel471, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         0)
        bSizer1632.Add(self.m_textCtrl711, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1341.Add(bSizer1632, 1, wx.EXPAND, 5)

        bSizer1641 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1181 = wx.StaticText(self.m_panel471, wx.ID_ANY, u"状态", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1181.Wrap(-1)
        bSizer1641.Add(self.m_staticText1181, 0, wx.TOP | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice3Choices = [u"进行中", u"暂停中", u"完已成", u"已完成", u"已取消"]
        self.m_choice3 = wx.Choice(self.m_panel471, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0)
        self.m_choice3.SetSelection(0)
        bSizer1641.Add(self.m_choice3, 0, wx.ALL, 5)

        bSizer1341.Add(bSizer1641, 1, wx.EXPAND, 5)

        bSizer166 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1161 = wx.StaticText(self.m_panel471, wx.ID_ANY, u"开始日期", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.m_staticText1161.Wrap(-1)
        bSizer166.Add(self.m_staticText1161, 0, wx.TOP | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl731 = wx.TextCtrl(self.m_panel471, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         0)
        self.m_textCtrl731.Enable(False)

        bSizer166.Add(self.m_textCtrl731, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1341.Add(bSizer166, 1, wx.EXPAND, 5)

        bSizer165 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1171 = wx.StaticText(self.m_panel471, wx.ID_ANY, u"限定日期", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.m_staticText1171.Wrap(-1)
        bSizer165.Add(self.m_staticText1171, 0, wx.TOP | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl741 = wx.TextCtrl(self.m_panel471, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         0)
        bSizer165.Add(self.m_textCtrl741, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1341.Add(bSizer165, 1, wx.EXPAND, 5)

        self.m_staticText121 = wx.StaticText(self.m_panel471, wx.ID_ANY, u"上次更新", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText121.Wrap(-1)
        bSizer1341.Add(self.m_staticText121, 0, wx.ALL, 5)

        bSizer1332.Add(bSizer1341, 1, 0, 5)

        bSizer1351 = wx.BoxSizer(wx.VERTICAL)

        bSizer1381 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1151 = wx.StaticText(self.m_panel471, wx.ID_ANY, u"内容", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1151.Wrap(-1)
        bSizer1381.Add(self.m_staticText1151, 0,
                       wx.BOTTOM | wx.LEFT | wx.TOP | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl721 = wx.TextCtrl(self.m_panel471, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_MULTILINE | wx.NO_BORDER)
        bSizer1381.Add(self.m_textCtrl721, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1351.Add(bSizer1381, 1, wx.EXPAND, 5)

        bSizer1332.Add(bSizer1351, 1, wx.EXPAND, 5)

        bSizer1361 = wx.BoxSizer(wx.VERTICAL)

        bSizer1391 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1191 = wx.StaticText(self.m_panel471, wx.ID_ANY, u"备注", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1191.Wrap(-1)
        bSizer1391.Add(self.m_staticText1191, 0,
                       wx.BOTTOM | wx.LEFT | wx.TOP | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl76 = wx.TextCtrl(self.m_panel471, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        bSizer1391.Add(self.m_textCtrl76, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1361.Add(bSizer1391, 1, wx.EXPAND, 5)

        bSizer1332.Add(bSizer1361, 1, wx.EXPAND, 5)

        bSizer1371 = wx.BoxSizer(wx.VERTICAL)

        bSizer1332.Add(bSizer1371, 1, 0, 5)

        bSizer1321.Add(bSizer1332, 0, wx.EXPAND, 5)

        bSizer131.Add(bSizer1321, 0, wx.EXPAND, 5)

        self.m_panel471.SetSizer(bSizer131)
        self.m_panel471.Layout()
        bSizer131.Fit(self.m_panel471)
        self.m_listbook4.AddPage(self.m_panel471, u"Plan", False)
        self.m_panel491 = wx.Panel(self.m_listbook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer77 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel331 = wx.Panel(self.m_panel491, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        bSizer78 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl521 = wx.TextCtrl(self.m_panel331, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_CENTRE | wx.NO_BORDER)
        self.m_textCtrl521.SetFont(wx.Font(16, 70, 90, 92, False, "华文楷体"))

        bSizer78.Add(self.m_textCtrl521, 0, wx.EXPAND | wx.RIGHT, 5)

        self.m_textCtrl531 = wx.TextCtrl(self.m_panel331, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl531.SetFont(wx.Font(15, 70, 90, 90, False, "华文楷体"))

        bSizer78.Add(self.m_textCtrl531, 1, wx.EXPAND | wx.RIGHT, 5)

        self.m_panel331.SetSizer(bSizer78)
        self.m_panel331.Layout()
        bSizer78.Fit(self.m_panel331)
        bSizer77.Add(self.m_panel331, 1, wx.EXPAND, 5)

        self.m_panel341 = wx.Panel(self.m_panel491, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        bSizer79 = wx.BoxSizer(wx.VERTICAL)

        m_listBox5Choices = []
        self.m_listBox5 = wx.ListBox(self.m_panel341, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 220),
                                     m_listBox5Choices, 0)
        bSizer79.Add(self.m_listBox5, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText901 = wx.StaticText(self.m_panel341, wx.ID_ANY, u"000000000000", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText901.Wrap(-1)
        bSizer79.Add(self.m_staticText901, 0, wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText109 = wx.StaticText(self.m_panel341, wx.ID_ANY, u"Add Note", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText109.Wrap(-1)
        bSizer79.Add(self.m_staticText109, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl541 = wx.TextCtrl(self.m_panel341, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(-1, 50), wx.TE_MULTILINE)
        bSizer79.Add(self.m_textCtrl541, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText87 = wx.StaticText(self.m_panel341, wx.ID_ANY, u"Font Size", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText87.Wrap(-1)
        bSizer79.Add(self.m_staticText87, 0, wx.RIGHT | wx.LEFT, 5)

        bSizer114 = wx.BoxSizer(wx.VERTICAL)

        bSizer82 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button33 = wx.Button(self.m_panel341, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size(25, -1), 0)
        self.m_button33.SetFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))

        bSizer82.Add(self.m_button33, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_slider1 = wx.Slider(self.m_panel341, wx.ID_ANY, 15, 1, 50, wx.DefaultPosition, wx.DefaultSize,
                                   wx.SL_HORIZONTAL)
        bSizer82.Add(self.m_slider1, 1, wx.EXPAND | wx.TOP, 5)

        self.m_button34 = wx.Button(self.m_panel341, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size(25, -1), 0)
        self.m_button34.SetFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))

        bSizer82.Add(self.m_button34, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer114.Add(bSizer82, 0, wx.EXPAND, 5)

        self.m_staticText88 = wx.StaticText(self.m_panel341, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText88.Wrap(-1)
        bSizer114.Add(self.m_staticText88, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT | wx.LEFT, 5)

        bSizer79.Add(bSizer114, 0, wx.EXPAND, 5)

        m_choice11Choices = [u"Garamond", u"Century", u"Bookman Old Style", u"Javanese Text", u"Palatino Linotype",
                             u"Segoe Print", u"等线", u"方正舒体", u"仿宋", u"黑体", u"华文楷体", u"华文隶书", u"华文宋体", u"华文新魏", u"华文行楷",
                             u"微软雅黑", u"幼圆", u"宋体"]
        self.m_choice11 = wx.Choice(self.m_panel341, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11Choices,
                                    0)
        self.m_choice11.SetSelection(10)
        bSizer79.Add(self.m_choice11, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText89 = wx.StaticText(self.m_panel341, wx.ID_ANY, u"time", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText89.Wrap(-1)
        bSizer79.Add(self.m_staticText89, 0, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_panel341.SetSizer(bSizer79)
        self.m_panel341.Layout()
        bSizer79.Fit(self.m_panel341)
        bSizer77.Add(self.m_panel341, 0, wx.EXPAND | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        self.m_panel491.SetSizer(bSizer77)
        self.m_panel491.Layout()
        bSizer77.Fit(self.m_panel491)
        self.m_listbook4.AddPage(self.m_panel491, u"Note", False)
        self.m_panel501 = wx.Panel(self.m_listbook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer167 = wx.BoxSizer(wx.VERTICAL)

        bSizer168 = wx.BoxSizer(wx.VERTICAL)

        bSizer170 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1371 = wx.StaticText(self.m_panel501, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.m_staticText1371.Wrap(-1)
        bSizer170.Add(self.m_staticText1371, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl96 = wx.TextCtrl(self.m_panel501, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0 | wx.NO_BORDER)
        bSizer170.Add(self.m_textCtrl96, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText1381 = wx.StaticText(self.m_panel501, wx.ID_ANY, u"Label", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.m_staticText1381.Wrap(-1)
        bSizer170.Add(self.m_staticText1381, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl97 = wx.TextCtrl(self.m_panel501, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0 | wx.NO_BORDER)
        bSizer170.Add(self.m_textCtrl97, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        m_choice6Choices = [u"技术知识", u"百科知识", u"搜集整理"]
        self.m_choice6 = wx.Choice(self.m_panel501, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice6Choices, 0)
        self.m_choice6.SetSelection(0)
        bSizer170.Add(self.m_choice6, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText139 = wx.StaticText(self.m_panel501, wx.ID_ANY, u"CTime", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText139.Wrap(-1)
        bSizer170.Add(self.m_staticText139, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText142 = wx.StaticText(self.m_panel501, wx.ID_ANY, u"000000000000", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText142.Wrap(-1)
        bSizer170.Add(self.m_staticText142, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText140 = wx.StaticText(self.m_panel501, wx.ID_ANY, u"MTime", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText140.Wrap(-1)
        bSizer170.Add(self.m_staticText140, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText143 = wx.StaticText(self.m_panel501, wx.ID_ANY, u"2022-05-23 12:13:12", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText143.Wrap(-1)
        bSizer170.Add(self.m_staticText143, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer168.Add(bSizer170, 0, wx.EXPAND, 5)

        bSizer171 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl100 = wx.TextCtrl(self.m_panel501, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl100.SetFont(wx.Font(16, 70, 90, 90, False, "华文楷体"))

        bSizer171.Add(self.m_textCtrl100, 1, wx.EXPAND, 5)

        bSizer168.Add(bSizer171, 1, wx.EXPAND, 5)

        bSizer167.Add(bSizer168, 1, wx.EXPAND, 5)

        bSizer169 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer172 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText141 = wx.StaticText(self.m_panel501, wx.ID_ANY, u"Encyclopedia Database Search",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText141.Wrap(-1)
        self.m_staticText141.SetFont(wx.Font(15, 72, 90, 90, False, "Century"))

        bSizer172.Add(self.m_staticText141, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer175 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button27 = wx.Button(self.m_panel501, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer175.Add(self.m_button27, 0, wx.ALL, 5)

        self.m_button26 = wx.Button(self.m_panel501, wx.ID_ANY, u"ClearAll", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer175.Add(self.m_button26, 0, wx.ALL, 5)

        bSizer172.Add(bSizer175, 1, wx.EXPAND, 5)

        bSizer179 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button24 = wx.Button(self.m_panel501, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer179.Add(self.m_button24, 0, wx.ALL, 5)

        self.m_button25 = wx.Button(self.m_panel501, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer179.Add(self.m_button25, 0, wx.ALL, 5)

        self.m_button231 = wx.Button(self.m_panel501, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button231.SetDefault()
        bSizer179.Add(self.m_button231, 0, wx.ALL, 5)

        bSizer172.Add(bSizer179, 1, wx.EXPAND, 5)

        bSizer169.Add(bSizer172, 1, wx.EXPAND, 5)

        bSizer167.Add(bSizer169, 0, wx.EXPAND, 5)

        self.m_panel501.SetSizer(bSizer167)
        self.m_panel501.Layout()
        bSizer167.Fit(self.m_panel501)
        self.m_listbook4.AddPage(self.m_panel501, u"Library", False)
        self.m_panel511 = wx.Panel(self.m_listbook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_listbook4.AddPage(self.m_panel511, u"a page", False)
        self.m_panel52 = wx.Panel(self.m_listbook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_listbook4.AddPage(self.m_panel52, u"a page", False)

        bSizer180.Add(self.m_listbook4, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel43.SetSizer(bSizer180)
        self.m_panel43.Layout()
        bSizer180.Fit(self.m_panel43)
        self.m_notebook1.AddPage(self.m_panel43, u"Function", False)
        self.m_panel441 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer112 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_listbook3 = wx.Listbook(self.m_panel441, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT)
        self.m_panel45 = wx.Panel(self.m_listbook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer119 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1131 = wx.BoxSizer(wx.VERTICAL)

        bSizer117 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl681 = wx.TextCtrl(self.m_panel45, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         0 | wx.NO_BORDER)
        self.m_textCtrl681.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        bSizer117.Add(self.m_textCtrl681, 1, wx.EXPAND, 5)

        bSizer1131.Add(bSizer117, 0, wx.EXPAND, 5)

        self.m_textCtrl671 = wx.TextCtrl(self.m_panel45, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl671.SetFont(wx.Font(15, 72, 90, 90, False, "Century"))

        bSizer1131.Add(self.m_textCtrl671, 1, wx.EXPAND, 5)

        bSizer118 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText111 = wx.StaticText(self.m_panel45, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText111.Wrap(-1)
        bSizer118.Add(self.m_staticText111, 0, wx.RIGHT, 5)

        self.m_slider2 = wx.Slider(self.m_panel45, wx.ID_ANY, 15, 1, 50, wx.DefaultPosition, wx.DefaultSize,
                                   wx.SL_HORIZONTAL)
        bSizer118.Add(self.m_slider2, 1, wx.LEFT, 5)

        self.m_staticText118 = wx.StaticText(self.m_panel45, wx.ID_ANY, u"T:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText118.Wrap(-1)
        bSizer118.Add(self.m_staticText118, 0, wx.LEFT, 5)

        self.m_staticText119 = wx.StaticText(self.m_panel45, wx.ID_ANY, u"0000", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText119.Wrap(-1)
        bSizer118.Add(self.m_staticText119, 0, wx.RIGHT | wx.LEFT, 5)

        self.m_staticText112 = wx.StaticText(self.m_panel45, wx.ID_ANY, u"2022-4-27 20:18:20", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText112.Wrap(-1)
        bSizer118.Add(self.m_staticText112, 0, wx.RIGHT | wx.LEFT, 5)

        self.m_staticText113 = wx.StaticText(self.m_panel45, wx.ID_ANY, u"20220427223610", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText113.Wrap(-1)
        bSizer118.Add(self.m_staticText113, 0, wx.RIGHT | wx.LEFT, 5)

        bSizer1131.Add(bSizer118, 0, wx.EXPAND, 5)

        bSizer115 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_checkBox4 = wx.CheckBox(self.m_panel45, wx.ID_ANY, u"ReadType", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox4.SetValue(True)
        bSizer115.Add(self.m_checkBox4, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText1091 = wx.StaticText(self.m_panel45, wx.ID_ANY, u"ReadNotice:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1091.Wrap(-1)
        bSizer115.Add(self.m_staticText1091, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl691 = wx.TextCtrl(self.m_panel45, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         0)
        bSizer115.Add(self.m_textCtrl691, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        self.m_staticText110 = wx.StaticText(self.m_panel45, wx.ID_ANY, u"Label:", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText110.Wrap(-1)
        bSizer115.Add(self.m_staticText110, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl72 = wx.TextCtrl(self.m_panel45, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0)
        bSizer115.Add(self.m_textCtrl72, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        bSizer1131.Add(bSizer115, 0, wx.EXPAND, 5)

        bSizer119.Add(bSizer1131, 1, wx.EXPAND, 5)

        bSizer1142 = wx.BoxSizer(wx.VERTICAL)

        m_listBox6Choices = []
        self.m_listBox6 = wx.ListBox(self.m_panel45, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, -1), m_listBox6Choices,
                                     0)
        bSizer1142.Add(self.m_listBox6, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        m_choice1Choices = [u"Garamond", u"Century", u"Bookman Old Style", u"Javanese Text", u"Palatino Linotype",
                            u"Segoe Print", u"等线", u"方正舒体", u"仿宋", u"黑体", u"华文楷体", u"华文隶书", u"华文宋体", u"华文新魏", u"华文行楷",
                            u"微软雅黑", u"幼圆"]
        self.m_choice1 = wx.Choice(self.m_panel45, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(1)
        bSizer1142.Add(self.m_choice1, 0, wx.ALL | wx.EXPAND, 5)

        bSizer119.Add(bSizer1142, 0, wx.EXPAND, 5)

        self.m_panel45.SetSizer(bSizer119)
        self.m_panel45.Layout()
        bSizer119.Fit(self.m_panel45)
        self.m_listbook3.AddPage(self.m_panel45, u"iRead", True)
        self.m_panel46 = wx.Panel(self.m_listbook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer116 = wx.BoxSizer(wx.VERTICAL)

        bSizer123 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1291 = wx.BoxSizer(wx.VERTICAL)

        bSizer121 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1071 = wx.StaticText(self.m_panel46, wx.ID_ANY, u"Notification", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1071.Wrap(-1)
        bSizer121.Add(self.m_staticText1071, 0, wx.ALL, 5)

        self.m_textCtrl70 = wx.TextCtrl(self.m_panel46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE)
        bSizer121.Add(self.m_textCtrl70, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1291.Add(bSizer121, 1, wx.EXPAND, 5)

        bSizer122 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1081 = wx.StaticText(self.m_panel46, wx.ID_ANY, u"Server Notice", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1081.Wrap(-1)
        bSizer122.Add(self.m_staticText1081, 0, wx.ALL, 5)

        self.m_textCtrl71 = wx.TextCtrl(self.m_panel46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE)
        bSizer122.Add(self.m_textCtrl71, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1291.Add(bSizer122, 1, wx.EXPAND, 5)

        bSizer123.Add(bSizer1291, 1, wx.EXPAND, 5)

        bSizer1302 = wx.BoxSizer(wx.VERTICAL)

        bSizer1261 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1111 = wx.StaticText(self.m_panel46, wx.ID_ANY, u"Version  Update Notice", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1111.Wrap(-1)
        bSizer1261.Add(self.m_staticText1111, 0, wx.ALL, 5)

        self.m_textCtrl682 = wx.TextCtrl(self.m_panel46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_MULTILINE)
        bSizer1261.Add(self.m_textCtrl682, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1302.Add(bSizer1261, 1, wx.EXPAND, 5)

        bSizer1281 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1131 = wx.StaticText(self.m_panel46, wx.ID_ANY, u"About", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.m_staticText1131.Wrap(-1)
        bSizer1281.Add(self.m_staticText1131, 0, wx.ALL, 5)

        self.m_textCtrl701 = wx.TextCtrl(self.m_panel46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_MULTILINE)
        bSizer1281.Add(self.m_textCtrl701, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1302.Add(bSizer1281, 1, wx.EXPAND, 5)

        bSizer123.Add(bSizer1302, 1, wx.EXPAND, 5)

        bSizer116.Add(bSizer123, 1, wx.EXPAND, 5)

        bSizer133 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_checkBox5 = wx.CheckBox(self.m_panel46, wx.ID_ANY, u"Notification Start Display", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer133.Add(self.m_checkBox5, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_checkBox6 = wx.CheckBox(self.m_panel46, wx.ID_ANY, u"Server Statue", wx.DefaultPosition, wx.DefaultSize,
                                       0)
        bSizer133.Add(self.m_checkBox6, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1271 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1121 = wx.StaticText(self.m_panel46, wx.ID_ANY, u"Last Version:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1121.Wrap(-1)
        bSizer1271.Add(self.m_staticText1121, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl692 = wx.TextCtrl(self.m_panel46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         0)
        bSizer1271.Add(self.m_textCtrl692, 0, wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer133.Add(bSizer1271, 0, wx.EXPAND, 5)

        bSizer116.Add(bSizer133, 0, wx.EXPAND, 5)

        self.m_panel46.SetSizer(bSizer116)
        self.m_panel46.Layout()
        bSizer116.Fit(self.m_panel46)
        self.m_listbook3.AddPage(self.m_panel46, u"iConfig", False)
        self.m_panel47 = wx.Panel(self.m_listbook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer124 = wx.BoxSizer(wx.VERTICAL)

        bSizer125 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl73 = wx.TextCtrl(self.m_panel47, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE)
        bSizer125.Add(self.m_textCtrl73, 1, wx.EXPAND, 5)

        bSizer124.Add(bSizer125, 1, wx.EXPAND, 5)

        bSizer126 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer127 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText114 = wx.StaticText(self.m_panel47, wx.ID_ANY, u"All IP List", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText114.Wrap(-1)
        bSizer127.Add(self.m_staticText114, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        m_listBox7Choices = []
        self.m_listBox7 = wx.ListBox(self.m_panel47, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox7Choices,
                                     0)
        bSizer127.Add(self.m_listBox7, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button48 = wx.Button(self.m_panel47, wx.ID_ANY, u"Delete IP", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer127.Add(self.m_button48, 0, wx.ALL | wx.EXPAND, 5)

        bSizer126.Add(bSizer127, 1, wx.EXPAND, 5)

        bSizer130 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText117 = wx.StaticText(self.m_panel47, wx.ID_ANY, u"Comment List", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText117.Wrap(-1)
        bSizer130.Add(self.m_staticText117, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        m_listBox9Choices = []
        self.m_listBox9 = wx.ListBox(self.m_panel47, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox9Choices,
                                     0)
        bSizer130.Add(self.m_listBox9, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button44 = wx.Button(self.m_panel47, wx.ID_ANY, u"Delect Comment", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer130.Add(self.m_button44, 0, wx.ALL | wx.EXPAND, 5)

        bSizer126.Add(bSizer130, 1, wx.EXPAND, 5)

        bSizer128 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText115 = wx.StaticText(self.m_panel47, wx.ID_ANY, u"Deny List", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText115.Wrap(-1)
        bSizer128.Add(self.m_staticText115, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        m_listBox8Choices = []
        self.m_listBox8 = wx.ListBox(self.m_panel47, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox8Choices,
                                     0)
        bSizer128.Add(self.m_listBox8, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button43 = wx.Button(self.m_panel47, wx.ID_ANY, u"Remove to Deny List", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizer128.Add(self.m_button43, 0, wx.ALL | wx.EXPAND, 5)

        bSizer126.Add(bSizer128, 1, wx.EXPAND, 5)

        bSizer129 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText116 = wx.StaticText(self.m_panel47, wx.ID_ANY, u"Deny Notice", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText116.Wrap(-1)
        bSizer129.Add(self.m_staticText116, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl74 = wx.TextCtrl(self.m_panel47, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0)
        bSizer129.Add(self.m_textCtrl74, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button411 = wx.Button(self.m_panel47, wx.ID_ANY, u"Join to Deny List", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        bSizer129.Add(self.m_button411, 0, wx.ALL | wx.EXPAND, 5)

        bSizer126.Add(bSizer129, 1, wx.EXPAND, 5)

        bSizer124.Add(bSizer126, 1, wx.EXPAND, 5)

        self.m_panel47.SetSizer(bSizer124)
        self.m_panel47.Layout()
        bSizer124.Fit(self.m_panel47)
        self.m_listbook3.AddPage(self.m_panel47, u"Comment", False)
        self.m_panel48 = wx.Panel(self.m_listbook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer1301 = wx.BoxSizer(wx.VERTICAL)

        self.m_listCtrl1 = wx.ListCtrl(self.m_panel48, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer1301.Add(self.m_listCtrl1, 1, wx.EXPAND, 5)

        self.m_staticText1201 = wx.StaticText(self.m_panel48, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.m_staticText1201.Wrap(-1)
        bSizer1301.Add(self.m_staticText1201, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel48.SetSizer(bSizer1301)
        self.m_panel48.Layout()
        bSizer1301.Fit(self.m_panel48)
        self.m_listbook3.AddPage(self.m_panel48, u"Load", False)
        self.m_panel41 = wx.Panel(self.m_listbook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer1601 = wx.BoxSizer(wx.VERTICAL)

        self.m_listCtrl5 = wx.ListCtrl(self.m_panel41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer1601.Add(self.m_listCtrl5, 1, wx.EXPAND, 5)

        bSizer1631 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText135 = wx.StaticText(self.m_panel41, wx.ID_ANY, u"2022-5-23 10:34:19", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText135.Wrap(-1)
        bSizer1631.Add(self.m_staticText135, 0, wx.ALL, 5)

        self.m_staticText136 = wx.StaticText(self.m_panel41, wx.ID_ANY, u"Value", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText136.Wrap(-1)
        bSizer1631.Add(self.m_staticText136, 0, wx.ALL, 5)

        bSizer1601.Add(bSizer1631, 0, wx.EXPAND, 5)

        bSizer1611 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_checkBox61 = wx.CheckBox(self.m_panel41, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1611.Add(self.m_checkBox61, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText133 = wx.StaticText(self.m_panel41, wx.ID_ANY, u"Frequency", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText133.Wrap(-1)
        bSizer1611.Add(self.m_staticText133, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice4Choices = [u"1", u"2", u"3", u"5", u"10", u"15", u"30"]
        self.m_choice4 = wx.Choice(self.m_panel41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0)
        self.m_choice4.SetSelection(0)
        bSizer1611.Add(self.m_choice4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText1341 = wx.StaticText(self.m_panel41, wx.ID_ANY, u"Number", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.m_staticText1341.Wrap(-1)
        bSizer1611.Add(self.m_staticText1341, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice5Choices = [u"50", u"100", u"200", u"500", u"1000"]
        self.m_choice5 = wx.Choice(self.m_panel41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0)
        self.m_choice5.SetSelection(0)
        bSizer1611.Add(self.m_choice5, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText1321 = wx.StaticText(self.m_panel41, wx.ID_ANY, u"Time", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1321.Wrap(-1)
        bSizer1611.Add(self.m_staticText1321, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1601.Add(bSizer1611, 0, wx.EXPAND, 5)

        self.m_panel41.SetSizer(bSizer1601)
        self.m_panel41.Layout()
        bSizer1601.Fit(self.m_panel41)
        self.m_listbook3.AddPage(self.m_panel41, u"MeWa", False)

        bSizer112.Add(self.m_listbook3, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel441.SetSizer(bSizer112)
        self.m_panel441.Layout()
        bSizer112.Fit(self.m_panel441)
        self.m_notebook1.AddPage(self.m_panel441, u"Write", False)
        self.m_panel481 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer192 = wx.BoxSizer(wx.VERTICAL)

        bSizer193 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText172 = wx.StaticText(self.m_panel481, wx.ID_ANY, u"选择数据库", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText172.Wrap(-1)
        bSizer193.Add(self.m_staticText172, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice7Choices = []
        self.m_choice7 = wx.Choice(self.m_panel481, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice7Choices, 0)
        self.m_choice7.SetSelection(0)
        bSizer193.Add(self.m_choice7, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText173 = wx.StaticText(self.m_panel481, wx.ID_ANY, u"选择数据表", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText173.Wrap(-1)
        bSizer193.Add(self.m_staticText173, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice8Choices = []
        self.m_choice8 = wx.Choice(self.m_panel481, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice8Choices, 0)
        self.m_choice8.SetSelection(0)
        bSizer193.Add(self.m_choice8, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button38 = wx.Button(self.m_panel481, wx.ID_ANY, u"详细信息", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer193.Add(self.m_button38, 0, wx.ALL, 5)

        self.m_button35 = wx.Button(self.m_panel481, wx.ID_ANY, u"插入", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button35.SetDefault()
        bSizer193.Add(self.m_button35, 0, wx.ALL, 5)

        self.m_button36 = wx.Button(self.m_panel481, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button36.SetDefault()
        bSizer193.Add(self.m_button36, 0, wx.ALL, 5)

        self.m_button37 = wx.Button(self.m_panel481, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer193.Add(self.m_button37, 0, wx.ALL, 5)

        self.m_button39 = wx.Button(self.m_panel481, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer193.Add(self.m_button39, 0, wx.ALL, 5)

        bSizer192.Add(bSizer193, 0, wx.EXPAND, 5)

        self.m_listCtrl8 = wx.ListCtrl(self.m_panel481, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer192.Add(self.m_listCtrl8, 1, wx.ALL | wx.EXPAND, 5)

        bSizer194 = wx.BoxSizer(wx.VERTICAL)

        bSizer192.Add(bSizer194, 1, wx.EXPAND, 5)

        self.m_panel481.SetSizer(bSizer192)
        self.m_panel481.Layout()
        bSizer192.Fit(self.m_panel481)
        self.m_notebook1.AddPage(self.m_panel481, u"MySQL", False)
        self.m_panel412 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer1642 = wx.BoxSizer(wx.VERTICAL)

        bSizer1651 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button321 = wx.Button(self.m_panel412, wx.ID_ANY, u"测试", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1651.Add(self.m_button321, 0, wx.ALL, 5)

        self.m_button332 = wx.Button(self.m_panel412, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button332.SetDefault()
        bSizer1651.Add(self.m_button332, 0, wx.ALL, 5)

        self.m_button342 = wx.Button(self.m_panel412, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1651.Add(self.m_button342, 0, wx.ALL, 5)

        self.m_button351 = wx.Button(self.m_panel412, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1651.Add(self.m_button351, 0, wx.ALL, 5)

        bSizer1642.Add(bSizer1651, 0, wx.EXPAND, 5)

        self.m_grid21 = wx.grid.Grid(self.m_panel412, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid21.CreateGrid(5, 5)
        self.m_grid21.EnableEditing(True)
        self.m_grid21.EnableGridLines(True)
        self.m_grid21.EnableDragGridSize(False)
        self.m_grid21.SetMargins(0, 0)

        # Columns
        self.m_grid21.EnableDragColMove(False)
        self.m_grid21.EnableDragColSize(True)
        self.m_grid21.SetColLabelSize(30)
        self.m_grid21.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid21.EnableDragRowSize(True)
        self.m_grid21.SetRowLabelSize(80)
        self.m_grid21.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid21.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer1642.Add(self.m_grid21, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel412.SetSizer(bSizer1642)
        self.m_panel412.Layout()
        bSizer1642.Fit(self.m_panel412)
        self.m_notebook1.AddPage(self.m_panel412, u"a page", True)
        self.m_panel403 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer140 = wx.BoxSizer(wx.VERTICAL)

        bSizer141 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl95 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, u"2021年下半学期网络三班课程表", wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_CENTRE | wx.NO_BORDER)
        self.m_textCtrl95.SetFont(wx.Font(15, 70, 90, 90, False, "华文中宋"))

        bSizer141.Add(self.m_textCtrl95, 0, wx.ALL | wx.EXPAND, 5)

        bSizer140.Add(bSizer141, 0, wx.EXPAND, 5)

        bSizer149 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer150 = wx.BoxSizer(wx.VERTICAL)

        bSizer151 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText120 = wx.StaticText(self.m_panel403, wx.ID_ANY, u"上午", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText120.Wrap(-1)
        self.m_staticText120.SetFont(wx.Font(18, 70, 90, 90, False, "华文中宋"))

        bSizer151.Add(self.m_staticText120, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer150.Add(bSizer151, 1, 0, 5)

        bSizer152 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1211 = wx.StaticText(self.m_panel403, wx.ID_ANY, u"下午", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1211.Wrap(-1)
        self.m_staticText1211.SetFont(wx.Font(18, 70, 90, 90, False, "华文中宋"))

        bSizer152.Add(self.m_staticText1211, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer150.Add(bSizer152, 1, 0, 5)

        bSizer149.Add(bSizer150, 0, wx.EXPAND, 5)

        bSizer1471 = wx.BoxSizer(wx.VERTICAL)

        bSizer159 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText131 = wx.StaticText(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText131.Wrap(-1)
        bSizer159.Add(self.m_staticText131, 0, wx.ALL, 5)

        bSizer160 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText126 = wx.StaticText(self.m_panel403, wx.ID_ANY, u"星期一", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText126.Wrap(-1)
        self.m_staticText126.SetFont(wx.Font(15, 70, 90, 90, False, "华文中宋"))

        bSizer160.Add(self.m_staticText126, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer159.Add(bSizer160, 1, 0, 5)

        bSizer161 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText127 = wx.StaticText(self.m_panel403, wx.ID_ANY, u"星期二", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText127.Wrap(-1)
        self.m_staticText127.SetFont(wx.Font(15, 70, 90, 90, False, "华文中宋"))

        bSizer161.Add(self.m_staticText127, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer159.Add(bSizer161, 1, 0, 5)

        bSizer162 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText128 = wx.StaticText(self.m_panel403, wx.ID_ANY, u"星期三", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText128.Wrap(-1)
        self.m_staticText128.SetFont(wx.Font(15, 70, 90, 90, False, "华文中宋"))

        bSizer162.Add(self.m_staticText128, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer159.Add(bSizer162, 1, 0, 5)

        bSizer163 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText129 = wx.StaticText(self.m_panel403, wx.ID_ANY, u"星期四", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText129.Wrap(-1)
        self.m_staticText129.SetFont(wx.Font(15, 70, 90, 90, False, "华文中宋"))

        bSizer163.Add(self.m_staticText129, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer159.Add(bSizer163, 1, 0, 5)

        bSizer164 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText130 = wx.StaticText(self.m_panel403, wx.ID_ANY, u"星期五", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText130.Wrap(-1)
        self.m_staticText130.SetFont(wx.Font(15, 70, 90, 90, False, "华文中宋"))

        bSizer164.Add(self.m_staticText130, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer159.Add(bSizer164, 1, 0, 5)

        bSizer1471.Add(bSizer159, 0, wx.EXPAND, 5)

        bSizer146 = wx.BoxSizer(wx.VERTICAL)

        bSizer142 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText122 = wx.StaticText(self.m_panel403, wx.ID_ANY, u"08:20\n09:40", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText122.Wrap(-1)
        bSizer142.Add(self.m_staticText122, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl751 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl751.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer142.Add(self.m_textCtrl751, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl761 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl761.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer142.Add(self.m_textCtrl761, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl771 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl771.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer142.Add(self.m_textCtrl771, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl78 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl78.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer142.Add(self.m_textCtrl78, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl79 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl79.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer142.Add(self.m_textCtrl79, 1, wx.ALL | wx.EXPAND, 5)

        bSizer146.Add(bSizer142, 1, wx.EXPAND, 5)

        bSizer1431 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText123 = wx.StaticText(self.m_panel403, wx.ID_ANY, u"10:10\n11:30", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText123.Wrap(-1)
        bSizer1431.Add(self.m_staticText123, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl80 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl80.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer1431.Add(self.m_textCtrl80, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl81 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl81.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer1431.Add(self.m_textCtrl81, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl82 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl82.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer1431.Add(self.m_textCtrl82, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl83 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl83.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer1431.Add(self.m_textCtrl83, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl84 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl84.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer1431.Add(self.m_textCtrl84, 1, wx.ALL | wx.EXPAND, 5)

        bSizer146.Add(bSizer1431, 1, wx.EXPAND, 5)

        bSizer1471.Add(bSizer146, 1, wx.EXPAND, 5)

        bSizer158 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText132 = wx.StaticText(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText132.Wrap(-1)
        bSizer158.Add(self.m_staticText132, 0, wx.ALL, 5)

        bSizer1471.Add(bSizer158, 0, 0, 5)

        bSizer148 = wx.BoxSizer(wx.VERTICAL)

        bSizer144 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText124 = wx.StaticText(self.m_panel403, wx.ID_ANY, u"13:10\n14:30", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText124.Wrap(-1)
        bSizer144.Add(self.m_staticText124, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl85 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl85.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer144.Add(self.m_textCtrl85, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl86 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl86.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer144.Add(self.m_textCtrl86, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl87 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl87.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer144.Add(self.m_textCtrl87, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl88 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl88.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer144.Add(self.m_textCtrl88, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl89 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl89.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer144.Add(self.m_textCtrl89, 1, wx.ALL | wx.EXPAND, 5)

        bSizer148.Add(bSizer144, 1, wx.EXPAND, 5)

        bSizer145 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText125 = wx.StaticText(self.m_panel403, wx.ID_ANY, u"14:45\n16:05", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText125.Wrap(-1)
        bSizer145.Add(self.m_staticText125, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl90 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl90.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer145.Add(self.m_textCtrl90, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl91 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl91.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer145.Add(self.m_textCtrl91, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl92 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl92.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer145.Add(self.m_textCtrl92, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl93 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl93.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer145.Add(self.m_textCtrl93, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl94 = wx.TextCtrl(self.m_panel403, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.NO_BORDER)
        self.m_textCtrl94.SetFont(wx.Font(11, 70, 90, 90, False, "华文中宋"))

        bSizer145.Add(self.m_textCtrl94, 1, wx.ALL | wx.EXPAND, 5)

        bSizer148.Add(bSizer145, 1, wx.EXPAND, 5)

        bSizer1471.Add(bSizer148, 1, wx.EXPAND, 5)

        bSizer149.Add(bSizer1471, 1, wx.EXPAND, 5)

        bSizer140.Add(bSizer149, 1, wx.EXPAND, 5)

        self.m_panel403.SetSizer(bSizer140)
        self.m_panel403.Layout()
        bSizer140.Fit(self.m_panel403)
        self.m_notebook1.AddPage(self.m_panel403, u"Timetable", False)
        self.m_panel6 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer23 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel10 = wx.Panel(self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer27 = wx.BoxSizer(wx.VERTICAL)

        bSizer86 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel37 = wx.Panel(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        bSizer92 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText981 = wx.StaticText(self.m_panel37, wx.ID_ANY, u"SQL Config", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText981.Wrap(-1)
        self.m_staticText981.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        bSizer92.Add(self.m_staticText981, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer651 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer32 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText14 = wx.StaticText(self.m_panel37, wx.ID_ANY, u"Host", wx.DefaultPosition, wx.Size(-1, 25), 0)
        self.m_staticText14.Wrap(-1)
        bSizer32.Add(self.m_staticText14, 0, wx.ALL, 5)

        self.m_staticText151 = wx.StaticText(self.m_panel37, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.Size(-1, 25), 0)
        self.m_staticText151.Wrap(-1)
        bSizer32.Add(self.m_staticText151, 0, wx.ALL, 5)

        self.m_staticText16 = wx.StaticText(self.m_panel37, wx.ID_ANY, u"SQL User", wx.DefaultPosition, wx.Size(-1, 25),
                                            0)
        self.m_staticText16.Wrap(-1)
        bSizer32.Add(self.m_staticText16, 0, wx.ALL, 5)

        self.m_staticText17 = wx.StaticText(self.m_panel37, wx.ID_ANY, u"Passwd", wx.DefaultPosition, wx.Size(-1, 25),
                                            0)
        self.m_staticText17.Wrap(-1)
        bSizer32.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.m_staticText18 = wx.StaticText(self.m_panel37, wx.ID_ANY, u"Database", wx.DefaultPosition, wx.Size(-1, 25),
                                            0)
        self.m_staticText18.Wrap(-1)
        bSizer32.Add(self.m_staticText18, 0, wx.ALL, 5)

        self.m_staticText19 = wx.StaticText(self.m_panel37, wx.ID_ANY, u"Charset", wx.DefaultPosition, wx.Size(-1, 25),
                                            0)
        self.m_staticText19.Wrap(-1)
        bSizer32.Add(self.m_staticText19, 0, wx.ALL, 5)

        bSizer651.Add(bSizer32, 0, 0, 5)

        bSizer34 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl4 = wx.TextCtrl(self.m_panel37, wx.ID_ANY, u"localhost", wx.DefaultPosition, wx.Size(200, 25), 0)
        bSizer34.Add(self.m_textCtrl4, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self.m_panel37, wx.ID_ANY, u"3306", wx.DefaultPosition, wx.Size(-1, 25), 0)
        bSizer34.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self.m_panel37, wx.ID_ANY, u"root", wx.DefaultPosition, wx.Size(-1, 25), 0)
        bSizer34.Add(self.m_textCtrl6, 0, wx.ALL, 5)

        bSizer37 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl7 = wx.TextCtrl(self.m_panel37, wx.ID_ANY, u"nichenyang", wx.DefaultPosition, wx.Size(200, 25),
                                       wx.TE_PASSWORD)
        bSizer37.Add(self.m_textCtrl7, 0, wx.ALL, 5)

        bSizer34.Add(bSizer37, 0, 0, 5)

        self.m_textCtrl8 = wx.TextCtrl(self.m_panel37, wx.ID_ANY, u"analizepy", wx.DefaultPosition, wx.Size(-1, 25), 0)
        bSizer34.Add(self.m_textCtrl8, 0, wx.ALL, 5)

        self.m_textCtrl9 = wx.TextCtrl(self.m_panel37, wx.ID_ANY, u"utf8", wx.DefaultPosition, wx.Size(-1, 25), 0)
        bSizer34.Add(self.m_textCtrl9, 0, wx.ALL, 5)

        bSizer651.Add(bSizer34, 1, wx.EXPAND, 5)

        bSizer92.Add(bSizer651, 1, wx.EXPAND, 5)

        self.m_button30 = wx.Button(self.m_panel37, wx.ID_ANY, u"Test", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer92.Add(self.m_button30, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel37.SetSizer(bSizer92)
        self.m_panel37.Layout()
        bSizer92.Fit(self.m_panel37)
        bSizer86.Add(self.m_panel37, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1382 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel381 = wx.Panel(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        bSizer93 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText991 = wx.StaticText(self.m_panel381, wx.ID_ANY, u"User Login", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText991.Wrap(-1)
        self.m_staticText991.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        bSizer93.Add(self.m_staticText991, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer66 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer30 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText21 = wx.StaticText(self.m_panel381, wx.ID_ANY, u"FAS User", wx.DefaultPosition,
                                            wx.Size(-1, 25), 0)
        self.m_staticText21.Wrap(-1)
        bSizer30.Add(self.m_staticText21, 0, wx.ALL, 5)

        self.m_staticText22 = wx.StaticText(self.m_panel381, wx.ID_ANY, u"Passwd", wx.DefaultPosition, wx.Size(-1, 25),
                                            0)
        self.m_staticText22.Wrap(-1)
        bSizer30.Add(self.m_staticText22, 0, wx.ALL, 5)

        bSizer66.Add(bSizer30, 0, 0, 5)

        bSizer31 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl11 = wx.TextCtrl(self.m_panel381, wx.ID_ANY, u"zhaozhi", wx.DefaultPosition, wx.Size(-1, 25), 0)
        bSizer31.Add(self.m_textCtrl11, 0, wx.ALL, 5)

        bSizer36 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl12 = wx.TextCtrl(self.m_panel381, wx.ID_ANY, u"zhaozhi", wx.DefaultPosition, wx.Size(200, 25),
                                        wx.TE_PASSWORD)
        bSizer36.Add(self.m_textCtrl12, 0, wx.ALL, 5)

        bSizer31.Add(bSizer36, 0, 0, 5)

        bSizer66.Add(bSizer31, 0, 0, 5)

        bSizer93.Add(bSizer66, 1, wx.EXPAND, 5)

        self.m_panel381.SetSizer(bSizer93)
        self.m_panel381.Layout()
        bSizer93.Fit(self.m_panel381)
        bSizer1382.Add(self.m_panel381, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel40 = wx.Panel(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        bSizer88 = wx.BoxSizer(wx.VERTICAL)

        self.m_button291 = wx.Button(self.m_panel40, wx.ID_ANY, u"创建所需数据库", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer88.Add(self.m_button291, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel40.SetSizer(bSizer88)
        self.m_panel40.Layout()
        bSizer88.Fit(self.m_panel40)
        bSizer1382.Add(self.m_panel40, 1, wx.ALL | wx.EXPAND, 5)

        bSizer86.Add(bSizer1382, 1, wx.EXPAND, 5)

        bSizer27.Add(bSizer86, 1, wx.EXPAND, 5)

        self.m_panel10.SetSizer(bSizer27)
        self.m_panel10.Layout()
        bSizer27.Fit(self.m_panel10)
        bSizer23.Add(self.m_panel10, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel6.SetSizer(bSizer23)
        self.m_panel6.Layout()
        bSizer23.Fit(self.m_panel6)
        self.m_notebook1.AddPage(self.m_panel6, u"Config", False)
        self.m_panel36 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer871 = wx.BoxSizer(wx.VERTICAL)

        bSizer901 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl57 = wx.TextCtrl(self.m_panel36, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE)
        self.m_textCtrl57.SetFont(wx.Font(25, 70, 90, 90, False, wx.EmptyString))

        bSizer901.Add(self.m_textCtrl57, 1, wx.EXPAND | wx.TOP, 5)

        bSizer871.Add(bSizer901, 1, wx.EXPAND, 5)

        bSizer1141 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_listbook21 = wx.Listbook(self.m_panel36, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT)
        self.m_panel371 = wx.Panel(self.m_listbook21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer881 = wx.BoxSizer(wx.VERTICAL)

        bSizer891 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer912 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText963 = wx.StaticText(self.m_panel371, wx.ID_ANY, u"lim", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText963.Wrap(-1)
        self.m_staticText963.SetFont(wx.Font(30, 70, 90, 90, False, wx.EmptyString))

        bSizer912.Add(self.m_staticText963, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        bSizer921 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText972 = wx.StaticText(self.m_panel371, wx.ID_ANY, u"x  -->", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText972.Wrap(-1)
        bSizer921.Add(self.m_staticText972, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl59 = wx.TextCtrl(self.m_panel371, wx.ID_ANY, u"oo", wx.DefaultPosition, wx.Size(40, -1), 0)
        bSizer921.Add(self.m_textCtrl59, 0, wx.RIGHT | wx.LEFT, 5)

        bSizer912.Add(bSizer921, 0, wx.EXPAND | wx.LEFT, 5)

        bSizer891.Add(bSizer912, 0, wx.EXPAND, 5)

        self.m_textCtrl58 = wx.TextCtrl(self.m_panel371, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.TE_PROCESS_ENTER)
        self.m_textCtrl58.SetFont(wx.Font(25, 70, 90, 90, False, wx.EmptyString))

        bSizer891.Add(self.m_textCtrl58, 1, wx.ALL | wx.EXPAND, 5)

        bSizer881.Add(bSizer891, 1, wx.EXPAND, 5)

        self.m_panel371.SetSizer(bSizer881)
        self.m_panel371.Layout()
        bSizer881.Fit(self.m_panel371)
        self.m_listbook21.AddPage(self.m_panel371, u"极限", True)
        self.m_panel382 = wx.Panel(self.m_listbook21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer931 = wx.BoxSizer(wx.VERTICAL)

        bSizer95 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer96 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText982 = wx.StaticText(self.m_panel382, wx.ID_ANY, u"f(x)=", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText982.Wrap(-1)
        self.m_staticText982.SetFont(wx.Font(25, 70, 90, 90, False, wx.EmptyString))

        bSizer96.Add(self.m_staticText982, 0, wx.ALL, 5)

        bSizer95.Add(bSizer96, 0, 0, 5)

        self.m_textCtrl61 = wx.TextCtrl(self.m_panel382, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_PROCESS_ENTER)
        self.m_textCtrl61.SetFont(wx.Font(25, 70, 90, 90, False, wx.EmptyString))

        bSizer95.Add(self.m_textCtrl61, 1, wx.ALL | wx.EXPAND, 5)

        bSizer931.Add(bSizer95, 1, wx.EXPAND, 5)

        self.m_panel382.SetSizer(bSizer931)
        self.m_panel382.Layout()
        bSizer931.Fit(self.m_panel382)
        self.m_listbook21.AddPage(self.m_panel382, u"导数", False)
        self.m_panel391 = wx.Panel(self.m_listbook21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer97 = wx.BoxSizer(wx.VERTICAL)

        bSizer99 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1001 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText992 = wx.StaticText(self.m_panel391, wx.ID_ANY, u"∫", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText992.Wrap(-1)
        self.m_staticText992.SetFont(wx.Font(50, 70, 90, 90, False, wx.EmptyString))

        bSizer1001.Add(self.m_staticText992, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        bSizer99.Add(bSizer1001, 0, 0, 5)

        self.m_textCtrl63 = wx.TextCtrl(self.m_panel391, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_PROCESS_ENTER)
        self.m_textCtrl63.SetFont(wx.Font(25, 70, 90, 90, False, wx.EmptyString))

        bSizer99.Add(self.m_textCtrl63, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1011 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1001 = wx.StaticText(self.m_panel391, wx.ID_ANY, u"dx", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1001.Wrap(-1)
        self.m_staticText1001.SetFont(wx.Font(35, 70, 90, 90, False, wx.EmptyString))

        bSizer1011.Add(self.m_staticText1001, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer99.Add(bSizer1011, 0, wx.ALIGN_BOTTOM, 5)

        bSizer97.Add(bSizer99, 1, wx.EXPAND, 5)

        self.m_panel391.SetSizer(bSizer97)
        self.m_panel391.Layout()
        bSizer97.Fit(self.m_panel391)
        self.m_listbook21.AddPage(self.m_panel391, u"不定积分", False)
        self.m_panel401 = wx.Panel(self.m_listbook21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer102 = wx.BoxSizer(wx.VERTICAL)

        bSizer104 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer105 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1011 = wx.StaticText(self.m_panel401, wx.ID_ANY, u"∫", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1011.Wrap(-1)
        self.m_staticText1011.SetFont(wx.Font(50, 70, 90, 90, False, wx.EmptyString))

        bSizer105.Add(self.m_staticText1011, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        bSizer108 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl65 = wx.TextCtrl(self.m_panel401, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size(40, 35), 0)
        self.m_textCtrl65.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        bSizer108.Add(self.m_textCtrl65, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        self.m_textCtrl66 = wx.TextCtrl(self.m_panel401, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(40, 35), 0)
        self.m_textCtrl66.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        bSizer108.Add(self.m_textCtrl66, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        bSizer105.Add(bSizer108, 1, wx.EXPAND, 5)

        bSizer104.Add(bSizer105, 0, wx.EXPAND, 5)

        bSizer106 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl67 = wx.TextCtrl(self.m_panel401, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_PROCESS_ENTER)
        self.m_textCtrl67.SetFont(wx.Font(25, 70, 90, 90, False, wx.EmptyString))

        bSizer106.Add(self.m_textCtrl67, 1, wx.ALL | wx.EXPAND, 5)

        bSizer104.Add(bSizer106, 1, wx.EXPAND, 5)

        bSizer107 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1021 = wx.StaticText(self.m_panel401, wx.ID_ANY, u"d", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1021.Wrap(-1)
        self.m_staticText1021.SetFont(wx.Font(35, 70, 90, 90, False, wx.EmptyString))

        bSizer107.Add(self.m_staticText1021, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.m_textCtrl68 = wx.TextCtrl(self.m_panel401, wx.ID_ANY, u"x", wx.DefaultPosition, wx.Size(50, 40), 0)
        self.m_textCtrl68.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        bSizer107.Add(self.m_textCtrl68, 0, wx.ALIGN_BOTTOM | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        bSizer104.Add(bSizer107, 0, wx.ALIGN_BOTTOM, 5)

        bSizer102.Add(bSizer104, 1, wx.EXPAND, 5)

        self.m_panel401.SetSizer(bSizer102)
        self.m_panel401.Layout()
        bSizer102.Fit(self.m_panel401)
        self.m_listbook21.AddPage(self.m_panel401, u"定积分", False)
        self.m_panel411 = wx.Panel(self.m_listbook21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer111 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel411.SetSizer(bSizer111)
        self.m_panel411.Layout()
        bSizer111.Fit(self.m_panel411)
        self.m_listbook21.AddPage(self.m_panel411, u"微分方程", False)
        self.m_panel421 = wx.Panel(self.m_listbook21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer109 = wx.BoxSizer(wx.VERTICAL)

        bSizer1374 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_radioBtn2 = wx.RadioButton(self.m_panel421, wx.ID_ANY, u"2D", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_radioBtn2.SetValue(True)
        bSizer1374.Add(self.m_radioBtn2, 0, wx.ALL, 5)

        self.m_radioBtn1 = wx.RadioButton(self.m_panel421, wx.ID_ANY, u"3D", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1374.Add(self.m_radioBtn1, 0, wx.ALL, 5)

        bSizer109.Add(bSizer1374, 0, wx.EXPAND, 5)

        self.m_textCtrl69 = wx.TextCtrl(self.m_panel421, wx.ID_ANY, u"sin(x)", wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_PROCESS_ENTER)
        self.m_textCtrl69.SetFont(wx.Font(25, 70, 90, 90, False, wx.EmptyString))

        bSizer109.Add(self.m_textCtrl69, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.m_panel421.SetSizer(bSizer109)
        self.m_panel421.Layout()
        bSizer109.Fit(self.m_panel421)
        self.m_listbook21.AddPage(self.m_panel421, u"画图", False)
        self.m_panel44 = wx.Panel(self.m_listbook21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer110 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText103 = wx.StaticText(self.m_panel44, wx.ID_ANY,
                                             u"为了方便，所以就遵循着sympy模块的语法规范，\n根号下x就写为：sqrt(x)\n\ne的x次幂写为：exp(x)\n\nx的平方写为：x**2\n\n圆周率Π写为：pi\n\n自然常数写为：E\n\n无穷写为：oo\n\n对于复杂的表达式需要用圆括号括起来，且仅用此一种括号",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText103.Wrap(-1)
        self.m_staticText103.SetFont(wx.Font(13, 70, 90, 90, False, wx.EmptyString))

        bSizer110.Add(self.m_staticText103, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel44.SetSizer(bSizer110)
        self.m_panel44.Layout()
        bSizer110.Fit(self.m_panel44)
        self.m_listbook21.AddPage(self.m_panel44, u"说明", False)

        bSizer1141.Add(self.m_listbook21, 1, wx.EXPAND | wx.BOTTOM, 5)

        bSizer871.Add(bSizer1141, 1, wx.EXPAND, 5)

        self.m_panel36.SetSizer(bSizer871)
        self.m_panel36.Layout()
        bSizer871.Fit(self.m_panel36)
        self.m_notebook1.AddPage(self.m_panel36, u"Math", False)
        self.m_panel13 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer38 = wx.BoxSizer(wx.VERTICAL)

        bSizer98 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText107 = wx.StaticText(self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText107.Wrap(-1)
        bSizer98.Add(self.m_staticText107, 1, wx.ALL, 5)

        self.m_staticText104 = wx.StaticText(self.m_panel13, wx.ID_ANY, u"不回首（其二）", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText104.Wrap(-1)
        self.m_staticText104.SetFont(wx.Font(26, 70, 90, 90, False, "华文新魏"))

        bSizer98.Add(self.m_staticText104, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText962 = wx.StaticText(self.m_panel13, wx.ID_ANY, u"昭质", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText962.Wrap(-1)
        self.m_staticText962.SetFont(wx.Font(16, 70, 90, 90, False, "华文新魏"))

        bSizer98.Add(self.m_staticText962, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText952 = wx.StaticText(self.m_panel13, wx.ID_ANY,
                                             u"寒食三旬立重楼，一轮明月挂九州\n灯红酒绿条条过，映得满江镜中囚\n微风何时不曾有，唯独月下游子愁\n踏过江山千万遍，白鬓微霜难定宿\n几经世载已入秋，无欲无舍更无留\n请君一杯相思酒，饮毕难有相思愁",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText952.Wrap(-1)
        self.m_staticText952.SetFont(wx.Font(18, 70, 90, 90, False, "华文新魏"))

        bSizer98.Add(self.m_staticText952, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText108 = wx.StaticText(self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText108.Wrap(-1)
        bSizer98.Add(self.m_staticText108, 1, wx.ALL, 5)

        bSizer38.Add(bSizer98, 1, wx.EXPAND, 5)

        bSizer601 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline1 = wx.StaticLine(self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer601.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText631 = wx.StaticText(self.m_panel13, wx.ID_ANY, u"Eternal", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText631.Wrap(-1)
        bSizer601.Add(self.m_staticText631, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText64 = wx.StaticText(self.m_panel13, wx.ID_ANY, u"www.nichenyang.cn", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText64.Wrap(-1)
        bSizer601.Add(self.m_staticText64, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText106 = wx.StaticText(self.m_panel13, wx.ID_ANY, u"Think Power Eternal", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText106.Wrap(-1)
        bSizer601.Add(self.m_staticText106, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText66 = wx.StaticText(self.m_panel13, wx.ID_ANY, u"The Quieter You Are, The More You Hear",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText66.Wrap(-1)
        bSizer601.Add(self.m_staticText66, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer38.Add(bSizer601, 0, wx.EXPAND, 5)

        self.m_panel13.SetSizer(bSizer38)
        self.m_panel13.Layout()
        bSizer38.Fit(self.m_panel13)
        self.m_notebook1.AddPage(self.m_panel13, u"About", False)

        bSizer2.Add(self.m_notebook1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.menuitem1, id=self.m_menuItem1.GetId())
        self.Bind(wx.EVT_MENU, self.menuitem12, id=self.m_menuItem12.GetId())
        self.Bind(wx.EVT_MENU, self.menuitem2, id=self.m_menuItem2.GetId())
        self.Bind(wx.EVT_MENU, self.menuitem3, id=self.m_menuItem3.GetId())
        self.Bind(wx.EVT_MENU, self.menuitem10, id=self.m_menuItem10.GetId())
        self.Bind(wx.EVT_MENU, self.menuitem5, id=self.m_menuItem5.GetId())
        self.Bind(wx.EVT_MENU, self.menuitem6, id=self.m_menuItem6.GetId())
        self.Bind(wx.EVT_MENU, self.menuitem4, id=self.m_menuItem4.GetId())
        self.Bind(wx.EVT_MENU, self.menuitem7, id=self.m_menuItem7.GetId())
        self.Bind(wx.EVT_MENU, self.menuitem8, id=self.m_menuItem8.GetId())
        self.Bind(wx.EVT_MENU, self.menuitem9, id=self.m_menuItem9.GetId())
        self.m_notebook1.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onnotebookpagechanged1)
        self.m_listCtrl4.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onlistitemactivated4)
        self.m_listCtrl4.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onlistitemselected4)
        self.m_button2.Bind(wx.EVT_BUTTON, self.button2)
        self.m_button221.Bind(wx.EVT_BUTTON, self.button221)
        self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onlistitenactived2)
        self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_SELECTED, self.listitemselected2)
        self.m_listCtrl6.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onlistitemselected6)
        self.m_textCtrl75.Bind(wx.EVT_TEXT, self.textCtrl75)
        self.m_listbook4.Bind(wx.EVT_LISTBOOK_PAGE_CHANGED, self.onlistbookpagechanged4)
        self.m_button28.Bind(wx.EVT_BUTTON, self.button28)
        self.m_button29.Bind(wx.EVT_BUTTON, self.button29)
        self.m_button311.Bind(wx.EVT_BUTTON, self.button311)
        self.m_listCtrl7.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onlistitemselected7)
        self.m_button31.Bind(wx.EVT_BUTTON, self.button31)
        self.m_button331.Bind(wx.EVT_BUTTON, self.button331)
        self.m_button301.Bind(wx.EVT_BUTTON, self.button301)
        self.m_button32.Bind(wx.EVT_BUTTON, self.button32)
        self.m_listCtrl3.Bind(wx.EVT_LIST_ITEM_SELECTED, self.listitemselected3)
        self.m_listBox5.Bind(wx.EVT_LISTBOX, self.listbox5)
        self.m_button33.Bind(wx.EVT_BUTTON, self.button33)
        self.m_slider1.Bind(wx.EVT_SCROLL, self.slider1)
        self.m_button34.Bind(wx.EVT_BUTTON, self.button34)
        self.m_choice11.Bind(wx.EVT_CHOICE, self.choice11)
        self.m_button27.Bind(wx.EVT_BUTTON, self.button27)
        self.m_button26.Bind(wx.EVT_BUTTON, self.button26)
        self.m_button24.Bind(wx.EVT_BUTTON, self.button24)
        self.m_button25.Bind(wx.EVT_BUTTON, self.button25)
        self.m_button231.Bind(wx.EVT_BUTTON, self.button231)
        self.m_listbook3.Bind(wx.EVT_LISTBOOK_PAGE_CHANGED, self.onlistbookpagechanged3)
        self.m_slider2.Bind(wx.EVT_SCROLL, self.slider2)
        self.m_listBox6.Bind(wx.EVT_LISTBOX, self.listbox6)
        self.m_choice1.Bind(wx.EVT_CHOICE, self.choice1)
        self.m_listBox7.Bind(wx.EVT_LISTBOX, self.listbox7)
        self.m_button48.Bind(wx.EVT_BUTTON, self.button48)
        self.m_listBox9.Bind(wx.EVT_LISTBOX, self.listbox9)
        self.m_button44.Bind(wx.EVT_BUTTON, self.button44)
        self.m_listBox8.Bind(wx.EVT_LISTBOX, self.listbox8)
        self.m_button43.Bind(wx.EVT_BUTTON, self.button43)
        self.m_button411.Bind(wx.EVT_BUTTON, self.button411)
        self.m_listCtrl5.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onlistitemselected5)
        self.m_checkBox61.Bind(wx.EVT_CHECKBOX, self.checkbox61)
        self.m_choice7.Bind(wx.EVT_CHOICE, self.onchoice7)
        self.m_choice8.Bind(wx.EVT_CHOICE, self.onchoice8)
        self.m_button38.Bind(wx.EVT_BUTTON, self.button38)
        self.m_button35.Bind(wx.EVT_BUTTON, self.button35)
        self.m_button36.Bind(wx.EVT_BUTTON, self.button36)
        self.m_button37.Bind(wx.EVT_BUTTON, self.button37)
        self.m_button39.Bind(wx.EVT_BUTTON, self.button39)
        self.m_listCtrl8.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onlistitemselected8)
        self.m_button321.Bind(wx.EVT_BUTTON, self.button321)
        self.m_button332.Bind(wx.EVT_BUTTON, self.button332)
        self.m_button30.Bind(wx.EVT_BUTTON, self.button30)
        self.m_button291.Bind(wx.EVT_BUTTON, self.button291)
        self.m_textCtrl58.Bind(wx.EVT_TEXT_ENTER, self.textctrl58)
        self.m_textCtrl61.Bind(wx.EVT_TEXT_ENTER, self.textctrl61)
        self.m_textCtrl63.Bind(wx.EVT_TEXT_ENTER, self.textctrl63)
        self.m_textCtrl67.Bind(wx.EVT_TEXT_ENTER, self.textctrl67)
        self.m_textCtrl69.Bind(wx.EVT_TEXT_ENTER, self.textctrl69)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def menuitem1(self, event):
        event.Skip()

    def menuitem12(self, event):
        event.Skip()

    def menuitem2(self, event):
        event.Skip()

    def menuitem3(self, event):
        event.Skip()

    def menuitem10(self, event):
        event.Skip()

    def menuitem5(self, event):
        event.Skip()

    def menuitem6(self, event):
        event.Skip()

    def menuitem4(self, event):
        event.Skip()

    def menuitem7(self, event):
        event.Skip()

    def menuitem8(self, event):
        event.Skip()

    def menuitem9(self, event):
        event.Skip()

    def onnotebookpagechanged1(self, event):
        event.Skip()

    def onlistitemactivated4(self, event):
        event.Skip()

    def onlistitemselected4(self, event):
        event.Skip()

    def button2(self, event):
        event.Skip()

    def button221(self, event):
        event.Skip()

    def onlistitenactived2(self, event):
        event.Skip()

    def listitemselected2(self, event):
        event.Skip()

    def onlistitemselected6(self, event):
        event.Skip()

    def textCtrl75(self, event):
        event.Skip()

    def onlistbookpagechanged4(self, event):
        event.Skip()

    def button28(self, event):
        event.Skip()

    def button29(self, event):
        event.Skip()

    def button311(self, event):
        event.Skip()

    def onlistitemselected7(self, event):
        event.Skip()

    def button31(self, event):
        event.Skip()

    def button331(self, event):
        event.Skip()

    def button301(self, event):
        event.Skip()

    def button32(self, event):
        event.Skip()

    def listitemselected3(self, event):
        event.Skip()

    def listbox5(self, event):
        event.Skip()

    def button33(self, event):
        event.Skip()

    def slider1(self, event):
        event.Skip()

    def button34(self, event):
        event.Skip()

    def choice11(self, event):
        event.Skip()

    def button27(self, event):
        event.Skip()

    def button26(self, event):
        event.Skip()

    def button24(self, event):
        event.Skip()

    def button25(self, event):
        event.Skip()

    def button231(self, event):
        event.Skip()

    def onlistbookpagechanged3(self, event):
        event.Skip()

    def slider2(self, event):
        event.Skip()

    def listbox6(self, event):
        event.Skip()

    def choice1(self, event):
        event.Skip()

    def listbox7(self, event):
        event.Skip()

    def button48(self, event):
        event.Skip()

    def listbox9(self, event):
        event.Skip()

    def button44(self, event):
        event.Skip()

    def listbox8(self, event):
        event.Skip()

    def button43(self, event):
        event.Skip()

    def button411(self, event):
        event.Skip()

    def onlistitemselected5(self, event):
        event.Skip()

    def checkbox61(self, event):
        event.Skip()

    def onchoice7(self, event):
        event.Skip()

    def onchoice8(self, event):
        event.Skip()

    def button38(self, event):
        event.Skip()

    def button35(self, event):
        event.Skip()

    def button36(self, event):
        event.Skip()

    def button37(self, event):
        event.Skip()

    def button39(self, event):
        event.Skip()

    def onlistitemselected8(self, event):
        event.Skip()

    def button321(self, event):
        event.Skip()

    def button332(self, event):
        event.Skip()

    def button30(self, event):
        event.Skip()

    def button291(self, event):
        event.Skip()

    def textctrl58(self, event):
        event.Skip()

    def textctrl61(self, event):
        event.Skip()

    def textctrl63(self, event):
        event.Skip()

    def textctrl67(self, event):
        event.Skip()

    def textctrl69(self, event):
        event.Skip()


