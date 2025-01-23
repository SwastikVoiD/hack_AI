import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve

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

        # Apply animations
        self.animate_button()
        self.animate_background_color()

    def handle_login(self):
        # Simulate a successful login (can be replaced with actual logic)
        if self.username_input.text() == "admin" and self.password_input.text() == "password":
            print("Login Successful!")
        else:
            print("Login Failed!")

    def animate_button(self):
        # Create animation for the login button
        animation = QPropertyAnimation(self.login_button, b"size")
        animation.setDuration(300)  # Duration of the animation in milliseconds
        animation.setStartValue(self.login_button.size())
        animation.setEndValue(self.login_button.size() * 1.1)  # Make it 10% bigger
        animation.setEasingCurve(QEasingCurve.OutBounce)  # Apply easing curve for a smooth animation
        animation.setLoopCount(-1)  # Loop the animation infinitely
        animation.start()

    def animate_background_color(self):
        # Create background color animation
        animation = QPropertyAnimation(self, b"palette")
        animation.setDuration(1000)
        start_color = QColor(46, 59, 78)  # Dark color
        end_color = QColor(52, 152, 219)  # Lighter color (blue)
        
        # Apply the color change
        animation.setStartValue(start_color)
        animation.setEndValue(end_color)
        animation.setEasingCurve(QEasingCurve.Linear)  # Smooth transition
        animation.start()

# Main function to run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
