#Packages importés
import os
from bs4 import BeautifulSoup
import requests


#Module importés
import dict_url_cat
import all_pictures
import all_categories








def extract_pict_all_cat(url):
    urls_cat=all_categories.all_cat_urls(url)
    for url in urls_cat :
        name_cat=url.replace('http://books.toscrape.com/catalogue/category/books/','').split('_')[0]
        dict_urls=dict_url_cat.urls_one_category(url)
        for value in dict_urls.values() :
            list_urls=value
        os.chdir('%s' %name_cat) #On se place dans le dossier correspondant à la catégorie
        os.mkdir('Images')
        os.chdir('Images')
        for url in list_urls :
            all_pictures.pictures_by_category(url)
        os.chdir(os.pardir) # on sort du dossier Images
        os.chdir(os.pardir) # on sort du dossier Images
  

def extract_pict_one_cat(url):
    name_cat=url.replace('http://books.toscrape.com/catalogue/category/books/','').split('_')[0]
    os.mkdir('Images')           # création du dossier Images de catégories
    os.chdir('Images')                  #on se place dans le dossier Images de la catégorie
    dict_urls=dict_url_cat.urls_one_category(url)
    for i in dict_urls.values():
        for url in i:
            all_pictures.pictures_by_category(url)
    os.chdir(os.pardir) # on sort du dossier Images
    os.chdir(os.pardir)


def extract_pict_one_book(url):
    response = requests.get(url)
    response.raise_for_status()
    if response.ok:
        soup = BeautifulSoup(response.content, "lxml")
    name_cat= soup.find(class_='breadcrumb').find_all('li')[-2].get_text().replace('\n','').lower() 
    os.mkdir('Images')         # création du dossier Images de catégories
    os.chdir('Images')                 #on se place dans le dossier Images de la catégorie
    all_pictures.pictures_by_category(url)
    os.chdir(os.pardir) # on sort du dossier Images
    os.chdir(os.pardir) 


