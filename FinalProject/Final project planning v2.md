#Lulu Jiao

#CS5003 22Fall 11/18/2022

#final project planning part 2

## Job Openings Tracker

### 1 Project description

Job Openings Tracker has 2 main functions and related techniques:

1. use web scraping by Python to scrap the job-related information we need from job websites and store them in Excel or other online forms(like google docs or Notion)
2. use a scraping robot to keep track of the job openings and update the data.

The first difference with the Final Project Version1.0 is I'm going to do the job openings tracker instead of the application tracker because updating the application status manually can be smaller work and it's hard to test when I'm not actually going on the application process. Second, I'm not going to display the data and implement the functions on the self-designed website but in excel or online form because these forms already have beautiful interfaces and powerful features to do data analysis and classification. 

### 2 Required Elements Planning

#### 2.1 Classes/Objects

| Scape.py：<br />to scrap all the job-related information we need from a website |
| ------------------------------------------------------------ |
| Load_job_object():<br />''' to return a beautiful soup object which contains all the information of HTML document.  <br />PARAMETER: title, location(so that everyone can tailor the job search by job title and locations)<br />RETURN: job_object''' |
| extract_title():<br />''' use beautifulsoup.find() to extract the job title information from the beautiful soup object<br />PARAMETER: job_object<br />RETURN: title --strings of job titles''' |
| extract_company():<br />''' to extract the company information from the beautiful soup object<br />PARAMETER: job_object<br />RETURN: company --strings of companies''' |
| ……any other information that we need such as location and job description |

| Save.py:<br />use loop to save all the extracted information in a list of lists and use pandas modules to output in desired forms in an excel document |
| ------------------------------------------------------------ |
| list_information():<br />'''to convert strings of the extracted information to lists<br />PARAMETER: extract_info --strings of extracted information<br />RETURN: list_info -- list fo extracted information |
| job_list():<br />''' to loop all the information and save them in a list of lists where a list contains all the information of one job position<br />PARAMETER: list_info<br />RETURN: job_list --list of lists |
| write_excel():<br />'''use Pandas module to output the information in an excel document''' |

| Reuse.py:<br />to create a URL list and loop over it so that we don't need to rewrite the code to scrape multiple pages and websites |
| ------------------------------------------------------------ |

| Scraping_bot.py<br />use the crypto tracker to create a web scraping bot that does scraping and updates the excel document every 24 hours. |
| ------------------------------------------------------------ |

#### 2.2 Data structures

1. I will extract the information first by the tag or structure of the HTML document when inspecting the website.
2. The extracted information will be stored in the list by title, location, company, and so on, and can be accessed by their index.
3. to print them out by title with all other information, I will store them in a list of lists.

#### 2.3 Basic Programming Skills

1. Use the strings method to extract information
2. use lists, and maybe other data structures to store the extracted information and URLs and their method to manipulate the data
3. Use the while and for loops to iterate the information and URLs 
4. Use try-except block to deal with the exceptions
5. use classes/objects to deal with data with the same manipulations like titles and locations to do extraction and conversion to lists.

### 3 Testing Plan

| test_scape.py：<br />to test the functions of Scape.py       |
| ------------------------------------------------------------ |
| test_Load_job_object():<br />'''test the function Load_job_object() whether it can return a beautiful_soup object properly by printing the object.''' |
| test_extract_title():<br />'''test the function extract_title() whether it can extract the title information from HTML properly using the if-else statement''' |
| extract_company():<br />'''test the function extract_title() whether it can extract the company information from HTML properly using the if-else statement''' |
| ……any other test similar to the above                        |

| test_Save.py:<br />to test the functions of Save.py          |
| ------------------------------------------------------------ |
| test_list_information():<br />''' to test list_information() whether it can convert the strings to lists using if-else statement.''' |
| test_job_list():<br />''' to test job_list() whether it can create a list of lists based on the existing lists in our desired way using if-else statement.''' |
| test_write_excel():<br />''' to test write_excel() whether it can output an excel document by displaying it.''' |

| test_Reuse.py:<br />to test Reuse.py whether it works for scaping multiple websites by displaying the output of every website. |
| ------------------------------------------------------------ |

| test_Scraping_bot.py<br />to test Scaping_bot.py whether it works to scape the website every 24 hours by displaying the output of the scaping every 10 minutes, which is a smaller time interval and make sure that there's updates on the website during this interval. |
| ------------------------------------------------------------ |

### 4 Lingering Questions

1. Large job websites like Linkedin has anti-scraping technique to prevent unauthorized scraping. How to deal with the anti-scraping technique and is it legal to do that when scrapping is not for commercial purposes?
2. find a way to output data to online forms so that it can be updated in real-time instead of creating a new excel document every time do scraping.

### 5 Resources 

- **Selenium**: Selenium is a web testing library. It is used to automate browser activities.
- **BeautifulSoup**: Beautiful Soup is a Python package for parsing HTML and XML documents. It creates parse trees that are helpful to extract the data easily.
- **Pandas**: Pandas is a library used for data manipulation and analysis. It is used to extract the data and store it in the desired format. 

1. how to scrap job openings in general.

   Scraping indeed job data using Python https://www.chrislovejoy.me/job-scraper

   Linkedin job scraper https://github.com/kirkhunter/linkedin-jobs-scraper

2. how to use Beautiful Soup to pull information from HTML or XML documents

   https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

3. how to use Pandas modules to write excel

   https://pythonbasics.org/write-excel/

4. how to scrap multiple pages

   https://www.geeksforgeeks.org/python-web-scraping-tutorial/

5. how to use the crypto tracker to create a web scraping bot that continuously does scraping 

   https://www.geeksforgeeks.org/how-to-build-web-scraping-bot-in-python/?ref=rp

6. visa status tracker/appointment tracker

   https://moyu.ac.cn/

   https://github.com/yuzeming/CEACStatTracker

   https://tuixue.online/visa/

   https://github.com/Trinkle23897/tuixue.online-visa

7. website scrapping in general

   https://wshuyi.medium.com/%E5%A6%82%E4%BD%95%E7%94%A8-python-%E7%88%AC%E6%95%B0%E6%8D%AE-%E4%B8%80-%E7%BD%91%E9%A1%B5%E6%8A%93%E5%8F%96-5424e6c72d40

8. A Complete Guide to Web Scraping Job Postings

   https://www.octoparse.com/blog/web-scraping-job-postings

9. How to use request modules with Python

   https://www.w3schools.com/python/module_requests.asp









