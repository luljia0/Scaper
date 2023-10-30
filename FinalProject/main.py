import scrape
import write
import scrape_pages
def main():
    print('*'* 20 + 'Amazon Job Openings Scraper' + '*' * 20)
    amazon = scrape.Scape('https://www.amazon.jobs/en/')
    #search by job title and location
    title = input('Please input the job title:')
    location = input('Please input the job location:')
    amazon.search(title, location)
    #scrape the first page
    amazon_soup = amazon.create_soup()
    title_list = amazon.extract_title(amazon_soup)
    location_list = amazon.extract_location(amazon_soup)
    id_list = amazon.extract_id(amazon_soup)
    link_list = amazon.extract_link(amazon_soup)
    sheet_path = input('PLease input the sheet path(RETURN to default):')
    sheet_name = input('PLease input the sheet name(RETURN to default):')
    amazon_sheet = write.Write(sheet_path, sheet_name)
    amazon_df = amazon_sheet.create_dataframe(title_list, location_list, id_list, link_list)
    amazon_sheet.write_sheet(amazon_df,1)

    #loop over the number of pages from page2
    total_pages  = scrape_pages.get_total_pages(amazon_soup) 
    for page in range(2, total_pages): 
        #open the next page
        amazon.click_button(scrape_pages.page_Xpath(page)) 
        #create soup object
        amazon_soup = amazon.create_soup()
        #extract information 
        title_list = amazon.extract_title(amazon_soup)
        location_list = amazon.extract_location(amazon_soup)
        id_list = amazon.extract_id(amazon_soup)
        link_list = amazon.extract_link(amazon_soup)
        #write to google sheet
        amazon_sheet = write.Write(sheet_path, sheet_name)
        amazon_df = amazon_sheet.create_dataframe(title_list, location_list, id_list, link_list)
        amazon_sheet.write_sheet(amazon_df,page)

if __name__ == '__main__':
    main()



        



    
    
    
    