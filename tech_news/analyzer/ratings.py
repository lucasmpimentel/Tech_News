from tech_news.database import find_news
from collections import Counter

TOP = 5


# Requisito 10
def top_5_news():
    result = []

    busca = sorted(
        sorted(find_news(), key=(lambda el: el["title"])),
        reverse=True,
        key=(lambda el: el["comments_count"])
    )[:TOP]

    if busca:
        for noticia in busca:
            titulo = noticia.get("title")
            url = noticia.get("url")
            result.append((titulo, url))

    return result


# Requisito 11
def top_5_categories():
    busca = sorted(find_news(), key=(lambda el: el["category"]))

    categorias = Counter([item["category"] for item in busca])

    result = [item[0] for item in categorias.most_common()[:TOP]]

    return result
