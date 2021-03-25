from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
import sys
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUiType
import os
import shutil
from time import sleep

ui, _ = loadUiType('main.ui')


class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        self.setWindowIcon(QIcon('Resources/icon.ico'))
        self.setWindowTitle('Easy File(Beta v1.0.2)')
        self.setFixedSize(800, 312)

    def about_message(self):
        QMessageBox.information(self, 'Beta Version', """Thank you for choosing the application. Please be aware that this is a beta version and it never reflects the final quality
Please, if you encounter any problem, restart the application
Or send it to me
islam.kamel@agr.svu.edu.eg
Thank you""")

    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.Handel_Browse)
        self.pushButton_2.clicked.connect(self.Proc_Files)

    def Handel_Browse(self):
        select_folder = QFileDialog.getExistingDirectory(self, caption='Select Folder', directory='/')
        self.lineEdit.setText(select_folder)
        QApplication.processEvents()
        return select_folder

    def Tracking_Proc(self):
        # self.plainTextEdit.setPlainText('islam')
        pass

    def Proc_Files(self):
        logo = 'Logo'
        icon = 'Icons'
        png = 'PNG Image'
        photo = 'Image\'s'
        document = 'Documents'
        program = 'Programs'
        compressed = 'Compressed'
        font = 'Fonts'
        svg = 'SVG'
        work_place = self.lineEdit.text()
        os.chdir(work_place)

        self.Logo_File(work_place, logo)
        # sleep(0.05)
        self.Icon_File(work_place, icon)
        # sleep(0.05)
        self.PNG_File(work_place, png)
        # sleep(0.05)
        self.Jpg_and_other_Photo(work_place, photo)
        # sleep(0.05)
        self.Documents_File(work_place, document)
        # sleep(0.05)
        self.EXE_File(work_place, program)
        # sleep(0.05)
        self.Fonts_File(work_place, font)
        # sleep(0.05)
        self.SVG_File(work_place, svg)
        # sleep(0.05)
        self.Compressed_File(work_place, compressed)
        self.Font_family(work_place, font)
        # sleep(0.01)
        self.about_message()

    try:
        def Logo_File(self, work_place, folder):
            for file in os.listdir(work_place):
                if 'logo' in file.lower() and not os.path.isdir(file):
                    file_found = True
                    if not os.path.exists(folder):
                        os.mkdir(folder)
                    shutil.copy(file, folder)
                    os.remove(file)
                    self.plainTextEdit.appendPlainText(f'{file} Move To {work_place}/{folder} success')
                    QApplication.processEvents()
            sleep(0.1)

        def Icon_File(self, work_place, folder):
            for file in os.listdir(work_place):
                if 'icon' in file.lower() and not os.path.isdir(file):
                    if not os.path.exists(folder):
                        os.mkdir(folder)
                    shutil.copy(file, folder)
                    os.remove(file)
                    self.plainTextEdit.appendPlainText(f'{file} Move To {work_place}/{folder} success')
                    QApplication.processEvents()
            sleep(0.1)

        def PNG_File(self, work_place, folder):
            for file in os.listdir(work_place):
                if file.endswith('.png') and not os.path.isdir(file):
                    if not os.path.exists(folder):
                        os.mkdir(folder)
                    shutil.copy(file, folder)
                    os.remove(file)
                    self.plainTextEdit.appendPlainText(f'{file} Move To {work_place}/{folder} success')
                    QApplication.processEvents()
            sleep(0.1)

        def Jpg_and_other_Photo(self, work_place, folder):
            for file in os.listdir(work_place):
                if file.endswith(('.jpj', '.jpg', '.jfif', '.jpeg')) and not os.path.isdir(file):
                    if not os.path.exists(folder):
                        os.mkdir(folder)
                    shutil.copy(file, folder)
                    os.remove(file)
                    self.plainTextEdit.appendPlainText(f'{file} Move To {work_place}/{folder} success')
                    QApplication.processEvents()
            sleep(0.1)

        def Documents_File(self, work_place, folder):
            for file in os.listdir(work_place):
                if file.endswith(('.doc', '.docx', '.odt', '.pdf', '.xls', '.xlsx', '.ods', '.ppt', '.pptx',
                                  '.txt')) and not os.path.isdir(file):
                    if not os.path.exists(folder):
                        os.mkdir(folder)
                    shutil.copy(file, folder)
                    os.remove(file)
                    self.plainTextEdit.appendPlainText(f'{file} Move To {work_place}/{folder} success')
                    QApplication.processEvents()
            sleep(0.1)

        def EXE_File(self, work_place, folder):
            for file in os.listdir(work_place):
                if file.endswith('.exe') and not os.path.isdir(file):
                    if not os.path.exists(folder):
                        os.mkdir(folder)
                    shutil.copy(file, folder)
                    os.remove(file)
                    self.plainTextEdit.appendPlainText(f'{file} Move To {work_place}/{folder} success')
                    QApplication.processEvents()
            sleep(0.1)

        def Compressed_File(self, work_place, folder):
            for file in os.listdir(work_place):
                if file.endswith(('.rar', '.7z', '.tar', '.ar', '.a', '.s7z', '.gzip', '.rte', '.pup', '.deb', '.mpkg',
                                  '.zip')) and not os.path.isdir(file):
                    if not os.path.exists(folder):
                        os.mkdir(folder)
                    shutil.copy(file, folder)
                    os.remove(file)
                    self.plainTextEdit.appendPlainText(f'{file} Move To {work_place}/{folder} success')
                    QApplication.processEvents()
            sleep(0.1)

        def Fonts_File(self, work_place, folder):
            for file in os.listdir(work_place):
                if file.endswith(
                        ('.ttf', '.otf', '.woff', '.woff2', '.eot', '.TTF')) and not os.path.isdir(file):
                    if not os.path.exists(folder):
                        os.mkdir(folder)
                    shutil.copy(file, folder)
                    os.remove(file)
                    self.plainTextEdit.appendPlainText(f'{file} Move To {work_place}/{folder} success')
                    QApplication.processEvents()
            sleep(0.1)

        def SVG_File(self, work_place, folder):
            for file in os.listdir(work_place):
                if file.endswith('.svg') and not os.path.isdir(file):
                    if not os.path.exists(folder):
                        os.mkdir(folder)
                    shutil.copy(file, folder)
                    os.remove(file)
                    self.plainTextEdit.appendPlainText(f'{file} Move To {work_place}/{folder} success')
                    QApplication.processEvents()
            sleep(0.1)

        # def Font_family(work_place, folder):
        #     if os.path.exists(folder):
        #         os.chdir(f'{work_place}/{folder}')
        #         for file in os.listdir(f'{work_place}/{folder}'):
        #             if '-' in file:
        #                 name = file.split('-')
        #                 font_family = name[0]
        #                 if not os.path.exists(font_family):
        #                     os.mkdir(font_family)
        #                 try:
        #                     if font_family in file and not os.path.isdir(file):
        #                         shutil.copy(file, font_family)
        #                         os.remove(file)
        #                 except FileNotFoundError:
        #                     continue
        #
        #             if '_' in file:
        #                 name = file.split('_')
        #                 font_family = name[0]
        #                 if not os.path.exists(font_family):
        #                     os.mkdir(font_family)
        #                 try:
        #                     if font_family in file and not os.path.isdir(file):
        #                         shutil.copy(file, font_family)
        #                         os.remove(file)
        #                 except FileNotFoundError:
        #                     continue
        #             if ' ' in file:
        #
        #                 if not os.path.exists(font_family):
        #                     os.mkdir(font_family)
        #                 try:
        #                     if font_family in file and not os.path.isdir(file):
        #                         shutil.copy(file, font_family)
        #                         os.remove(file)
        #                 except FileNotFoundError:
        #                     continue
        #             else:
        #                 name = file.split('.')
        #                 font_family = name[0]
        #                 if not os.path.exists(font_family):
        #                     os.mkdir(font_family)
        #                 try:
        #                     if font_family in file and not os.path.isdir(file):
        #                         shutil.copy(file, font_family)
        #                         os.remove(file)
        #                 except FileNotFoundError:
        #                     continue

    except Exception:
        pass
        # sort font by name in folder
        # Font_family(work_place, folder)


#


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
