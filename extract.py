import json

def get_likely_tweets(texts):
	likely_discounts = []

	# pick posts with certain keywords 
	keywords = ['discount', 'off', 'code', 'free', 'save', '%']
	for entry in texts: 
		if any(keyword in entry for keyword in keywords):
			likely_discounts.append(entry)
			#print(entry)
	return likely_discounts

def get_likely_codes(texts):
	
	likely_discounts = get_likely_tweets(texts)

	likely_codes = []

	# most codes are either in all caps or in quotation marks, pick these words
	for entry in likely_discounts:
		temp = entry.split('\"') #checks for quoted values
		for chunk in temp:
			if ([chunk.strip()] == chunk.strip().split()):
				#print (chunk.strip())
				likely_codes.append(chunk.strip())

		temp = entry.split(' ') #checks for all caps 
		for chunk in temp:
			if (chunk.isupper()):
				likely_codes.append(chunk)

	# remove duplicates
	likely_codes = set(likely_codes)
	return likely_codes

def get_codes(texts):
	'''
	Return a list of codes given a list of tweet texts 
	'''
	likely_codes = get_likely_codes(texts)

	cleaned_codes = []

	# remove quotation marks and duplicates
	for entry in likely_codes:
		cleaned_codes.append(entry.replace('"', ''))
	cleaned_codes = set(cleaned_codes)

	lengthy_codes = []

	# remove codes that are too short, these are usually false positives 
	for entry in cleaned_codes:
		if len(entry) > 3:
			lengthy_codes.append(entry)
	return lengthy_codes
			