import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QPushButton, QTextEdit


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My PyQt App")

        # Create a central widget for the window
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a grid layout for the central widget
        grid_layout = QGridLayout(central_widget)

        # Create a label and add it to the grid layout
        label = QLabel("Enter some text:")
        grid_layout.addWidget(label, 0, 0)

        # Create a text edit widget and add it to the grid layout
        text_edit = QTextEdit()
        grid_layout.addWidget(text_edit, 1, 0)

        # Create a button and add it to the grid layout
        button = QPushButton("Process text")
        grid_layout.addWidget(button, 2, 0)

        # Connect the button to a slot method
        button.clicked.connect(
            lambda: self.process_text(text_edit.toPlainText()))

    def process_text(self, text):
        # Process the text here
        processed_text = text.upper()

        # Create a new window to display the processed text
        new_window = QMainWindow()
        new_window.setWindowTitle("Processed Text")
        new_window.setGeometry(100, 100, 400, 400)

        # Create a central widget for the new window
        central_widget = QWidget(new_window)
        new_window.setCentralWidget(central_widget)

        # Create a label to display the processed text
        label = QLabel(processed_text, central_widget)
        label.setGeometry(10, 10, 380, 380)

        # Show the new window
        new_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
