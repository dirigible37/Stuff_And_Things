s = "newegg"
i = "1070"


data = {'man' : 'msi', 'model':'ftw', 'datetime':'123456', 'price':'59.99'}

def write_data (site_name, item_name, data_obj):
	file_name = "./data/"+site_name+"/"+item_name
	target = open(file_name, "w")
	target.write(data_obj['man'] + " " + data_obj['model'] + " " + data_obj['price'] + " " + data_obj['datetime'])

write_data(s, i, data)
