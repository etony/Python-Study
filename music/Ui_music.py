# Form implementation generated from reading ui file 'C:\Users\tony\Desktop\eric\music.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(581, 458)
        Dialog.setSizeGripEnabled(True)
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 360, 441, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pbPause = QtWidgets.QPushButton(Dialog)
        self.pbPause.setGeometry(QtCore.QRect(30, 390, 75, 24))
        self.pbPause.setObjectName("pbPause")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 330, 381, 16))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(40, 70, 471, 192))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 290, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.hsVule = QtWidgets.QSlider(Dialog)
        self.hsVule.setGeometry(QtCore.QRect(170, 390, 160, 22))
        self.hsVule.setProperty("value", 50)
        self.hsVule.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.hsVule.setObjectName("hsVule")
        self.lb_time = QtWidgets.QLabel(Dialog)
        self.lb_time.setGeometry(QtCore.QRect(460, 360, 111, 16))
        self.lb_time.setObjectName("lb_time")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        # self.listWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        # self.listWidget.customContextMenuRequested.connect(self.generateMenu)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pbPause.setText(_translate("Dialog", "暂停"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_2.setText(_translate("Dialog", "添加mp3"))
        self.lb_time.setText(_translate("Dialog", "TextLabel"))

    def generateMenu(self, pos):
        menu = QtWidgets.QMenu()
        ico_del = QtGui.QIcon('del.png')
        ico_clear = QtGui.QIcon('clear.png') 
        self.item1 = menu.addAction(ico_del,u"删除")
        self.item2 = menu.addAction(ico_clear,u"清空")
        #menu.popup(QtGui.QCursor.pos())
        self.action = menu.exec(self.listWidget.mapToGlobal(pos))
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
