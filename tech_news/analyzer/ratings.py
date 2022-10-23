from tech_news.database import find_news


# Requisito 10
def top_5_news():
    result = []

    busca = sorted(
        sorted(find_news(), key=(lambda el: el["title"])),
        reverse=True,
        key=(lambda el: el["comments_count"])
    )[:5]

    if busca:
        for noticia in busca:
            titulo = noticia.get("title")
            url = noticia.get("url")
            result.append((titulo, url))
    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
