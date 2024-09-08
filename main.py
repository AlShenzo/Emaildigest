import requests
from send_email import send_email



url='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=61a06b758397412aa4049959e9a59599&language=en'

api_key='61a06b758397412aa4049959e9a59599'
# make request
request = requests.get(url)
#get dictionary with data
content = request.json()

# access article title and description
body = ""
for article in content['articles'][0:20]:#[0:20] to give us only 20 emails if more than 20
    if article['title'] is not None: # in case one of the title has none type sometime it does
        body = "Subject: Today's News" \
              +'\n'+ body + article['title'] + '\n' \
                + article['description'] \
                +'\n' +article['url']+ 2*'\n'

body = body.encode('utf-8')

send_email(body)







