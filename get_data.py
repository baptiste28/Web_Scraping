from bs4 import BeautifulSoup
import requests
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

#If the file exists do nothing
if os.path.exists('./html_code.html'):
    pass

#If the file does not exist, call the function html_code_stored_in_a_file. 
#Keep in mind that we have to uncomment mannualy some part of the HTML code and save the file!!!!!
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

    #find all headings
    for i in table.thead.find('tr', class_=False):
        title=i.text.strip()
        headers.append(title)

    # remove the Rk heading
    headers2=headers[2:]    
    print(headers2)
    #remove empty elements from the list of headings
    new_headers = list(filter(None, headers2))
    print(new_headers)

    #open the csv file
    csv_file = open('nba.csv', 'w')
    #create a writer
    csv_writer = csv.writer(csv_file)
    #write the headings to the csv file
    csv_writer.writerow(new_headers)

    rows = []
    #get all the data from the table rows
    for tr in table.tbody.findAll('tr'):
       for td in tr.findAll('td'):       
               value = td.text
               rows.append(value)

    #split the data into 30 lists because we have 30 teams
    spli_team = np.array_split(rows,30)
    for array in spli_team:
        b = (list(array))

        #add the rows to the csv file
        csv_writer.writerow(b)

#close the file
csv_file.close()



