import json
import urllib.request

with open('key.txt', 'r') as f:
	key = f.readline()

term = 'food' #search term from user input
num_tags = 5 # number of tags to search

# key is my secret key, which i'm using for testing purposes

# Authorize: https://www.instagram.com/oauth/authorize/?client_id=847eb5f761f84423b8921c2359540197&redirect_uri=http://ashiqueh.me/&response_type=token&scope=public_content

# json response with list of tags
response = urllib.request.urlopen('https://api.instagram.com/v1/tags/search?q=' + term + '&access_token=' + key)

#lol ghetto py3 workaround. 
response_string = response.read().decode('utf-8')

#now that response is a string, we can get the json object:
data = json.loads(response_string)

#gets data array from json object
data = data['data'] 

l = [] # dict for tags

for obj in data:
	l.append ([obj['name'],obj['media_count']])
# now we have a neat list of lists [ [name,coutn] ] !!

# sort high to low by 2nd element (count)
l.sort(key=lambda o:o[1])
l.reverse()

# trim list
l = l[:num_tags]

#extract just the tags
tags = [item[0] for item in l]

print (tags)