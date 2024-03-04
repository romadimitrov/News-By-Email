import requests
from send_email import send_email

topic = 'bitcoin'
api_key = '591efdcef62b4ac690051e6ffb224e93'
url = 'https://newsapi.org/v2/everything?' \
        f'q={topic}&' \
        'from=2024-02-04&' \
        'sortBy=publishedAt&' \
        'apiKey=591efdcef62b4ac690051e6ffb224e93&' \
        'language=en'

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article title and description
body = 'Subject: Today\'s news\n'
for article in content['articles'][0:20]:
    if article['title'] is not None and article['description'] is not None:
        body = body + article['title'] + '\n' + article['description'] \
            + '\n'+ article['url'] + 2*'\n'

body = body.encode("utf-8")   
send_email(body)
