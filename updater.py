import sys
import os
import urllib.request, urllib.error

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep


class UpdateWindow(QMainWindow):

    def __init__(self):
        super(UpdateWindow, self).__init__()
        loadUi("updatewindow.ui", self)

        self.progress_bar = self.findChild(QProgressBar, "downloadProgressBar")
        self.progress_bar.setValue(0)

        self.thread_class = ThreadClass()
        self.thread_class.start()
        self.thread_class.update_progressbar.connect(self.update_progressbar)

        self.completed = None

    def update_bar(self, val):
        self.progress_bar.setValue(val)


class ThreadClass(QThread):
    def __init__(self):
        super(ThreadClass, self).__init__()
        self.completed = None
        self.update_progressbar = pyqtSignal(float)

    def run(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        connection = urllib.request.URLopener()
        connection.retrieve("http://helgisteinarr.com/discord_letters/testfile.txt", dir_path + "testfile.txt",
                            reporthook=self.status)

    def status(self, count, blockSize, totalSize):
        self.completed = int(count * blockSize * 100 / totalSize)
        self.update_progressbar.emit(self.completed)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = UpdateWindow()
    window.show()

    UpdateWindow.retrieve_file(window)
    sys.exit(app.exec_())
