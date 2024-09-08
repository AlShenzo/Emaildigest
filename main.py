import requests
from send_email import send_email

url=('https://newsapi.org/v2/'
     'top-headlines?sources=techcrunch&'
     'apiKey=61a06b758397412aa4049959e9a59599')

api_key='61a06b758397412aa4049959e9a59599'
# make request
request = requests.get(url)
#get dictionary with data
content = request.json()

# access article title and description
body = ""
for article in content['articles']:
    if article['title'] is not None: # in case one of the title has none type sometime it does
        body = body + article['title'] + '\n' + article['description'] +2*'\n'

subject = 'Daily Tech Digestion'

body = body.encode('utf-8')


send_email(body)







