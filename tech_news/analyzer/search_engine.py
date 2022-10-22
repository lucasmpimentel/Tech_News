from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    lista_noticias = []

    busca = search_news({"title": {"$regex": title, "$options": "i"}})

    for noticias in busca:
        lista_noticias.append((noticias["title"], noticias["url"]))
    return lista_noticias


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
