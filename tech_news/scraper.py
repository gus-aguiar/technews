import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        response.raise_for_status()
        return response.text
    except Exception:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    elementos = selector.css(".entry-title a::attr(href)")
    return elementos.getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(".nav-links a.next::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    date = selector.css(".meta-date::text").get()
    author = selector.css(".author a::text").get()
    reading_time = int(
        selector.css(".meta-reading-time::text").re_first(r"\d+")
    )
    summary = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()
    category = selector.css(".category-style .label::text").get()
    return {
        "url": url,
        "title": title,
        "timestamp": date,
        "writer": author,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    site_content = fetch("https://blog.betrybe.com/")
    list_news = scrape_updates(site_content)
    news = []

    for idx in range(amount):
        if idx % len(list_news) == 0:
            site_content = fetch(scrape_next_page_link(site_content))
            list_news.extend(scrape_updates(site_content))
        if idx < len(list_news):
            news_content = fetch(list_news[idx])
            if news_content:
                news.append(scrape_news(news_content))

    create_news(news)

    return news
