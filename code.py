
# coding: utf-8

# In[5]:

import os
import csv
import re
import xlrd


# In[64]:

def convert_to_csv():
    wb = xlrd.open_workbook('C:\\Users\\student\\Desktop\\exam\\tables\\source.xls', encoding_override='utf-8')
    sheet = wb.sheet_by_index(0)
    csv_table = open('csv_table.csv', 'w', encoding='utf-8')
    wr = csv.writer(csv_table, quoting = csv.QUOTE_ALL)
    
    for rownum in range(sheet.nrows):
        wr.writerow(sheet.row_values(rownum))
    
    csv_table.close()


# In[65]:

convert_to_csv()


# In[92]:

def exp_dates():
    with open('csv_table.csv', newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        with open('C:\\Users\\student\\Desktop\\dates.csv', newline = '') as csvfile:
            dates = csv.writer(csvfile, delimiter = ',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in f:
                row = int(raw['created'])
                
                
                
exp_dates()


# In[ ]:




# In[ ]:



