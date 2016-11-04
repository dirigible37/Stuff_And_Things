import write_data
import requests, bs4 
from datetime import datetime

r = requests.get('http://www.newegg.com/Product/Product.aspx?Item=N82E16814487259')

soup = bs4.BeautifulSoup(r.text, "html.parser")

data = soup.select('div meta[itemprop="price"]')

price = data[0]['content']

site = "newegg"
item = "1070"

data_obj = {'man':'EVGA', 'model':'ftw', 'datetime':str(datetime.now()), 'price':price}

write_data.write_out(site, item, data_obj)
