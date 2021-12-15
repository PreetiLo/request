import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

r.status_code


r.headers['content-type']


r.encoding


r.text


r.json()
# {'private_gists': 419, 'total_private_repos': 77, ...}