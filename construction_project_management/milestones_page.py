from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem

class MilestonesPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QVBoxLayout()

        # Create a label for the title
        self.layout.addWidget(QLabel("Key Milestones and Deadlines"))

        # Create a table widget for displaying milestones
        self.milestones_table = QTableWidget(0, 3)  # Start with 0 rows and 3 columns
        self.milestones_table.setHorizontalHeaderLabels(["Milestone", "Deadline", "Status"])
        self.layout.addWidget(self.milestones_table)

        # Back button to return to the dashboard
        back_button = QPushButton("Back to Dashboard")
        back_button.clicked.connect(self.main_window.show_dashboard)
        self.layout.addWidget(back_button)

        self.setLayout(self.layout)

    def add_milestone(self, milestone, deadline, status):
        # Add a new milestone to the table
        row_position = self.milestones_table.rowCount()
        self.milestones_table.insertRow(row_position)
        self.milestones_table.setItem(row_position, 0, QTableWidgetItem(milestone))
        self.milestones_table.setItem(row_position, 1, QTableWidgetItem(deadline))
        self.milestones_table.setItem(row_position, 2, QTableWidgetItem(status))
