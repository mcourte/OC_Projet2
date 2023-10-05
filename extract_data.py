import requests
import os
import pandas as pd
from bs4 import BeautifulSoup

import all_categories
import extraire_donnees
import dict_url_cat 




def extract_donnees_all_cat(url):
    books_data={}
    dict_urls={}
    urls_cat=all_categories.all_cat_urls(url)
    df=pd.DataFrame(books_data)
    df=df.reindex(('URL','UPC','Titre','Price (incl. tax)','Price (excl. tax)','Availability','Description','Categorie','Note /5'),axis=1)  #permet de réorganiser la liste des colonnes (axis =0 : lignes , axis=1 : colonnes)
    for url in urls_cat :
        df.drop(df.index, inplace=True)
        name_cat=url.replace('http://books.toscrape.com/catalogue/category/books/','').split('_')[0]
        dict_urls=dict_url_cat.urls_one_category(url)
        for value in dict_urls.values() :
            list_urls=value
        os.chdir('%s' %name_cat) #On se place dans le dossier correspondant à la catégorie
        for url in list_urls :
                response = requests.get(url)
                response.raise_for_status()
                if response.ok:
                    books_data=extraire_donnees.extraire_donnees(url)
                    df=pd.concat([df, pd.DataFrame([books_data])],ignore_index=True) #On ajoute dans le DF vide toutes les lignes correspondant à chaque URL sans ré-écrire l'index à chaque foi
                    df.to_csv ('data_books.csv', encoding='utf-8-sig', index=False) #On créer le fichier .csv correspondant au DF   
                 #else : print('Erreur.....')
        os.chdir(os.pardir)
       



def extract_donnees_one_cat(url):
    books_data={}
    dict_urls={}
    name_cat=url.replace('http://books.toscrape.com/catalogue/category/books/','').split('_')[0]
    os.chdir('%s' %name_cat) #On se place dans le dossier correspondant à la catégorie
    df=pd.DataFrame(books_data)
    df=df.reindex(('URL','UPC','Titre','Price (incl. tax)','Price (excl. tax)','Availability','Description','Categorie','Note /5'),axis=1)  #permet de réorganiser la liste des colonnes (axis =0 : lignes , axis=1 : colonnes)
    dict_urls=dict_url_cat.urls_one_category(url)
    for i in dict_urls.values():
        for url in i:
            response = requests.get(url)
            response.raise_for_status()
            if response.ok:
                books_data=extraire_donnees.extraire_donnees(url)
                df=pd.concat([df, pd.DataFrame([books_data])],ignore_index=True) #On ajoute dans le DF vide toutes les lignes correspondant à chaque URL sans ré-écrire l'index à chaque fois
            else : print('Erreur.....')
    df.to_csv ('data_books.csv', encoding='utf-8-sig', index=False) #On créer le fichier .csv correspondant au DF


def extract_donnees_one_book(url):
    books_data={}
    df=pd.DataFrame(books_data)
    df=df.reindex(('URL','UPC','Titre','Price (incl. tax)','Price (excl. tax)','Availability','Description','Categorie','Note /5'),axis=1)  #permet de réorganiser la liste des colonnes (axis =0 : lignes , axis=1 : colonnes)
    response = requests.get(url)
    response.raise_for_status()
    if response.ok:
        soup = BeautifulSoup(response.content, "lxml")
        name_cat= soup.find(class_='breadcrumb').find_all('li')[-2].get_text().replace('\n','').lower() 
        os.chdir('%s' %name_cat) #On se place dans le dossier correspondant à la catégorie
        books_data=extraire_donnees.extraire_donnees(url)
        df=pd.concat([df, pd.DataFrame([books_data])],ignore_index=True) #On ajoute dans le DF vide toutes les lignes correspondant à chaque URL sans ré-écrire l'index à chaque fois
        df.to_csv ('data_books.csv', encoding='utf-8-sig', index=False) #On créer le fichier .csv correspondant au DF
    else : print('Erreur.....')