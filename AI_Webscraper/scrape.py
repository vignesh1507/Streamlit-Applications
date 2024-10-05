from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os

CHROMEDRIVER_PATH = "/Users/vigneshskanda/Downloads/AI_Webscraper/chromedriver" #input your own chromedriver path here

def scrape_website(website):
    print("Connecting to Chrome...")
    options = Options()
    options.add_argument("--headless")  # Run headless if you don't need a UI
    service = Service(CHROMEDRIVER_PATH)

    try:
        with webdriver.Chrome(service=service, options=options) as driver:
            driver.get(website)
            print("Navigated! Scraping page content...")
            html = driver.page_source
            return html
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def extract_body_content(html_content):
    if html_content is None:
        print("No HTML content to extract.")
        return ""
    
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
