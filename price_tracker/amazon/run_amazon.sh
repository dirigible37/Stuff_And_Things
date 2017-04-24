while read p; do
	python amazon_request.py $p	
done <items.txt
