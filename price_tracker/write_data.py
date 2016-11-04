def write_out (site_name, item_name, data_obj):
	file_name = "/home/wmohr/Stuff_And_Things/price_tracker/data/"+site_name+"/"+item_name
	target = open(file_name, "a")
	target.write(data_obj['man'] + " " + data_obj['model'] + " " + data_obj['price'] + " " + data_obj['datetime'] + "\n")
