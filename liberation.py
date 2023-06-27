import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import driverpath

#TODO: Ensure UBlock is active, they get NO ad revenue from this!
def stringize(link_string):
    link_string = link_string.split('/')[6]
    link_string = link_string.replace('-', ' ')
    return link_string

def main():
    chrome_options = Options()
    ublock_path = ''
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

    # Filter links that start with 'https://www.browndailyherald.com/' and bad ones
    
    # Links that will always be present but we don't want.
    bad_links = ['https://www.browndailyherald.com/page/about',
                 'https://www.browndailyherald.com/page/join', 
                 'https://www.browndailyherald.com/page/contact', 
                 'https://www.browndailyherald.com/page/advertise', 
                 'https://www.browndailyherald.com/page/dei', 
                 'https://www.browndailyherald.com/page/subscribe', 
                 'https://www.browndailyherald.com/', 
                 'https://www.browndailyherald.com/page/submit', 
                 'https://www.browndailyherald.com/newsletters']
    

    for link in links:
        href = link.get('href')
        if href and href.startswith('https://www.browndailyherald.com/article/') and href not in bad_links and href not in bdh_links:
            bdh_links.append(href)

    for i in range(10):
        print("[" + str(i) + "] " + stringize(bdh_links[i]))
    driver.quit() 
    
    choice = input("Enter the number of the article you want to read\nor enter 10 for information on why BDH's terms of service are bad: ")


if __name__ == '__main__':
    main()
