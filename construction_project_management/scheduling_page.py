from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTableWidget, QTableWidgetItem, QAbstractItemView

class SchedulingPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel("Crew Scheduling System"))

        self.worker_input = QLineEdit()
        self.layout.addWidget(QLabel("Add New Worker"))
        self.layout.addWidget(self.worker_input)
        add_worker_button = QPushButton("Add Worker")
        self.layout.addWidget(add_worker_button)
        add_worker_button.clicked.connect(self.add_worker)

        self.worker_list = QListWidget()
        self.layout.addWidget(QLabel("Assigned Workers"))
        self.layout.addWidget(self.worker_list)

        self.schedule_table = QTableWidget(0, 3)  # Start with 0 rows and 3 columns
        self.schedule_table.setHorizontalHeaderLabels(["Worker", "Task", "Project"])
        self.schedule_table.setDragDropMode(QAbstractItemView.InternalMove)
        self.layout.addWidget(self.schedule_table)

        back_button = QPushButton("Back to Dashboard")
        back_button.clicked.connect(self.main_window.show_dashboard)
        self.layout.addWidget(back_button)

        self.setLayout(self.layout)

    def add_worker(self):
        worker_name = self.worker_input.text()
        if worker_name:
            row_position = self.schedule_table.rowCount()
            self.schedule_table.insertRow(row_position)
            self.schedule_table.setItem(row_position, 0, QTableWidgetItem(worker_name))
            self.schedule_table.setItem(row_position, 1, QTableWidgetItem("Task"))  # Placeholder for task
            self.schedule_table.setItem(row_position, 2, QTableWidgetItem("Project"))  # Placeholder for project
            self.worker_input.clear()  # Clear the input field
