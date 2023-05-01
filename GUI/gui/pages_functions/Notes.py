from PyQt5.QtWidgets import  QWidget


from ui.pages.Notes import  Ui_Form

class Notes(QWidget):
    def __init__(self):
        super(Notes,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)



        self.notes_line = self.ui.lineEdit
        self.notes_line_btn = self.ui.pushButton_9

        self.notes_line_btn.clicked.connect(self.change)

    def change(self):
        text = self.notes_line.text()
        self.ui.textEdit.append(text)