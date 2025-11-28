"""
This file contains the HTML content for the setup guide.
"""

HELP_HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { font-family: sans-serif; line-height: 1.4; }
    h2 { color: #333; border-bottom: 1px solid #ccc; padding-bottom: 5px; }
    h3 { color: #555; }
    ol { padding-left: 20px; }
    li { margin-bottom: 10px; }
    code { background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px; font-family: monospace; }
    .note { background-color: #fffbe6; border-left: 4px solid #ffc107; padding: 10px; margin: 10px 0; }
</style>
</head>
<body>

<h2>Setup Guide: Google API & Sheets</h2>
<p>To use this tool, you need to configure two things from the Google Cloud Platform:</p>
<ol>
    <li><b>YouTube Data API v3 Keys:</b> To search for channels.</li>
    <li><b>A Google Service Account:</b> To write data to your Google Sheet.</li>
</ol>

<hr>

<h3>Part 1: Create a Google Cloud Project</h3>
<ol>
    <li>Go to the <a href="https://console.cloud.google.com/">Google Cloud Console</a> and sign in.</li>
    <li>Click the project dropdown at the top of the page and click <b>"New Project"</b>.</li>
    <li>Give your project a name (e.g., "YouTube Scraper") and click <b>"Create"</b>.</li>
    <li>Make sure your new project is selected in the dropdown.</li>
</ol>

<h3>Part 2: Enable Required APIs</h3>
<ol>
    <li>In the search bar at the top, search for and enable the following two APIs:
        <ul>
            <li><b>YouTube Data API v3</b></li>
            <li><b>Google Sheets API</b></li>
        </ul>
    </li>
    <li>For each one, click on it and then click the <b>"ENABLE"</b> button.</li>
</ol>

<h3>Part 3: Create YouTube API Keys</h3>
<ol>
    <li>In the Google Cloud Console, navigate to <b>"APIs & Services" > "Credentials"</b>.</li>
    <li>Click <b>"+ CREATE CREDENTIALS"</b> at the top and select <b>"API key"</b>.</li>
    <li>A new key will be generated. Click <b>"COPY"</b> to copy it.</li>
    <li>In this app, go to <b>Settings</b>, click the <b>"Add"</b> button under "YouTube API Keys", and paste the key.</li>
    <li>It is recommended to create multiple API keys (e.g., 3-5) to avoid hitting daily usage limits. Repeat the steps above to create more keys and add them all to the app.</li>
</ol>

<h3>Part 4: Create a Service Account for Google Sheets</h3>
<ol>
    <li>Go back to <b>"APIs & Services" > "Credentials"</b>.</li>
    <li>Click <b>"+ CREATE CREDENTIALS"</b> and select <b>"Service account"</b>.</li>
    <li>Give the service account a name (e.g., "sheets-writer") and click <b>"CREATE AND CONTINUE"</b>.</li>
    <li>For "Role", select <b>"Project" > "Editor"</b> and click <b>"Continue"</b>.</li>
    <li>Click <b>"Done"</b> on the last step.</li>
    <li>You will now see the service account in your list. Find the email address for this new service account (it looks like an email, e.g., <code>sheets-writer@your-project.iam.gserviceaccount.com</code>). **Copy this email address.**</li>
</ol>

<h3>Part 5: Share Your Google Sheet</h3>
<ol>
    <li>Open the Google Sheet you want to write data to.</li>
    <li>Click the **"Share"** button in the top-right corner.</li>
    <li>In the "Add people and groups" field, **paste the service account's email address** you copied in the previous step.</li>
    <li>Ensure it has **"Editor"** permissions.</li>
    <li>Click **"Send"** (uncheck "Notify people" if you wish).</li>
</ol>

<h3>Part 6: Get the Service Account JSON File</h3>
<ol>
    <li>Go back to the Google Cloud Console (<b>"APIs & Services" > "Credentials"</b>).</li>
    <li>Click on the service account you created.</li>
    <li>Go to the <b>"KEYS"</b> tab.</li>
    <li>Click <b>"ADD KEY" > "Create new key"</b>.</li>
    <li>Select **JSON** as the key type and click <b>"CREATE"</b>.</li>
    <li>A `.json` file will be downloaded to your computer. **Keep this file safe!**</li>
    <li>In this app, go to <b>Settings</b>, click the **"Browse..."** button next to "Service Account File", and select the `.json` file you just downloaded.</li>
</ol>

<h3>Part 7: Get the Sheet ID</h3>
<ol>
    <li>Open your Google Sheet.</li>
    <li>Look at the URL in your browser's address bar. It will look like this: <br><code>https://docs.google.com/spreadsheets/d/THIS_IS_THE_SHEET_ID/edit#gid=0</code></li>
    <li>Copy the long string of letters and numbers between <code>/d/</code> and ` /edit`.</li>
    <li>In this app, go to <b>Settings</b> and paste this into the **"Sheet ID"** field.</li>
</ol>

<p class="note">You are now ready to start scraping!</p>

<p>Created by Abu Bakar Siddique Naief</p>

</body>
</html>
"""
