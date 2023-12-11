import sys
from datetime import datetime

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit

from .utilities.keyboard import VirtualKeyboard
from .utilities.imgbutton import img_button
#from RD_Ops1 import RFIDDatabaseOperations

import os

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        current_directory=os.getcwd()
        # Set window dimensions
        self.width = 480
        self.height = 800
        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Set background image
        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap(os.path.join(current_directory, "gui/assets/background.png")))
        self.background_image.setGeometry(0, 0, self.width, self.height)
        # Create label for date and time
        self.date_time_label = QLabel(self)
        self.date_time_label.setGeometry(5, 4, 190, 20)
        # Set font for date and time label
        font_small = QFont("inika", 15, QFont.Bold)
        self.date_time_label.setFont(font_small)
        # Initial date and time display
        self.update_date_time()

    def eventFilter(self, obj, event):
        if obj == self.password_field and event.type() == QtCore.QEvent.MouseButtonPress:
            self.virtual_keyboard.text_edit.setPlainText(self.password_field.text())
            if self.virtual_keyboard.exec_() == QtWidgets.QDialog.Accepted:
                self.password_field.setText(self.virtual_keyboard.text_edit.toPlainText())
        return super().eventFilter(obj, event)

    def update_date_time(self):
        # Get current date and time
        current_datetime = datetime.now()

        # Format the date as "14th June 2023"
        formatted_date = current_datetime.strftime("%d{} %B %Y").format(
            "th" if 10 <= current_datetime.day <= 19 else
            {1: "st", 2: "nd", 3: "rd"}.get(current_datetime.day % 10, "th")
        )

        # Get the current day
        current_day = current_datetime.strftime("%A")

        # Format the time as "hh:mm:ss"
        formatted_time = current_datetime.strftime("%H:%M:%S")

        # Update date and time labels
        current_datetime_str = f"{formatted_date} - {formatted_time}"
        self.date_time_label.setText(current_datetime_str)

        self.backbtn = img_button(self, "assets/icons/BackIcon.png", 30,30, (5, 44), self.openSplashScreen,"", "#D9D9D9")

        # Create the label
        label = QLabel("Password", self)
        label.setStyleSheet("color: #808080")
        label.move(18, 106)

        # Create the password field
        self.password_field = QLineEdit(self)
        self.password_field.setPlaceholderText("here")
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.textChanged.connect(self.verify_password)
        self.password_field.setFixedSize(355, 30)
        self.password_field.move(108, 100)
        self.password_field.installEventFilter(self)
        self.virtual_keyboard = VirtualKeyboard(self.password_field)



        self.deviceMenu = img_button(self,"gui/images/icons/DeviceIcon.png", 55, 100, (18, 142), self.close, "Device", "#D9D9D9")
        self.deviceMenu.setEnabled(False)

        self.UserMenu = img_button(self, "gui/images/icons/UserIcon.png", 55, 100, (133, 142), self.openUserScreen,"User", "#D9D9D9")
        self.UserMenu.setEnabled(False)

        self.CommMenu = img_button(self, "gui/images/icons/CommIcon.png", 55, 100, (248, 142), self.openComm,"Comm", "#D9D9D9")
        self.CommMenu.setEnabled(False)

        self.LogMenu = img_button(self, "gui/images/icons/DeviceIcon.png", 55, 100, (363, 142), self.close,"Log","#D9D9D9")
        self.LogMenu.setEnabled(False)

        self.PrinterMenu = img_button(self, "gui/images/icons/printerIcon.png", 55, 100, (18, 264), self.close,"Printer","#D9D9D9")
        self.PrinterMenu.setEnabled(False)

        self.VerifyButton = img_button(self, "gui/images/icons/UserVerifyIcon.png", 55, 100, (133, 264), self.UserVerification,"Verify User","#D9D9D9")
        self.VerifyButton.setEnabled(False)

        self.canteen = img_button(self, "gui/images/icons/CanteenIcon.png", 55, 100, (248, 264), self.openCanteenMenu, "Canteen", "#D9D9D9")
        self.canteen.setEnabled(False)

    def verify_password(self):
        password = self.password_field.text()
        print("Entered Password:", password)

        # Perform password verification logic here
        # For example, check if the password matches a predefined value
        # TODO password to be done dynamically.
        expected_password = "ADMIN"
        is_password_matched = (password == expected_password)
        print("Password Matched:", is_password_matched)

        # Enable or disable buttons based on password verification result
        self.deviceMenu.setEnabled(is_password_matched)
        self.UserMenu.setEnabled(is_password_matched)
        self.CommMenu.setEnabled(is_password_matched)
        self.LogMenu.setEnabled(is_password_matched)
        self.VerifyButton.setEnabled(is_password_matched)
        self.canteen.setEnabled(is_password_matched)

    def openUserScreen(self):
        from UserMenu import UserWindow
        self.openUserScreen = UserWindow()
        self.openUserScreen.show()
        self.close()

    def openSplashScreen(self):
        from epitage import SplashWindow
        openSplashScreen = SplashWindow()
        openSplashScreen.show()
        self.close()

    def UserVerification(self):
        from userverification_1 import CardVerificatiion
        self.UserVerification = CardVerificatiion()
        self.UserVerification.show()
        self.close()

    def openCanteenMenu(self):
        from canteen_main import canteenMain
        self.openCanteenMenu = canteenMain()
        self.openCanteenMenu.show()
        self.close()

    def openComm(self):
        from CommsManagement import comm_man
        self.openComm = comm_man()
        self.openComm.show()
        self.close()


class BackgroundThread(QtCore.QThread):
    def __init__(self, rfid_operations):
        super().__init__()
        self.rfid_operations = rfid_operations

    def run(self):
        self.rfid_operations.run_operations()

    def stop(self):
        self.rfid_operations.stop_operations()


