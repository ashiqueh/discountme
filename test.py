# some testing with base64

from base64 import b64encode
from base64 import b64decode

s = "nlVxUHeInQM9X6JgQcZjZJYeT:sUiaOVuwrGJAYAV6uW0DWrU9nv09TNvVWzOgEZnlfgDu0AZHyj"
print(s)
encoded_s = s.encode('utf-8')
print(encoded_s)
b64_encoded_s = b64encode(encoded_s)
print(b64_encoded_s)
string_b64 = bytes.decode(b64_encoded_s)
print(string_b64)
b64_decoded = b64decode(b64_encoded_s)
print (b64_decoded)