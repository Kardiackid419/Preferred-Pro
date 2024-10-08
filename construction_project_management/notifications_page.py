from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget

class NotificationsPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QVBoxLayout()

        # Create a label for the notifications page
        self.layout.addWidget(QLabel("Notifications or Task Alerts"))

        # Create a list widget to display notifications
        self.notifications_list = QListWidget()
        self.layout.addWidget(self.notifications_list)

        # Back button to return to the dashboard
        back_button = QPushButton("Back to Dashboard")
        back_button.clicked.connect(self.main_window.show_dashboard)
        self.layout.addWidget(back_button)

        self.setLayout(self.layout)

    def add_notification(self, notification):
        # Add a new notification to the list
        self.notifications_list.addItem(notification)
