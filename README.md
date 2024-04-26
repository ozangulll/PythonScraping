# Python Web Scraping for Excursion Market

This Python script is designed to collect tour details from [Excursion Market](https://www.excursionmarket.com/all-tours) website. The script utilizes Python libraries such as Selenium and BeautifulSoup to scrape tour details and saves them into a Microsoft Word document.

## Requirements

Before running this script, make sure you have Python installed. You'll also need to install the following Python libraries:

- BeautifulSoup4
- requests
- Selenium
- python-docx

You can install these libraries using pip:

pip install beautifulsoup4
pip install requests
pip install selenium
pip install python-docx


You'll also need to download and install the [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and specify its path in the script.

## How to Use

Follow these steps to use the script:

1. Install Python and required libraries.
2. Download and install the Chrome WebDriver.
3. Specify the path to your Chrome WebDriver in the script.
4. Modify the `os.environ['USERPROFILE']` part in the script to the desired folder path where you want to save the Word document.
5. Run the Python script to collect tour details. It will generate a Word document named `consolidated_include_notinclude_bring.docx` containing tour details.
6. Open the generated Word document to view the tour details.

Please note that web scraping should be done in compliance with the terms of use and permissions of the target website. Also, the code may need adjustments due to changes in the website's structure.

## License

This project is licensed under the MIT License. For more information, please refer to the LICENSE file.
