from bs4 import BeautifulSoup as Bs
import time
import csv
import requests




START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
headers= ["proper_name","bayer_designation","distance","spectral_class","mass","radius","luminiosity"]
stars_data=[]

site = requests.get(START_URL, verify=False)
time.sleep(10)

soup = Bs(site.text, 'html.parser')

for tr_tags in soup.find_all('tr'):
    td_list = tr_tags.find_all('td')
    stars_data.append(td_list)


with open("data.csv",'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)
    