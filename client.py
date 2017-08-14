import requests

user_query = {'query_string': 'test test'}
r = requests.post("http://127.0.0.1:5000", data=user_query)

print(r.text)
