import json
import urllib.request

print("Don't forget to chcp 65001") # this is a reminder to me when i run this program from command line

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

# now we get the recent posts for those tags. 

#https://api.instagram.com/v1/tags/{tag-name}/media/recent?access_token=ACCESS-TOKEN

posts = [] #all posts

for tag in tags:
	response = urllib.request.urlopen('https://api.instagram.com/v1/tags/'+ tag + '/media/recent?' + '&access_token=' + key)
	response_string = response.read().decode('utf-8')
	data = json.loads(response_string)
	data = data['data'] # array of posts
	for obj in data:
		posts.append([obj['caption'],obj['likes'],obj['link']])

print(posts)

#now i have a list of posts 
#need to retrieve more posts, check notes for SO link to potential solution 
#retrieve posts, and validate each to see if it's relevant
#for now, print out body text of the posts which are relevant

