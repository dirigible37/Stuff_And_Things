import requests, bs4 
from datetime import datetime

r = requests.get('https://slickdeals.net/deals/video-card/')

soup = bs4.BeautifulSoup(r.text, "html.parser")

lines = soup.find_all('a', {"class" : "itemTitle"})

for line in lines:
    print(line.string)




'''
Reference Material

cells = soup.findAll('td', {"class" : "lft lm"})

soup = bs4.BeautifulSoup(r.text, "html.parser")
data = soup.select('div[class="itemPrice wide"]')
price = data[0]['content']
site = "newegg"
item = "1070"
data_obj = {'man':'EVGA', 'model':'ftw', 'datetime':str(datetime.now()), 'price':price}
write_data.write_out(site, item, data_obj)
'''
