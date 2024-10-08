from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QLineEdit
from project_details_window import ProjectDetailsWindow  # Import the class

class ProjectsPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QVBoxLayout()

        # Create a label for the projects page
        self.layout.addWidget(QLabel("Current Projects"))

        # Create a list widget to display current projects
        self.projects_list = QListWidget()
        self.projects_list.itemDoubleClicked.connect(self.open_project_details)  # Double-click signal
        self.layout.addWidget(self.projects_list)

        # Form to add new projects
        self.project_name_input = QLineEdit()
        self.project_name_input.setPlaceholderText("Project Name")
        self.layout.addWidget(self.project_name_input)

        self.project_description_input = QLineEdit()
        self.project_description_input.setPlaceholderText("Project Description")
        self.layout.addWidget(self.project_description_input)

        # Add button to create new projects
        add_project_button = QPushButton("Add Project")
        add_project_button.clicked.connect(self.add_project)
        self.layout.addWidget(add_project_button)

        # Back button to return to the dashboard
        back_button = QPushButton("Back to Dashboard")
        back_button.clicked.connect(self.main_window.show_dashboard)
        self.layout.addWidget(back_button)

        self.setLayout(self.layout)

    def add_project(self):
        # Get the project name and description
        project_name = self.project_name_input.text()
        project_description = self.project_description_input.text()

        if project_name:  # Ensure project name is not empty
            # Add project details to the list as "Project Name: Description"
            self.projects_list.addItem(f"{project_name}: {project_description}")
            # Clear the input fields
            self.project_name_input.clear()
            self.project_description_input.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a project name.")

    def open_project_details(self, item):
        # Create and open the project details window when a project is double-clicked
        details_window = ProjectDetailsWindow(item.text(), self)
        details_window.exec_()
