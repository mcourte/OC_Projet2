import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
import time


import all_categories
import urls_by_category
import extraire_donnees
import all_pictures
import folder_by_categories

start=time.time()
#Adresse URL

url ='http://books.toscrape.com/'

#Création de tous les dossiers

folder_by_categories.create_folder_category(url)

#Création d'un DataFrame vide

books_data={}

df=pd.DataFrame(books_data)
df=df.reindex(('URL','UPC','Titre','Price (incl. tax)','Price (excl. tax)','Availability','Description','Categorie','Note /5'),axis=1)  #permet de réorganiser la liste des colonnes (axis =0 : lignes , axis=1 : colonnes)
#Ici on réorganise les colonnes car l'odre des items dans le dictionnaire créer dans "extraire données" n'est pas le bon 

# Adresse URL de tous les livres

urls_cat=all_categories.all_cat_urls(url)

#Création d'un dictionnaire avec en key les listes de catégories et en value les urls correspondantes

#Faire fonction avec urls_by_cat en return
for url in urls_cat:
    name_cat=url.replace('http://books.toscrape.com/catalogue/category/books/','').split('_')[0]
    list='list_' + name_cat
    urls=[]
    urls=urls_by_category.url_by_category(url)
    urls_by_cat={list:urls}
   

#Faire fonction Extraire données
    
    for value in urls_by_cat.values():
        list_url=[]
        list_url.append(value)
        for url in list_url:
            df.drop(df.index, inplace=True)
            for i in url :
                response = requests.get(i)
                if response.ok:
                    books_data=extraire_donnees.extraire_donnees(i)
                    df=pd.concat([df, pd.DataFrame([books_data])],ignore_index=True) #On ajoute dans le DF vide toutes les lignes correspondant à chaque URL sans ré-écrire l'index à chaque fois
                    os.chdir('%s' %name_cat) #On se place dans le dossier correspondant à la catégorie
                    df.to_csv ('data_books.csv', encoding='utf-8', index=False) #On créer le fichier .csv correspondant au DF
                    os.chdir(os.pardir) #On sort du dossier de la catégorie
                else : print('Erreur.....')
#Faire fonction Enregistrer les photos associées à chaque livre

    for value in urls_by_cat.values():
        list_url=[]
        list_url.append(value)
        for url in list_url:
            os.mkdir('%s/Images' %name_cat)           # création du dossier Images de catégories
            os.chdir('%s/Images' %name_cat)                  #on se place dans le dossier Images de la catégorie
            for i in url:   
                all_pictures.pictures_by_category(i)
            os.chdir(os.pardir) # on sort du dossier Images
            os.chdir(os.pardir)

                    

end_time=(time.time()-start)

print(end_time)




