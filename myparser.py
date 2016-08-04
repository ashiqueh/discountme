from html.parser import HTMLParser

class TwitterParser (HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []
        self.resources = []
        self.current_resource = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            #<div class="js-tweet-text-container">
            if ('class','js-tweet-text-container') in attrs:
                url = 'https://instagram.com' + dict(attrs)['href']
                #print (url)
                self.data.append(url) # appends url to data
        	# [ ('class','_8mlbc _vbtk2 _t5r8b') ]   ---- this is a post
        	# [ ('class','_oidfu') ] ---- this is the "next page" button 
        if tag == 'meta':
            if ('property','og:video') in attrs or ('property','og:image') in attrs:
                url = dict(attrs)['content']
                url = url.split('?ig_cache_key',1)[0]
                self.resources.append(url)
                self.current_resource = url 

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
    	pass
