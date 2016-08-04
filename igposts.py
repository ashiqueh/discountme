
# now we get the recent posts for those tags. 

#https://api.instagram.com/v1/tags/{tag-name}/media/recent?access_token=ACCESS-TOKEN

'''
# key is my secret key, which i'm using for testing purposes

# Authorize: https://www.instagram.com/oauth/authorize/?client_id=ID&redirect_uri=http://ashiqueh.me/&response_type=token&scope=public_content

# json response with list of tags
response = urllib.request.urlopen('https://api.instagram.com/v1/tags/search?q=' + term + '&access_token=' + igkey)

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
'''

#term = 'food' #search term from user input
#num_tags = 5 # number of tags to search
#num_pages = 3 # number of pages to search

posts = [] #all posts

for tag in tags:
	next_min_id = ""
	for i in range(0, num_pages):
		response = urllib.request.urlopen('https://api.instagram.com/v1/tags/'+ tag + '/media/recent?' + '&count=33&next_min_id=' + next_min_id + '&access_token=' + key)
		#print('https://api.instagram.com/v1/tags/'+ tag + '/media/recent?' + '&count=33&access_token=' + key)
		response_string = response.read().decode('utf-8')
		data = json.loads(response_string)
		#pagination info
		pagination = data.get('pagination', '')
		#print (pagination)
		next_min_id = pagination.get('next_min_id', '') #get the next page id if it exists 
		data = data['data'] # array of posts
		for obj in data:
			posts.append([obj['caption'],obj['likes'],obj['link']])

#posts = list(set(posts)) #remove duplicates

#posts[0][6] = "dabadidoo"
for post in posts: 
	post[1] = ""

#removes duplicates in posts (still doesn't work, not sure why -)
# TODO: convert the post json into a useful object (probably array of arrays or maybe a dict), then apply logic to that

post_set = (map(tuple, posts))
post_set = set(post_set)
posts = map(list, post_set)

# THIS DOESNT WORK because the count on each post is different, even if the post is the same - remove count and solve the problem. 
#posts=list(posts for posts,_ in itertools.groupby(posts))

print(posts)

#now i have a list of posts 
#need to retrieve more posts, check notes for SO link to potential solution 
# -- above is basically done .. 

#retrieve posts, and validate each to see if it's relevant
#for now, print out body text of the posts which are relevant

#get it verified by instagram then actually troubleshoot lol 

#actually instagram is terrible and won't let me do this legally. hi twitter