#Lulu Jiao
#cs5001 22fall 12/13/2022
#final project--amazon job openings scraper

import write
import unittest
import pandas as pd
class test_write(unittest.TestCase):
    def test_init(self):
        writer = write.Write('', '')
        self.assertEqual(writer.sheet_name, 'Amazon Job Openings Tracker')
    def test_create_dataframe(self):
        '''test create_dataframe function by printing the dataframe'''
        writer = write.Write('','')
        df = writer.create_dataframe([1,2,3],[1,2,3],[1,2,3],[1,2,3])
        print(df)
        return df
    def test_write_sheet(self):
        '''test write_sheet function by checking whether the data is written to the google sheet'''
        writer = write.Write('','')
        df = pd.DataFrame({'row1':[1,2,3]})
        writer.write_sheet(df, 1)
def main():
    test = test_write()
    test.test_init()
    test.test_create_dataframe()
    test.test_write_sheet()
if __name__=='__main__':
    main()
