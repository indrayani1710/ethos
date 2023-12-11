import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow ,QPushButton , QLineEdit, QCheckBox
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt, QTimer, QDateTime
from datetime import datetime
from utilities.imgbutton import img_button
from utilities.timer import DateTimeWidget


import os
os.environ['QT_QPA_PLATFORM'] = 'eglfs'




class copyUser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.width = 480
        self.height = 800
        self.resize(480, 800)

        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap("images/background.png"))
        self.background_image.setGeometry(0, 0, self.width, self.height)

        self.copyUser = img_button(self, "images/icons/copyUserIcon50x50.png", 50, 50, [215, 34], self.close,"Delete", "#D9D9D9")
        self.copyUser.setEnabled(False)

        self.backbtnv2 = img_button(self, "images/icons/BackIcon.png", 30, 30, (5, 44), self.close,"", "#D9D9D9")


        cancel_btn = img_button(self, "images/icons/Cancel_btn.png", 100, 100, [147, 729], self.close,"Cancel", "#D9D9D9")
        cancel_btn.resize(85,35)

        copy_btn = img_button(self, "images/icons/copyBtn.png", 100, 100, [248, 729], self.close,"Delete", "#D9D9D9")      #TODO function to be added to delete.
        copy_btn.resize(85,35)

        #labels & textfields

        label = QLabel("ID", self)
        label.setStyleSheet("color: #808080")
        label.move(18, 101)

        self.ID_field = QLineEdit(self)
        self.ID_field.setFixedSize(355, 30)
        self.ID_field.move(108, 96)

        label = QLabel("Card", self)
        label.setStyleSheet("color: #808080")
        label.move(18, 140)
        # checkbox for Card
        self.cardCheckbox = QCheckBox(self)
        self.cardCheckbox.setGeometry(108, 135, 100, 40)
        self.cardCheckbox.setStyleSheet("QCheckBox::indicator""{""width : 20px;""height : 20px;""}"
                                        "QCheckBox::indicator:pressed""{""background-color : orange;""}")
        #self.cardCheckbox.move(108, 135)

        label = QLabel("Thumb", self)
        label.setStyleSheet("color: #808080")
        label.move(158, 140)
        # checkbox for Thumb
        self.thumbCheckbox = QCheckBox(self)
        self.thumbCheckbox.setGeometry(223, 135, 100, 40)
        self.thumbCheckbox.setStyleSheet("QCheckBox::indicator""{""width : 20px;""height : 20px;""}"
                                        "QCheckBox::indicator:pressed""{""background-color : orange;""}")
        #self.thumbCheckbox.move(223, 135)

        label = QLabel("Face", self)
        label.setStyleSheet("color: #808080")
        label.move(278, 140)
        # checkbox for Face
        self.faceCheckbox = QCheckBox(self)
        self.faceCheckbox.setGeometry(321, 135, 100, 40)
        self.faceCheckbox.setStyleSheet("QCheckBox::indicator""{""width : 20px;""height : 20px;""}"
                                        "QCheckBox::indicator:pressed""{""background-color : orange;""}")
        #self.faceCheckbox.move(321, 135)

        label = QLabel("Photo", self)
        label.setStyleSheet("color: #808080")
        label.move(382, 140)
        # checkbox for Photo
        self.photoCheckbox = QCheckBox(self)
        self.photoCheckbox.setGeometry(433, 135, 100, 40)
        self.photoCheckbox.setStyleSheet("QCheckBox::indicator""{""width : 20px;""height : 20px;""}"
                                        "QCheckBox::indicator:pressed""{""background-color : orange;""}")
        #self.photoCheckbox.move(433, 135)

        

        


    # to add condition for the checkboxes
    # def on_checkbox_state_change(state):
    #    if state == 2:  # 2 corresponds to Qt.Checked
    #        print("Checkbox is checked")
    #    else:
    #        print("Checkbox is unchecked")

    def openfoodMenu(self):
        from foodMenu import food_menu
        self.openfoodMenu = food_menu()
        self.openfoodMenu.show()
        self.close()

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = copyUser()
    datetime_widget = DateTimeWidget()
    window.show()
    sys.exit(app.exec_())