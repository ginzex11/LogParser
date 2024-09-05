# app/app_manager.py

from utils.logger import setup_logging
import gui
from data.data_handler import CSVHandler

class AppManager:
    def __init__(self):
        setup_logging()  # Initialize logging configuration
        self.gui_manager = GUIManager()
        self.csv_handler = CSVHandler()

    def run(self):
        # Get the file path from the user
        file_path = self.gui_manager.get_file_path()

        # Load the file using CSVHandler
        data_frame = self.csv_handler.load_file(file_path)

        if data_frame.empty:
            self.gui_manager.show_message("Error", "Failed to load the file.")
        else:
            self.gui_manager.show_message("Success", "File loaded successfully!")
            # Proceed with further processing or display

if __name__ == '__main__':
    app_manager = AppManager()
    app_manager.run()
