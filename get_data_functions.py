from bs4 import BeautifulSoup
import requests
import os
import pandas
import csv
import numpy as np

class Get_data():
    
    def __init__(self):
        self.season = input("Please enter the year of the season: ")
        self.url = 'https://www.basketball-reference.com/leagues/NBA_{}_standings.html'.format(self.season)

    def html_code_stored_in_a_file(self):
        url=self.url

        source=requests.get(url).text
        soup=BeautifulSoup(source, 'lxml')

        file=open('html_code.html','w')
        file.write(soup.prettify())
        file.close

    def find_table(self,html_file):
        soup = BeautifulSoup(html_file, 'lxml')
        table = soup.find(class_='sortable stats_table')
        #print(table)
        return table

    def get_headers(self,table):
        headers = []
        #find all headings
        for i in table.thead.find('tr', class_=False):
            title=i.text.strip()
            headers.append(title)

            # remove the Rk heading
            headers2=headers[2:]    
            #remove empty elements from the list of headings
            new_headers = list(filter(None, headers2))

        return new_headers

    def find_rows(self,table):
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
            #print(b)
        return spli_team 

    def replace(self):
        with open('html_code.html', 'r') as html_file:
            file_content = html_file.read()
            file_content= file_content.replace(" <!--", "")
        with open('html_code.html', 'w') as html_file:
            html_file.write(file_content)


data=Get_data()
data.html_code_stored_in_a_file()
data.replace()

 #open the file
with open('html_code.html') as html_file:
    table = data.find_table(html_file)
    headers = data.get_headers(table)
    csv_file = open('nba_test.csv', 'w')
    #create a writer
    csv_writer = csv.writer(csv_file)
    #write the headings to the csv file
    csv_writer.writerow(headers)
    r = data.find_rows(table)
        
    for array in r:
        b = (list(array))
        #add the rows to the csv file
        csv_writer.writerow(b)
               
#close the file
csv_file.close()


    


