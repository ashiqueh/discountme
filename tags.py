import json
import urllib.request
import urllib.parse

def get_tag_list_api(key, query):
	'''
	Return a list of popular tags and usage counts given an api key and query, using Instagram's API. 
	'''
	query = urllib.request.quote(query) # convert to % encoding  
	print('Encoded query: ' + query)

	# json response with list of tags
	response = urllib.request.urlopen('https://api.instagram.com/v1/tags/search?q=' + query + '&access_token=' + key)

	# convert response into something readable by py3
	response_string = response.read().decode('utf-8')

	# now that response is a string, we can parse the json using python's json library
	data = json.loads(response_string)

	# gets data array from json object (this actually contains the data)
	data = data['data'] 

	l = [] # dict for tags

	# append list of [tag, count] to list 
	for obj in data:
		l.append([obj['name'],obj['media_count']])

	return l 

def get_tags(query):
	'''
	Return an sorted list of tags directly and indirectly associated with a query, using Instagram's API. 
	'''

	num_tags = 15 # number of tags to search

	with open('key.txt', 'r') as f:
		igkey = f.readline()
		f.readline() 
		twitterkey = f.readline().strip()
		f.readline()
	
	# now we have a neat list of lists [ [name,count] ] !!
	l = get_tag_list_api(igkey, query)

	# sort high to low by 2nd element (count)
	l.sort(key=lambda o:o[1])
	l.reverse()

	# trim list 
	l = l[:num_tags]

	# extract just the tags
	tags = [item[0] for item in l]

	tags.append(urllib.request.quote(query))

	print('tags: ')
	print(tags)

	return tags 