import psycopg2
from psycopg2 import extras
from dao.dbConfig import localSourceConfig as localConfig
from service import globalValue

class Client:
    """客户信息操作类"""
    def __init__(self,config=localConfig):
        self.db = psycopg2.connect(dbname="postgres",
                                   user="lian",
                                   password="Bigdata@123",
                                   host="120.46.130.234",
                                   port="26000")
        self.cursor = self.db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        # self.cursor.execute("SELECT VERSION()")
        # data = self.cursor.fetchone()
        # print("Database version : %s " % data['VERSION()'])ERSION()")
        # data = self.cursor.fetchone()
        # print("Database version : %s " % data['VERSION()'])
        self.staff = globalValue.get_staff()

    def tableDelDB(self,type,id):
        """直接表格上进行删除"""
        if type == '个人':
            try:
                self.cursor.execute("delete from client where cid=%s",(id))
                self.db.commit()
                return True
            except Exception as e:
                print("erro")
                print(e)
                return False
        elif type == '团队':
            try:
                self.cursor.execute("delete from team where ttid=%s",(id))
                self.db.commit()
                return True
            except Exception as e:
                print(e)
                return False


    def findClient(self,type,name,times):
        """直接表格上进行修改"""
        name = '%' + str(name) + '%'
        print(times)
        if type == '个人':
            self.cursor.execute("select * from client where cname like %s and accomodation_times>=%s",(name,int(times)))
            data = self.cursor.fetchall()
            return data
        elif type == '团队':
            self.cursor.execute("select * from team where tname like %s and accomodation_times>=%s",(name,int(times)))
            data = self.cursor.fetchall()
            return data

    def addClientDB(self,cname,cid,cphone,cage,csex):
        """增加客户"""
        try:
            self.cursor.execute("insert into client(cname,cid,cphone,cage,csex,register_sid,accomodation_times) values(%s,%s,%s,%s,%s,%s,%s)",
                                (cname,cid,cphone,cage,csex,self.staff.sid,0))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False


    def addTeamDB(self,tname,ttid,tphone):
        """增加团体"""
        try:
            self.cursor.execute("insert into team(tname,ttid,tphone,check_in_sid,accomodation_times) values(%s,%s,%s,%s,%s)",
                                (tname,ttid,tphone,self.staff.sid,0))
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
