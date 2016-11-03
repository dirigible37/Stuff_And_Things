def write_data (site_name, item_name, data_obj):
	file_name = "/data/"+site_name+"/"+item_name
	target = open(file_name, "a")
	target.write(data_obj)
