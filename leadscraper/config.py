"""
Configuration for the YouTube Lead Scraper.

It's highly recommended to use environment variables for sensitive data
like API keys, rather than hardcoding them in this file.
"""
import os

# --- YouTube API Configuration ---
# IMPORTANT: Load your API keys from environment variables for security.
# Example: YOUTUBE_API_KEYS="key1,key2,key3"
# Then uncomment the line below.
# YOUTUBE_API_KEYS = os.environ.get("YOUTUBE_API_KEYS", "").split(",")

# For demonstration, placeholder keys are included here.
# Replace these or use environment variables.
YOUTUBE_API_KEYS = [
    "AIzaSyDfj1IIy5CZQQTTARWb0GS9XT1GCoOeQRg",
    "AIzaSyA9i7z-E5o1SNU2ajUHJeB175vTYg1B8cY",
    "AIzaSyCxD6_YMiq6Y4QRP70ViuVRwCZDH1NmT0o",
    "AIzaSyClENLt9jAj7e9MWG5jda7GK4v3emO5Fk4",
    "AIzaSyD9K2NT_SRfjzZKWNojWT28JhNDIh7nilk"
]

# Filter out any empty keys that might result from splitting an empty string
YOUTUBE_API_KEYS = [key for key in YOUTUBE_API_KEYS if key]

if not YOUTUBE_API_KEYS:
    raise ValueError("YouTube API keys are not configured. Please set them in config.py or as an environment variable.")

# --- Google Sheets Configuration ---
# Path to your Google Service Account JSON file.
SERVICE_ACCOUNT_FILE = "/home/abu-naief/youtube_automation/sheets-sa.json"
# The ID of the Google Sheet to which data will be saved.
SHEET_ID = "1INSlR0Cwc3Ao9slzJuN5vM-cODpVVY71TFUrCdd1bgA"
# The name of the worksheet within the Google Sheet.
SHEET_NAME = "Sheet1"

# --- Scraping & Filtering Parameters ---
# Maximum number of search results to fetch per API call (max 50).
MAX_RESULTS_PER_SEARCH = 50
# Maximum number of valid channels to add to the sheet for a single keyword.
MAX_VALID_PER_KEYWORD = 100

# Set of allowed country codes (ISO 3166-1 alpha-2).
# Leave empty to allow all countries: ALLOWED_COUNTRIES = set()
ALLOWED_COUNTRIES = {
    "US", "CA", "GB", "AU",
    "DZ","AO","BJ","BW","BF","BI","CM","CV","CF","TD","KM","CG","CD","DJ","EG",
    "GQ","ER","SZ","ET","GA","GM","GH","GN","GW","KE","LS","LR","LY","MG","MW",
    "ML","MR","MU","MA","MZ","NA","NE","NG","RW","ST","SN","SC","SL","SO","ZA",
    "SS","SD","TZ","TG","TN","UG","ZM","ZW"
}

# --- Performance & State Management ---
# Number of threads to use for fetching channel details concurrently.
THREAD_WORKERS = 5
# Number of rows to buffer before writing to Google Sheets in a single batch.
BATCH_APPEND_SIZE = 50
# File to store progress (checkpoints) to allow for resuming interrupted scrapes.
CHECKPOINT_FILE = "youtube_checkpoint.json"