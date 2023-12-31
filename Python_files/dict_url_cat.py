
# Modules importés
import Python_files.urls_by_category as urls_by_category



def urls_one_category(url):
    '''La fonction permet de créer un dictionnaire listant tous les URLs des livres pour une catégorie'''
    dict_url = {}
    name_cat = url.replace('http://books.toscrape.com/catalogue/category/books/', '').split('_')[0]
    urls = []
    urls = urls_by_category.url_by_category(url)
    dict_url[name_cat] = urls  

    return dict_url  
