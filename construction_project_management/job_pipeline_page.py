from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class JobPipelinePage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QVBoxLayout()

        # Title label for the job pipeline page
        self.layout.addWidget(QLabel("Job Pipeline Tracker"))

        # Back button to return to the dashboard
        back_button = QPushButton("Back to Dashboard")
        back_button.clicked.connect(self.main_window.show_dashboard)
        self.layout.addWidget(back_button)

        self.setLayout(self.layout)
