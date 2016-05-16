'''
1395059493.847eb5f.15640fd231f1427cac2880683aca1df6

Authorize: 
https://www.instagram.com/oauth/authorize/?client_id=847eb5f761f84423b8921c2359540197&redirect_uri=http://ashiqueh.me/&response_type=token&scope=public_content

process:

http://stackoverflow.com/questions/13921910/python-urllib2-receive-json-response-from-url
basically use urllib and json, and do some clever stuff with the data 

sandbox mode = just returns posts from me .... well that's stupid, instagram...  prolly reasons
	- make some fake posts / edit my own recent post descriptions to test this in sandbox i guess??
	- or make a fake IG account to test with??

user enters search term
get search results from tags/search
take 3? most popular tags, and retrieve recent posts on that
parse through descriptions, find posts with:
	- percent signs
	- numbers from 0-100
	- all caps words
	- "discount", "code", "off", "free", etc... (keywords)
initially, return the raw text of these posts
now the fun part... figure out a way to view the actual discount code and eliminate the noise
display codes!!

'''

