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

def repl(bdh_links):
    choice = input("Enter the number of the article you want to read\nor enter 10 for information on why BDH's terms of service are bad: ")
    if choice == '10':
        print("BDH's terms of service are very sad and certainly are not a representation of the Brown community's ideals.\nThe service partners with Google's monopolistic advertisting scheme to track you across websites, view your browsing history, and provide you advertising based on information gathered via stalking your every move on the web.\nThese tactics are employed against students, classmates, faculty, and the community.\nThe herald should allow students due process and not censor access when users do not agree to the invasion of their privacy.\nAnd with the latest initiatives, now if you don't agree to their terms, you can't even read the news on paper as the paper prints are going away.\These are sad days for the Brown community.\n")
    else:
        chrome_options = Options()
        ublock_path = ''
        driver = webdriver.Chrome(driverpath.get())
        driver.get(bdh_links[int(choice)])
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            print(paragraph.get_text())

        driver.quit()


def main():
    chrome_options = Options()
    ublock_path = ''
    driver = webdriver.Chrome(driverpath.get())
    driver.get('https://www.browndailyherald.com/')
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

    while True:
        repl(bdh_links)

if __name__ == '__main__':
    main()
