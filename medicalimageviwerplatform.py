import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

#    Functions   ==============================================================


#      Class     ==============================================================
#  class naming: as you wish Upper case - lower case

class MedicalImageViewerPlatform(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Image Viewer Platform v1.0.0")
        self.setGeometry(300, 300, 400, 400)
        # Create Menubar
        self.menubar = self.menuBar()
        self.menubar.setNativeMenuBar(False)
        # MenuActions
        #    FileMenuActions
        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(self.close)
        #    ImageProcessingMenuActions
        self.contrast_action = QAction("Contrast")
        self.brightness_action = QAction("Brightness")
        self.gamma_action = QAction("Gamma")
        #    ViewMenuActions
        #    HelpMenuActions
        self.doc_action = QAction("Documentation")
        self.release_action = QAction("Release Notes")
        self.license_action = QAction("View License")

        # Align menus
        file_menu = self.menubar.addMenu("파일")
        file_menu.addSeparator()
        file_menu.addAction(self.quit_action)

        imageprocessing_menu = self.menubar.addMenu("영상처리")
        self.contrast_action.addAction(self.contrast_action)
        self.brightness_action.addAction(self.brightness_action)
        self.gamma_action.addAction(self.gamma_action)
        imageprocessing_menu.addSeparator()
        
        help_menu = self.menubar.addMenu("도움말")
        help_menu.addSeparator()
        help_menu.addAction(self.doc_action)
        help_menu.addAction(self.release_action)
        help_menu.addAction(self.license_action)

#      Main      ==============================================================
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MedicalImageViewerPlatform()
    window.show()
    app.exec_()