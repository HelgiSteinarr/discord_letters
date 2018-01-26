import sys
import os
import urllib.request, urllib.error
import csv

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainwindow.ui", self)

        self.main_window = self

        self.current_version = 0  # Changes after the update check function is run

        self.text_input = self.findChild(QLineEdit, "inputText")
        self.convert_button = self.findChild(QPushButton, "convertButton")
        self.output_box = self.findChild(QPlainTextEdit, "outputBox")
        self.copy_button = self.findChild(QPushButton, "copyButton")
        self.copy_label = self.findChild(QLabel, "copyLabel")
        self.clear_button = self.findChild(QPushButton, "clearButton")
        self.updateAvailableLabel = self.findChild(QLabel, "updateAvailableLabel")
        self.v_nr_label = self.findChild(QLabel, "versionNrLabel")
        self.update_button = self.findChild(QPushButton, "updateNowButton")

        update_available = self.check_for_updates()  # Return true or false

        self.v_nr_label.setText("V. " + str(self.current_version))

        if update_available:
            self.updateAvailableLabel.setText("UPDATE AVAILABLE")
            self.updateAvailableLabel.setStyleSheet("color: green;")

            self.update_button.pressed.connect(self.update_button_pressed)
        else:
            self.updateAvailableLabel.setText("")
            self.update_button.hide()

        self.convert_button.pressed.connect(self.convert_text)
        self.copy_button.pressed.connect(self.copy_button_pressed)
        self.clear_button.pressed.connect(self.clear_button_pressed)

        self.copy_label.setText("")  # sets the label as blank

        self.number_dict = {0: ":zero:", 1: ":one:", 2: ":two:", 3: ":three:", 4: ":four:", 5: ":five:", 6: ":six:",
                            7: ":seven:", 8: ":eight:", 9: ":nine:", 10: ":ten:"}
        self.alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                           "s", "t", "u", "v", "w", "x", "y", "z"]

    def convert_text(self):
        print("first")
        self.output_box.setPlainText("")
        data_string = ""
        print("dr1")
        for char in self.text_input.text():
            print("dr2")
            try:
                int(char) + 0

                for key, value in self.number_dict.items():
                    if int(char) == key:
                        data_string += value + " "
            except ValueError:
                if char.lower() in self.alpha_list:
                    data_string += ":regional_indicator_" + char.lower() + ": "
                elif char == " ":
                    data_string += "      "
                else:
                    msgbox = QMessageBox()
                    msgbox.setWindowTitle("Error")
                    msgbox.setIcon(QMessageBox.Warning)
                    msgbox.setText("\nConverting the letter '" + char + "' did not work properly.. please either remove"
                                                                        " or change that letter.\n")
                    msgbox.setDefaultButton(QMessageBox.Ok)
                    msgbox.exec_()

        self.output_box.setPlainText(data_string)
        self.copy_label.setText("")

    def copy_button_pressed(self):

        if len(self.output_box.document().toPlainText()) < 1:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Warning")
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setText("\nNo text in output box\n")
            msgbox.setDefaultButton(QMessageBox.Ok)

            msgbox.exec_()

        else:
            try:
                command = 'echo ' + self.output_box.document().toPlainText() + ' | clip'
                os.system(command)
                self.copy_label.setText("Copied to clipboard")
                self.copy_label.setStyleSheet("color: green;")
            except:
                self.copy_label.setText("Copy failed")
                self.copy_label.setStyleSheet("color: red;")

    def clear_button_pressed(self):
        self.output_box.setPlainText("")
        self.copy_label.setText("")
        self.text_input.setText("")

    def update_button_pressed(self):
        print("b4")
        os.system("start updater.exe")
        print("after")
        sys.exit()

    def check_for_updates(self):
        try:
            new_version = 0
            # Temp folder created with the newest version number
            local_filename, headers = urllib.request.urlretrieve('http://helgisteinarr.com/discord_letters/version'
                                                                 '/newest_version')
            with open(local_filename, "r") as version_file:
                data = csv.reader(version_file, delimiter=",")
                for i in data:
                    new_version = i[0]
                version_file.close()

            with open("version", "r") as version_file:
                self.current_version = version_file.read()
                version_file.close()

            print("current v:" + self.current_version)
            print("new v:" + new_version)
            if new_version > self.current_version:
                return True
            else:
                return False
        except urllib.error.URLError:
            pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
