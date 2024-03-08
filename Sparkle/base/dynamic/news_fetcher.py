import json
import requests
from datetime import datetime

def get_articles():
    all_articles = []
    result = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=54221123bc0f436d861fd14a82266119')

    content = json.loads(result.content)
    articles = content['articles']
    for article in articles:
        title = article['title']
        description = article['description']
        origin = article['url']
        content = article['content']
        created_date = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ').date()


        formatted_date = datetime.strftime(created_date, '%Y-%m-%d')
        all_articles.append({'title':title,
                            'description': description, 'origin':origin, 'content': content, 'created': formatted_date})
    return all_articles