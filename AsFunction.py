import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pymysql
import pyttsx3

import AsDialog


# 使用数据库
def exesql(type, succmsg, errormsg, value):
    db, cursor = linktosql()
    if db == False:
        showtips("Error", "本地数据库连接失败！\n" + cursor)
    else:
        try:
            cursor.execute(value)
            if type == "select":
                datas = cursor.fetchall()
                return datas
            else:
                db.commit()
            db.close()
            if succmsg != "":
                showtips("Success", succmsg)
        except Exception as e:
            db.close()
            if errormsg == "":
                showtips("Error", str(e))
            else:
                showtips("Error", errormsg)


# 连接本地数据库函数
def linktosql():
    host = 'localhost'
    port = 3306
    sqluser = 'root'
    password = 'nichenyang'
    database = 'analizepy'
    charset = 'utf8'

    try:
        db = pymysql.connect(host=host, port=port, user=sqluser, password=password, database=database, charset=charset)
        cursor = db.cursor()
        return db, cursor
    except Exception as e:
        return False, str(e)


# 连接服务器的数据库函数
def linktosersql():
    try:
        db = pymysql.connect(host='114.115.153.152', port=3306, user='analizepy', password='PBs8mFsrBMKNenrJ',
                             database='analizepy', charset='utf8')
        cursor = db.cursor()
        return db, cursor, '1'
    except Exception as e:
        showtips("Error", str(e))


# 一键创建所需数据库以及数据表函数
def createsql(self):
    print("未定")


# 数据库连通性测
def sqltest():
    db, cursor = linktosql()
    if not db:
        db.close()
        return 0
    else:
        db.close()
        return 1


# 搜索引擎
def supersearch(self):
    title = self.m_textCtrl75.GetValue()
    if title == "":
        pass
    else:
        limitss = self.m_comboBox1.GetStringSelection()
        sqlinsert = "SELECT name,type,size,time,path FROM fileinfo WHERE name LIKE '%s'\
                         ORDER BY time DESC LIMIT %s" % (
            ('%' + title + '%'), int(limitss))
        datas = exesql("select", "", "", sqlinsert)
        self.m_listCtrl2.ClearAll()
        self.m_listCtrl2.InsertColumn(0, "Name", width=200)
        self.m_listCtrl2.InsertColumn(1, "Type", width=50)
        self.m_listCtrl2.InsertColumn(2, "Size", width=150)
        self.m_listCtrl2.InsertColumn(3, "MTime", width=120)
        self.m_listCtrl2.InsertColumn(4, "Path", width=600)
        idx = 0
        for i in datas:
            index = self.m_listCtrl2.InsertStringItem(idx, str(i[0]))
            self.m_listCtrl2.SetStringItem(index, 1, str(i[1]))
            self.m_listCtrl2.SetStringItem(index, 2, "{0:.2f}KB/{1:.2f}MB".format(int(i[2]) / 1024,
                                                                                  int(i[2]) / 1024 / 1024))
            self.m_listCtrl2.SetStringItem(index, 3, str(i[3]))
            self.m_listCtrl2.SetStringItem(index, 4, str(i[4]))
            idx += 1

            # limitss = self.m_comboBox12.GetStringSelection()
            sqlinsert = "SELECT title,label,ctime FROM eds WHERE title LIKE '%s' LIMIT %s" % (
                ('%' + title + '%'), int(limitss))
            datas = exesql("select", "", "", sqlinsert)
            self.m_listCtrl6.ClearAll()
            self.m_listCtrl6.InsertColumn(0, "Title", width=200)
            self.m_listCtrl6.InsertColumn(1, "Label", width=200)
            self.m_listCtrl6.InsertColumn(2, "CTime", width=200)
            idx = 0
            for i in datas:
                index = self.m_listCtrl6.InsertStringItem(idx, str(i[0]))
                self.m_listCtrl6.SetStringItem(index, 1, str(i[1]))
                self.m_listCtrl6.SetStringItem(index, 2, str(i[2]))
                idx += 1


# 弹出单提示弹窗
def showtips(title, value):
    """
    class mydia(AsDialog.MyDialog1):
        def mbutton19(self, event):
            print("right!")
            self.Destroy()
    dia = mydia(None, title, value)
    dia.ShowModal()
    """
    dia = AsDialog.MyDialog1(None, title, value)
    dia.ShowModal()
    # dia.m_button19()


# 弹出确认弹窗
def showconfirmtips(title, mesg, execute):
    # 虽然可以通过继承来重构按钮的点击方法，但是作为一个中间模块，是做不到的，因为这种方法也算是
    # 自定义的，毕竟中间模块最怕的就是自定义了，现在唯一能做的的就是哪个函数用到了就重新写一遍
    # ，在这里就不再继承了。
    print("Hello")


# 发送邮件
def sendmail(receive, title, value):
    sender = 'zhaozhinet@163.com'
    receiver = receive
    smtpServer = 'smtp.163.com'
    username = 'zhaozhinet@163.com'
    password = 'KGQYLSKRZYRPQGFV'
    mail_title = title
    mail_body = value
    message = MIMEText(mail_body, 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpServer)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string())
        smtp.quit()
        showtips("Success", "邮件发送成功！")
    except Exception as e:
        showtips("Error", str(e))


# 语音播报
def say(value):
    st = pyttsx3.init()
    nowtime = str(time.strftime('%H:%M:%S', time.localtime(time.time())))
    st.setProperty('rate', 150)
    st.setProperty('volume', 1.0)
    st.say(value + nowtime)
    st.runAndWait()