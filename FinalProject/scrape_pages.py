#Lulu Jiao
#cs5001 22fall 12/13/2022
#final project--amazon job openings scraper

'''to get the variable needed to scape over pages'''
def get_total_pages(soup):
    '''get the total number of pages so that we can iterate over it'''
    total_pages_html = soup.find_all('button', {'class': 'page-button'})
    total_pages = int(total_pages_html[4].text)
    return total_pages
def page_Xpath(page):
    '''get the the Xpath of page-switch button of everypage so that we can click it and open the next page'''
    page_Xpath = "//button[@data-label='" + str(int(page)) + "']"
    return page_Xpath
        

'''amazon = scrape.Scape('https://www.amazon.jobs/en/')
amazon.search('software engineer', 'united states')
amazon_soup = amazon.create_soup()
print(get_total_pages(amazon_soup))
amazon.click_button(page_Xpath(1))'''






    
    