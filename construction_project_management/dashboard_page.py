from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt


class DashboardPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)

        # Set the background color for the whole window, excluding buttons and label
        self.setStyleSheet("""
            QWidget {
                background-color: green;
            }
            QLabel {
                background-color: transparent;
                color: black;
            }
            QPushButton {
                background-color: none;
                color: black;
            }
        """)

        # Create and style the welcome label
        welcome_label = QLabel("Welcome to the Construction Project Management Tool Dashboard")
        welcome_label.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(welcome_label)

        # Define buttons and their corresponding callback functions
        buttons = [
            ("Current Projects", self.main_window.show_projects_page),
            ("Crew Scheduling", self.main_window.show_scheduling_page),
            ("Key Milestones and Deadlines", self.main_window.show_milestones_page),
            ("Notifications or Task Alerts", self.main_window.show_notifications_page),
            ("Job Pipeline Tracker", self.main_window.show_job_pipeline_page)
        ]

        # Create and style the buttons
        for text, callback in buttons:
            button = QPushButton(text)
            button.clicked.connect(callback)
            button.setStyleSheet("background-color: none; color: black;")
            self.layout.addWidget(button)

        self.setLayout(self.layout)
