import requests
print "request to create article 1"
resp = requests.post("http://localhost:5000/article/1", json = {'vote': 1,
                                                                'title': 'first article',
                                                                'content': 'some',
                                                                'author': 'foo',
                                                                })
print resp.json(), resp.status_code

print "request to view created article"
resp = requests.get("http://localhost:5000/article/1")
print resp.json(), resp.status_code

print "request to create article 2"
resp = requests.post("http://localhost:5000/article/2", json = {'vote': 1})
print resp.json(), resp.status_code

print "request to upvote created article 1"
resp = requests.put("http://localhost:5000/article/1", json = {'vote': 2})
print resp.json(), resp.status_code

print "request to list created articles in descending order of vote"
resp = requests.get("http://localhost:5000/articles")
print resp.json(), resp.status_code
