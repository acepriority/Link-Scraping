# Link-Scraping

This repository contains a collection of Python scripts that provide various functionalities, including a YouTube video downloader, weather updates, and Google searching. Each script is described below:

# YouTube Video Downloader

The YouTube video downloader script allows you to download YouTube videos directly to your local machine. It utilizes the `pytube` library to fetch video information and download the desired video. To use the script, follow the steps below:

1. Install the required dependencies by running the following command:

   ```
   pip install pytube
   ```

2. Run the script `YoutubeScraping.py`.

3. A GUI window will appear where you can paste the YouTube video URL and click the "DOWNLOAD" button. The video will be downloaded and saved to your default download location.

Please note that downloading videos from YouTube may violate YouTube's terms of service or copyright laws. Ensure that you have the necessary rights or permissions before downloading any videos.

## Weather Update

The weather update script provides current weather information for a given location using the OpenWeather API. To use the script, follow the steps below:

1. Install the required dependencies by running the following command:

   ```
   pip install requests
   ```

2. Run the script `WeatherUpdates.py`.

3. The script will prompt you to enter the name of a city or location. After entering the location, the script will retrieve the current weather information, including temperature, humidity, wind speed, and weather conditions.

Ensure that you have an active internet connection to retrieve the weather information from the OpenWeather API.

## Google Searching

The Google searching script allows you to perform a Google search and retrieve the top search results directly from the command line. To use the script, follow the steps below:

1. Install the required dependencies by running the following command:

   ```
   pip install beautifulsoup4
   pip install requests
   ```

2. Run the script `GoogleSearch.py`.

3. The script will prompt you to enter the search query. After entering the query, the script will retrieve the top search results from Google and display the title and URL of each result.

Ensure that you have an active internet connection to perform the Google search and retrieve the search results.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

The scripts provided in this repository are for educational purposes only. The usage of these scripts is at your own risk. Ensure that you comply with the terms of service and applicable laws when using these scripts. We do not take any responsibility for the misuse of these scripts or any consequences that may arise from their usage.
