#Lulu Jiao
#cs5001 22fall 12/13/2022
#final project--amazon job openings scraper

import pandas as pd #converting it into a Pandas DataFrame
import pygsheets #read and write to googlesheet
class Write:
    '''to write the extracted information to Google sheets'''
    def __init__(self, sheet_path , sheet_name):
        #authorization
        if sheet_path == '':
            sheet_path = '/Users/jiaolulu/Desktop/Northeastern/CS5003/FinalProject/ggsheet.json'
        if sheet_name == '':
            sheet_name = 'Amazon Job Openings Tracker'
        self.sheet_name = sheet_name
        self.gc = pygsheets.authorize(service_file= sheet_path)

    def create_dataframe(self, title_list, location_list, id_list, link_list):
        '''use pandas to create a dataframe for the extracted information'''
        #convert list to dictionary
        job_data = {'Title': title_list,
        'Location': location_list,
        'ID': id_list,
        'Application Link': link_list}
        df = pd.DataFrame(job_data)
        return df
    def write_sheet(self, df, page):
        '''write the dataframe to the google sheets'''
        #open the google spreadsheet
        sh = (self.gc).open(self.sheet_name)
        #select the first sheet 
        wks = sh[0]
        #update the first sheet with df, starting at cell B2. 
        wks.set_dataframe(df,(int(page-1)*10+1,1))


        

'''amazon = scrape.Scape('https://www.amazon.jobs/en/')
soup = amazon.search('software development intern', 'united states')
title_list = amazon.extract_title(soup)
location_list = amazon.extract_location(soup)
id_list = amazon.extract_id(soup)
link_list = amazon.extract_link(soup)
amazon_sheet = Write()
amazon_df = amazon_sheet.create_dataframe(title_list, location_list, id_list, link_list)
amazon_sheet.write_sheet(amazon_df)'''









