#Packages importés


# Importation des modules
import urls_by_category



def urls_one_category(url):
    dict_url = {}
    name_cat = url.replace('http://books.toscrape.com/catalogue/category/books/', '').split('_')[0]
    urls = []
    urls = urls_by_category.url_by_category(url)
    dict_url[name_cat] = urls  # Si la catégorie n'existe pas encore dans le dictionnaire, créez une nouvelle liste

    return dict_url  # Renvoi le dictionnaire une fois que la boucle est terminée
