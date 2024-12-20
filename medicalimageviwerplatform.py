import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MedicalImageViewerPlatform(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Medical Image Viewer Platform v1.0.0")
        self.setGeometry(300, 300, 400, 400)

        # Create Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create Menubar
        self.menubar = self.menuBar()
        self.menubar.setNativeMenuBar(False)

        # File Menu
        self.create_file_menu()

        # Image Processing Menu
        self.create_image_processing_menu()

        # Help Menu
        self.create_help_menu()

        # Add Label to Layout
        self.create_label_CT_button(layout)

        # Status Bar
        self.statusBar().showMessage("Ready")

    def create_file_menu(self):
        file_menu = self.menubar.addMenu("파일")
        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(self.close)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_action)

    def create_image_processing_menu(self):
        imageprocessing_menu = self.menubar.addMenu("영상처리")
        self.contrast_action = QAction("Contrast")
        self.brightness_action = QAction("Brightness")
        self.gamma_action = QAction("Gamma")
        imageprocessing_menu.addAction(self.contrast_action)
        imageprocessing_menu.addAction(self.brightness_action)
        imageprocessing_menu.addAction(self.gamma_action)
        imageprocessing_menu.addSeparator()

    def create_help_menu(self):
        help_menu = self.menubar.addMenu("도움말")
        self.doc_action = QAction("Documentation")
        self.release_action = QAction("Release Notes")
        self.license_action = QAction("View License")
        help_menu.addSeparator()
        help_menu.addAction(self.doc_action)
        help_menu.addAction(self.release_action)
        help_menu.addAction(self.license_action)
        help_menu.addSeparator()

    def create_label_CT_button(self, layout):
        label_CT_open_button = QLabel("CT folder", self)
        label_CT_open_button.setAlignment(Qt.AlignCenter)
        font = label_CT_open_button.font()
        font.setFamily("Times New Roman")
        label_CT_open_button.setFont(font)
        layout.addWidget(label_CT_open_button)

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MedicalImageViewerPlatform()
    window.show()
    app.exec_()
