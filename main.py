import requests

api_key = '591efdcef62b4ac690051e6ffb224e93'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-02-04&sortBy=publishedAt&apiKey=591efdcef62b4ac690051e6ffb224e93'

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article title and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])
    print('')