import sys
from PySide6.QtWidgets import QLabel, QMainWindow, QPushButton
from PySide6.QtGui import QPixmap, QFont, QIcon
from PySide6.QtCore import Qt, QTimer
from datetime import datetime
from .utilities.imgbutton import img_button
import subprocess
import os

class SplashWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        current_directory=os.getcwd()
        # Set window dimensions
        #TODO to convert this into parameters
        self.width = 480
        self.height = 800
        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Set background image
        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap(os.path.join(current_directory,"gui/assets/background.png")))
        self.background_image.setGeometry(0, 0, self.width, self.height)

        # Create label for date and time
        self.date_time_label = QLabel(self)
        self.date_time_label.setGeometry(5, 4, 190, 20)

        # Set font for date and time label
        font_small = QFont("inika", 15, QFont.Bold)
        self.date_time_label.setFont(font_small)

        # Set font for date and time label
        font_big = QFont("inika", 20, QFont.Normal)

        self.logoImage = QLabel(self)
        self.logoImage.setPixmap(QPixmap(os.path.join(current_directory,"gui/assets/EpitageLogo_final.png")))
        self.logoImage.setGeometry(50,154,381,277)

        # Create label for additional date
        self.additional_date_label = QLabel(self)
        self.additional_date_label.setGeometry(50, 509, 380,26)
        self.additional_date_label.setAlignment(Qt.AlignHCenter)
        self.additional_date_label.setFont(font_small)
        #self.additional_date_label.setAlignment(Qt.AlignVCenter)

        # Create label for time
        self.time_label = QLabel(self)
        self.time_label.setGeometry(205, 547, 300, 30)
        self.time_label.setFont(font_small)

        self.menu_btn = img_button(self, os.path.join(current_directory,"gui/assets/icons/MenuIcon.png"), 75, 100, (190, 623), self.openMenuScreen, "Menu", "#D9D9D9")

        # Update date and time every second 
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)

        # Initial date and time display
        self.update_date_time()

        #TODO making the timer function into a reusable function
        #app.installEventFilter(self)
        # Create a button for shutdown and reboot with an image
        self.shutdown_reboot_button = QPushButton(self)
        self.shutdown_reboot_button.setGeometry(5, 44, 30, 30)  # Position and size of the button

        # Load and set the button's image
        image_path = os.path.join(current_directory,"gui/assets/icons/shutdown_button.png")  # Replace with the actual path to your image
        pixmap = QPixmap(image_path)
        self.shutdown_reboot_button.setIcon(QIcon(pixmap))
        self.shutdown_reboot_button.setIconSize(pixmap.size())

        # Remove the rectangular frame and arrow
        self.shutdown_reboot_button.setFlat(True)

        # Set a blank style sheet to remove any potential unwanted styles
        self.shutdown_reboot_button.setStyleSheet("QPushButton { border: none; }")

        # Disable focus indicator and border
        #self.shutdown_reboot_button.setFocusPolicy(Qt.NoFocus)

    '''
    def eventFilter(self, obj, event):      # Debugging script for 2 cursors . this function prints out events on the raspi terminal.
        # Custom event handler to intercept and print events
        print("Event:", event.type(), "Target:", obj)
        return super().eventFilter(obj, event)

    '''

    def shutdown_device(self):
        # Execute the shutdown command
        subprocess.run(["sudo", "shutdown", "-h", "now"])

    def reboot_device(self):
        # Execute the reboot command
        subprocess.run(["sudo", "reboot"])
    
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
        self.additional_date_label.setText(f"{current_day} , {formatted_date}")
        self.time_label.setText(formatted_time)

    def openMenuScreen(self):
        from .device_menu import MenuWindow
        self.openMenuScreen = MenuWindow()
        self.openMenuScreen.show()    
