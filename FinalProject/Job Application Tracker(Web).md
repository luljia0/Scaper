#Lulu Jiao 

#Final Project Planning- Job Application Tracker(Web)

#CS5003 22 Fall 10/27/2022

## Job Application Tracker(Web)

### 1.1 Problem Description 

Job searching can be time-taking and time-sensitive. It would be more effective if there was a website to 

1. keep track of the job openings, collect them and add them easily to your wishlist with all the related information.
2. keep track of the status of the application, update the status automatically by linking to your personal email or application account and notify you of the deadlines

### 1.2 Background 

#### 1.2.1 Necessity

According to statistics, it takes 21-80 job applications to get one job offer.[^1]And things could be worse in some competitive industries and positions. And every application cycle could be a long process, from searching, applying, and interviewing to accepting/rejecting, which can last up to a few months. And every step would be time-consuming and tiring, like customizing the resume and sending it, checking the application website and email to keep track of the status. There is also a lot of related information like job descriptions, contacts, and company introductions to manage. But most of the things are repetitive and can be tracked automatically. So, job hunters need a website to solve these problems by the functions mentioned in 1.1

[^1]: *How Many Applications Does It Take To Get A Job? [2022] – Zippia*. (2022, September 14). https://www.zippia.com/advice/how-many-applications-does-it-take-to-get-a-job/

#### 1.2.2 Competitor Analysis[^2]

[^2]: https://www.makeuseof.com/apps-for-job-seekers-to-organize-track-and-get-reminders-of-job-applications/

There have been some websites to solve the following problems partly. So it's necessary to do an analysis to learn from their pros and improve their cons

**Huntr**

https://huntr.co/track/boards/6356e6516d10a9002837e2b9/board

**pros:** 

1. keep all job-related information all in one app including contacts, notes, contacts, and documents.

**cons:**

1. Built-in job search to find an opportunity and save it in Board by one click
2. No automatic tracking, need to update the status manually.

main interface

<img src="/Users/jiaolulu/Library/Application Support/typora-user-images/image-20221027140211737.png" alt="image-20221027140211737" style="zoom: 25%;" />

add a position to be tracked 

<img src="/Users/jiaolulu/Library/Application Support/typora-user-images/image-20221027140624629.png" alt="image-20221027140624629" style="zoom:25%;" />

**Kiter**

https://www.account.kiter.app/opportunities/81f27362-9500-4578-b44e-267c269526c7

**pros:**

1. Built-in job search to find an opportunity and save it in Board by one click
2. Use the chrome extension to save job positions on board

**cons:**

1. No filters for companies, or positions. The searching keyword can mislead you to the wrong post. For example, when you want to search for an Amazon position and type in Amazon, the company related to Amazon might appear in the search results.
2. don't have job descriptions in some positions
3. No automatic tracking, need to update the status manually.
4. can't classify the positions by status eg. Interested, applied.

Main interface

<img src="/Users/jiaolulu/Library/Application Support/typora-user-images/image-20221027150739311.png" alt="image-20221027150739311" style="zoom:25%;" />

Search for a job and track the status

<img src="/Users/jiaolulu/Library/Application Support/typora-user-images/image-20221027150813216.png" alt="image-20221027150813216" style="zoom:25%;" />



### 1.3 Challenges

**overall:**

1. How to build up a website's front-end interface--HTML CSS Javascipt
2. how to build up a website's  back-end logic ---Python Django/Flask

**by functions:**

1. How to collect, storage data from other websites---web scraping with Python

   Specifically, how to collect the job information from the companies' websites and how to identify the application status from personal email or application account and get it updated to the application tracker

   https://www.edureka.co/blog/web-scraping-with-python/

2. how to classify data in Python --scikit-learn

   Specifically, how to classify the job information into a company, job title, deadlines, job descriptions.

   https://www.activestate.com/resources/quick-reads/how-to-classify-data-in-python/

3. how to push notifications to users within the website and by email or message ---GetResponse

   https://www.getresponse.com/features/web-push-notifications?utm_source=google&utm_medium=cpc&camp=17499637384&adgroup=141453388967&kw=Push%20notifications%20tool&type=p&device=c&creative={AdId}&gclid=CjwKCAjw2OiaBhBSEiwAh2ZSP9aW2N4vYS_MxJHaqFSqWlrwLroCOGGsSwQVPiWqh4Wxq_EpzlOi4BoCBkAQAvD_BwE

   <img src="/Users/jiaolulu/Library/Application Support/typora-user-images/image-20221027213021034.png" alt="image-20221027213021034" style="zoom:25%;" />

### 1.4 Problems that can be solved now 

1. how to build up a website's  back-end logic ---Python

   - how to realize the function by clicking somewhere in interface. Eg. close the current page by clicking on the cross

2. how to made website accessed 

   - buy a domain
   - set up a cloud server
   - upload the website

   