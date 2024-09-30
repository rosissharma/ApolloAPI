from requests_html import AsyncHTMLSession
import dateparser

class Scraper():

    async def scrapedata(self, url):
        session = AsyncHTMLSession()
        response = await session.get(url)
        await response.html.arender()
        
        # array to store all the articles
        articles_list = []

        #Cover both TV and Movies from Hollywood Reporter
        if "hollywoodreporter.com" in url:
            for article in response.html.find('div.story'):
                try:
                    title = article.find('h3#title-of-a-story > a.c-title__link', first=True).text.strip()
                    link = article.find('h3#title-of-a-story > a', first=True).attrs['href']
                    content = article.find('p.c-dek', first=True).text.strip()
                    image = article.find('img.c-lazy-image__img', first=True).attrs['src']
                    image_alt_text = article.find('img.c-lazy-image__img', first=True).attrs['alt']
                    author = article.find('div.c-tagline > a > span', first=True).text
                    tag = article.find('a.c-span__link', first=True).text
                    published = dateparser.parse(article.find('time.c-timestamp', first=True).text.strip())

                    articles_list.append({
                            'title': title,
                            'link': link,
                            'content': content,
                            'image': image,
                            'image_alt_text': image_alt_text,
                            'author': author,
                            'tag': tag,
                            'published': published,
                            'source': 'Hollywood Reporter'
                        })
                except Exception as e:
                    print('ERROR: ', e)
                    pass
        # Grab latest news from Entertainment Weekly
        elif "ew.com" in url:
            for article in response.html.find('main div.featured__latest-feed a.comp'):
                try:
                    title = article.find('span.card__title-text', first=True).text.strip()
                    link = article.find('a.comp', first=True).attrs['href']
                    image = article.find('div.img-placeholder > img.card__img', first=True).attrs['data-src']
                    image_alt_text = article.find('img.card__img', first=True).attrs['alt']
                    author = article.find('div.card__byline', first=True).attrs['data-byline'].replace('By ', '')
                    tag = article.find('div.card-meta', first=True).attrs['data-taxonomy']
                    published = dateparser.parse(article.find('div.card-meta', first=True).attrs['data-block-date'])

                    articles_list.append({
                            'title': title,
                            'link': link,
                            'image': image,
                            'image_alt_text': image_alt_text,
                            'author': author,
                            'tag': tag,
                            'published': published,
                            'source': 'Entertainment Weekly'
                        })
                except Exception as e:
                    print('ERROR: ', e)
                    pass
        # Grab latest news from Variety
        elif "variety.com" in url:
            for article in response.html.find('li.o-tease-list__item'):
                try:
                    title = article.find('h3#title-of-a-story', first=True).text.strip()
                    link = article.find('a.c-title__link', first=True).attrs['href']
                    image = article.find('img.c-lazy-image__img', first=True).attrs['src']
                    image_alt_text = article.find('img.c-lazy-image__img', first=True).attrs['alt']
                    tag = article.find('a.c-span__link', first=True).text.strip()
                    published = dateparser.parse(article.find('time.c-timestamp', first=True).text.strip())

                    articles_list.append({
                            'title': title,
                            'link': link,
                            'image': image,
                            'image_alt_text': image_alt_text,
                            'tag': tag,
                            'published': published,
                            'source': 'Variety'
                        })
                except Exception as e:
                    print('ERROR: ', e)
                    pass
        
        # return all the stored articles
        return articles_list