from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
scraper = Scraper()

urls = [
    "https://www.hollywoodreporter.com/c/movies/movie-news/",
    "https://www.hollywoodreporter.com/c/tv/tv-news/",
    "https://ew.com/",
    "https://variety.com/v/tv/news/",
    "https://variety.com/v/film/news/"
]

@app.get("/")
async def read_root():
    articles = []
    for url in urls:
         articles.extend(await scraper.scrapedata(url))
    sorted_list = sorted(articles, key=lambda x: x['published'], reverse=True)
    return sorted_list

# @app.get("/articles/{publisher}")
# def read_articles_by_publisher(publisher: str):
#     publisher_articles = [article for article in articles if publisher.lower() in article['link'].lower()]
#     return publisher_articles