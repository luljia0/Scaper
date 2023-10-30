#Lulu Jiao
#cs5001 22fall 12/13/2022
#final project--amazon job openings scraper

from selenium import webdriver #to automated the website
from selenium.webdriver.common.by import By #newly updated usage for wevdriver
import time
from bs4 import BeautifulSoup #to return and parse a html object

class Scape:
    '''to scrape one page and extract information from it
    ATTRIBUTES: url
    METHODS: click_button, search, create_soup, extract_title, extract_location, extract_id, extract_link'''
    def __init__(self, url): 
        self.url = url
        self.driver = webdriver.Chrome("/Users/jiaolulu/Desktop/Northeastern/CS5003/FinalProject/chrome_webdriver/chromedriver ")
    
    def click_button(self, Xpath):
        '''to locate a button element and click it'''
        self.driver.find_element(By.XPATH, str(Xpath)).click()  
        time.sleep(3)
    
    def search(self, title, location):
        '''to search job openings by title and location'''
        self.driver.get(self.url)  
        # waiting for the page to load
        time.sleep(3) 
        #locate title search
        search_title = self.driver.find_elements(By.XPATH,"//input[@id='search_typeahead']")[1]
        #enter title 
        search_title.send_keys(title)
        #locate location search
        search_location = self.driver.find_elements(By.XPATH,"//input[@id='location-typeahead']")[1]
        #enter location 
        search_location.send_keys(location)
        #locate search button
        self.click_button("//button[@id='search-button']")
        #self.driver.find_element(By.XPATH, "//button[@id='search-button']").click()
    
    def create_soup(self):
        '''to return beautiful soup object'''
        job_src = self.driver.page_source
        soup = BeautifulSoup(job_src, 'lxml')  
        return soup
    
    def extract_title(self,soup):
        '''extract all titles information and return it as a list'''
        title_html = soup.find_all('h3', {'class': 'job-title'})
        title_list = []
        for title in title_html:
            title_list.append(title.text)
        return title_list
    
    def extract_location(self,soup):
        '''extract all location information and return it as a list'''
        location_html = soup.find_all('p', {'class': 'location-and-id'})
        location_list = []
        for location in location_html:
            location_list.append(location.text[0: len(location.text)-18])
        return location_list
    
    def extract_id(self,soup):
        '''extract all id information and return it as a list'''
        id_html = soup.find_all('p', {'class': 'location-and-id'})
        id_list = []
        for id in id_html:
            id_list.append(id.text[len(id.text)-7: len(id.text)])
        return id_list
    
    def extract_link(self,soup):
        '''extract all application link information and return it as a list'''
        link_html = soup.find_all('a')
        link_list = []
        for link in link_html:
            link_list.append(link.get('href'))
        link_list = link_list[26:36]
        for i in range(len(link_list)):
            link_list[i] = 'https://www.amazon.jobs' + link_list[i] #to make it a validate link
        return link_list



        
        



    


    

'''amazon = Scape('https://www.amazon.jobs/en/')
amazon.search('software development', 'united states')
soup = amazon.create_soup()
amazon.extract_title(soup)
amazon.extract_location(soup)
amazon.extract_id(soup)
amazon.extract_link(soup)'''



