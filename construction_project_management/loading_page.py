import os
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QProgressBar
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer

class LoadingPage(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window  # Reference to the main window for page transitions

        # Layout for the loading page
        layout = QVBoxLayout()

        # Create a QLabel to hold the logo
        self.logo_label = QLabel()

        # Load the logo image with a relative path
        logo_path = os.path.join(os.path.dirname(__file__), 'preferred_logo.png')
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            if not pixmap.isNull():
                # Set the pixmap to the label
                self.logo_label.setPixmap(pixmap)
                # Extract the dominant color from the logo
                dominant_color = self.get_dominant_color(pixmap.toImage())
            else:
                self.logo_label.setText("Failed to load image")
                dominant_color = Qt.black
        else:
            self.logo_label.setText("Image not found")
            dominant_color = Qt.black

        self.logo_label.setAlignment(Qt.AlignCenter)

        # Add the logo label to the layout
        layout.addWidget(self.logo_label)

        # Create a QProgressBar
        self.progress_bar = QProgressBar()
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setTextVisible(False)

        # Style the progress bar for a solid fill
        self.progress_bar.setStyleSheet(f'''
            QProgressBar {{
                border: 2px solid grey;
                border-radius: 5px;
                background-color: #FFFFFF;
            }}
            QProgressBar::chunk {{
                background-color: {dominant_color.name()};
                width: 100%;
            }}
        ''')

        # Add the progress bar to the layout
        layout.addWidget(self.progress_bar)

        # Set the layout for this widget
        self.setLayout(layout)

        # Simulate the loading process with smoother transitions
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(30)  # Update every 30 ms for smoother progress
        self.progress_value = 0

    def get_dominant_color(self, image):
        # Extracts the color from the center pixel of the image
        image = image.convertToFormat(QImage.Format_RGB32)
        color = image.pixelColor(image.width() // 2, image.height() // 2)
        return color

    def update_progress(self):
        # Increment the progress bar value for smooth effect
        if self.progress_value < 100:
            self.progress_value += 1
            self.progress_bar.setValue(self.progress_value)
        else:
            self.timer.stop()
            self.main_window.show_dashboard()  # Transition to the dashboard after loading
