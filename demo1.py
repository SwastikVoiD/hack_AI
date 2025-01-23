import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aesthetic Login")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #2e3b4e;")
        
        # Create and apply modern fonts
        font = QFont("Roboto", 12)  # Use "Roboto" or any other installed modern font

        # Central widget layout
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        
        # Create username label and text field
        self.username_label = QLabel("Username")
        self.username_label.setStyleSheet("color: white; font-size: 14px;")
        self.username_label.setFont(font)
        self.username_input = QLineEdit()
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("background-color: #34495e; color: white; border-radius: 5px; padding: 5px;")
        
        # Create password label and text field
        self.password_label = QLabel("Password")
        self.password_label.setStyleSheet("color: white; font-size: 14px;")
        self.password_label.setFont(font)
        self.password_input = QLineEdit()
        self.password_input.setFont(font)
        self.password_input.setStyleSheet("background-color: #34495e; color: white; border-radius: 5px; padding: 5px;")
        self.password_input.setEchoMode(QLineEdit.Password)
        
        # Create Login Button
        self.login_button = QPushButton("Login")
        self.login_button.setFont(QFont("Roboto", 14, QFont.Bold))
        self.login_button.setStyleSheet("""
            background-color: #1abc9c;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
            border: none;
        """)
        self.login_button.clicked.connect(self.handle_login)

        # Add widgets to layout
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        # Set the layout for the window
        self.setLayout(layout)

    def handle_login(self):
        # Simulate a successful login (can be replaced with actual logic)
        if self.username_input.text() == "admin" and self.password_input.text() == "password":
            print("Login Successful!")
        else:
            print("Login Failed!")

# Main function to run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
