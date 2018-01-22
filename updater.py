import sys
import os
import urllib, urllib.request, urllib.error

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import QThread, pyqtSignal


class UpdateWindow(QMainWindow):

    def __init__(self):
        super(UpdateWindow, self).__init__()
        loadUi("updatewindow.ui", self)

        self.progress_bar = self.findChild(QProgressBar, "downloadProgressBar")
        self.filename_label = self.findChild(QLabel, "filenameLabel")
        self.progress_bar.setValue(0)
        self.filename_label.setText("")

        self.thread_class = ThreadClass()
        self.thread_class.start()
        self.thread_class.update_progressbar.connect(self.update_bar)
        self.thread_class.update_filename.connect(self.update_filename)

        self.completed = None

    def update_bar(self, val):
        self.progress_bar.setValue(val)

    def update_filename(self, filename):
        self.filename_label.setText(filename)


class ThreadClass(QThread):

    update_progressbar = pyqtSignal(float)
    update_filename = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        connection = urllib.request.URLopener()
        self.file_name = "main.exe"
        connection.retrieve("http://helgisteinarr.com/discord_letters/main.exe",
                            os.path.join(dir_path, "testfile.txt"), reporthook=self.status)
        self.status(1, 100, 100)
        self.file_name = "mainwindow.ui"
        connection.retrieve("http://helgisteinarr.com/discord_letters/mainwindow.ui",
                            os.path.join(dir_path, "testfile.txt"), reporthook=self.status)
        self.status(1, 100, 100)
        self.file_name = "updatewindow.ui"
        connection.retrieve("http://helgisteinarr.com/discord_letters/updatewindow.ui",
                            os.path.join(dir_path, "testfile.txt"), reporthook=self.status)
        self.status(1, 100, 100)
        self.file_name = "dl_logo.png"
        connection.retrieve("http://helgisteinarr.com/discord_letters/dl_logo.png",
                            os.path.join(dir_path, "testfile.txt"), reporthook=self.status)
        self.status(1, 100, 100)
        os.system("start main.exe")
        sys.exit()

    def status(self, count, blockSize, totalSize):
        print(count)
        print(blockSize)
        print(totalSize)
        completed = int(count * blockSize * 100 / totalSize)
        self.update_progressbar.emit(completed)
        self.update_filename.emit(self.file_name)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = UpdateWindow()
    window.show()
    sys.exit(app.exec_())
