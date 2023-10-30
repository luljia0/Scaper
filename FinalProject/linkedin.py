from selenium import webdriver
from selenium.webdriver.common.by import By #newly updated usage for wevdriver
from selenium.webdriver.common.keys import Keys #enter by keyboard
from selenium.webdriver import ChromeOptions #skip security check
import time

class scrape:
    def __init__(self, url, user_email, user_pw, job_title):
        self.url = url
        self.user_email = user_email
        self.user_pw = user_pw
        self.job_title = job_title
    def log_search(self):
        '''
        open and log in your linkedin account
        PARAMETER: None
        RETURN: None
        '''
        # Creating a webdriver instance
        driver = webdriver.Chrome("/Users/jiaolulu/Desktop/Northeastern/CS5003/FinalProject/chrome_webdriver/chromedriver ")
        #todo skip security check

        driver.get(self.url)   
        # waiting for the page to load
        time.sleep(5) 
        '''log in first'''
        # locate username
        username = driver.find_element(By.ID, 'session_key')
        # Enter Your Email Address
        username.send_keys(self.user_email)
        # entering password
        pword = driver.find_element(By.ID, 'session_password')
        # Enter Your Password
        pword.send_keys(self.user_pw)   
        # Clicking on the log in button
        # Format (syntax) of writing XPath -->
        # //tagname[@attribute='value']
        driver.find_element(By.XPATH, "//button[@class='sign-in-form__submit-button']").click()
        '''search by title'''   
        # waiting for the page to load longer because of security check
        time.sleep(10) 
        #locate search
        search = driver.find_element(By.CLASS_NAME, "artdeco-button__text")
        #enter job title
        search.send_keys(self.job_title)
        #enter by keyboard
        search.send_keys(Keys.ENTER)


    '''def extract_jd(self, link_list):
        descip_list = []
        bq_list = []
        pq_list = []
        for link in link_list:
            self.driver.get(link)
            time.sleep(5) 
            jd_src = self.driver.page_source
            jd_soup = BeautifulSoup(jd_src, 'lxml') 
            description = jd_soup.find('meta', {'property':'og:description'})
            descip_list.append(description)
            self.driver.close()
        print()'''