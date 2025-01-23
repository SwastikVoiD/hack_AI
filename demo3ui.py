import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFormLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt

class WasteManagementSystem(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Waste Management System")
        self.setGeometry(100, 100, 600, 400)

        # Set the window icon (use your own icon path)
        self.setWindowIcon(QIcon('app_icon.png'))  # Ensure 'app_icon.png' is in the same folder or specify the correct path
        
        # Set color palette for the application
        self.setStyleSheet("""
            QWidget {
                background-color: #f4f4f4;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
        """)

        # Initialize UI components
        self.login_page = QWidget(self)
        self.home_page = QWidget(self)

        # Set the layout for both pages
        self.create_login_page()
        self.create_home_page()

        # Initially, show the login page
        self.login_page.show()
        self.home_page.hide()

    def create_login_page(self):
        # Login page layout
        login_layout = QVBoxLayout()

        # Username and Password fields
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Password")

        # Login button
        login_button = QPushButton("Login", self)
        login_button.clicked.connect(self.handle_login)

        # Label for error messages
        self.error_label = QLabel("", self)
        self.error_label.setStyleSheet("color: red;")

        # Add widgets to layout
        login_layout.addWidget(self.username_input)
        login_layout.addWidget(self.password_input)
        login_layout.addWidget(login_button)
        login_layout.addWidget(self.error_label)

        # Set the layout of the login page
        self.login_page.setLayout(login_layout)

    def handle_login(self):
        # Dummy credentials (this can be replaced with database or API-based authentication)
        trial_username = "admin"
        trial_password = "password"

        # Get input values
        username = self.username_input.text()
        password = self.password_input.text()

        # Validate credentials
        if username == trial_username and password == trial_password:
            self.error_label.setText("")  # Clear error message
            self.login_page.hide()  # Hide the login page
            self.home_page.show()   # Show the home page
        else:
            self.error_label.setText("Invalid Credentials! Please try again.")  # Show error message

    def create_home_page(self):
        # Home page layout
        home_layout = QVBoxLayout()

        # Title
        title_label = QLabel("Waste Management Dashboard", self)
        title_label.setFont(QFont("Arial", 18))
        home_layout.addWidget(title_label)

        # Buttons for different waste management options
        self.schedule_button = QPushButton("Waste Collection Schedule", self)
        self.schedule_button.setFont(QFont("Arial", 12))
        self.schedule_button.setStyleSheet("background-color: #3498db; color: white; padding: 10px; border-radius: 5px;")
        self.schedule_button.clicked.connect(self.show_schedule)

        self.recycling_button = QPushButton("Recycling Information", self)
        self.recycling_button.setFont(QFont("Arial", 12))
        self.recycling_button.setStyleSheet("background-color: #9b59b6; color: white; padding: 10px; border-radius: 5px;")
        self.recycling_button.clicked.connect(self.show_recycling_info)

        self.report_button = QPushButton("Generate Waste Report", self)
        self.report_button.setFont(QFont("Arial", 12))
        self.report_button.setStyleSheet("background-color: #1abc9c; color: white; padding: 10px; border-radius: 5px;")
        self.report_button.clicked.connect(self.show_report)

        # Add buttons to the layout
        home_layout.addWidget(self.schedule_button)
        home_layout.addWidget(self.recycling_button)
        home_layout.addWidget(self.report_button)

        # Set the layout of the home page
        self.home_page.setLayout(home_layout)

    def show_schedule(self):
        # Function to show waste collection schedule
        print("Showing Waste Collection Schedule...")

    def show_recycling_info(self):
        # Function to show recycling information
        print("Showing Recycling Information...")

    def show_report(self):
        # Function to generate waste report
        print("Generating Waste Report...")

# Main function to run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set application icon globally
    app.setWindowIcon(QIcon('493154.webp'))  # Ensure 'app_icon.png' is in the same folder or specify the correct path

    window = WasteManagementSystem()
    window.show()
    sys.exit(app.exec_())
