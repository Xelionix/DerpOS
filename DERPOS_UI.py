import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QTextBrowser, QMdiArea, QMdiSubWindow, QPushButton, QWidget, QVBoxLayout, QFileDialog

class DerpOSUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DerpOS")
        self.setGeometry(100, 100, 800, 600)

        menubar = self.menuBar()
        start_menu = menubar.addMenu("Start")

        settings_action = QAction("Settings", self)
        settings_action.triggered.connect(self.show_settings)
        start_menu.addAction(settings_action)

        file_manager_action = QAction("File Manager", self)
        file_manager_action.triggered.connect(self.show_file_manager)
        start_menu.addAction(file_manager_action)

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

    def show_settings(self):
        settings_dialog = SettingsDialog()
        self.mdi.addSubWindow(settings_dialog)
        settings_dialog.show()

    def show_file_manager(self):
        file_manager_dialog = FileManagerDialog()
        self.mdi.addSubWindow(file_manager_dialog)
        file_manager_dialog.show()

class PopupDialog(QMdiSubWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(200, 200, 400, 300)

        widget = QWidget()
        self.setWidget(widget)

class SettingsDialog(PopupDialog):
    def __init__(self):
        super().__init__("Settings")
        layout = QVBoxLayout()
        label = QTextBrowser()
        label.setPlainText("Customize your DerpOS settings here.")
        layout.addWidget(label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setWidget(widget)

class FileManagerDialog(PopupDialog):
    def __init__(self):
        super().__init__("File Manager")
        layout = QVBoxLayout()
        label = QTextBrowser()
        label.setPlainText("Manage your files and directories here.")
        layout.addWidget(label)
        open_file_button = QPushButton("Open File")
        open_file_button.clicked.connect(self.open_file)
        layout.addWidget(open_file_button)
        widget = QWidget()
        widget.setLayout(layout)
        self.setWidget(widget)

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)", options=options)
        if file_name:
            print(f"Opened file: {file_name}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DerpOSUI()
    window.show()
    sys.exit(app.exec_())
