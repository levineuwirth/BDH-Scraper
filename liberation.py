import time
from selenium import webdriver
from bs4 import BeautifulSoup
from driverpath import driverpath

def main():
    driver = webdriver.Chrome(driverpath.get())
    driver.get('https://www.browndailyherald.com/')

    # Wait for the page to load (adjust the delay as needed)
    time.sleep(2)  # 2 seconds delay

    page_source = driver.page_source

    # Get the links which are to other BDH pages.
    # We initially got the main page, so we need to find the latest articles.
    soup = BeautifulSoup(page_source, 'html.parser')
    links = soup.find_all('a')
    bdh_links = []

    # Filter links that start with 'https://www.browndailyherald.com/'
    for link in links:
        href = link.get('href')
        if href and href.startswith('https://www.browndailyherald.com/'):
            bdh_links.append(href)

    print(bdh_links)

    driver.quit()

if __name__ == '__main__':
    main()