import time
import requests
import parsel


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
    getContent = parsel.Selector(text=html_content)
    return getContent.css(".entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    getContent = parsel.Selector(text=html_content)
    return getContent.css(".next::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    getContent = parsel.Selector(html_content)
    return {
        "url": getContent.css("link[rel=canonical]::attr(href)").get(),
        "title": getContent.css("h1.entry-title::text").get().strip(),
        "timestamp": getContent.css("li.meta-date::text").get(),
        "writer": getContent.css(".author ::text").get(),
        "comments_count": len(getContent.css("ol.comment-list").getall()) or 0,
        "summary": "".join(
            getContent.css(".entry-content > p:nth-of-type(1) ::text").getall()
        ).strip(),
        "tags": getContent.css("a[rel=tag]::text").getall(),
        "category": getContent.css("span.label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
