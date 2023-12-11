import sys
from gui.device_splashscreen import SplashWindow
from PySide6.QtWidgets import QApplication
from datetime import datetime
import os


def main():
    print("ethos firmware started")
    os.environ['QT_QPA_PLATFORM'] = 'eglfs'
    app = QApplication(sys.argv)
    window = SplashWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    # This block will only be executed if the script is run directly, not if it's imported
    main()
