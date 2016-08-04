import extract
import tags
import tweets

if __name__ == "__main__":
	print("Don't forget to chcp 65001") # this is a reminder to me when I run this program from command line
	print('Enter your query')
	query = input()

	list_of_tags = tags.get_tags(query)

	list_of_tweets = tweets.get_tweets(list_of_tags)

	result = extract.get_codes(list_of_tweets)

	for code in result:
		print (code)
