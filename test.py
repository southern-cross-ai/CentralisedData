import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


def scrape_static_content(url, time_limit, output_file):
    """
    Scrape static content using requests and BeautifulSoup with a time limit and save to a text file.
    """
    start_time = time.time()  # Start the timer
    
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = soup.find_all('h2')  # Example: Adjust based on actual tag and class
        
        with open(output_file, 'a', encoding='utf-8') as file:
            for headline in headlines:
                if time.time() - start_time > time_limit:  # Check if time limit is exceeded
                    print("Time limit exceeded while scraping static content.")
                    break
                headline_text = headline.get_text(strip=True)
                print(f"Static headline: {headline_text}")
                file.write(f"Static headline: {headline_text}\n")  # Write headline to file
    else:
        print(f"Failed to retrieve content from {url} with status code {response.status_code}")


def scrape_dynamic_content(url, time_limit, output_file):
    """
    Scrape dynamic content using Selenium with a time limit.
    Scrapes both headings and the content of linked articles.
    """
    start_time = time.time()  # Start the timer

    # Initialize Selenium WebDriver with headless options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    driver = webdriver.Chrome(options=chrome_options)  # Initialize Selenium WebDriver with options

    try:
        driver.get(url)
        driver.implicitly_wait(10)  # Wait for dynamic content to load
        
        headlines = driver.find_elements(By.TAG_NAME, 'h2')  # Example: Adjust based on actual tag and class
        
        with open(output_file, 'a', encoding='utf-8') as file:
            for headline in headlines:
                if time.time() - start_time > time_limit:  # Check if time limit is exceeded
                    print("Time limit exceeded while scraping dynamic content.")
                    break

                headline_text = headline.text  # Corrected line
                link = headline.find_element(By.TAG_NAME, 'a')
                if link:
                    article_url = link.get_attribute('href')
                    
                    print(f"Scraping article: {headline_text} from {article_url}")
                    file.write(f"Headline: {headline_text}\n")

                    # Scrape content from the article link
                    article_content = scrape_article_content(article_url, time_limit, start_time)
                    file.write(f"Content: {article_content}\n\n")

    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")
    finally:
        driver.quit()

    """
    Scrape dynamic content using Selenium with a time limit and save to a text file.
    """
    start_time = time.time()  # Start the timer
    driver = webdriver.Chrome()  # Initialize Selenium WebDriver

    try:
        driver.get(url)
        driver.implicitly_wait(10)  # Wait for dynamic content to load
        
        headlines = driver.find_elements(By.TAG_NAME, 'h2')  # Example: Adjust based on actual tag and class
        
        with open(output_file, 'a', encoding='utf-8') as file:
            for headline in headlines:
                if time.time() - start_time > time_limit:  # Check if time limit is exceeded
                    print("Time limit exceeded while scraping dynamic content.")
                    break
                headline_text = headline.text
                print(f"Dynamic headline: {headline_text}")
                file.write(f"Dynamic headline: {headline_text}\n")  # Write headline to file
    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")
    finally:
        driver.quit()

# URL to scrape
url_to_test = "https://www.buzzfeed.com/au/tag/australia"

# Time limit in seconds
time_limit = 10

# Output file to store scraped data
output_file = 'scraped_data.txt'

# Scrape static content with a time limit and save to file
print(f"Scraping static content from {url_to_test}")
scrape_static_content(url_to_test, time_limit, output_file)

# Scrape dynamic content with a time limit and save to file
print(f"Scraping dynamic content from {url_to_test}")
scrape_dynamic_content(url_to_test, time_limit, output_file)
