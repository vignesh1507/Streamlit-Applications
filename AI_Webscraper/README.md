# AI Web Scraper

This idea is a web scraping application/prototype built using Streamlit, BeautifulSoup, Selenium and Groq. It allows users to input a website URL, scrape content from that website, and download the parsed data in various formats.

## Prerequisites

Make sure you have the following installed on your local machine:

- Python 3.7 or later
- Chrome Browser
- ChromeDriver compatible with your Chrome version

## Installation

1. Clone the repository (or download the files) to your local machine.
2. Navigate to the project directory in your terminal.
3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Streamlit Application

1. Ensure the ChromeDriver path is correctly set in `scrape.py`.
2. Run the Streamlit application:

   ```bash
   streamlit run streamlit.py
   ```

3. Open your web browser and navigate to the URL provided in the terminal (typically `http://localhost:8501`).

## Usage

1. Enter the website URL you want to scrape.
2. Click on "Scrape Website" to fetch the content.
3. View the scraped content and optionally extract specific links.
4. Describe the data you want to parse and download the results in CSV, JSON, or XML formats.

## Troubleshooting

- If you encounter any issues with the ChromeDriver then ensure that:
  - The path to your ChromeDriver is correct.
  - Your ChromeDriver version matches your installed Chrome version.


This `README.md` file will help users understand how to set up and run our Streamlit web scraper effectively!
