import requests

url=('https://newsapi.org/v2/'
     'top-headlines?sources=techcrunch&'
     'apiKey=61a06b758397412aa4049959e9a59599')

api_key='61a06b758397412aa4049959e9a59599'
# make request
request = requests.get(url)
#get dictionary with data
content = request.json()

# access article title and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])




