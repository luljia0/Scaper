#Lulu Jiao

#CS5001 22fall 12/13/2022

#Final project

### 1 Project description

Amazon Job Openings Scraper: scape the job information from Amazon website and save it in Google sheets.

1. use **selenium webdriver** to control websites automatically to open websites, search by title and location, and switch pages.
2. use **BeautifulSoup** module to get an html object, parse it and locate elements
3. Use **Pandas** module to get the dataframe so that we can write it to forms
4. use **pygsheets** to load Googlesheet API path in Python to enable writing on google sheets

### 2 Any changes to the project from Planning document

1. control the websites automatically instead of manually
1. didn't do the scraping_bot which can keep track of openings updates because of time limitation and some bugs.
1. the list of titles, locations, companies, and links are converted to a dictionary so that we can convert it to dataframe instead of a list of lists
1. the functions in each class changed based on need.

### 3 Reflection

I learned how to do scraping a website in general, specifically how to use Selenium, Beautifulsoup, Pandas modules and write data to an online document. And I learned how to read HTML files and locate elements by xpath, which prepares me to learn front-end development. But I was supposed to do scraping on LinkedIn but it needs a security check after I control the website automatically. If I could start over, I would do it on LinkedIn, which collects positions from different companies instead of a single company because we can only apply for 1 position in the same company. 

**COULD DO BETTER**

1. scape.py Class Scrape def extract_link(self,soup)

   How to locate the desired link directly instead of locating href and picking them from lists

2. how to get the total pages directly instead of picking them from lists of elements. Both 1 and 2 are about how to locate the elements with the same XPath and similar tags

3. how to scrape over pages without switching the pages actually

4. write the data without columns for every loop

5. Loop from page 1 instead of page 2 to make the main function more simple.

### 4 Acknowledgements/Citations  

1. how to scrap job openings in general.

   Scraping indeed job data using Python https://www.chrislovejoy.me/job-scraper

   Linkedin job scraper https://github.com/kirkhunter/linkedin-jobs-scraper

   scape LinkedIn using selenium and Beautifulsoup in python https://www.geeksforgeeks.org/scrape-linkedin-using-selenium-and-beautiful-soup-in-python/

2. HTML elements https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element

3. how to locate from duplicate elements https://blog.51cto.com/omaidb/4120730

4. use Webdriver to locate elements https://selenium-python.readthedocs.io/locating-elements.html

5. how to use Beautiful Soup to pull information from HTML or XML documents

   https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

6. how to use Pandas modules to write excel

   https://pythonbasics.org/write-excel/

7. reading and writing to Google spreadsheets using Python

   https://erikrood.com/Posts/py_gsheets.html

   https://www.makeuseof.com/tag/read-write-google-sheets-python/

8. how to scrap multiple pages

   https://www.geeksforgeeks.org/python-web-scraping-tutorial/

9. how to use the crypto tracker to create a web scraping bot that continuously does scraping 

   https://www.geeksforgeeks.org/how-to-build-web-scraping-bot-in-python/?ref=rp

10. website scrapping in general

    https://wshuyi.medium.com/%E5%A6%82%E4%BD%95%E7%94%A8-python-%E7%88%AC%E6%95%B0%E6%8D%AE-%E4%B8%80-%E7%BD%91%E9%A1%B5%E6%8A%93%E5%8F%96-5424e6c72d40

11. A Complete Guide to Web Scraping Job Postings

    https://www.octoparse.com/blog/web-scraping-job-postings

    

### Modules installation

1. install selenium

   ```
   sudo -H pip3 install -U selenium
   ```
   
2. install beautifulsoup

   ```python 
   sudo pip3 install beautifulsoup4
   ```

3. install pandas

   ```
   pip3 install pandas
   ```
   
4. install pygsheets

   ```
   pip3 install pygsheets
   ```

   **Note that install all the modules in then same environment, better in a virtual environment with the Python version you use especially when you have different versions of Python.**

