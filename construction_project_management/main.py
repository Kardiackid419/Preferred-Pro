from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from dashboard_page import DashboardPage
from projects_page import ProjectsPage
from scheduling_page import SchedulingPage
from milestones_page import MilestonesPage
from notifications_page import NotificationsPage
from job_pipeline_page import JobPipelinePage
from loading_page import LoadingPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Construction Project Management Tool")

        # Create the central widget
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Initialize and add the different pages to the central widget
        self.dashboard_page = DashboardPage(self)
        self.projects_page = ProjectsPage(self)
        self.scheduling_page = SchedulingPage(self)
        self.milestones_page = MilestonesPage(self)
        self.notifications_page = NotificationsPage(self)
        self.job_pipeline_page = JobPipelinePage(self)

        # Initialize the loading page and pass self (MainWindow) as argument
        self.loading_page = LoadingPage(self)

        # Add widgets to the central widget (stack)
        self.central_widget.addWidget(self.loading_page)
        self.central_widget.addWidget(self.dashboard_page)
        self.central_widget.addWidget(self.projects_page)
        self.central_widget.addWidget(self.scheduling_page)
        self.central_widget.addWidget(self.milestones_page)
        self.central_widget.addWidget(self.notifications_page)
        self.central_widget.addWidget(self.job_pipeline_page)

        # Set the default page to the loading page
        self.central_widget.setCurrentWidget(self.loading_page)

    # Define the methods to show different pages
    def show_dashboard(self):
        self.central_widget.setCurrentWidget(self.dashboard_page)

    def show_projects_page(self):
        self.central_widget.setCurrentWidget(self.projects_page)

    def show_scheduling_page(self):
        self.central_widget.setCurrentWidget(self.scheduling_page)

    def show_milestones_page(self):
        self.central_widget.setCurrentWidget(self.milestones_page)

    def show_notifications_page(self):
        self.central_widget.setCurrentWidget(self.notifications_page)

    def show_job_pipeline_page(self):
        self.central_widget.setCurrentWidget(self.job_pipeline_page)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
