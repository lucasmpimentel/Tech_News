from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    lista_noticias = []

    busca = search_news({"title": {"$regex": title, "$options": "i"}})

    for noticia in busca:
        lista_noticias.append((noticia["title"], noticia["url"]))
    return lista_noticias


# Requisito 7
def search_by_date(date):
    result = []

    try:
        data = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        lista_noticias = search_news({"timestamp": data})

        for noticia in lista_noticias:
            result.append((noticia["title"], noticia["url"]))

        return result

    except (ValueError):
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    lista_noticias = []

    busca = search_news({"tags": {"$regex": tag, "$options": "i"}})

    for noticia in busca:
        lista_noticias.append((noticia["title"], noticia["url"]))

    return lista_noticias


# Requisito 9
def search_by_category(category):
    lista_noticias = []

    busca = search_news({"category": {"$regex": category, "$options": "i"}})

    for noticia in busca:
        lista_noticias.append((noticia["title"], noticia["url"]))

    return lista_noticias
