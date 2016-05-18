import json
import urllib.request
import urllib.parse
import urllib.error
import itertools
from base64 import b64encode

import json
from pprint import pprint

print("Don't forget to chcp 65001") # this is a reminder to me when i run this program from command line

with open('key.txt', 'r') as f:
	igkey = f.readline()
	f.readline()
	twitterkey = f.readline().strip()
	f.readline()
	consumer_key = f.readline() 
	consumer_secret = f.readline()

term = 'food' #search term from user input
num_tags = 5 # number of tags to search
num_pages = 3 # number of pages to search
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


#Twitter authentication and stuff :)

query = "daniel wellington"
query = query.encode('ascii') #encode to ascii

print(twitterkey)
btwitter = twitterkey.encode('utf-8')
b64twitter = b64encode(btwitter)
twitterkey = bytes.decode(b64twitter)
print(twitterkey)
url = "https://api.twitter.com/oauth2/token"
#data = {"grant_type" : "client_credentials"}
#data = urllib.parse.urlencode(data)
data = "grant_type=client_credentials"
data = data.encode('utf-8')
headers = {'Authorization' : "Basic "+twitterkey+"", 'Content-Length' : '29','User-Agent':'myapp v1','Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
method = "POST"
request = urllib.request.Request(url,data,headers,method)
try:
	response = urllib.request.urlopen(request)
except urllib.error.HTTPError as e:
	print(e.fp.read())
	print("ERROR: 403, rate limit exceeded")

auth_response = bytes.decode(response.read())
auth_response_json = json.loads(auth_response)
bearer_token = auth_response_json['access_token']

print(response.read())
print(bearer_token)
print(type(bearer_token))

'''
GET /1.1/search/tweets.json?q=danielwellington&count=30 HTTP/1.1
Host: api.twitter.com
User-Agent: My Twitter App v1.0.23
Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%2FAAAAAAAAAAAA
                      AAAAAAAA%3DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Accept-Encoding: gzip
'''

bearer_dict = "Bearer " + bearer_token
print("Bearer dict: " + bearer_dict)

url = 'https://api.twitter.com/1.1/search/tweets.json?q='+ query +'&count=100'
headersz = {'User-Agent' : "discount-me", 'Authorization' : bearer_dict}
headersz = {}
print(type(headers))
method = 'GET'

data=""
data  = data.encode('utf-8')

headers = {'Authorization' : "Bearer "+bearer_token+"", 'User-Agent':'myapp v1'}

request = urllib.request.Request(url, data=None, headers=headers, method=method)
response = urllib.request.urlopen(request)

search_response = bytes.decode(response.read())
search_response_json = json.loads(search_response)

with open('response100.json', 'w') as out:
	json.dump(search_response_json, out, indent=4)

#print(search_response_json) #IT WORKED!!!

#cache the token from response

#import twitter.oauth_dance

#access_key, access_secret = twitter.oauth_dance("discount-me", consumer_key, consumer_secret)


#(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
