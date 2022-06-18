import psycopg2
from psycopg2 import extras
from PyQt5.QtWidgets import QMessageBox
from dao.dbConfig import localSourceConfig as localConfig


class Staff:
    """
    员工操作类
    """

    def __init__(self, config=localConfig):
        self.db = psycopg2.connect(dbname="postgres",
                                   user="lian",
                                   password="Bigdata@123",
                                   host="120.46.130.234",
                                   port="26000")
        self.cursor = self.db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        self.username = None
        self.password = None
        self.srole = None
        self.sid = None
        self.sname = None
        self.ssex = None
        self.stime = None
        self.sidcard = None
        self.sphone = None

    def userLogin(self, username, password):
        """
        员工登录操作
        :return: row[6]：员工权限    或False：登录失败
        """
        try:
            self.cursor.execute("select * from staff")
            data = self.cursor.fetchall()
            for row in data:
                if row['susername'] == username and row['spassword'] == password and row["sstate"] == 1:
                    self.username = username
                    self.password = password
                    self.sid = row['sid']
                    self.sname = row['sname']
                    self.ssex = row['ssex']
                    self.stime = row['stime']
                    self.srole = row['srole']
                    self.sidcard = row['sidcard']
                    self.sphone = row['sphone']
                    self.sstate = row["sstate"] == 1
                    return row['srole']
        except Exception as e:
            print(e)
            return False

    def modifyPasswd(self, sid, newPasswd, oldPasswd):
        """员工登录后修改密码"""

        try:
            self.cursor.execute("select * from staff where sid=%s ", (sid))
            data = self.cursor.fetchall()[0]
            # print(data)
            if data['spassword'] == oldPasswd:
                self.cursor.execute("update staff set spassword=%s where sid=%s ", (newPasswd, sid))
                self.db.commit()
                self.password = newPasswd
                print("ok")
                return True
            else:
                print("no")
                return False
        except Exception as e:
            print(e)
            return False

    def forgetPasswd(self, newPasswd, sid, sidcard):
        """员工登录时忘记密码，使用身份证找回"""
        try:
            self.cursor.execute("select * from staff where sid=%s", sid)
            data = self.cursor.fetchall()[0]
            # print(data)
            if data['sidcard'] == sidcard:
                self.cursor.execute("update staff set spassword=%s where sid=%s", (newPasswd, sid))
                self.db.commit()
                self.password = newPasswd
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def addStaff(self, sid, sname, ssex, stime, susername, spassword, srole, sidcard, sphone):
        """管理者增加员工"""
        print(
            "insert into staff values(\'{sid}\',\'{sname}\',\'{ssex}\',\'{stime}\',\'{susername}\',\'{spassword}\', \'{srole}\', \'{sidcard}\', \'{sphone}\',{sstate});".format
            (sid=sid, sname=sname, ssex=ssex, stime=stime, susername=susername, spassword=spassword, srole=srole,
             sidcard=sidcard, sphone=sphone, sstate=1))

        try:
            self.cursor.execute("select sid from staff where sid='{sid}' or susername like '{susername}';".format(sid=sid,susername=susername))
            data = self.cursor.fetchall()
            if len(data) > 0:
                QMessageBox().information(None, "提示", "该工号或者账户名已存在！", QMessageBox.Yes)
                return False
            else:
                self.cursor.execute(
                    "insert into staff values(\'{sid}\',\'{sname}\',\'{ssex}\',\'{stime}\',\'{susername}\',\'{spassword}\', \'{srole}\', \'{sidcard}\', \'{sphone}\',{sstate});".format
                    (sid=sid, sname=sname, ssex=ssex, stime=stime, susername=susername, spassword=spassword,
                     srole=srole, sidcard=sidcard, sphone=sphone, sstate=1))
                self.db.commit()
            return True
        except Exception as e:
            print(e)
            QMessageBox().information(None, "提示", "该工号已存在！", QMessageBox.Yes)
            return False

    def getStaff(self, sname):
        """管理者查看员工"""
        print(
            "select * from staff where sname like \'{sname}\'and sstate=1;".format(sname=sname))

        try:
            self.cursor.execute("select * from staff where sname like \'{sname}\' and sstate=1;".format(sname=sname))
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(e)
            return False

    def deleteStaff(self, sid, sname, sidcard):
        """管理者删除员工信息"""

        print(
            "update staff set sstate=0 where sid=\'{sid}\';".format(sid=sid))

        try:
            self.cursor.execute(
                "update staff set sstate=0 where sid=\'{sid}\';".format(sid=sid))

            self.db.commit()
            return True
        except Exception as e:
            print(e)
            QMessageBox().information(None, "提示", "没有相关员工信息！", QMessageBox.Yes)
            return False

    def delStaffOnTable(self, sid):
        """表格上直接删除"""
        # print("delete from staff where sid=\'{sid}\';".format(sid=sid))
        try:
            # self.cursor.execute("select * from team where check_in_sid=\'{sid}\';".format(sid=sid))
            # data = self.cursor.fetchall()
            # if len(data) > 0:
            #     return False
            print("update staff set sstate=0 where sid=\'{sid}\';".format(sid=sid))
            self.cursor.execute("update staff set sstate=0 where sid=\'{sid}\';".format(sid=sid))
            self.db.commit()
            return True
            # data = self.cursor.fetchall()
            # if len(data) > 0:
            #     return False
            # else:
            #     self.cursor.execute("delete from staff where sid=\'{sid}\';".format(sid=sid))
            #     self.db.commit()
            #     return True
        except Exception as e:
            print(e)
            return False

    def modifyStaffOnTable(self, row, column, value, sid):
        """表格上直接修改"""
        # 字典方法得到要修改的列
        SQL_COLUMN = ['sid', 'sname', 'ssex', 'stime', 'susername', 'spassword', 'srole', 'sidcard', 'sphone']
        try:
            print("update staff set {col}=\'{value}\' where sid=\'{sid}\';".format(col=SQL_COLUMN[column], value=value,
                                                                                   sid=sid))
            self.cursor.execute(
                "update staff set {col}=\'{value}\' where sid=\'{sid}\';".format(col=SQL_COLUMN[column], value=value,
                                                                                 sid=sid))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
