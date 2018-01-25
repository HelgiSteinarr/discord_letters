import sys
import os
import urllib
import urllib.request
import urllib.error
import csv

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
        self.file_name = None  # don't you love PEP8...

    def __del__(self):
        self.wait()

    def run(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        connection = urllib.request.URLopener()
        self.file_name = "main.exe"
        connection.retrieve("http://helgisteinarr.com/discord_letters/main.exe",
                            os.path.join(dir_path, "main.exe"), reporthook=self.status)
        self.status(1, 100, 100)
        self.file_name = "mainwindow.ui"
        connection.retrieve("http://helgisteinarr.com/discord_letters/mainwindow.ui",
                            os.path.join(dir_path, "mainwindow.ui"), reporthook=self.status)
        self.status(1, 100, 100)
        self.file_name = "updatewindow.ui"
        connection.retrieve("http://helgisteinarr.com/discord_letters/updatewindow.ui",
                            os.path.join(dir_path, "updatewindow.ui"), reporthook=self.status)
        self.status(1, 100, 100)
        self.file_name = "dl_logo.png"
        connection.retrieve("http://helgisteinarr.com/discord_letters/dl_logo.png",
                            os.path.join(dir_path, "dl_logo.png"), reporthook=self.status)
        self.status(1, 100, 100)

        # TODO: change version number in version file after update
        local_filename, headers = urllib.request.urlretrieve('http://helgisteinarr.com/discord_letters/version'
                                                             '/newest_version')
        new_version = None
        with open(local_filename, "r") as version_file:
            data = csv.reader(version_file, delimiter=",")
            for i in data:
                new_version = i[0]
            version_file.close()
        with open("version", "w") as version_file:
            version_file.write(new_version)
            version_file.close()

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
