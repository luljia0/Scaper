#Lulu Jiao
#cs5001 22fall 12/13/2022
#final project--amazon job openings scraper

import scrape
import unittest
class test_Class(unittest.TestCase):
    def test_init(self):
        '''test the constructor'''
        scaper = scrape.Scape('https://www.amazon.jobs/en/')
        self.assertEqual(scaper.url, 'https://www.amazon.jobs/en/')
    
    def test_click_button(self):
        '''because it is called in search function, so will be tested in it'''
        pass

    def test_search(self):
        '''test search function by displaying'''
        scaper = scrape.Scape('https://www.amazon.jobs/en/')
        scaper.search('software intern', 'seattle')
    
    def test_create_soup(self):
        '''test create_soup by printing'''
        scaper = scrape.Scape('https://www.amazon.jobs/en/')
        scaper.search('software intern', 'seattle')
        soup = scaper.create_soup()
        print(soup)
    
    def test_extract_title(self):
        '''test extract_tile function note that results might change because the website is dynamic'''
        scaper = scrape.Scape('https://www.amazon.jobs/en/')
        scaper.search('software intern', 'seattle')
        soup = scaper.create_soup()
        title_list = scaper.extract_title(soup)
        self.assertAlmostEqual(title_list, ['Software Development Engineer Intern 2023 - AR-Adroit ', 'Amazon Robotics - Software Development Engineer (SDE) Intern - Summer 2023, Business Intelligence/ Stats', 'Manager, Systems Engineering IAM, Project Kuiper', 'Network Development Engineer II - AMZ5610330', 'Network Development Engineer II - AMZ5907384', 'Sr. Principal PMT-ES, Amazon Connect', 'Sr. Systems Development Engineer - Identity and Access Management (IAM), Enterprise Engineering, Project Kuiper', 'Systems Development Engineer - Identity and Access Management (IAM), Enterprise Engineering, Project Kuiper', 'Quality Assurance Engineer Internship – 2023 (US)', 'Principal Product Manager – External Services - AMZ6030115'])
    
    def test_extract_location(self):
        '''test extract_location function in the same way as extract_title'''
        scaper = scrape.Scape('https://www.amazon.jobs/en/')
        scaper.search('software intern', 'seattle')
        soup = scaper.create_soup()
        location_list = scaper.extract_location(soup)
        print(location_list)
        self.assertEqual(location_list, ['USA, WA, Seattle', 'USA, WA, Seattle', 'USA, WA, Bellevue', 'USA, WA, Seattle', 'USA, WA, Seattle', 'USA, WA, Seattle', 'USA, WA, Bellevue', 'USA, WA, Bellevue', 'USA, WA, Seattle', 'USA, WA, Seattle'])
    
    def test_extract_id(self):
        '''test extract_id function in the same way as extract_title'''
        scaper = scrape.Scape('https://www.amazon.jobs/en/')
        scaper.search('software intern', 'seattle')
        soup = scaper.create_soup()
        id_list = scaper.extract_id(soup)
        self.assertEqual(id_list, ['2294182', '2289085', '2293167', '2271502', '2271323', '2214984', '2197629', '2197628', '2141837', '2279080'])
    
    def test_extract_link(self):
        '''test extract_link function in the same way as extract_title'''
        scaper = scrape.Scape('https://www.amazon.jobs/en/')
        scaper.search('software intern', 'seattle')
        soup = scaper.create_soup()
        link_list = scaper.extract_link(soup)  
        self.assertEqual(link_list, ['https://www.amazon.jobs/en/jobs/2294182/software-development-engineer-intern-2023-ar-adroit', 'https://www.amazon.jobs/en/jobs/2289085/amazon-robotics-software-development-engineer-sde-intern-summer-2023-business-intelligence-stats', 'https://www.amazon.jobs/en/jobs/2293167/manager-systems-engineering-iam-project-kuiper', 'https://www.amazon.jobs/en/jobs/2271502/network-development-engineer-ii-amz5610330', 'https://www.amazon.jobs/en/jobs/2271323/network-development-engineer-ii-amz5907384', 'https://www.amazon.jobs/en/jobs/2214984/sr-principal-pmt-es-amazon-connect', 'https://www.amazon.jobs/en/jobs/2197629/sr-systems-development-engineer-identity-and-access-management-iam-enterprise-engineering-project-kuiper', 'https://www.amazon.jobs/en/jobs/2197628/systems-development-engineer-identity-and-access-management-iam-enterprise-engineering-project-kuiper', 'https://www.amazon.jobs/en/jobs/2141837/quality-assurance-engineer-internship-2023-us', 'https://www.amazon.jobs/en/jobs/2279080/principal-product-manager-external-services-amz6030115'])
def main():
    test = test_Class()
    test.test_init()
    test.test_click_button()
    test.test_search()
    test.test_create_soup()
    test.test_extract_title()
    test.test_extract_location
    test.test_extract_id()
    test.test_extract_link()
if __name__=='__main__':
    main()
        







    

        
        


        