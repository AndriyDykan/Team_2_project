from PyQt5.QtWidgets import  QWidget


from ui.pages.Adress import  Ui_Form

class Adress(QWidget):
    def __init__(self):
        super(Adress,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        self.adress_line = self.ui.lineEdit
        self.adress_line_btn = self.ui.pushButton_9

        self.adress_line_btn.clicked.connect(self.change)

    def change(self):
        text = self.adress_line.text()
        self.ui.textEdit.append(text)












