"""
GUI components for the YouTube Lead Scraper application.
"""
from PyQt6.QtCore import QThread, QObject, pyqtSignal
from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit,
    QPushButton, QTextEdit, QHBoxLayout, QSpinBox, QDialog,
    QListWidget, QDialogButtonBox, QInputDialog, QMessageBox,
    QFileDialog
)
from . import settings
from . import scraper
from . import help_text

class HelpWindow(QDialog):
    """A simple dialog to show the setup guide."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Setup Guide")
        self.setMinimumSize(600, 500)
        
        layout = QVBoxLayout(self)
        text_browser = QTextEdit()
        text_browser.setReadOnly(True)
        text_browser.setHtml(help_text.HELP_HTML)
        
        layout.addWidget(text_browser)
        
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

class ScraperWorker(QObject):
    """
    Runs the scraping process in a separate thread.
    """
    log_message = pyqtSignal(str)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, params):
        super().__init__()
        self.params = params
        self._is_running = True

    def run(self):
        """Starts the scraping."""
        try:
            app_settings = settings.load_settings()
            # Basic validation
            if not app_settings.get("youtube_api_keys"):
                self.error.emit("No YouTube API keys found. Please add them in Settings.")
                return
            if not all([app_settings.get("sheet_id"), app_settings.get("service_account_file")]):
                self.error.emit("Google Sheets information is incomplete. Please configure it in Settings.")
                return

            scraper.run_scraper(
                params=self.params,
                settings=app_settings,
                log_callback=self.log_message.emit,
                should_stop=lambda: not self._is_running
            )
        except Exception as e:
            self.error.emit(f"An error occurred: {e}")
        finally:
            self.finished.emit()

    def stop(self):
        """Stops the scraping process."""
        self._is_running = False
        self.log_message.emit("Stopping process...")


class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setMinimumWidth(600)
        
        self.layout = QVBoxLayout(self)
        
        # --- Help Button ---
        help_layout = QHBoxLayout()
        help_layout.addStretch()
        self.help_button = QPushButton("Setup Guide")
        help_layout.addWidget(self.help_button)
        self.layout.addLayout(help_layout)
        
        # --- Google Sheets Settings ---
        self.layout.addWidget(QLabel("Google Sheets Settings"))
        
        self.sheet_id_input = QLineEdit()
        self.layout.addWidget(QLabel("Sheet ID:"))
        self.layout.addWidget(self.sheet_id_input)
        
        self.sheet_name_input = QLineEdit()
        self.layout.addWidget(QLabel("Worksheet Name:"))
        self.layout.addWidget(self.sheet_name_input)
        
        sa_layout = QHBoxLayout()
        self.sa_file_input = QLineEdit()
        self.sa_file_input.setPlaceholderText("Path to your service account .json file")
        browse_btn = QPushButton("Browse...")
        browse_btn.clicked.connect(self.browse_service_account_file)
        sa_layout.addWidget(self.sa_file_input)
        sa_layout.addWidget(browse_btn)
        self.layout.addWidget(QLabel("Service Account File:"))
        self.layout.addLayout(sa_layout)

        # --- YouTube API Keys ---
        self.layout.addWidget(QLabel("YouTube API Keys"))
        self.api_keys_list = QListWidget()
        self.layout.addWidget(self.api_keys_list)
        
        keys_btn_layout = QHBoxLayout()
        add_key_btn = QPushButton("Add")
        add_key_btn.clicked.connect(self.add_api_key)
        edit_key_btn = QPushButton("Edit")
        edit_key_btn.clicked.connect(self.edit_api_key)
        remove_key_btn = QPushButton("Remove")
        remove_key_btn.clicked.connect(self.remove_api_key)
        keys_btn_layout.addWidget(add_key_btn)
        keys_btn_layout.addWidget(edit_key_btn)
        keys_btn_layout.addWidget(remove_key_btn)
        keys_btn_layout.addStretch()
        self.layout.addLayout(keys_btn_layout)
        
        # --- Dialog Buttons ---
        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)
        
        self.help_window = HelpWindow(self)
        self.help_button.clicked.connect(self.help_window.show)
        
        self.load_and_display_settings()

    def load_and_display_settings(self):
        """Loads settings and populates the fields."""
        self.current_settings = settings.load_settings()
        self.sheet_id_input.setText(self.current_settings.get("sheet_id", ""))
        self.sheet_name_input.setText(self.current_settings.get("sheet_name", "Sheet1"))
        self.sa_file_input.setText(self.current_settings.get("service_account_file", ""))
        
        self.api_keys_list.clear()
        for key in self.current_settings.get("youtube_api_keys", []):
            self.api_keys_list.addItem(key)

    def browse_service_account_file(self):
        """Opens a file dialog to select the service account JSON file."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Service Account File", "", "JSON Files (*.json)")
        if file_path:
            self.sa_file_input.setText(file_path)

    def add_api_key(self):
        """Adds a new API key."""
        text, ok = QInputDialog.getText(self, "Add API Key", "Enter new API key:")
        if ok and text:
            self.api_keys_list.addItem(text)

    def edit_api_key(self):
        """Edits the selected API key."""
        selected_item = self.api_keys_list.currentItem()
        if not selected_item:
            return
        text, ok = QInputDialog.getText(self, "Edit API Key", "Edit API key:", QLineEdit.EchoMode.Normal, selected_item.text())
        if ok and text:
            selected_item.setText(text)

    def remove_api_key(self):
        """Removes the selected API key."""
        selected_item = self.api_keys_list.currentItem()
        if not selected_item:
            return
        reply = QMessageBox.question(self, "Remove API Key", "Are you sure you want to remove this key?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.api_keys_list.takeItem(self.api_keys_list.row(selected_item))

    def accept(self):
        """Saves the settings and closes the dialog."""
        keys = [self.api_keys_list.item(i).text() for i in range(self.api_keys_list.count())]
        self.current_settings["sheet_id"] = self.sheet_id_input.text()
        self.current_settings["sheet_name"] = self.sheet_name_input.text()
        self.current_settings["service_account_file"] = self.sa_file_input.text()
        self.current_settings["youtube_api_keys"] = keys
        
        settings.save_settings(self.current_settings)
        super().accept()

    def reject(self):
        """Closes the dialog without saving, reloading the original settings."""
        self.load_and_display_settings()
        super().reject()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Lead Scraper")
        self.setGeometry(100, 100, 900, 700)

        # --- Central Widget and Layout ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # --- Settings Button ---
        settings_layout = QHBoxLayout()
        settings_layout.addStretch() # Pushes the button to the right
        self.settings_button = QPushButton("Settings")
        settings_layout.addWidget(self.settings_button)
        main_layout.addLayout(settings_layout)

        # --- Input Fields ---
        inputs_layout = QVBoxLayout()
        
        self.keywords_input = QLineEdit()
        self.keywords_input.setPlaceholderText("Enter keywords, separated by commas")
        inputs_layout.addWidget(QLabel("Keywords:"))
        inputs_layout.addWidget(self.keywords_input)

        subs_layout = QHBoxLayout()
        self.min_subs_input = QSpinBox()
        self.min_subs_input.setRange(0, 100_000_000)
        self.max_subs_input = QSpinBox()
        self.max_subs_input.setRange(0, 100_000_000)
        subs_layout.addWidget(QLabel("Min Subscribers:"))
        subs_layout.addWidget(self.min_subs_input)
        subs_layout.addStretch()
        subs_layout.addWidget(QLabel("Max Subscribers:"))
        subs_layout.addWidget(self.max_subs_input)
        inputs_layout.addLayout(subs_layout)

        self.inactivity_input = QSpinBox()
        self.inactivity_input.setRange(1, 3650) # Up to 10 years
        self.inactivity_input.setValue(90)
        inactivity_layout = QHBoxLayout()
        inactivity_layout.addWidget(QLabel("Max Inactivity (days):"))
        inactivity_layout.addWidget(self.inactivity_input)
        inactivity_layout.addStretch()
        inputs_layout.addLayout(inactivity_layout)

        main_layout.addLayout(inputs_layout)

        # --- Control Buttons ---
        buttons_layout = QHBoxLayout()
        self.start_button = QPushButton("Start Scraping")
        self.stop_button = QPushButton("Stop Scraping")
        self.stop_button.setEnabled(False)
        buttons_layout.addWidget(self.start_button)
        buttons_layout.addWidget(self.stop_button)
        main_layout.addLayout(buttons_layout)

        # --- Log Area ---
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        main_layout.addWidget(QLabel("Log:"))
        main_layout.addWidget(self.log_area)

        # --- Settings Window ---
        self.settings_window = SettingsWindow(self)
        self.settings_button.clicked.connect(self.settings_window.show)

        # --- Worker Setup ---
        self.thread = None
        self.worker = None
        self.start_button.clicked.connect(self.start_scraping)
        self.stop_button.clicked.connect(self.stop_scraping)

    def start_scraping(self):
        """Prepares and starts the scraper worker."""
        # Validate inputs
        if not self.keywords_input.text():
            QMessageBox.warning(self, "Input Error", "Please enter at least one keyword.")
            return

        # Get params from GUI
        params = {
            "keywords": [k.strip() for k in self.keywords_input.text().split(",")],
            "min_subs": self.min_subs_input.value(),
            "max_subs": self.max_subs_input.value(),
            "inactivity_days": self.inactivity_input.value()
        }

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.log_area.clear()

        self.thread = QThread()
        self.worker = ScraperWorker(params)
        self.worker.moveToThread(self.thread)

        # Connect signals
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_scraping_finished)
        self.worker.log_message.connect(self.update_log)
        self.worker.error.connect(self.on_scraping_error)

        self.thread.start()

    def stop_scraping(self):
        """Stops the scraper worker."""
        if self.worker:
            self.worker.stop()
        self.stop_button.setEnabled(False)

    def on_scraping_finished(self):
        """Cleans up after the scraper has finished."""
        if self.thread:
            self.thread.quit()
            self.thread.wait()
        self.thread = None
        self.worker = None
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def update_log(self, message):
        """Appends a message to the log area."""
        self.log_area.append(message)

    def on_scraping_error(self, message):
        """Shows an error message."""
        QMessageBox.critical(self, "Scraping Error", message)
        self.update_log(f"ERROR: {message}")

