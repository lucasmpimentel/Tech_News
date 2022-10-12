import time
import requests


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
            )
        if res.status_code == 200:
            return res.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
