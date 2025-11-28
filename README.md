# YouTube Lead Scraper

A user-friendly desktop application for finding YouTube channel leads based on keywords and other filters. The application allows you to scrape channel information and save it to a Google Sheet.

## Features

-   **Keyword-based Search:** Find channels based on your search terms.
-   **Advanced Filtering:** Filter channels by subscriber count and inactivity.
-   **Configurable Settings:** Easily manage your YouTube API keys, Google Sheet ID, and other settings through the app.
-   **Background Scraping:** The app remains responsive while it scrapes in the background.
-   **Cross-Platform:** Packaged to run on different operating systems.

## How to Use

1.  **Download the Application:**
    -   Go to the [GitHub Releases page](https://github.com/your-username/your-repo/releases) (this is a placeholder link).
    -   Download the `YouTubeLeadScraper` executable for your operating system.

2.  **Initial Setup (Settings):**
    -   The first time you run the application, click the **"Settings"** button in the top-right corner.
    -   **Google Sheets Configuration:**
        -   **Sheet ID:** Paste the ID of your Google Sheet.
        -   **Worksheet Name:** Enter the name of the worksheet you want to save data to (e.g., "Sheet1").
        -   **Service Account File:** Click "Browse..." and select your Google Service Account `.json` file. You need to have Google Sheets API and Google Drive API enabled for your service account.
    -   **YouTube API Keys:**
        -   Click "Add" to enter one or more YouTube Data API v3 keys.
    -   Click **"Save"**.

3.  **Start Scraping:**
    -   Enter your desired keywords in the "Keywords" field, separated by commas.
    -   Set the minimum and maximum subscriber counts.
    -   Set the maximum inactivity period in days.
    -   Click **"Start Scraping"**.

4.  **View Results:**
    -   The application will log its progress in the text area.
    -   The scraped leads will be added to your configured Google Sheet.

## For Developers

To build the application from the source, install the dependencies from `requirements.txt` and run the `pyinstaller` command found in the development history.
