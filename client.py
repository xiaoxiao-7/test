import requests

user_query = {'query_string': 'tpv amount of radd table from apac'}
# user_query = {'name' : "jane", 'like' : 'apple'}
r = requests.post("http://127.0.0.1:5000", data=user_query)

print(r.text)
