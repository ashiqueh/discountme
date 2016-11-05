import json
import urllib.request
import urllib.parse
import urllib.error
from base64 import b64encode
from bs4 import BeautifulSoup
import re 

def get_tweet_list_from_json():
	'''
	Return a list of tweet texts from a Twitter API JSON result 
	'''
	# open the json file 
	with open('response.json', encoding="utf-8") as data_file:    
	    data = json.load(data_file)

	data = data['statuses'] #unwrap statuses
	texts = []

	# extract texts from json 
	for idx,entry in enumerate(data):
		texts.append(data[idx].get('text',''))

	return texts 

def get_tweets_from_api(key, tags):
	'''
	Return a list of tweets from top N tags 
	'''
	twitterkey = key # twitter api key

	# text key -> utf-8 encode -> b64 encode -> convert to string
	btwitter = twitterkey.encode('utf-8')
	b64twitter = b64encode(btwitter)
	twitterkey = bytes.decode(b64twitter)

	# twitter api stuff: authentication 
	url = u"https://api.twitter.com/oauth2/token"
	data = u"grant_type=client_credentials"
	data = data.encode('utf-8')
	headers = {u'Authorization' : u"Basic "+twitterkey+"", 'Content-Length' : u'29',u'User-Agent':u'myapp v1',u'Content-Type':u'application/x-www-form-urlencoded;charset=UTF-8'}
	method = "POST".encode('utf-8')
	request = urllib.request.Request(url,data,headers,method)
	try:
		response = urllib.request.urlopen(request)
	except urllib.error.HTTPError as e:
		print(e.fp.read())
		print("ERROR: 403, rate limit exceeded.. probably") 

	# TODO: Cache the bearer token so it's only refreshed occasionally 
	# grab bearer_token from twitter API response 
	auth_response = bytes.decode(response.read())
	auth_response_json = json.loads(auth_response)
	bearer_token = auth_response_json['access_token']

	list_of_tweet_texts = []

	#ttags = (tag for tag in tags if isinstance(tag, unicode)) #removes un-encodable characters

	#for tag in tags:
	#	tag = urllib.parse.unquote(tag).encode('gbk')
	#	tag = urllib.parse.quote(tag)


	for tag in tags:
		# more twitter api stuff: this is where the search api is used 
		t = urllib.parse.quote(tag) # url encodes tags with special characters
		url = 'https://api.twitter.com/1.1/search/tweets.json?q='+ t +'&count=100'
		#scheme, netloc, path, query, fragment = urllib.parse.urlsplit(url) # must encode because tags may not be properly encoded
		#path = urllib.parse.quote(path)
		#url = urllib.parse.urlunsplit((scheme, netloc, path, query, fragment))
		#url = urllib.parse.quote(url)
		#url = urllib.parse.unquote(url)
		method = 'GET'
		data = ""
		data  = data.encode('utf-8')
		headers = {'Authorization' : "Bearer "+bearer_token+"", 'User-Agent':'myapp v1'}

		request = urllib.request.Request(url, data=None, headers=headers, method=method)
		# decode response to json 
		response = urllib.request.urlopen(request)

		search_response = bytes.decode(response.read())
		search_response_json = json.loads(search_response)

		# dump json into a file 
		with open('response.json', 'w') as out:
			json.dump(search_response_json, out, indent=4)

		# reads the json file that was just created and extracts the tweet texts 
		list_of_tweet_texts.extend(get_tweet_list_from_json())

	return list_of_tweet_texts

def get_tweets_from_html(tags):
	'''
	Return a list of tweets from the HTML of a twitter search result.
	'''
	num_tags = 1
	list_of_tags = tags[:num_tags]

	tweet_texts = [] 

	for tag in list_of_tags:
		url = 'https://twitter.com/search?q=' + tag + '&src=typd'
		try:
			resp = urllib.request.urlopen(url)
		except Exception as e:
			print('Unable to retrieve resource: %s' % picture)
		# decode and unquote html
		html = bytes.decode(resp.read())
		html = urllib.parse.unquote(html)
		# html parser
		soup = BeautifulSoup(html, 'html.parser')
		res = soup.find_all('div', class_='js-tweet-text-container')
		# for each tweet, remove html elements (leaving only text), add to list 
		for tweet in res:
			#print(tweet)
			tweet_texts.append((re.sub(r'\<[^>]*\>', '', str(tweet))).replace('\n',''))

	return tweet_texts

def get_tweets(tags):
	'''
	Return a list of relevant tweets given a list of tags. 
	'''
	with open('key.txt', 'r') as f:
		igkey = f.readline()
		f.readline() 
		twitterkey = f.readline().strip()
		f.readline()

	tweets = get_tweets_from_api(twitterkey, tags)
	tweets.extend(get_tweets_from_html(tags))

	return tweets 