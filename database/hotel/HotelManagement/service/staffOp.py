from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from ui.staff import Ui_MainWindow
from dao.dbOpStaff import Staff
from service import globalValue


class StaffOP(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(StaffOP, self).__init__(parent)
        self.setupUi(self)
        self.inputdate.setCalendarPopup(True)
        self.stackedWidget.setCurrentIndex(0)
        self.staff = globalValue.get_staff()
        self.welcome.setText(self.staff.sname)
        self.role.setText('权限：' + self.staff.srole)
        self.name.setText(self.staff.sname)
        self.sname.setText(self.staff.sname)
        self.ssex.setText(self.staff.ssex)
        self.srole.setText(self.staff.srole)
        self.stime.setText(str(self.staff.stime))
        self.sphone.setText(self.staff.sphone)
        self.sidcard.setText(self.staff.sidcard)
        self.sidcard_2.setText(self.staff.sid)
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 绑定事件
        self.searchNB.clicked.connect(self.searchStaff)
        self.commitAdd.clicked.connect(self.addStaff)
        self.commitDe.clicked.connect(self.deleteStaff)
        self.commitTableDel.clicked.connect(self.tableDel)
        self.commitTableModify.clicked.connect(self.tableModify)

    def searchStaff(self):
        sname = str(self.searchName.text())
        s_sname = '%' + sname + '%'
        if int(self.staff.srole) > 1:
            self.data = self.staff.getStaff(s_sname)
            if type(self.data) == bool:
                self.showAllStaff()
                QMessageBox().information(None, "提示", "查询为空！", QMessageBox.Yes)
                return

            self.rowNum = len(self.data)
            if self.rowNum == 0:
                self.showAllStaff()
                QMessageBox().information(None, "提示", "查询为空！", QMessageBox.Yes)
                return
            self.columnNum = len(self.data[0])

            self.searchTable.setRowCount(self.rowNum)
            self.searchTable.setColumnCount(self.columnNum)
            for i, da in enumerate(self.data):
                # 字典转列表
                da = list(da.values())
                for j in range(self.columnNum):
                    self.itemContent = QTableWidgetItem(('%s') % (da[j]))
                    self.searchTable.setItem(i, j, self.itemContent)
        else:
            QMessageBox().information(None, "提示", "权限不符合要求！", QMessageBox.Yes)

    def addStaff(self):
        # 返回值是列表
        sid = self.inputsid.text().split()
        sname = self.inputname.text().split()
        if self.inputmale.isChecked():
            ssex = '男'
        elif self.inputfemale.isChecked():
            ssex = '女'
        else:
            ssex = ''
        stime = self.inputdate.date().toPyDate()
        susername = self.inputuser.text().split()
        spwd = self.inputpwd.text().split()
        srole = self.inputrole.text().split()
        sidcard = self.inputidcard.text().split()
        sphone = self.inputphone.text().split()
        if sid == '' or ssex == '' or sname == '' or stime == '' or susername == '' or spwd == '' \
                or srole == '' or sidcard == '' or sphone == '':
            QMessageBox().information(None, "提示", "信息不能为空！", QMessageBox.Yes)
            return False
        if int(self.staff.srole) > 1:
            ret = self.staff.addStaff(sid[0], sname[0], ssex, stime, susername[0], spwd[0], srole[0], sidcard[0],
                                      sphone[0])
            if ret:
                QMessageBox().information(None, "提示", "添加成功！", QMessageBox.Yes)
        else:
            QMessageBox().information(None, "提示", "权限不符合要求！", QMessageBox.Yes)

    def showAllStaff(self):
        self.data = self.staff.getStaff('%')

        self.rowNum = len(self.data)
        self.columnNum = len(self.data[0])
        self.deleteTable.setRowCount(self.rowNum)
        self.deleteTable.setColumnCount(self.columnNum)
        for i, da in enumerate(self.data):
            # 字典转列表
            da = list(da.values())
            for j in range(self.columnNum):
                self.itemContent = QTableWidgetItem(('%s') % (da[j]))
                self.deleteTable.setItem(i, j, self.itemContent)

    def deleteStaff(self):
        self.showAllStaff()
        sid = str(self.desid.text())
        sname = str(self.dename.text())
        sidcard = str(self.deidcard.text())

        if sid == '' or sname == '':
            QMessageBox().information(None, "提示", "信息不能为空！", QMessageBox.Yes)
            return False
        if int(self.staff.srole) > 1:
            s = Staff()
            ret = s.deleteStaff(sid, sname, sidcard)
            if ret:
                print("删除员工 %s 成功！", (sname))
            self.showAllStaff()
            QMessageBox().information(None, "提示", "删除成功！", QMessageBox.Yes)
            return True
        else:
            QMessageBox().information(None, "提示", "权限不符合要求！", QMessageBox.Yes)
            return False

    def tableDel(self):
        row_selected = self.searchTable.selectedItems()
        if len(row_selected) == 0:
            return
        row = row_selected[0].row()
        sid = self.searchTable.item(row,0).text()
        print("del on table sid:"+sid)
        # 标志是否删除成果
        flag = self.staff.delStaffOnTable(sid)
        if flag:
            self.searchTable.removeRow(row)
            QMessageBox().information(None, "提示", "删除成功！", QMessageBox.Yes)
        else:
            QMessageBox().information(None, "提示", "该员工暂有任务未处理完，不许离职！", QMessageBox.Yes)
    def tableModify(self):
        row_selected = self.searchTable.selectedItems()

        if len(row_selected) == 0:
            return
        row = row_selected[0].row()
        column = row_selected[0].column()
        value = self.modifyvalue.text()
        sid = self.searchTable.item(row,0).text()
        self.staff.modifyStaffOnTable(row, column, value,sid)
        tvalue = QTableWidgetItem(('%s') % (value))

        self.searchTable.setItem(row, column, tvalue)
        QMessageBox().information(None, "提示", "修改成功！", QMessageBox.Yes)
