# project_details_window.py
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QFileDialog, QTextEdit, QLineEdit
from PyQt5.QtGui import QPixmap

class ProjectDetailsWindow(QDialog):
    def __init__(self, project_details, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Project Details")
        self.layout = QVBoxLayout()

        # Extract project name and description
        project_name, project_description = project_details.split(": ")

        # Project name label
        self.project_name_label = QLabel(f"Project: {project_name}")
        self.layout.addWidget(self.project_name_label)

        # Project description text area
        self.project_description = QTextEdit()
        self.project_description.setPlainText(project_description)
        self.layout.addWidget(self.project_description)

        # Add image upload button and display area
        self.upload_button = QPushButton("Upload Image")
        self.upload_button.clicked.connect(self.upload_image)
        self.layout.addWidget(self.upload_button)

        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)

        # Location input (for Google Maps)
        self.location_input = QLineEdit()
        self.location_input.setPlaceholderText("Enter project address")
        self.layout.addWidget(self.location_input)

        # Placeholder for Google Maps (you can integrate Google Maps here)
        self.map_label = QLabel("Map would display here (Google Maps integration coming)")
        self.layout.addWidget(self.map_label)

        self.setLayout(self.layout)

    def upload_image(self):
        # Open file dialog to upload an image
        options = QFileDialog.Options()
        image_file, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.xpm *.jpg *.jpeg)", options=options)
        if image_file:
            pixmap = QPixmap(image_file)
            self.image_label.setPixmap(pixmap.scaled(400, 400, aspectRatioMode=True))  # Display scaled image
