#Modules importés

import all_categories


def dict_cat(url) :
    dict_category={}
    urls_cat=all_categories.all_cat_urls(url)
    for url in urls_cat:
        name_cat=url.replace('http://books.toscrape.com/catalogue/category/books/','').split('_')[0]
        dict_category[name_cat]=url
    return dict_category




