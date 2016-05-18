import json


#wrap these guys in functions:
# extract text
# extract url (uhh)
# extract like texts
# extract percentages
# extract discount codes, clean codes

with open('response100.json', encoding="utf-8") as data_file:    
    data = json.load(data_file)

data = data['statuses'] #unwrap statuses

#data = data.decode('utf-8')

texts = []
#urls = []

#print(data)

#print (type(data[0]['entities']['media'][0]['url']))

for idx,entry in enumerate(data):
	texts.append(data[idx].get('text',''))

	##print (data[idx].get('text','')) # works for text
	##print (data[idx].get('entities','')) #works for entities
	##print (data[idx].get('entities','').get('media','')) #works for entities

	#CONCLUSION: urls are not uniformly placed - why twitter?!?!?! 

likely_discounts = []

for entry in texts: #i think this can be made more efficient - look for all words on one pass through ? 
	if ('%' in entry) or ('discount' in entry) or ('off' in entry) or ('code' in entry) or ('free' in entry):
		likely_discounts.append(entry)
		#print(entry)

# now that we have the likely candidates, we can try and parse for a number (not sure how to do)

# after, we can extract the actual discount code, as follows:

# split at quotation marks
# parse through each entry, and if the size is just one word, add this to the list of likely codes

likely_codes = []

for entry in likely_discounts:
	temp = entry.split('\"')
	for chunk in temp:
		if ([chunk.strip()] == chunk.strip().split()):
			#print (chunk.strip())
			likely_codes.append(chunk.strip())

likely_codes = set(likely_codes)

cleaned_codes = []

for entry in likely_codes:
	cleaned_codes.append(entry)

for entry in likely_codes:
	print (entry)
		