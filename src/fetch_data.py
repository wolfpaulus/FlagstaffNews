""" This module fetches the latest news from the Arizona Daily Sun website. """
from requests import get
from bs4 import BeautifulSoup


def fetch_news() -> list[dict]:
    """Fetch the latest news from the Arizona Daily Sun website.
    Returns:
        list[dict]: A list of dictionaries containing the title, link, and description of the news.
    """
    news = []
    url = "https://www.abc15.com/news/region-northern-az/flagstaff.rss"
    try:
        response = get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'xml')
        for item in soup.find_all('item')[:5]:
            print(item)
            news.append({
                'title': item.title.text,
                'link': item.link.text,
                'description': item.description.text
            })
    except OSError as e:
        print(e)
    return news


if __name__ == '__main__':
    print(fetch_news())
