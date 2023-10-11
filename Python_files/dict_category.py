#Modules importés

import Python_files.all_category as all_category


def dict_cat(url) :
    '''La fonction permet de créer un dictionnaire listant tous les URLs des livres pour toues les catégories'''

    dict_category={}
    urls_cat=all_category.all_cat_urls(url)
    for url in urls_cat:
        name_cat=url.replace('http://books.toscrape.com/catalogue/category/books/','').split('_')[0]
        dict_category[name_cat]=url
    return dict_category




