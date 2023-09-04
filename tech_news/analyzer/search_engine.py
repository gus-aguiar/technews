from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    consulta = {"title": {"$regex": title, "$options": "i"}}
    retorno_do_banco = search_news(consulta)
    resultado = []
    for documento in retorno_do_banco:
        resultado.append((documento["title"], documento["url"]))
    return resultado


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    consulta = {"category": {"$regex": category, "$options": "i"}}
    retorno_do_banco = search_news(consulta)
    resultado = []
    for documento in retorno_do_banco:
        resultado.append((documento["title"], documento["url"]))
    return resultado
