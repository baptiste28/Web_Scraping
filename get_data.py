from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import pandas
import csv
import pprint
import numpy as np


#Keep in mind that we have to uncomment mannualy some part of the HTML code and save the file!!!!!
def html_code_stored_in_a_file(url):
    source=requests.get(url).text
    soup=BeautifulSoup(source, 'lxml')

    file=open('html_code.html','w+')
    file.write(soup.prettify())
    file.close

url = 'https://www.basketball-reference.com/leagues/NBA_2021_standings.html'

#if the file exists do nothing
if os.path.exists('./html_code.html'):
    pass
#if the file does not exist, call the function html_code_stored_in_a_file
else:
    html_code_stored_in_a_file(url)

#open the file
with open('html_code.html') as html_file:

    soup = BeautifulSoup(html_file, 'lxml')
    table = soup.find(class_='sortable stats_table')
    #print(table.prettify())

    
    caption = table.caption.text
    print(caption)

    headers = []
    #upper_headings = table.thead.find('tr').text
    #print(upper_headings)

    for i in table.thead.find('tr', class_=False):
        title=i.text.strip()
        headers.append(title)

    headers2=headers[2:]    
    print(headers2)
    new_headers = list(filter(None, headers2))
    print(new_headers)

    csv_file = open('nba.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(new_headers)
    pprint.pprint(len(new_headers))

    

    data_frame=pandas.DataFrame(columns=new_headers)

    rows = []
    for tr in table.tbody.findAll('tr'):
       for td in tr.findAll('td'):       
               value = td.text
               rows.append(value)

 
    spli_team = np.array_split(rows,30)
    for array in spli_team:
        b = (list(array))
        csv_writer.writerow(b)
        





    # #for tr in table.tbody.find('tr'):
    # #     for td in tr.findAll('td'):       
    # #         value = td.text
    # #         rows.append(value)
    # #     print(rows)
    # #         #data_frame.append(rows)
    # # #print(data_frame)

    csv_writer.writerow(rows)

csv_file.close()



