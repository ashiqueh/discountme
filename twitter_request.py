'''
GET /1.1/search/tweets.json?q=danielwellington&count=30 HTTP/1.1
Host: api.twitter.com
User-Agent: My Twitter App v1.0.23
Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%2FAAAAAAAAAAAA
                      AAAAAAAA%3DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Accept-Encoding: gzip
'''
import urllib.request

# https://api.twitter.com/1.1/search/tweets.json?q=from%3ACmdr_Hadfield%20%23nasa&result_type=popular

# https://api.twitter.com/1.1/search/tweets.json?q=danielwellington&count=100

'''
GET /1.1/search/tweets.json?q=danielwellington&count=30 HTTP/1.1
Authorization:
OAuth oauth_consumer_key="DC0sePOBbQ8bYdC8r4Smg",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1463501586",oauth_nonce="752996313",oauth_version="1.0",oauth_token="547891264-CPEXoMH4WTgIcr73dsvWJ0ymIF9HCoRRMlJ9JNZb",oauth_signature="1%2FsMSvRfDT15eWSYhTzxgcbGHTc%3D"
Host:
api.twitter.com
X-Target-URI:
https://api.twitter.com
Connection:
Keep-Alive
'''