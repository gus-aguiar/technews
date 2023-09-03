import requests
import time
from parsel import Selector


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
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# initial commit
