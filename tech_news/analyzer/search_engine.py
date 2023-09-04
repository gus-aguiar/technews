from tech_news.database import search_news
from datetime import datetime


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
    try:
        data_objeto = datetime.strptime(date, "%Y-%m-%d")
        data_formatada = data_objeto.strftime("%d/%m/%Y")
        consulta = {"timestamp": data_formatada}
        retorno_do_banco = search_news(consulta)
        resultado = []
        for documento in retorno_do_banco:
            resultado.append((documento["title"], documento["url"]))
        if not resultado:
            return []
        return resultado
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    consulta = {"category": {"$regex": category, "$options": "i"}}
    retorno_do_banco = search_news(consulta)
    resultado = []
    for documento in retorno_do_banco:
        resultado.append((documento["title"], documento["url"]))
    return resultado
