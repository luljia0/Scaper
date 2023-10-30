#Lulu Jiao
#cs5001 22fall 12/13/2022
#final project--amazon job openings scraper

import scrape_pages
import scrape
import unittest
class test_scrape_pages(unittest.TestCase):
    def test_get_total_pages(self):
        scaper = scrape.Scape('https://www.amazon.jobs/en/')
        scaper.search('software intern', 'seattle')
        soup = scaper.create_soup()
        total_pages = scrape_pages.get_total_pages(soup)
        self.assertEqual(total_pages,8)
    def test_page_Xpath(self):
        page_Xpath = scrape_pages.page_Xpath(2)
        self.assertEqual(page_Xpath, "//button[@data-label='2']")


def main():
    test = test_scrape_pages()
    test.test_get_total_pages()
    test.test_page_Xpath()
if __name__=='__main__':
    main()