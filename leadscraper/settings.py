"""
Handles loading and saving of application settings.
"""
import json
import os

def get_settings_path():
    """
    Determines the path for the settings.json file in a user-specific directory.
    """
    # Use a standard cross-platform location for app data
    app_data_path = os.getenv("APPDATA") or os.path.expanduser("~/.config")
    app_dir = os.path.join(app_data_path, "YouTubeLeadScraper")
    os.makedirs(app_dir, exist_ok=True)
    return os.path.join(app_dir, "settings.json")

def load_settings():
    """
    Loads settings from the settings.json file.
    Returns a dictionary with default values if the file doesn't exist.
    """
    settings_path = get_settings_path()
    if not os.path.exists(settings_path):
        return {
            "youtube_api_keys": [],
            "sheet_id": "",
            "sheet_name": "Sheet1",
            "service_account_file": ""
        }
    try:
        with open(settings_path, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        # If file is corrupted or can't be read, return defaults
        return {
            "youtube_api_keys": [],
            "sheet_id": "",
            "sheet_name": "Sheet1",
            "service_account_file": ""
        }

def save_settings(settings):
    """
    Saves the provided settings dictionary to the settings.json file.
    """
    settings_path = get_settings_path()
    with open(settings_path, "w") as f:
        json.dump(settings, f, indent=4)
