import os

# import pymysql
import random
import socket

import pymysql

import AsFunction
from pymysql.converters import escape_string

import time
from concurrent.futures import ThreadPoolExecutor

import wx

import AsDesktop
import AsDialog

from sympy import *
from sympy.plotting import plot
from sympy.plotting import plot3d

import psutil

# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ


pool = ThreadPoolExecutor(1)
pools = ThreadPoolExecutor(1)
pool1 = ThreadPoolExecutor(1)
pool2 = ThreadPoolExecutor(1)

REMOTE_IP = ('114.115.153.152', 9574)
BUFFER_SIZE = 1024
SOCKET_TIMEOUT_TIME = 120


def send_socket_info(self, handle, msg, side='server', do_encode=True, do_print_info=True):
    """
    发送socket info，并根据side打印不同的前缀信息
    :param self:
    :param handle: socket句柄
    :param msg: 要发送的内容
    :param side: 默认server端
    :param do_encode: 是否需要encode，默认True
    :param do_print_info: 是否需要打印socket信息，默认True
    :return:
    """
    if do_encode:
        handle.send(msg.encode())
    else:
        handle.send(msg)

    if do_print_info:
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        if side == 'server':
            print(f'Server send --> {current_time} - {msg}')
            self.m_textCtrl1021.AppendText(f'\nServer send --> {current_time} - {msg}')
        else:
            print(f'Client send --> {current_time} - {msg}')
            self.m_textCtrl1021.AppendText(f'\nClient send --> {current_time} - {msg}')


def receive_socket_info(self, handle, expected_msg, side='server', do_decode=True, do_print_info=True):
    """
    循环接收socket info，判断其返回值，直到指定的值出现为止，防止socket信息粘连，并根据side打印不同的前缀信息
    :param self:
    :param handle: socket句柄
    :param expected_msg: 期待接受的内容，如果接受内容不在返回结果中，一直循环等待，期待内容可以为字符串，也可以为多个字符串组成的列表或元组
    :param side: 默认server端
    :param do_decode: 是否需要decode，默认True
    :param do_print_info: 是否需要打印socket信息，默认True
    :return:
    """
    while True:
        if do_decode:
            socket_data = handle.recv(BUFFER_SIZE).decode()
        else:
            socket_data = handle.recv(BUFFER_SIZE)

        if do_print_info:
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            if side == 'server':
                print(f'Server received ==> {current_time} - {socket_data}')
                self.m_textCtrl1021.AppendText(f'\nServer received ==> {current_time} - {socket_data}')
            else:
                print(f'Client received ==> {current_time} - {socket_data}')
                self.m_textCtrl1021.AppendText(f'\nClient received ==> {current_time} - {socket_data}')

        # 如果expected_msg为空，跳出循环
        if not expected_msg:
            break

        if isinstance(expected_msg, (list, tuple)):
            flag = False
            for expect in expected_msg:  # 循环判断每个期待字符是否在返回结果中
                if expect in socket_data:  # 如果有任意一个存在，跳出循环
                    flag = True
                    break
            if flag:
                break
        else:
            if expected_msg in socket_data:
                break
        time.sleep(3)  # 每隔3秒接收一次socket
    return socket_data


def get_textctrl_value(self):
    while True:
        value = self.m_textCtrl811.GetValue()
        if ">" in value:
            self.m_textCtrl811.Clear()
            return value


# 连接服务器的客户端程序，放在线程中使用
def clientreport(self):
    ip, port = REMOTE_IP
    client = socket.socket()  # 使用TCP方式传输
    print(f'开始连接服务端 {ip}:{port} ...')
    # self.m_textCtrl1021
    self.m_textCtrl1021.AppendText(f'\n开始连接服务端 {ip}:{port} ...')

    client.connect((ip, port))  # 连接远程服务端
    print(f'连接服务端 {ip}:{port} 成功')
    self.m_textCtrl1021.AppendText(f'\n连接服务端 {ip}:{port} 成功')

    client.settimeout(SOCKET_TIMEOUT_TIME)  # 设置客户端超时时间

    # 与服务端握手，达成一致
    send_socket_info(self=self, handle=client, side='client', msg='客户端已就绪')

    receive_socket_info(self=self, handle=client, side='client', expected_msg='服务端已就绪')

    # 与服务端交互
    while True:
        # answer = input('请输入要发送给服务端的信息：')
        answer = get_textctrl_value(self)
        send_socket_info(self, handle=client, side='client', msg=answer)

        socket_data = receive_socket_info(self, handle=client, side='client', expected_msg='')
        if 'quit' in socket_data:
            send_socket_info(self, handle=client, side='client', msg='quit')
            break

    # 断开socket连接
    client.close()
    print(f'与服务端 {ip}:{port} 断开连接')
    self.m_textCtrl1021.AppendText(f'\n与服务端 {ip}:{port} 断开连接')


# 提示语和时间展示函数
def startread(self):
    readn = 30
    while True:
        time.sleep(1)
        nowtime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        self.m_staticText1193.SetLabel(str(nowtime))

        mem = psutil.virtual_memory()
        swm = psutil.swap_memory()
        # print(mem, swm)

        self.m_staticText152.SetLabel("{0:.2f}GB".format(int(mem.total) / 1024 / 1024 / 1024))
        self.m_staticText154.SetLabel("{0:.2f}GB".format(mem.available / 1024 / 1024 / 1024))
        self.m_staticText156.SetLabel("{0:.2f}GB".format(mem.used / 1024 / 1024 / 1024))
        self.m_staticText158.SetLabel("{0}%".format(str(mem.percent)))
        self.m_staticText160.SetLabel("{0:.2f}GB".format(swm.total / 1024 / 1024 / 1024))
        self.m_staticText162.SetLabel("{0:.2f}GB".format(swm.used / 1024 / 1024 / 1024))
        self.m_staticText164.SetLabel("{0:.2f}GB".format(swm.free / 1024 / 1024 / 1024))
        self.m_staticText166.SetLabel("{0}%".format(str(swm.percent)))

        readn += 1
        if readn >= 30:
            datas = AsFunction.exesql("select", "", "", "SELECT body FROM sentences ORDER BY rand() limit 1")
            self.m_staticText1182.SetLabel(str(datas[0][0]))
            # 语音播报文字！
            AsFunction.say(str(datas[0][0]))
            readn = 0


def startmons(self):
    pools.submit(startread, self)


# Write界面的加载留言墙刷新事件
def WriteMeWa(self):
    while True:
        choise = self.m_checkBox61.GetValue()
        pr = self.m_choice4.GetStringSelection()
        if choise:
            time.sleep(int(pr))
            nowtime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            self.m_staticText1321.SetLabel(str(nowtime))
            db, cursor, message = AsFunction.linktosersql()
            if message != "1":
                AsFunction.showtips("Message", "服务器数据库连接失败！")
                db.close()
            else:
                try:
                    number = self.m_choice5.GetStringSelection()
                    sql = "SELECT name,give,time,value FROM ireadmsg ORDER BY time DESC limit %s" % int(number)
                    cursor.execute(sql)
                    datas = cursor.fetchall()

                    self.m_listCtrl5.ClearAll()
                    self.m_listCtrl5.InsertColumn(0, "昵称", width=100)
                    self.m_listCtrl5.InsertColumn(1, "留言给", width=100)
                    self.m_listCtrl5.InsertColumn(2, "时间", width=150)
                    self.m_listCtrl5.InsertColumn(3, "内容", width=400)
                    idx = 0
                    for i in datas:
                        index = self.m_listCtrl5.InsertStringItem(idx, str(i[0]))
                        self.m_listCtrl5.SetStringItem(index, 1, str(i[1]))
                        self.m_listCtrl5.SetStringItem(index, 2, str(i[2]))
                        self.m_listCtrl5.SetStringItem(index, 3, str(i[3]))
                        idx += 1
                    db.close()
                    nowtime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                    self.m_staticText1321.SetLabel(nowtime)
                except:
                    db.close()
        else:
            break


# 留言墙启动函数
def WriteMeWas(self):
    pool1.submit(WriteMeWa, self)


# 上传文件函数
def startanalize(file, self, rangevalue):
    list1 = []
    try:
        for i in os.listdir(str(file)):
            list1.append(i)
    except Exception as e:
        print(str(e))
        pass

    for index in list1:
        filepath = os.path.join(file, index)
        if os.path.isdir(filepath):
            args = [filepath, self, rangevalue]
            pool.submit(lambda p: startanalize(*p), args)
        else:
            lastname = os.path.splitext(index)
            filetype = lastname[1]
            size = os.path.getsize(filepath)

            filepath = eval(repr(filepath).replace('\\', '/'))
            results = AsFunction.exesql("select", "", "",
                                        "select path from fileinfo where path='%s'" % filepath)

            if str(results) == "()":
                now = time.strftime('%Y%m%d%H%M%S', time.localtime(os.path.getmtime(filepath)))

                sqlinsert = "INSERT INTO fileinfo(type, \
                                               name, size, path, time) \
                                               VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
                            (filetype, index, size, filepath, int(now))
                AsFunction.exesql("insert", "", "", sqlinsert)
            else:
                now = time.strftime('%Y%m%d%H%M%S', time.localtime(os.path.getmtime(filepath)))
                AsFunction.exesql("update", "", "",
                                  "UPDATE fileinfo SET time=%s WHERE name='%s'" % (int(now), index))

            # 文件上传操作结束后进行进度条的改变
            guagecurrentvalue = self.m_gauge2.GetValue()
            guagecurrentvalue += 1
            # 进度条的值加1
            self.m_gauge2.SetValue(guagecurrentvalue)
            # 标签的值也加1
            self.m_staticText101.SetLabel(str(guagecurrentvalue))

            # 百分比标签加1
            getvalue = float(self.m_staticText931.GetLabel())
            getvalue += rangevalue
            self.m_staticText931.SetLabel(str(getvalue))

            # 判断是否是最后一次到这里
            if "100.0" in str(getvalue) or "99.9999" in str(getvalue):
                self.m_button2.Enable(True)
                self.m_button221.Enable(True)


# 列表框双击事件
def listboxsevents(self, event):
    item = event.GetEventObject().GetStringSelection()

    if os.path.isdir(item):
        list1 = []
        lastpath = os.path.join(item, os.pardir)
        abspaths = os.path.abspath(lastpath)
        list1.append(abspaths)
        try:
            sublist = os.listdir(item)
            for i in sublist:
                filepath = os.path.join(item, i)
                list1.append(filepath)
            event.GetEventObject().Set(list1)
            item = list1
        except Exception as e:
            print(str(e))
            pass
    else:
        # print(os.path.abspath(item))
        if "File exise" in item or "://" not in item:
            AsFunction.showtips("Message", "这不是一个有效的文件路径！无法打开！")
        else:
            if os.path.exists(item):
                os.startfile(os.path.abspath(item))
            else:
                AsFunction.exesql("delete", "", "", "DELETE FROM fileinfo WHERE path='%s'" % item)
                AsFunction.showtips("Message", "文件已被删除或文件路径被修改，无法查看文件信息，数据库的信息也已被删除！")


# 列表框点击事件
def listboxsevent(self, event):
    filepath = event.GetEventObject().GetStringSelection()
    if "File exise" in filepath or ":/" not in filepath:
        pass
    else:
        # 判断文件是否存在
        if os.path.exists(filepath):
            try:
                # 返回文件最近修改日期
                mtime = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(os.path.getmtime(filepath)))
                self.m_textCtrl52.SetValue(mtime)

                # 返回文件创建时间
                ctime = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(os.path.getctime(filepath)))
                self.m_textCtrl50.SetValue(ctime)

                # 返回文件最近访问时间
                atime = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(os.path.getatime(filepath)))
                self.m_textCtrl51.SetValue(atime)

                # 返回文件名字
                filename = os.path.basename(filepath)
                self.m_textCtrl47.SetValue(filename)

                # 返回文件类型
                lastname = os.path.splitext(filename)
                filetype = lastname[1]
                self.m_textCtrl49.SetValue(filetype)

                # 返回文件大小
                filesize = os.path.getsize(filepath)
                self.m_textCtrl48.SetValue("{0:.2f}KB {1:.2f}MB".format(filesize / 1024, filesize / 1024 / 1024))

                # 设置文件路径
                self.m_textCtrl46.SetValue(filepath)
                # self.m_staticText12.SetLabel(filepath)
                # self.m_staticText1001.SetLabel(filepath)
            except Exception as e:
                AsFunction.showtips("Message", str(e))
        else:
            user = self.m_textCtrl11.GetValue()
            AsFunction.exesql("delete", "", "", "DELETE FROM fileinfo WHERE path='%s'" % filepath)
            AsFunction.showtips("Message", "文件已被删除或文件路径被修改，无法查看文件信息，数据库的信息也已被删除！")


# 统计数据库信息函数,因为要用到多线程，所以必须放在外部函数中
def Statistics(self, db, cursor):
    self.m_button47.Enable(False)
    # 获取数据库指所有文件总大小
    typelist = ['.txt', '.docx', '.xlsx', '.pptx', '.jpg', '.bmp', '.png', '.gif', '.flv', '.pdf', '.mp3', '.flac',
                '.mp4', '.avi', '.zip', '.rar', '.7z', '.iso', '.exe', '.bat', '.c', '.java', '.py', '.cpp', '.html',
                '.xml']

    datas = AsFunction.exesql("select", "", "", "SELECT SUM(size) FROM fileinfo")
    totalsize = int(datas[0][0])

    self.m_grid2.SetColLabelValue(0, "总数量")
    self.m_grid2.SetColLabelValue(1, "总大小")
    self.m_grid2.SetColLabelValue(2, "总占比")
    # self.m_grid1.SetColLabelValue(3,"A")
    # 分别对每个类型进行返回总和，百分比并设置文本
    j = 0
    for i in range(len(typelist)):
        datas = AsFunction.exesql("select", "", "",
                                  "SELECT COUNT(size) FROM fileinfo WHERE type='%s'" % (typelist[i]))
        # 获取到对应类型文件的总数
        countsize = datas[0][0]
        if datas[0][0]:
            # 如果总和存在，说明有文件，则进一步统计总大小
            datass = AsFunction.exesql("select", "", "",
                                       "SELECT SUM(size) FROM fileinfo WHERE type='%s'" % (typelist[i]))
            typesize = datass[0][0]
            # 列标签
            self.m_grid2.SetRowLabelValue(j, typelist[i])
            # 总数量
            self.m_grid2.SetCellValue(j, 0, str(countsize))
            # 总大小
            self.m_grid2.SetCellValue(j, 1, "{0:.2f}MB".format(typesize / 1024 / 1024))
            # 总占比
            self.m_grid2.SetCellValue(j, 2, "{0:.2f}%".format(typesize / totalsize * 100))
            j += 1
    self.m_grid2.ForceRefresh()
    db.close()
    self.m_button47.Enable(True)


# 笔记界面的刷新功能，为了能在其他函数里使用，就放在外面了
def NoteRefresh(self):
    self.m_listBox5.Clear()
    datas = AsFunction.exesql("select", "", "", "SELECT title FROM note")
    for i in datas:
        self.m_listBox5.Append(i)


# Write界面的刷新事件
def WriteRefresh(self):
    # 先连接本地数据库
    self.m_listBox6.Clear()
    datas = AsFunction.exesql("select", "", "", "SELECT title FROM iread")
    for i in datas:
        self.m_listBox6.Append(i)
    datas = AsFunction.exesql("select", "", "", "SELECT * FROM ireadconfig")
    # 通知文本框
    self.m_textCtrl70.SetValue(str(datas[0][0]))
    # 获取是否展示通知选择框
    display = int(datas[0][1])
    if display == 0:
        self.m_checkBox5.SetValue(False)
    elif display == 1:
        self.m_checkBox5.SetValue(True)

    # 获取状态信息
    statue = int(datas[0][2])
    if statue == 0:
        self.m_checkBox6.SetValue(False)
    elif statue == 1:
        self.m_checkBox6.SetValue(True)

    # 获取服务器维护通知
    self.m_textCtrl71.SetValue(str(datas[0][3]))

    # 获取版本信息
    self.m_textCtrl692.SetValue(str(datas[0][5]))
    self.m_textCtrl682.SetValue(str(datas[0][6]))

    # 获取关于信息
    self.m_textCtrl701.SetValue(str(datas[0][7]))


# 课表保存事件
def TimetableSave(self):
    id21 = self.m_textCtrl95.GetValue()
    if id21 == "":
        AsFunction.showtips("Message", "课表标题为空，无法保存！！请勿保存空值从而覆盖完整课表！")
    else:
        result = AsFunction.sqltest()
        if result == 0:
            AsFunction.showtips("Message", "数据库连接失败！")
        else:
            id1 = self.m_textCtrl751.GetValue()
            id2 = self.m_textCtrl80.GetValue()
            id3 = self.m_textCtrl85.GetValue()
            id4 = self.m_textCtrl90.GetValue()
            id5 = self.m_textCtrl761.GetValue()
            id6 = self.m_textCtrl81.GetValue()
            id7 = self.m_textCtrl86.GetValue()
            id8 = self.m_textCtrl91.GetValue()
            id9 = self.m_textCtrl771.GetValue()
            id10 = self.m_textCtrl82.GetValue()
            id11 = self.m_textCtrl87.GetValue()
            id12 = self.m_textCtrl92.GetValue()
            id13 = self.m_textCtrl78.GetValue()
            id14 = self.m_textCtrl83.GetValue()
            id15 = self.m_textCtrl88.GetValue()
            id16 = self.m_textCtrl93.GetValue()
            id17 = self.m_textCtrl79.GetValue()
            id18 = self.m_textCtrl84.GetValue()
            id19 = self.m_textCtrl89.GetValue()
            id20 = self.m_textCtrl94.GetValue()

            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id1, 1)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id2, 2)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id3, 3)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id4, 4)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id5, 5)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id6, 6)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id7, 7)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id8, 8)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id9, 9)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id10, 10)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id11, 11)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id12, 12)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id13, 13)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id14, 14)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id15, 15)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id16, 16)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id17, 17)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id18, 18)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id19, 19)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id20, 20)
            AsFunction.exesql("update", "", "", sql)
            sql = "UPDATE timetable SET value='%s' WHERE id=%s" % (id21, 21)
            AsFunction.exesql("update", "", "", sql)

            AsFunction.showtips("Message", id21 + "\n课表保存成功！")


# 课表刷新事件
def TimetableRefresh(self):
    datas = AsFunction.exesql("select", "", "", "SELECT value from timetable")
    self.m_textCtrl751.SetValue(datas[0][0])
    self.m_textCtrl80.SetValue(datas[1][0])
    self.m_textCtrl85.SetValue(datas[2][0])
    self.m_textCtrl90.SetValue(datas[3][0])
    self.m_textCtrl761.SetValue(datas[4][0])
    self.m_textCtrl81.SetValue(datas[5][0])
    self.m_textCtrl86.SetValue(datas[6][0])
    self.m_textCtrl91.SetValue(datas[7][0])
    self.m_textCtrl771.SetValue(datas[8][0])
    self.m_textCtrl82.SetValue(datas[9][0])
    self.m_textCtrl87.SetValue(datas[10][0])
    self.m_textCtrl92.SetValue(datas[11][0])
    self.m_textCtrl78.SetValue(datas[12][0])
    self.m_textCtrl83.SetValue(datas[13][0])
    self.m_textCtrl88.SetValue(datas[14][0])
    self.m_textCtrl93.SetValue(datas[15][0])
    self.m_textCtrl79.SetValue(datas[16][0])
    self.m_textCtrl84.SetValue(datas[17][0])
    self.m_textCtrl89.SetValue(datas[18][0])
    self.m_textCtrl94.SetValue(datas[19][0])
    self.m_textCtrl95.SetValue(datas[20][0])


# Write界面的Comment刷新事件
def WriteCommentRefresh(self):
    db, cursor, message = AsFunction.linktosersql()
    if message != "1":
        AsFunction.showtips("Message", "服务器数据库连接失败！")
        db.close()
    else:
        try:
            self.m_listBox7.Clear()
            self.m_listBox8.Clear()
            self.m_listBox9.Clear()
            sqlinsert = "SELECT DISTINCT ip FROM ireadcomment"
            cursor.execute(sqlinsert)
            datas = cursor.fetchall()
            for i in datas:
                self.m_listBox7.Append(i)

            sqlinsert = "SELECT ip FROM ircdenylist"
            cursor.execute(sqlinsert)
            datas = cursor.fetchall()
            for i in datas:
                self.m_listBox8.Append(i)

            db.close()
        except Exception as e:
            AsFunction.showtips("Message", "服务器数据库：" + str(e))
            db.close()


# 读取留言墙的删除事件
def WriteMeWaDelete(self):
    ctimes = self.m_staticText135.GetLabel()
    values = self.m_staticText136.GetLabel()
    if ctimes == "" or values == "":
        AsFunction.showtips("Message", "请选择留言！")
    else:
        db, cursor, message = AsFunction.linktosersql()
        if message != "1":
            AsFunction.showtips("Message", "服务器数据库连接失败！")
        else:
            values = escape_string(values)
            sql = ("DELETE FROM ireadmsg WHERE time='%s' AND value='%s'" % (ctimes, values))
            try:
                cursor.execute(sql)
                db.commit()
                AsFunction.showtips("Message", values + "\n此留言已删除！")
                db.close()
                self.m_staticText135.SetLabel("")
                self.m_staticText136.SetLabel("")
            except Exception as e:
                AsFunction.showtips("Message", str(e))
                db.close()


# 主界面的统计刷新事件
def StastacisRefresh(self):
    user = self.m_textCtrl11.GetValue()
    # 读取数据库中保存的已经读取过的整体文件信息
    self.m_grid2.SetColLabelValue(0, "总数量")
    self.m_grid2.SetColLabelValue(1, "总大小")
    self.m_grid2.SetColLabelValue(2, "总占比")

    datas = AsFunction.exesql("select", "", "", "SELECT statinfo FROM adminiconfig")
    result = statosql(str(datas[0][0]))
    # result = escape_string(result)
    j = 0
    for i in result:
        self.m_grid2.SetRowLabelValue(j, i[0])
        self.m_grid2.SetCellValue(j, 0, i[1])
        self.m_grid2.SetCellValue(j, 1, i[2])
        self.m_grid2.SetCellValue(j, 2, i[3])
        j += 1
    self.m_grid2.ForceRefresh()

    # 最近文件刷新
    top = self.m_comboBox11.GetStringSelection()
    datas = AsFunction.exesql("select", "", "",
                              "SELECT name,size,time,path FROM fileinfo ORDER BY time DESC LIMIT %s" % (int(top)))

    self.m_listCtrl4.ClearAll()
    self.m_listCtrl4.InsertColumn(0, "Name", width=200)
    self.m_listCtrl4.InsertColumn(1, "Size", width=80)
    self.m_listCtrl4.InsertColumn(2, "MTime", width=120)
    self.m_listCtrl4.InsertColumn(3, "Path", width=300)
    idx = 0
    for i in datas:
        index = self.m_listCtrl4.InsertStringItem(idx, str(i[0]))
        self.m_listCtrl4.SetStringItem(index, 1, "{0:.2f}MB".format(int(i[1]) / 1024 / 1024))
        self.m_listCtrl4.SetStringItem(index, 2, str(i[2]))
        self.m_listCtrl4.SetStringItem(index, 3, str(i[3]))
        idx += 1


# 所有文件统计信息转换函数，将常用的信息通过一定的转化转变成数据库可存取的格式，然后用此函数
# 进行转化成程序可读的字符
def statosql(value):
    sqldata = []
    index = value.splitlines()
    for i in index:
        indexs = i.split("@")
        sqldata.append(indexs)
    return sqldata


# 计划界面的刷新事件
def PlanRefresh(self):
    datas = AsFunction.exesql("select", "", "",
                              "SELECT name,plan,startdate,todate,statue,remarks FROM plantodo ORDER "
                              "BY startdaten DESC")
    self.m_listCtrl3.ClearAll()
    self.m_listCtrl3.InsertColumn(0, "Name", width=150)
    self.m_listCtrl3.InsertColumn(1, "Plan", width=200)
    self.m_listCtrl3.InsertColumn(2, "StartDate", width=200)
    self.m_listCtrl3.InsertColumn(3, "DeadLine", width=200)
    self.m_listCtrl3.InsertColumn(4, "Statue", width=100)
    self.m_listCtrl3.InsertColumn(5, "Remarks", width=200)

    idx = 0
    for i in datas:
        index = self.m_listCtrl3.InsertStringItem(idx, str(i[0]))
        self.m_listCtrl3.SetStringItem(index, 1, str(i[1]))
        self.m_listCtrl3.SetStringItem(index, 2, str(i[2]))
        self.m_listCtrl3.SetStringItem(index, 3, str(i[3]))
        self.m_listCtrl3.SetStringItem(index, 4, str(i[4]))
        self.m_listCtrl3.SetStringItem(index, 5, str(i[5]))
        idx += 1
    ctime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    self.m_staticText121.SetLabel("上次刷新：" + ctime)


# Write界面的Load的刷新事件
def WriteLoadRefresh(self):
    db, cursor, message = AsFunction.linktosersql()
    if message != "1":
        AsFunction.showtips("Message", "服务器数据库连接失败！")
        db.close()
    else:
        try:
            sqlinsert = "SELECT ip,loadnum,lastload FROM ireadload ORDER BY lastload DESC"
            cursor.execute(sqlinsert)
            datas = cursor.fetchall()
            self.m_listCtrl1.ClearAll()
            self.m_listCtrl1.InsertColumn(0, "IP", width=150)
            self.m_listCtrl1.InsertColumn(1, "LoadNum", width=100)
            self.m_listCtrl1.InsertColumn(2, "LastLoad", width=300)
            idx = 0
            for i in datas:
                index = self.m_listCtrl1.InsertStringItem(idx, str(i[0]))
                self.m_listCtrl1.SetStringItem(index, 1, str(i[1]))
                self.m_listCtrl1.SetStringItem(index, 2, str(i[2]))
                idx += 1
            db.close()
            ctime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            self.m_staticText1201.SetLabel("上次刷新：" + ctime)
        except Exception as e:
            AsFunction.showtips("Message", "服务器数据库：" + str(e))
            db.close()


# 顶部刷新条事件，为了让其他功能调用，就放在外面了
def menuitem1s(self, event):
    choice = self.m_notebook1.GetSelection()
    # 0主页，1搜索页，2计划页，3笔记页，4Write页，5数学页

    # 新版本2022年7月10日，08点25分
    # 0主页， 1搜索页， 2功能页， 3，Write页，4MySQL
    # 5时间表，6配置
    # 在功能页下面
    # 0发送邮件，1服务器，2密码，3计划，4笔记，5百科库
    if choice == 0:
        StastacisRefresh(self)
    elif choice == 1:
        pass
    elif choice == 2:
        choice = self.m_listbook4.GetSelection()
        if choice == 0:
            pass
        elif choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            PlanRefresh(self)
        elif choice == 4:
            NoteRefresh(self)
        elif choice == 5:
            pass
    elif choice == 3:
        choice = self.m_listbook3.GetSelection()
        if choice == 0 or choice == 1:
            WriteRefresh(self)
        elif choice == 2:
            WriteCommentRefresh(self)
        elif choice == 3:
            WriteLoadRefresh(self)
    elif choice == 4:
        pass
    elif choice == 5:
        TimetableRefresh(self)
    elif choice == 6:
        pass


# 搜索页面的打开文件路径事件
def SearchOpenPath(self, event):
    filepath = self.m_textCtrl77.GetValue()

    if ":/" not in filepath:
        AsFunction.showtips("Message", "请选择文件，或非目录！")
    else:
        # print(filepath)
        filepath = os.path.dirname(filepath)
        filepath = filepath + "//"
        # print(filepath)
        os.startfile(filepath)


# 主界面的打开文件路径事件
def StatisticsOpenPath(self, event):
    filepath = self.m_textCtrl46.GetValue()
    if "File exise" in filepath or ":/" not in filepath:
        AsFunction.showtips("Message", "请选择文件！")
    else:
        # print(filepath)
        filepath = os.path.dirname(filepath)
        filepath = filepath + "//"
        # print(filepath)
        os.startfile(filepath)


# Plan界面的保存/修改事件
def PlanSave(self, event):
    name = self.m_textCtrl711.GetValue()
    plan = self.m_textCtrl721.GetValue()
    startdate = self.m_textCtrl731.GetValue()
    todate = self.m_textCtrl741.GetValue()
    statue = self.m_choice3.GetStringSelection()
    remarks = self.m_textCtrl76.GetValue()
    if name == "" or plan == "" or todate == "":
        AsFunction.showtips("Message", "请补全新计划内容！")
    else:
        results = AsFunction.exesql("select", "", "", "select name from plantodo where name='%s'" % name)
        # 如果存在
        if str(results) != "()":
            sql = "UPDATE plantodo SET name='%s',plan='%s',todate='%s',\
            statue='%s',remarks='%s' WHERE startdate='%s'" % (
                name, plan, todate, statue, remarks, startdate)
            AsFunction.exesql("update", "", "", sql)
            AsFunction.showtips("Message", name + "\n本地数据库计划已修改！")
            menuitem1s(self, event)
        else:
            startdate = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            startdaten = int(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
            sql = "INSERT INTO plantodo (name,plan,startdate,startdaten,todate,\
            statue,remarks) VALUES ('%s','%s','%s',%s,'%s','%s','%s')" % (
                name, plan, startdate, startdaten, todate, statue, remarks)
            AsFunction.exesql("insert", "", "", sql)
            AsFunction.showtips("Message", name + "\n本地数据库新计划已保存！")


# 笔记界面的保存事件
def NoteSave(self, event):
    title = self.m_textCtrl521.GetValue()
    if title == "":
        AsFunction.showtips("Message", "标题为空，保存失败")
    else:
        nowtime = self.m_staticText901.GetLabel()
        if nowtime == "000000000000":
            AsFunction.showtips("Message", "你还没有选择笔记！")
        else:
            body = self.m_textCtrl531.GetValue()
            # 转义字符
            body = escape_string(body)

            fontsize = self.m_slider1.GetValue()
            sql = "UPDATE note SET title='%s',body='%s',fontsize=%s WHERE time=%s" % (
                title, str(body), fontsize, nowtime)
            AsFunction.exesql("update", title + "\n笔记已保存！", "", sql)
            now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            self.m_staticText89.SetLabel(str(now))
            # AsFunction.showtips("Message", title + "\n笔记已保存！")
            menuitem1s(self, event)


# Write界面的配置保存事件
def WriteiConfigSave(self, event):
    notification = self.m_textCtrl70.GetValue()
    display = 0
    statue = 0
    if self.m_checkBox5.GetValue():
        display = 1
    else:
        display = 0
    if self.m_checkBox6.GetValue():
        statue = 1
    else:
        statue = 0
    version = self.m_textCtrl692.GetValue()
    versionotice = self.m_textCtrl682.GetValue()

    sernotice = self.m_textCtrl71.GetValue()

    about = self.m_textCtrl701.GetValue()
    if notification == "" or sernotice == "":
        AsFunction.showtips("Message", "通知公告和服务器通知不能为空！")
    else:
        # 连接本地数据库
        # 转义字符
        # 为了达到原版的效果，通知和服务器通知将不再转义
        sql = "UPDATE ireadconfig SET notification='%s',display=%s,statue=%s,\
        sernotice='%s',version='%s',versionotice='%s',about='%s' WHERE type=1" % (
            notification, display, statue, sernotice, version, versionotice, about)
        AsFunction.exesql("update", "本地数据库ireadconfig已保存！", "", sql)
        # AsFunction.showtips("Message", "本地数据库ireadconfig已保存！")
        # 连接服务器数据库
        db, cursor, message = AsFunction.linktosersql()
        if message != "1":
            AsFunction.showtips("Message", "服务器数据库连接失败！")
            db.close()
        else:
            try:
                # 转义字符
                # 为了达到原版的效果，通知和服务器通知将不再转义
                sql = "UPDATE ireadconfig SET notification='%s',display=%s,statue=%s,sernotice='%s',\
                version='%s',versionotice='%s',about='%s' WHERE type=1" % (
                    notification, display, statue, sernotice, version, versionotice, about)
                cursor.execute(sql)
                db.commit()
                AsFunction.showtips("Message", "服务器数据库ireadconfig已保存！")
                db.close()
            except Exception as e:
                AsFunction.showtips("Message", str(e))
                db.close()


# Write界面的保存事件
def WriteSave(self, event):
    title = self.m_textCtrl681.GetValue()
    if title == "":
        AsFunction.showtips("Message", "文章标题不能为空！")
    else:
        ctime = self.m_staticText113.GetLabel()
        if ctime == "000000000000":
            AsFunction.showtips("Message", "你还没有选择文章！")
        else:
            readtype = 0
            title = escape_string(title)
            body = self.m_textCtrl671.GetValue()
            body = escape_string(body)
            if self.m_checkBox4.GetValue():
                readtype = 1
            else:
                readtype = 0
            readnotice = self.m_textCtrl691.GetValue()
            label = self.m_textCtrl72.GetValue()
            mtime = int(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
            ctime = self.m_staticText112.GetLabel()
            # 上传本地数据库
            sql = "UPDATE iread SET title='%s',body='%s',mtime=%s,readtype=%s,\
            readnotice='%s',label='%s' WHERE ctime='%s'" % (
                title, body, mtime, readtype, readnotice, label, ctime)
            AsFunction.exesql("update", title + "\n本地数据库文章已保存！", "", sql)
            # AsFunction.showtips("Message", title + "\n本地数据库文章已保存！")
            menuitem1s(self, event)

            db, cursor, message = AsFunction.linktosersql()
            if message != "1":
                AsFunction.showtips("Message", "服务器数据库连接失败！")
                db.close()
            else:
                try:
                    sql = "UPDATE iread SET title='%s',body='%s',mtime=%s,readtype=%s,\
                    readnotice='%s',label='%s' WHERE ctime='%s'" % (
                        title, body, mtime, readtype, readnotice, label, ctime)
                    cursor.execute(sql)
                    db.commit()
                    AsFunction.showtips("Message", title + "\n服务器数据库文章已保存！")
                    db.close()
                except Exception as e:
                    AsFunction.showtips("Message", str(e))
                    db.close()


# Write添加新文章事件
def WriteNew(self, event):
    title = self.m_textCtrl681.GetValue()
    if title == "":
        AsFunction.showtips("Message", "新文章标题不能为空！")
    else:
        title = escape_string(title)
        results = AsFunction.exesql("select", "", "", "select title from iread where title='%s'" % title)
        if str(results) != "()":
            AsFunction.showtips("Message", "文章标题已存在于本地数据库中，无法创建，请重新输入文章名字！")
        else:
            readtype = 0
            body = self.m_textCtrl671.GetValue()
            body = escape_string(body)
            if self.m_checkBox4.GetValue():
                readtype = 1
            else:
                readtype = 0
            readnotice = self.m_textCtrl691.GetValue()
            label = self.m_textCtrl72.GetValue()
            ctime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            mtime = int(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
            # 上传本地数据库
            sql = "INSERT INTO iread (title,body,ctime,mtime,readtype,readnotice,\
                label,type,readnum) VALUES ('%s','%s','%s',%s,%s,'%s','%s',1,0)" % (
                title, body, ctime, mtime, readtype, readnotice, label)
            AsFunction.exesql("insert", title + "\n本地数据库新文章已保存！", "", sql)

            # AsFunction.showtips("Message", title + "\n本地数据库新文章已保存！")
            menuitem1s(self, event)

            db, cursor, message = AsFunction.linktosersql()
            if message != "1":
                AsFunction.showtips("Message", "服务器数据库连接失败！")
                db.close()
            else:
                try:
                    sql = "INSERT INTO iread (title,body,ctime,mtime,readtype,readnotice,\
                        label,type,readnum) VALUES ('%s','%s','%s',%s,%s,'%s','%s',1,0)" % (
                        title, body, ctime, mtime, readtype, readnotice, label)
                    cursor.execute(sql)
                    db.commit()
                    db.close()
                    AsFunction.showtips("Message", title + "\n服务器数据库新文章已保存！")
                    # db.close()
                except Exception as e:
                    AsFunction.showtips("Message", str(e))
                    db.close()


# 笔记界面的创建笔记事件
def NoteNew(self, event):
    now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    fontsize = self.m_slider1.GetValue()

    class mydia(AsDialog.MyDialog2):
        def button32(self, event):
            title = self.m_textCtrl55.GetValue()
            if title == "":
                AsFunction.showtips("Error", "标题不能为空！")
            else:
                sqlinsert = "INSERT INTO note (title,body,fontsize,time) VALUES ('%s','%s',%s,%s)" % (
                    title, "", int(fontsize), int(now))
                AsFunction.exesql("delete", "文章\"{0}\"添加成功！".format(title), "", sqlinsert)
                self.Destroy()

    dia = mydia(None, "新增文章", "添加新的文章在Note里面", "")
    dia.ShowModal()
    menuitem1s(self, event)


# Note界面的删除事件
def NoteDelete(self, event):
    title = self.m_listBox5.GetStringSelection()
    if title == "":
        AsFunction.showtips("Message", "没有选择笔记！")
    else:
        value = self.m_textCtrl531.GetValue()

        class mydia(AsDialog.MyDialog2):
            def button32(self, event):
                sqlinsert = "DELETE FROM note WHERE title='%s'" % title
                AsFunction.exesql("delete", title + "\n此笔记已经删除！", "", sqlinsert)
                self.Destroy()

        dia = mydia(None, "删除确认", "删除\"{0}\"?".format(title), value)
        dia.ShowModal()
        menuitem1s(self, event)
        # 初始化标题栏和内容栏
        self.m_textCtrl521.SetValue("")
        self.m_textCtrl531.SetValue("")
        """
        nowtime = self.m_staticText901.GetLabel()
        if nowtime != "000000000000":
            self.m_staticText901.SetLabel("000000000000")
            AsFunction.showtips("Message", "笔记属于重要文件，为防止误触，请再次点击以确认删除此笔记！")
        else:
            sqlinsert = "DELETE FROM note WHERE title='%s'" % title
            AsFunction.exesql(self, "delete", title + "\n此笔记已经删除！", "", sqlinsert)
            # AsFunction.showtips("Message", title + "\n此笔记已经删除！")
            menuitem1s(self, event)
            # 初始化标题栏和内容栏
            self.m_textCtrl521.SetValue("")
            self.m_textCtrl531.SetValue("")
        """


# Write界面的删除事件
def WriteDelete(self, event):
    title = self.m_listBox6.GetStringSelection()
    if title == "":
        AsFunction.showtips("Message", "请先选择文章！")
    else:
        nowtime = self.m_staticText113.GetLabel()
        if nowtime != "000000000000":
            self.m_staticText113.SetLabel("000000000000")
            AsFunction.showtips("Message", "请再次点击以确认删除此文件！")
        else:
            sqlinsert = "DELETE FROM iread WHERE title='%s'" % title
            AsFunction.exesql("delete", title + "\n此文章在本地数据库已经删除！", "", sqlinsert)
            # AsFunction.showtips("Message", title + "\n此文章在本地数据库已经删除！")
            menuitem1s(self, event)
            # 初始化标题栏和内容栏
            self.m_textCtrl681.SetValue("")
            self.m_textCtrl671.SetValue("")
            # 连接服务器数据库
            db, cursor, message = AsFunction.linktosersql()
            if message != "1":
                AsFunction.showtips("Message", "服务器数据库连接失败！")
                db.close()
            else:
                try:
                    sqlinsert = "DELETE FROM iread WHERE title='%s'" % title
                    cursor.execute(sqlinsert)
                    db.commit()
                    AsFunction.showtips("Message", title + "\n此文章在服务器数据库已经删除！")
                    db.close()
                except Exception as e:
                    AsFunction.showtips("Message", "在服务器数据库中：" + str(e))
                    db.close()


# Plan界面的删除事件
def PlanDelete(self, event):
    startdate = self.m_textCtrl731.GetValue()
    if startdate == "":
        AsFunction.showtips("Message", "没有选择计划！")
    else:
        title = self.m_textCtrl711.GetValue()
        sqlinsert = "DELETE FROM plantodo WHERE startdate='%s'" % startdate
        AsFunction.exesql("delete", title + "\n此计划已经删除！", "", sqlinsert)
        # title = self.m_textCtrl711.GetValue()
        # AsFunction.showtips("Message", title + "\n此计划已经删除！")
        # 刷新当前状态
        menuitem1s(self, event)
        # 初始化标题栏和内容栏
        self.m_textCtrl711.SetValue("")
        self.m_textCtrl731.SetValue("")
        self.m_textCtrl741.SetValue("")
        self.m_textCtrl721.SetValue("")
        self.m_textCtrl76.SetValue("")


# 更新文件信息
def UpdateFileInfo(self):
    user = self.m_textCtrl11.GetValue()
    sql = "SELECT COUNT(path) FROM fileinfo"
    datas = AsFunction.exesql("select", "", "", sql)
    total = datas[0][0]
    self.m_staticText83.SetLabel(str(total))
    self.m_gauge2.SetRange(int(total))
    # 初始化进度条
    self.m_gauge2.SetValue(0)
    self.m_staticText101.SetLabel("0")
    self.m_button221.Enable(False)
    self.m_button2.Enable(False)

    sql = "SELECT path FROM fileinfo"
    datas = AsFunction.exesql("select", "", "", sql)
    # print(datas)
    for i in datas:
        # 文件上传操作结束后进行进度条的改变
        guagecurrentvalue = self.m_gauge2.GetValue()
        guagecurrentvalue += 1
        # 进度条的值加1
        self.m_gauge2.SetValue(guagecurrentvalue)
        # 标签的值也加1
        self.m_staticText101.SetLabel(str(guagecurrentvalue))
        if os.path.exists(i[0]):
            now = time.strftime('%Y%m%d%H%M%S', time.localtime(os.path.getmtime(i[0])))
            sqlinsert = "UPDATE fileinfo SET time=%s WHERE path='%s'" % (int(now), i[0])
            AsFunction.exesql("update", "", "", sqlinsert)
        else:
            AsFunction.exesql("delete", "", "", "DELETE FROM fileinfo WHERE path='%s'" % (i[0]))

    # 获取数据库指所有文件总大小
    typelist = ['.txt', '.docx', '.xlsx', '.pptx', '.jpg', '.bmp', '.png', '.gif', '.flv', '.pdf', '.mp3',
                '.flac', '.mp4', '.avi', '.zip', '.rar', '.7z', '.iso', '.exe', '.bat', '.c', '.java', '.py',
                '.cpp', '.html', '.xml']

    datas = AsFunction.exesql("select", "", "", "SELECT SUM(size) FROM fileinfo")
    totalsize = int(datas[0][0])

    j = 0
    value = ""
    for i in range(len(typelist)):
        sqlinsert = ("SELECT COUNT(size) FROM fileinfo WHERE type='%s'" % (typelist[i]))
        datas = AsFunction.exesql("select", "", "", sqlinsert)
        # 获取到对应类型文件的总数
        countsize = datas[0][0]
        if datas[0][0]:
            # 如果总和存在，说明有文件，则进一步统计总大小
            sqlinsert = ("SELECT SUM(size) FROM fileinfo WHERE type='%s'" % (typelist[i]))
            datass = AsFunction.exesql("select", "", "", sqlinsert)
            typesize = datass[0][0]
            # 列标签
            # 总数量
            # 总大小
            # 总占比
            # 此value值将获取到的结果转化为可存储于数据库的格式，并通过我定义的函数来转化为程序可读的格式
            value += str(typelist[i]) + "@" + str(countsize) + "@" + "{0:.2f}MB".format(
                typesize / 1024 / 1024) + "@" + "{0:.2f}%".format(typesize / totalsize * 100)
            value += "\n"
            j += 1

    value = escape_string(value)

    sqlinsert = "UPDATE adminiconfig SET statinfo='%s' WHERE type=1" % value
    AsFunction.exesql("update", "", "", sqlinsert)

    self.m_button221.Enable(True)
    self.m_button2.Enable(True)


# 窗体主类
class myframe(AsDesktop.MyFrame1):

    def button321(self, event):
        # 在后面添加列
        self.m_grid21.AppendCols(7)
        # 在下面添加行
        self.m_grid21.AppendRows(4)

        # self.m_grid21.
        self.m_grid21.ForceRefresh()


    # futures = pool.submit(startmons,self)
    def startmon(self):
        startmons(self)

    # 项目条刷新事件
    def menuitem1(self, event):
        menuitem1s(self, event)

    # 项目条清空事件
    def menuitem2(self, event):
        choise = self.m_notebook1.GetSelection()
        # 0主页，1搜索页，2计划页，3笔记页，4Write页，5数学页
        if choise == 0:
            # self.m_listBox10.Clear()
            # self.m_listBox11.Clear()
            self.m_grid2.ClearGrid()
            self.m_textCtrl46.Clear()
            self.m_textCtrl47.Clear()
            self.m_textCtrl48.Clear()
            self.m_textCtrl49.Clear()
            self.m_textCtrl50.Clear()
            self.m_textCtrl51.Clear()
            self.m_textCtrl52.Clear()
            self.m_dirPicker1.SetPath("")
        elif choise == 1:
            self.m_listCtrl2.ClearAll()
            self.m_textCtrl75.Clear()
            self.m_textCtrl77.Clear()
        elif choise == 2:
            self.m_listCtrl3.ClearAll()
            self.m_textCtrl711.Clear()
            self.m_textCtrl721.Clear()
            self.m_textCtrl731.Clear()
            self.m_textCtrl741.Clear()
            self.m_textCtrl76.Clear()
        elif choise == 3:
            title = self.m_textCtrl521.GetValue()
            body = self.m_textCtrl531.GetValue()
            AsFunction.showtips("Message", "标题和内容将会被清空！若是手误请复制下方获取到的内容，确定后将会永久清除！\n" + title + "\n" + body)
            self.m_textCtrl521.Clear()
            self.m_textCtrl531.Clear()
        elif choise == 4:
            choise = self.m_listbook3.GetSelection()
            if choise == 0 or choise == 1:
                title = self.m_textCtrl681.GetValue()
                body = self.m_textCtrl671.GetValue()

                AsFunction.showtips("Message", "标题和内容将会被清空！若是手误请复制下方获取到的内容，确定后将会永久清除！\n" + title + "\n" + body)
                self.m_textCtrl681.Clear()
                self.m_textCtrl671.Clear()
                self.m_textCtrl691.Clear()
                self.m_textCtrl72.Clear()
            elif choise == 2:
                pass
            elif choise == 3:
                pass
        elif choise == 5:
            self.m_textCtrl57.SetValue("")
            sel = self.m_listbook21.GetSelection()
            if sel == 0:
                self.m_textCtrl58.SetValue("")
            elif sel == 1:
                self.m_textCtrl61.SetValue("")
            elif sel == 2:
                self.m_textCtrl63.SetValue("")
            elif sel == 3:
                self.m_textCtrl67.SetValue("")
                self.m_textCtrl65.SetValue("")
                self.m_textCtrl66.SetValue("")
            elif sel == 4:
                pass
                # self.m_textCtrl58.SetValue("")
            elif sel == 5:
                self.m_textCtrl69.SetValue("")
            elif sel == 6:
                pass

    # 项目条打开路径事件
    def menuitem3(self, event):
        choise = self.m_notebook1.GetSelection()
        # 0主页，1搜索页，2计划页，3笔记页，4Write页，5数学页
        if choise == 0:
            StatisticsOpenPath(self, event)
        elif choise == 1:
            SearchOpenPath(self, event)
        elif choise == 2:
            pass
        elif choise == 3:
            pass
        elif choise == 4:
            choise = self.m_listbook3.GetSelection()
            if choise == 0 or choise == 1:
                pass
            elif choise == 2:
                pass
            elif choise == 3:
                pass
        elif choise == 5:
            pass

    # 项目条保存事件
    def menuitem4(self, event):
        choice = self.m_notebook1.GetSelection()
        # 0主页，1搜索页，2计划页，3笔记页，4Write页，5数学页

        # 新版本2022年7月10日，08点25分
        # 0主页， 1搜索页， 2功能页， 3，Write页，4MySQL
        # 5时间表，6配置
        # 在功能页下面
        # 0发送邮件，1服务器，2密码，3计划，4笔记，5百科库
        if choice == 0:
            # 主界面
            pass
        elif choice == 1:
            # 搜索界面
            pass
        elif choice == 2:
            # 功能界面
            choice = self.m_listbook4.GetSelection()
            if choice == 0:
                # 功能界面的发送邮件
                pass
            elif choice == 1:
                # 功能界面的服务器
                pass
            elif choice == 2:
                # 功能界面的密码
                pass
            elif choice == 3:
                # 功能界面的计划
                PlanSave(self, event)
            elif choice == 4:
                # 功能界面的笔记
                NoteSave(self, event)
            elif choice == 5:
                # 功能界面的百科库
                pass
        elif choice == 3:
            # Write界面
            choice = self.m_listbook3.GetSelection()
            if choice == 0:
                # Write界面的iRead
                WriteSave(self, event)
            elif choice == 1:
                # Write界面的iConfig
                WriteiConfigSave(self, event)
            elif choice == 2:
                # Write界面的评论
                pass
            elif choice == 3:
                # Write界面的登录次数统计
                pass
            elif choice == 4:
                # Write界面的留言墙
                pass
        elif choice == 4:
            # MySQL界面
            pass
        elif choice == 5:
            # 时间表
            TimetableSave(self)
        elif choice == 6:
            # 配置页面
            pass

    # 项目条New事件
    def menuitem5(self, event):
        choice = self.m_notebook1.GetSelection()
        # 新版本2022年7月10日，08点25分
        # 0主页， 1搜索页， 2功能页， 3，Write页，4MySQL
        # 5时间表，6配置
        # 在功能页下面
        # 0发送邮件，1服务器，2密码，3计划，4笔记，5百科库
        if choice == 0:
            # 主界面
            pass
        elif choice == 1:
            # 搜索界面
            pass
        elif choice == 2:
            # 功能界面
            choice = self.m_listbook4.GetSelection()
            if choice == 0:
                # 功能界面的发送邮件
                pass
            elif choice == 1:
                # 功能界面的服务器
                pass
            elif choice == 2:
                # 功能界面的密码
                pass
            elif choice == 3:
                # 功能界面的计划
                PlanSave(self, event)
            elif choice == 4:
                # 功能界面的笔记
                NoteNew(self, event)
            elif choice == 5:
                # 功能界面的百科库
                pass
        elif choice == 3:
            # Write界面
            choice = self.m_listbook3.GetSelection()
            if choice == 0:
                # Write界面的iRead
                WriteNew(self, event)
            elif choice == 1:
                pass
                # Write界面的iConfig
            elif choice == 2:
                # Write界面的评论
                pass
            elif choice == 3:
                # Write界面的登录次数统计
                pass
            elif choice == 4:
                # Write界面的留言墙
                pass
        elif choice == 4:
            # MySQL界面
            pass
        elif choice == 5:
            # 时间表
            pass
        elif choice == 6:
            # 配置页面
            pass

    # 项目条Delete事件
    def menuitem6(self, event):
        choice = self.m_notebook1.GetSelection()
        # 0主页，1搜索页，2计划页，3笔记页，4Write页，5数学页

        # 新版本2022年7月10日，08点25分
        # 0主页， 1搜索页， 2功能页， 3，Write页，4MySQL
        # 5时间表，6配置
        # 在功能页下面
        # 0发送邮件，1服务器，2密码，3计划，4笔记，5百科库
        if choice == 0:
            # 主界面
            pass
        elif choice == 1:
            # 搜索界面
            pass
        elif choice == 2:
            # 功能界面
            choice = self.m_listbook4.GetSelection()
            if choice == 0:
                # 功能界面的发送邮件
                pass
            elif choice == 1:
                # 功能界面的服务器
                pass
            elif choice == 2:
                # 功能界面的密码
                pass
            elif choice == 3:
                # 功能界面的计划
                PlanDelete(self, event)
            elif choice == 4:
                # 功能界面的笔记
                NoteDelete(self, event)
            elif choice == 5:
                # 功能界面的百科库
                pass
        elif choice == 3:
            # Write界面
            choice = self.m_listbook3.GetSelection()
            if choice == 0:
                # Write界面的iRead
                WriteDelete(self, event)
            elif choice == 1:
                # Write界面的iConfig
                pass
            elif choice == 2:
                # Write界面的评论
                pass
            elif choice == 3:
                # Write界面的登录次数统计
                pass
            elif choice == 4:
                WriteMeWaDelete(self)
                # Write界面的留言墙
        elif choice == 4:
            # MySQL界面
            pass
        elif choice == 5:
            # 时间表
            pass
        elif choice == 6:
            # 配置页面
            pass

    # 项目条打开Windows事件
    def menuitem7(self, event):
        os.system("taskmgr")

    def menuitem8(self, event):
        os.system("cmd")

    def menuitem9(self, event):
        os.system("explorer")

    def menuitem10(self, event):
        value = self.m_staticText1182.GetLabel()

        AsFunction.showtips("Message", value)

    # 列表框点击自动刷新
    def onlistbookpagechanged3(self, event):
        menuitem1s(self, event)

    def onnotebookpagechanged1(self, event):
        menuitem1s(self, event)

    def onlistbookpagechanged4(self, event):
        menuitem1s(self, event)

    # 留言墙列表点击事件
    def onlistitemselected5(self, event):
        index = event.GetIndex()
        name = event.GetEventObject().GetItem(index, 2)
        ctime = name.GetText()
        name = event.GetEventObject().GetItem(index, 3)
        value = name.GetText()
        self.m_staticText135.SetLabel(ctime)
        self.m_staticText136.SetLabel(value)

    # 搜索引擎文本框
    def textCtrl75(self, event):
        # limit = self.m_comboBox1.GetStringSelection()
        AsFunction.supersearch(self)

    # 多列表点击事件
    def onlistitenactived2(self, event):
        index = event.GetIndex()
        name = event.GetEventObject().GetItem(index, 4)
        names = name.GetText()
        if os.path.isdir(names):
            pass
        else:
            try:
                os.startfile(names)
            except Exception as e:
                sql = ("DELETE FROM fileinfo WHERE path='%s'" % names)
                AsFunction.exesql("delete", "", "", sql)
                AsFunction.showtips("Message", "文件已被删除或文件路径被修改，无法查看文件信息，数据库的信息也已被删除！")
                menuitem1s(self, event)

    def onlistitemactivated4(self, event):
        index = event.GetIndex()
        name = event.GetEventObject().GetItem(index, 3)
        names = name.GetText()
        if os.path.isdir(names):
            pass
        else:
            try:
                os.startfile(names)
            except Exception as e:
                sql = ("DELETE FROM fileinfo WHERE path='%s'" % names)
                AsFunction.exesql("delete", "", "", sql)
                AsFunction.showtips("Message", str(e) + "文件已被删除或文件路径被修改，无法查看文件信息，数据库的信息也已被删除！")
                menuitem1s(self, event)

    def onlistitemselected4(self, event):
        index = event.GetIndex()
        name = event.GetEventObject().GetItem(index, 3)
        filepath = name.GetText()

        if "File exise" in filepath or ":/" not in filepath:
            pass
        else:
            # 判断文件是否存在
            if os.path.exists(filepath):
                try:
                    # 返回文件最近修改日期
                    mtime = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(os.path.getmtime(filepath)))
                    self.m_textCtrl52.SetValue(mtime)

                    # 返回文件创建时间
                    ctime = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(os.path.getctime(filepath)))
                    self.m_textCtrl50.SetValue(ctime)

                    # 返回文件最近访问时间
                    atime = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(os.path.getatime(filepath)))
                    self.m_textCtrl51.SetValue(atime)

                    # 返回文件名字
                    filename = os.path.basename(filepath)
                    self.m_textCtrl47.SetValue(filename)

                    # 返回文件类型
                    lastname = os.path.splitext(filename)
                    filetype = lastname[1]
                    self.m_textCtrl49.SetValue(filetype)

                    # 返回文件大小
                    filesize = os.path.getsize(filepath)
                    self.m_textCtrl48.SetValue("{0:.2f}KB {1:.2f}MB".format(filesize / 1024, filesize / 1024 / 1024))

                    # 设置文件路径
                    self.m_textCtrl46.SetValue(filepath)
                    # self.m_staticText12.SetLabel(filepath)
                    # self.m_staticText1001.SetLabel(filepath)
                except Exception as e:
                    AsFunction.showtips("Message", str(e))
            else:
                sql = ("DELETE FROM fileinfo WHERE path='%s'" % filepath)
                AsFunction.exesql("delete", "", "", sql)
                AsFunction.showtips("Message", "文件已被删除或文件路径被修改，无法查看文件信息，数据库的信息也已被删除！")

    # 更新文件数据库按钮
    def button221(self, event):
        pool.submit(UpdateFileInfo, self)

    # 不是太确定还有没有用，先不改，留着吧
    # 这个不是句子刷新菜单吗，怎么会没用？之前怎么标记的。。。
    def menuitem12(self, event):
        sql = "SELECT body FROM sentences ORDER BY rand() limit 1"
        datas = AsFunction.exesql("select", "", "", sql)
        self.m_staticText1182.SetLabel(str(datas[0][0]))

    # 上传数据库按钮
    def button2(self, event):
        # self.m_checkBox31.GetValue()
        filepath = self.m_dirPicker1.GetPath()
        if filepath == "":
            AsFunction.showtips("Message", "请选择文件路径！")
        else:
            result = AsFunction.sqltest()
            if result == 0:
                AsFunction.showtips("Message", "数据库连接失败！")
            else:
                file_nums = sum([len(files) for root, dirs, files in os.walk(filepath)])
                if str(file_nums) == "0":
                    AsFunction.showtips("Message", filepath + "\n这是一个空文件夹，请重新选择！")
                else:

                    self.m_button2.Enable(False)
                    self.m_button221.Enable(False)
                    # self.m_textCtrl11.Enable(False)
                    # self.m_textCtrl12.Enable(False)

                    # 设置进度条的范围
                    self.m_gauge2.SetRange(file_nums)
                    # 初始化进度条
                    self.m_gauge2.SetValue(0)

                    # 设置总数标签
                    self.m_staticText83.SetLabel(str(file_nums))

                    # 计算单个文件占比
                    rangevalue = float(1 / file_nums) * 100

                    # 初始化百分比
                    self.m_staticText931.SetLabel("0.00000000000000000")

                    # 初始化上传总数
                    self.m_staticText101.SetLabel("0")

                    args = [filepath, self, rangevalue]
                    pool.submit(lambda p: startanalize(*p), args)

                    # 第二个文件夹摘选器

    def listitemselected2(self, event):
        index = event.GetIndex()
        name = self.m_listCtrl2.GetItem(index, 4)
        filepath = name.GetText()
        self.m_textCtrl77.SetValue(filepath)

    # 文件管理界面的第一个文件列表框
    """
    def listbox2(self, event):
        item = self.m_dirPicker2.GetPath()
        item = os.path.join(item, event.GetEventObject().GetStringSelection())

        if os.path.isdir(item):
            list1 = []
            lastpath = os.path.join(item, os.pardir)
            abspaths = os.path.abspath(lastpath)
            list1.append(abspaths)
            # print(abspaths)
            self.m_dirPicker2.SetPath(item)
            try:
                sublist = os.listdir(item)
                for i in sublist:
                    # filepath = os.path.join(item,i)
                    list1.append(i)
                event.GetEventObject().Set(list1)
                item = list1
            except Exception as e:
                print(str(e))
                pass
        else:
            # print(os.path.abspath(item))
            if "File exise" in item:
                pass
                # self.m_staticText12.SetLabel("Path: "+item)
            else:
                os.startfile(os.path.abspath(item))

    def dirpicker3(self, event):
        index = [self.m_dirPicker3.GetPath()]
        self.m_listBox3.Set(index)

    # 文件管理界面的第二个文件列表框
    def listbox3(self, event):
        item = self.m_dirPicker3.GetPath()
        item = os.path.join(item, event.GetEventObject().GetStringSelection())

        if os.path.isdir(item):
            list1 = []
            lastpath = os.path.join(item, os.pardir)
            abspaths = os.path.abspath(lastpath)
            list1.append(abspaths)
            # print(abspaths)
            self.m_dirPicker3.SetPath(item)
            try:

                sublist = os.listdir(item)
                for i in sublist:
                    # filepath = os.path.join(item,i)
                    list1.append(i)
                event.GetEventObject().Set(list1)
                item = list1
            except Exception as e:
                print(str(e))
                pass
        else:
            # print(os.path.abspath(item))
            if "File exise" in item:
                pass
                # self.m_staticText12.SetLabel("Path: "+item)
            else:
                os.startfile(os.path.abspath(item))

    # 数据库管理界面的选择按钮
    def checkbox3(self, event):
        choise = self.m_checkBox3.GetValue()
        self.m_textCtrl17.Enable(choise)
        self.m_textCtrl18.Enable(choise)
        self.m_textCtrl19.Enable(choise)
        self.m_textCtrl20.Enable(choise)
        self.m_textCtrl21.Enable(choise)
        self.m_textCtrl22.Enable(choise)

    # 数据库操作界面的Select按钮
    def button20(self, event):
        cloumname = self.m_textCtrl23.GetValue()
        tablename = self.m_textCtrl24.GetValue()
        if cloumname == "" or tablename == "":
            AsFunction.showtips("Message", "必选项不能留空！")
        else:
            if not self.m_checkBox3.GetValue():
                sql = "SELECT " + cloumname + " " + "FROM " + tablename
                wcloumname = self.m_textCtrl25.GetValue()
                woperator = self.m_textCtrl26.GetValue()
                wvalue = self.m_textCtrl27.GetValue()
                if wcloumname == "" or woperator == "" or wvalue == "":
                    pass
                else:
                    sql = sql + " WHERE " + wcloumname + woperator + "\'" + wvalue + "\'"
                limit = self.m_textCtrl28.GetValue()
                if limit == "":
                    pass
                else:
                    sql = sql + " LIMIT " + limit

                    datas = AsFunction.exesql(self, "select", sql)
                    self.m_listBox4.Clear()
                    for i in datas:
                        self.m_listBox4.Append(str(i))

    # 数据库操作界面的Insert按钮
    def button21(self, event):
        tablename = self.m_textCtrl29.GetValue()
        cloumlist = self.m_textCtrl30.GetValue()
        valuelist = self.m_textCtrl31.GetValue()
        if tablename == "" or cloumlist == "" or valuelist == "":
            AsFunction.showtips("Message", "必选项不能留空！")
        else:
            if not self.m_checkBox3.GetValue():
                db, cursor, user = AsFunction.linktosql(self.m_textCtrl11.GetValue(), self.m_textCtrl12.GetValue())
                if user == '0':
                    AsFunction.showtips("Message", "数据库连接失败！")
                else:
                    sql = "INSERT INTO " + tablename + " (" + cloumlist + ")" + " VALUES (" + valuelist + ")"
                    try:
                        cursor.execute(sql)
                        db.commit()
                        self.m_listBox4.Clear()
                        self.m_listBox4.Append("Success insert!")
                        db.close()
                    except Exception as e:
                        AsFunction.showtips("Message", str(e))
                        db.close()

    # 数据库操作界面的Update按钮
    def button22(self, event):
        indexcloum = self.m_textCtrl32.GetValue()
        indexvalue = self.m_textCtrl33.GetValue()
        updatecloum = self.m_textCtrl34.GetValue()
        updatevalue = self.m_textCtrl35.GetValue()
        tablename = self.m_textCtrl39.GetValue()
        if indexcloum == "" or indexvalue == "" or updatecloum == "" or updatevalue == "" or tablename == "":
            AsFunction.showtips("Message", "必选项不能留空！")
        else:
            if not self.m_checkBox3.GetValue():
                db, cursor, user = AsFunction.linktosql(self.m_textCtrl11.GetValue(), self.m_textCtrl12.GetValue())
                if user == '0':
                    AsFunction.showtips("Message", "数据库连接失败！")
                else:
                    sql = "UPDATE " + tablename + " SET " + updatecloum + "=" \
                          + updatevalue + " WHERE " + indexcloum + "=" + indexvalue
                    print(sql)
                    try:
                        cursor.execute(sql)
                        db.commit()
                        self.m_listBox4.Clear()
                        AsFunction.showtips("Message", "已提交更新！")
                        db.close()
                    except Exception as e:
                        AsFunction.showtips("Message", str(e))
                        db.close()

    # 数据库操作界面的Delect按钮
    def button23(self, event):
        tablename = self.m_textCtrl36.GetValue()
        cloumname = self.m_textCtrl37.GetValue()
        cloumvalue = self.m_textCtrl38.GetValue()
        if tablename == "" or cloumname == "" or cloumvalue == "":
            AsFunction.showtips("Message", "必选项不能留空！")
        else:
            if not self.m_checkBox3.GetValue():
                db, cursor, user = AsFunction.linktosql(self.m_textCtrl11.GetValue(), self.m_textCtrl12.GetValue())
                if user == '0':
                    AsFunction.showtips("Message", "数据库连接失败！")
                else:
                    sql = "DELETE FROM " + tablename + " WHERE " + cloumname + "=" + cloumvalue
                    # print(sql)
                    try:
                        cursor.execute(sql)
                        db.commit()

                        AsFunction.showtips("Message", "已提交删除！")
                        db.close()
                    except Exception as e:
                        self.m_listBox4.Append(str(e))
                        db.close()
    

    # 创建用户的OK按钮
    def button291(self, event):
        username = self.m_textCtrl53.GetValue()
        userpassword = self.m_textCtrl54.GetValue()
        passwordagain = self.m_textCtrl55.GetValue()
        if username == "" or userpassword == "" or passwordagain == "":
            AsFunction.showtips("Message", "用户信息不能为空！")
        else:
            if userpassword == passwordagain:
                    cursor.execute("select name from user where name='%s'" % username)
                    result = cursor.fetchall()
                    if result:
                        AsFunction.showtips("Message", "账户已存在，请重新输入！")
                    else:
                        sqlinsert = ("insert into user(name,password,type)\
                                        values ('%s','%s',%s)" % (str(username), str(userpassword), 1))
                        try:
                            cursor.execute(sqlinsert)
                            db.commit()
                        except:
                            db.rollback()
                        sqlinsert = "CREATE TABLE %s (\
                                  type VARCHAR(255),\
                                  name VARCHAR(255),\
                                   size BIGINT(255),\
                                   path VARCHAR(255),\
                                   time BIGINT(255))" % \
                                    username
                        try:
                            cursor.execute(sqlinsert)
                            db.commit()
                            AsFunction.showtips("Message", username + "账户创建成功！")
                            db.close()
                        except Exception as e:
                            AsFunction.showtips("Message", str(e) + "创建数据表错误，请联系开发者！\n zhaozhinet@163.com")
            else:
                AsFunction.showtips("Message", "两次密码不匹配，请确认密码！")

    # 表格点击事件，如果判断是路径就打开此文件，如果不是就显示出来
    # def grid1selectcell(self, event):
    #    co = event.GetCol()
    #    ro = event.GetRow()
    #    re = event.GetEventObject().GetCellValue(ro, co)
    #    if ":/" in re:
    #        self.m_textCtrl45.SetValue(re)

    # 主界面的打开文件按钮
    # def button29(self, event):
    #    path = self.m_textCtrl45.GetValue()
    #    if path != "":
    #        os.startfile(path)
    #    else:
    #        dia = AsDialog.MyDialog1(None, "请选择一个路径！")
    #        dia.ShowModal()
"""

    # 数据库测试连通性
    def button30(self, event):
        result = AsFunction.sqltest()
        if result == 1:
            AsFunction.showtips("Success", "数据库连接成功！")
        else:
            AsFunction.showtips("Error", "数据库连接失败！")

    # 笔记界面的列表框点击事件
    def listbox5(self, event):
        title = self.m_listBox5.GetStringSelection()
        if title == "":
            pass
        else:
            sqlinsert = ("SELECT body,fontsize,time FROM note WHERE title='%s'" % title)
            datass = AsFunction.exesql("select", "", "", sqlinsert)

            self.m_textCtrl521.SetValue(title)

            self.m_textCtrl531.SetValue(str(datass[0][0]))
            self.m_slider1.SetValue(int(datass[0][1]))
            self.m_staticText88.SetLabel(str(datass[0][1]))
            choise = self.m_choice11.GetStringSelection()
            self.m_textCtrl531.SetFont(wx.Font(int(datass[0][1]), 70, 90, 90, False, choise))
            self.m_staticText901.SetLabel(str(datass[0][2]))

    # 笔记界面的字体更改下拉框
    def choice11(self, event):
        choise = self.m_choice11.GetStringSelection()
        value = self.m_slider1.GetValue()
        self.m_textCtrl531.SetFont(wx.Font(int(value), 70, 90, 90, False, choise))

    # 滑动条事件
    def slider1(self, event):
        value = self.m_slider1.GetValue()
        self.m_staticText88.SetLabel(str(value))
        choise = self.m_choice11.GetStringSelection()
        self.m_textCtrl531.SetFont(wx.Font(int(value), 70, 90, 90, False, choise))

    # 滑动条两边加减按钮
    def button33(self, event):
        value = int(self.m_slider1.GetValue())
        value -= 1
        if value >= 1:
            self.m_slider1.SetValue(value)
            self.m_staticText88.SetLabel(str(value))
            choise = self.m_choice11.GetStringSelection()
            self.m_textCtrl531.SetFont(wx.Font(int(value), 70, 90, 90, False, choise))

    def button34(self, event):
        value = int(self.m_slider1.GetValue())
        value += 1
        if value <= 50:
            self.m_slider1.SetValue(value)
            self.m_staticText88.SetLabel(str(value))
            choise = self.m_choice11.GetStringSelection()
            self.m_textCtrl531.SetFont(wx.Font(int(value), 70, 90, 90, False, choise))

    # 复制文件按钮
    """
    def button7(self, event):
        dia = AsDialog.MyDialog2(None, "D://emailtest", "Creat File")
        dia.ShowModal()


    # 新建文件夹按钮
    def button11(self, event):
        if self.m_checkBox32.GetValue():
            parentpath = self.m_dirPicker3.GetPath()
            if parentpath == "":
                AsFunction.showtips("Message", "请先选择左边目录！")
            else:
                dia = AsDialog.MyDialog2(None, parentpath, "Creat Folder")
                dia.ShowModal()
        else:
            parentpath = self.m_dirPicker2.GetPath()
            if parentpath == "":
                AsFunction.showtips("Message", "请先选择右边目录！")
            else:
                dia = AsDialog.MyDialog2(None, parentpath, "Creat Folder")
                dia.ShowModal()
                # 新建文件按钮

    def button12(self, event):
        if self.m_checkBox32.GetValue():
            parentpath = self.m_dirPicker3.GetPath()
            if parentpath == "":
                AsFunction.showtips("Message", "请先选择左边目录！")
            else:
                dia = AsDialog.MyDialog2(None, parentpath, "Creat File")
                dia.ShowModal()
        else:
            parentpath = self.m_dirPicker2.GetPath()
            if parentpath == "":
                AsFunction.showtips("Message", "请先选择右边目录！")
            else:
                dia = AsDialog.MyDialog2(None, parentpath, "Creat File")
                dia.ShowModal()

    """

    # 以下是数学计算的文本框回车事件
    # 画图文本框
    def textctrl69(self, event):
        funct = self.m_textCtrl69.GetValue()
        if funct == "":
            AsFunction.showtips("Message", "请先输入函数！")
        else:
            try:
                choice = self.m_radioBtn2.GetValue()
                x, y = symbols('x y')
                if choice:
                    plot(funct)
                else:
                    plot3d(funct)
            except Exception as e:
                AsFunction.showtips("Message", str(e))

    # 计算导数的文本框回车事件
    def textctrl61(self, event):
        fx = self.m_textCtrl61.GetValue()
        if fx == "":
            AsFunction.showtips("Message", "请输入函数")
        else:
            x = symbols('x')
            try:
                re = diff(fx, x)
                self.m_textCtrl57.SetValue(str(re))
            except Exception as e:
                AsFunction.showtips("Message", str(e))

    # 计算极限的文本框回车事件
    def textctrl58(self, event):
        fx = self.m_textCtrl58.GetValue()
        if fx == "":
            AsFunction.showtips("Message", "请输入函数")
        else:
            to = self.m_textCtrl59.GetValue()
            if to == "":
                AsFunction.showtips("Message", "请输入x的极限")
            else:
                x = symbols('x')
                try:
                    re = limit(fx, x, to)
                    self.m_textCtrl57.SetValue(str(re))
                except Exception as e:
                    AsFunction.showtips("Message", str(e))

    # 计算不定积分文本框回车事件
    def textctrl63(self, event):
        fx = self.m_textCtrl63.GetValue()
        if fx == "":
            AsFunction.showtips("Message", "请输入函数")
        else:
            x = symbols('x')
            try:
                re = integrate(fx, x)
                self.m_textCtrl57.SetValue(str(re))
            except Exception as e:
                AsFunction.showtips("Message", str(e))

    # 计算定积分文本框回车事件
    def textctrl67(self, event):
        fx = self.m_textCtrl67.GetValue()
        if fx == "":
            AsFunction.showtips("Message", "请输入函数")
        else:
            x = symbols('x')
            x = self.m_textCtrl68.GetValue()
            if x == "":
                AsFunction.showtips("Message", "请输入积分变量")
            else:
                sd = self.m_textCtrl66.GetValue()
                st = self.m_textCtrl65.GetValue()
                if sd == "" or st == "":
                    AsFunction.showtips("Message", "请补全变量区间")
                else:
                    try:
                        re = integrate(fx, (x, sd, st))
                        self.m_textCtrl57.SetValue(str(re))
                    except Exception as e:
                        AsFunction.showtips("Message", str(e))

    # 列表点击按钮
    def listbox6(self, event):
        title = self.m_listBox6.GetStringSelection()
        if title == "":
            pass
        else:
            self.m_textCtrl681.SetValue(title)
            title = escape_string(title)
            sqlinsert = ("SELECT body,ctime,mtime,readtype,readnotice,label FROM iread WHERE title='%s'" % (
                title))
            datass = AsFunction.exesql("select", "", "", sqlinsert)
            # body
            self.m_textCtrl671.SetValue(str(datass[0][0]))
            # ctime
            self.m_staticText112.SetLabel(str(datass[0][1]))
            # mtime
            self.m_staticText113.SetLabel(str(datass[0][2]))
            # readtype
            if str(datass[0][3]) == "1":
                self.m_checkBox4.SetValue(True)
            else:
                self.m_checkBox4.SetValue(False)
            # readnotice
            self.m_textCtrl691.SetValue(str(datass[0][4]))
            # label
            self.m_textCtrl72.SetValue(str(datass[0][5]))

            # 以上内容都是读取自本地数据库，则下面是读取服务器数据库，仅获取一项阅读次数
            db, cursor, message = AsFunction.linktosersql()
            if message != "1":
                AsFunction.showtips("Message", "服务器数据库连接失败，无法读取文章阅读次数！")
            else:
                try:
                    sqlinsert = "SELECT readnum FROM iread WHERE title='%s'" % title
                    cursor.execute(sqlinsert)
                    datass = cursor.fetchall()
                    self.m_staticText119.SetLabel(str(datass[0][0]))
                    db.close()
                except Exception as e:
                    AsFunction.showtips("Message", str(e))

    # 更改字体类型下拉框
    def choice1(self, event):
        choise = self.m_choice1.GetStringSelection()
        value = self.m_slider2.GetValue()
        self.m_textCtrl671.SetFont(wx.Font(int(value), 70, 90, 90, False, choise))

    # write界面的滑动条按钮
    def slider2(self, event):
        value = self.m_slider2.GetValue()
        textfonts = self.m_choice1.GetStringSelection()
        self.m_staticText111.SetLabel(str(value))
        self.m_textCtrl671.SetFont(wx.Font(int(value), 70, 90, 90, False, textfonts))

    # 所有IP列表的点击事件，获取此IP下所有评论过的内容，给评论列表
    def listbox7(self, event):
        db, cursor, message = AsFunction.linktosersql()
        if message != "1":
            AsFunction.showtips("Message", "服务器数据库连接失败！")
            db.close()
        else:
            try:
                self.m_listBox9.Clear()
                ip = self.m_listBox7.GetStringSelection()
                sqlinsert = "SELECT body FROM ireadcomment WHERE ip='%s'" % ip
                cursor.execute(sqlinsert)
                datas = cursor.fetchall()
                for i in datas:
                    self.m_listBox9.Append(i)
                db.close()
            except Exception as e:
                AsFunction.showtips("Message", "服务器数据库：" + str(e))
                db.close()

    # 选定IP下的评论内容点击事件，将详细信息添加到文本框中
    def listbox9(self, event):
        db, cursor, message = AsFunction.linktosersql()
        if message != "1":
            AsFunction.showtips("Message", "服务器数据库连接失败！")
            db.close()
        else:
            try:
                self.m_textCtrl73.SetValue("")
                body = self.m_listBox9.GetStringSelection()
                body = escape_string(body)
                sqlinsert = "SELECT user,ctime,time FROM ireadcomment WHERE body='%s'" % body
                cursor.execute(sqlinsert)
                datas = cursor.fetchall()
                user = str(datas[0][0])
                ctime = str(datas[0][1])
                times = str(datas[0][2])

                sqlinsert = "SELECT title FROM iread WHERE ctime='%s'" % ctime
                cursor.execute(sqlinsert)
                datas = cursor.fetchall()
                article = str(datas[0][0])
                string = times + "\nUser: " + user + "\nComment: " + body + "\nArticle: " + article
                self.m_textCtrl73.SetValue(string)
                db.close()
            except Exception as e:
                AsFunction.showtips("Message", "服务器数据库：" + str(e))
                db.close()

    # 删除评论按钮
    def button44(self, event):
        body = self.m_listBox9.GetStringSelection()
        body = escape_string(body)
        if body == "":
            AsFunction.showtips("Message", "请先选择评论！")
        else:
            db, cursor, message = AsFunction.linktosersql()
            if message != "1":
                AsFunction.showtips("Message", "服务器数据库连接失败！")
                db.close()
            else:
                try:
                    self.m_listBox9.Clear()
                    sqlinsert = "DELETE FROM ireadcomment WHERE body='%s'" % body
                    cursor.execute(sqlinsert)
                    db.commit()
                    AsFunction.showtips("Message", body + "\n此评论已删除！")
                    menuitem1s(self, event)
                    db.close()
                except Exception as e:
                    AsFunction.showtips("Message", "服务器数据库：" + str(e))
                    db.close()

    # 删除指定IP下的所有评论
    def button48(self, event):
        ip = self.m_listBox7.GetStringSelection()
        if ip == "":
            AsFunction.showtips("Message", "请先选择IP!")
        else:
            db, cursor, message = AsFunction.linktosersql()
            if message != "1":
                AsFunction.showtips("Message", "服务器数据库连接失败！")
                db.close()
            else:
                try:
                    self.m_listBox9.Clear()
                    ip = self.m_listBox7.GetStringSelection()
                    sqlinsert = "DELETE FROM ireadcomment WHERE ip='%s'" % ip
                    cursor.execute(sqlinsert)
                    db.commit()
                    AsFunction.showtips("Message", ip + "\n此IP下的所有评论已删除！")
                    menuitem1s(self, event)
                    db.close()
                except Exception as e:
                    AsFunction.showtips("Message", "服务器数据库：" + str(e))
                    db.close()

    # 加入黑名单按钮
    def button411(self, event):
        ip = self.m_listBox7.GetStringSelection()
        if ip == "":
            AsFunction.showtips("Message", "请先选择IP!")
        else:
            notice = self.m_textCtrl74.GetValue()
            if notice == "":
                AsFunction.showtips("Message", "请输入禁止评论的原因！")
            else:
                db, cursor, message = AsFunction.linktosersql()
                if message != "1":
                    AsFunction.showtips("Message", "服务器数据库连接失败！")
                    db.close()
                else:
                    try:
                        cursor.execute("select ip from ircdenylist where ip='%s'" % ip)
                        results = cursor.fetchall()
                        if str(results) != "()":
                            AsFunction.showtips("Message", "此IP已被禁止评论！")
                            db.close()
                        else:
                            cursor.execute("INSERT INTO ircdenylist (ip,notice) VALUES ('%s','%s')" % (ip, notice))
                            AsFunction.showtips("Message", ip + "\n此IP已被禁止发表评论！")
                            db.commit()
                            menuitem1s(self, event)
                            db.close()
                    except Exception as e:
                        AsFunction.showtips("Message", "服务器数据库：" + str(e))
                        db.close()

    # 移出黑名单按钮
    def button43(self, event):
        ip = self.m_listBox8.GetStringSelection()
        if ip == "":
            AsFunction.showtips("Message", "请先选择被禁止评论的IP!")
        else:
            db, cursor, message = AsFunction.linktosersql()
            if message != "1":
                AsFunction.showtips("Message", "服务器数据库连接失败！")
                db.close()
            else:
                try:
                    sqlinsert = "DELETE FROM ircdenylist WHERE ip='%s'" % ip
                    cursor.execute(sqlinsert)
                    db.commit()
                    AsFunction.showtips("Message", ip + "\n此IP已解封！")
                    menuitem1s(self, event)
                    db.close()
                except Exception as e:
                    AsFunction.showtips("Message", "服务器数据库：" + str(e))
                    db.close()

    def listitemselected3(self, event):
        index = event.GetIndex()
        value = self.m_listCtrl3.GetItem(index, 0)
        name = value.GetText()
        self.m_textCtrl711.SetValue(name)

        value = self.m_listCtrl3.GetItem(index, 1)
        plan = value.GetText()
        self.m_textCtrl721.SetValue(plan)

        value = self.m_listCtrl3.GetItem(index, 2)
        startdate = value.GetText()
        self.m_textCtrl731.SetValue(startdate)

        value = self.m_listCtrl3.GetItem(index, 3)
        deadline = value.GetText()
        self.m_textCtrl741.SetValue(deadline)

        value = self.m_listCtrl3.GetItem(index, 4)
        statue = value.GetText()
        self.m_choice3.SetStringSelection(statue)

        value = self.m_listCtrl3.GetItem(index, 5)
        remarks = value.GetText()
        self.m_textCtrl76.SetValue(remarks)

    # 自动读取留言墙多选框
    def checkbox61(self, event):
        choise = self.m_checkBox61.GetValue()
        if choise:
            WriteMeWas(self)

    # 百科库的新建按钮
    def button231(self, event):
        title = self.m_textCtrl96.GetValue()
        if title == "":
            AsFunction.showtips("Message", "标题不能为空！")
        else:
            title = escape_string(title)
            sql = "select title from eds where title='%s'" % title
            results = AsFunction.exesql("select", "", "", sql)
            if str(results) != "()":
                AsFunction.showtips("Message", "标题已存在于本地数据库中，无法创建，请重新输入名字！")
            else:
                label = self.m_textCtrl97.GetValue()
                value = self.m_textCtrl100.GetValue()
                value = escape_string(value)
                ctime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                # 上传本地数据库
                sql = "INSERT INTO eds (title,value,label,ctime,mtime) VALUES ('%s','%s','%s','%s','%s')" % (
                    title, value, label, ctime, ctime)
                AsFunction.exesql("insert", "", "", sql)
                self.m_staticText142.SetLabel(ctime)
                AsFunction.showtips("Message", title + "\n本地数据库新内容已保存！")

    # 百科库页面的多列列表点击事件
    def onlistitemselected6(self, event):
        index = event.GetIndex()
        index = self.m_listCtrl6.GetItem(index, 0)
        title = index.GetText()

        index = event.GetIndex()
        index = self.m_listCtrl6.GetItem(index, 1)
        label = index.GetText()

        index = event.GetIndex()
        index = self.m_listCtrl6.GetItem(index, 2)
        ctime = index.GetText()
        if title == "" or ctime == "":
            pass
        else:
            title = escape_string(title)
            sql = "select value,mtime from eds where title='%s' and ctime='%s'" % (title, ctime)
            results = AsFunction.exesql("select", "", "", sql)
            dia = AsDialog.MyDialog3(None, title, label, ctime, str(results[0][1]), str(results[0][0]))
            dia.ShowModal()
            """
                self.m_textCtrl96.SetValue(title)
                self.m_staticText142.SetLabel(ctime)
                self.m_textCtrl97.SetValue(label)
                self.m_textCtrl100.SetValue(str(results[0][0]))
                self.m_staticText143.SetLabel(str(results[0][1]))
                """

    # 百科库页面的清空按钮
    def button26(self, event):
        self.m_textCtrl100.Clear()
        self.m_staticText142.SetLabel("000000000000")
        self.m_staticText143.SetLabel("000000000000")
        self.m_textCtrl97.Clear()
        self.m_textCtrl96.Clear()

    # 百科库页面的保存按钮
    def button25(self, event, ctmie=None):
        title = self.m_textCtrl96.GetValue()
        if title == "":
            AsFunction.showtips("Message", "标题为空，保存失败")
        else:
            ctime = self.m_staticText142.GetLabel()
            if ctime == "000000000000":
                AsFunction.showtips("Message", "请先加载文章")
            else:
                title = escape_string(title)
                value = self.m_textCtrl100.GetValue()
                # 转义字符
                value = escape_string(value)
                label = self.m_textCtrl97.GetValue()
                mtime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                sql = "UPDATE eds SET title='%s',value='%s',label='%s',mtime='%s' WHERE ctime='%s'" % (
                    title, value, label, mtime, ctime)
                AsFunction.exesql("update", "", "", sql)
                AsFunction.showtips("Message", title + "\n保存成功！")
                self.m_staticText143.SetLabel(mtime)

    # 百科库页面的删除按钮
    def button24(self, event):
        title = self.m_textCtrl96.GetValue()
        if title == "":
            AsFunction.showtips("Message", "请先加载文章！")
        else:
            ctime = self.m_staticText142.GetLabel()
            if ctime != "000000000000":
                self.m_staticText142.SetLabel("000000000000")
                AsFunction.showtips("Message", "请再次点击以确认删除！")
            else:
                sqlinsert = "DELETE FROM eds WHERE title='%s'" % title
                AsFunction.exesql("delete", "", "", sqlinsert)
                AsFunction.showtips("Message", title + "\n本地数据库已经删除！")

                # 初始化标题栏和内容栏
                self.m_textCtrl96.SetValue("")
                self.m_textCtrl97.Clear()
                self.m_textCtrl100.SetValue("")
                # self.m_listCtrl6.ClearAll()

    # 百科库页面的加载按钮
    def button27(self, event):
        title = self.m_textCtrl96.GetValue()
        if title == "":
            AsFunction.showtips("Message", "标题为空！")
        else:

            title = escape_string(title)
            sqlinsert = "SELECT value,label,ctime,mtime FROM eds WHERE title='%s'" % title
            datas = AsFunction.exesql("select", "", "", sqlinsert)
            if str(datas) == "()":
                AsFunction.showtips("Message", "标题不存在！")
            else:
                self.m_textCtrl100.SetValue(datas[0][0])
                self.m_textCtrl97.SetValue(datas[0][1])
                self.m_staticText142.SetLabel(datas[0][2])
                self.m_staticText143.SetLabel(datas[0][3])

    def button8(self, event):
        dia = AsDialog.MyDialog3(None, "title", "label", "ctime", "mtime", "values")
        dia.ShowModal()

    # 发送邮件按钮
    def button28(self, event):
        receive = self.m_comboBox3.GetStringSelection()
        title = self.m_textCtrl101.GetValue()
        value = self.m_textCtrl102.GetValue()
        if receive == "" or title == "" or value == "":
            AsFunction.showtips("Error", "收件人、主题和内容不能为空！")
        else:
            AsFunction.sendmail(receive, title, value)

    # 连接服务端按钮
    def button29(self, event):
        self.m_button29.Enable(False)
        # self.m_textCtrl1021.AppendText("开始")
        pool2.submit(clientreport, self)

    # 关闭线程按钮
    def button311(self, event):
        pool2.shutdown()
        self.m_textCtrl1021.AppendText("\n已提交停止线程！")
        self.m_button29.Enable(True)

    # 生成密码按钮
    def button301(self, event):
        selectbase = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        specil = self.m_textCtrl104.GetValue()
        maxleng = 61
        length = int(self.m_textCtrl105.GetValue())

        result = ''
        if self.m_checkBox7.GetValue():
            selectbase += specil
            maxleng += len(specil)
        for i in range(length):
            sl = random.randint(0, maxleng)
            result += selectbase[sl]
        self.m_textCtrl103.SetValue(str(result))

    # 刷新密码数据库按钮
    def button31(self, event):
        datas = AsFunction.exesql("select", "", "", "SELECT * FROM passwd")
        self.m_listCtrl7.ClearAll()
        self.m_listCtrl7.InsertColumn(0, "账号", width=120)
        self.m_listCtrl7.InsertColumn(1, "密码", width=150)
        self.m_listCtrl7.InsertColumn(2, "创建时间", width=150)
        idx = 0
        for i in datas:
            index = self.m_listCtrl7.InsertStringItem(idx, str(i[0]))
            self.m_listCtrl7.SetStringItem(index, 1, str(i[1]))
            self.m_listCtrl7.SetStringItem(index, 2, str(i[2]))

    # 随机生成5个密码按钮
    def button32(self, event):
        return super().button32(event)

    # 加入密码数据库按钮
    def button331(self, event):
        account = self.m_textCtrl106.GetValue()
        password = self.m_textCtrl103.GetValue()
        if account == "" or password == "":
            AsFunction.showtips("Error", "账号或密码不能为空！")
        else:
            ctime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            ctime = escape_string(ctime)
            sqli = "INSERT INTO passwd (account,password,ctime) VALUES ('%s','%s','%s')" % (account, password, ctime)
            print(sqli)
            AsFunction.exesql("insert", "", "", sqli)
            AsFunction.showtips("Success", "密码保存成功！")

    # 数据库页面的刷新事件
    def button39(self, event):
        host = 'localhost'
        port = 3306
        sqluser = 'root'
        password = 'nichenyang'
        database = 'analizepy'
        charset = 'utf8'

        db = pymysql.connect(host=host, port=port, user=sqluser, password=password,
                             charset=charset)
        cursor = db.cursor()

        cursor.execute("SHOW DATABASES")
        data = cursor.fetchall()

        self.m_choice8.Clear()
        for i in data:
            self.m_choice7.Append(i)

        db.close()

    # 数据库选择下拉框点击事件
    def onchoice7(self, event):
        database = self.m_choice7.GetStringSelection()
        host = 'localhost'
        port = 3306
        sqluser = 'root'
        password = 'nichenyang'
        charset = 'utf8'

        db = pymysql.connect(host=host, port=port, user=sqluser, password=password, database=database,
                             charset=charset)
        cursor = db.cursor()

        cursor.execute("SHOW TABLES")
        data = cursor.fetchall()

        self.m_choice8.Clear()
        for i in data:
            self.m_choice8.Append(i)

        db.close()

    # 数据表下拉框点击事件
    def onchoice8(self, event):
        database = self.m_choice7.GetStringSelection()
        host = 'localhost'
        port = 3306
        sqluser = 'root'
        password = 'nichenyang'
        charset = 'utf8'

        db = pymysql.connect(host=host, port=port, user=sqluser, password=password, database=database,
                             charset=charset)
        cursor = db.cursor()

        tables = self.m_choice8.GetStringSelection()
        cursor.execute("DESC %s" % tables)
        data = cursor.fetchall()
        ind = 0
        self.m_listCtrl8.ClearAll()
        for i in data:
            self.m_listCtrl8.InsertColumn(ind, i[0], width=200)
            ind += 1

        cursor.execute("SELECT * FROM %s" % tables)
        data = cursor.fetchall()
        idx = 0
        for i in data:
            index = self.m_listCtrl8.InsertStringItem(idx, str(i[0]))
            for j in range(1, ind):
                self.m_listCtrl8.SetStringItem(index, j, str(i[j]))
            idx += 1

        db.close()

        """
            self.m_listCtrl4.ClearAll()
            self.m_listCtrl4.InsertColumn(0, "Name", width=200)
            self.m_listCtrl4.InsertColumn(1, "Size", width=80)
            self.m_listCtrl4.InsertColumn(2, "MTime", width=120)
            self.m_listCtrl4.InsertColumn(3, "Path", width=300)
            idx = 0
            for i in datas:
                index = self.m_listCtrl4.InsertStringItem(idx, str(i[0]))
                self.m_listCtrl4.SetStringItem(index, 1, "{0:.2f}MB".format(int(i[1]) / 1024 / 1024))
                self.m_listCtrl4.SetStringItem(index, 2, str(i[2]))
                self.m_listCtrl4.SetStringItem(index, 3, str(i[3]))
                idx += 1
        """

    # 查看数据表详细信息
    def button38(self, event):
        database = self.m_choice7.GetStringSelection()
        host = 'localhost'
        port = 3306
        sqluser = 'root'
        password = 'nichenyang'
        charset = 'utf8'

        db = pymysql.connect(host=host, port=port, user=sqluser, password=password, database=database,
                             charset=charset)
        cursor = db.cursor()

        tables = self.m_choice8.GetStringSelection()
        cursor.execute("DESC %s" % tables)
        data = cursor.fetchall()

        self.m_listCtrl8.ClearAll()
        self.m_listCtrl8.InsertColumn(0, "Field", width=200)
        self.m_listCtrl8.InsertColumn(1, "Type", width=200)
        self.m_listCtrl8.InsertColumn(2, "Null", width=200)
        self.m_listCtrl8.InsertColumn(3, "Key", width=200)
        self.m_listCtrl8.InsertColumn(4, "Default", width=200)
        self.m_listCtrl8.InsertColumn(5, "Extra", width=200)

        idx = 0
        for i in data:
            index = self.m_listCtrl8.InsertStringItem(idx, str(i[0]))
            for j in range(1, 6):
                self.m_listCtrl8.SetStringItem(index, j, str(i[j]))
            idx += 1

        db.close()

    # 多列表点击事件
    def onlistitemselected8(self, event):
        index = event.GetIndex()
        name = event.GetEventObject().GetItem(index, 1)
        names = name.GetText()
        print(names)

        arr = []
        ind = 0
        while True:
            try:
                data = self.m_listCtrl8.GetColumn(ind)
                value = data.GetText()
                arr.append(value)
                ind += 1
            except:
                break
        print(arr)


if __name__ == '__main__':
    app = wx.App()
    mainwin = myframe(None)
    mainwin.startmon()
    mainwin.Show()
    app.MainLoop()
