import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
import time

import folder_by_categories
import all_categories
import urls_by_category_test
import extraire_données
import all_pictures


start=time.time()
#Adresse URL

url ='http://books.toscrape.com/'


folder_by_categories.create_folder_category(url)

all_categories.all_cat_urls(url)


with open('all_cat_urls.txt','r') as file:
    list_urls = [row.strip() for row in file]
    for url in list_urls:
        urls_by_category_test.url_by_category(url)



#Création d'un DataFrame vide

books_data={}

df=pd.DataFrame(books_data)
df=df.reindex(('URL','UPC','Titre','Price (incl. tax)','Price (excl. tax)','Availability','Description','Categorie','Note /5'),axis=1)  #permet de réorganiser la liste des colonnes (axis =0 : lignes , axis=1 : colonnes)
#Ici on réorganise les colonnes car l'odre des items dans le dictionnaire créer dans "extraire données" n'est pas le bon 

# Adresse URL de tous les livres
with open('all_cat_urls.txt','r') as file:
        list_urls = [row.strip() for row in file]

        for url in list_urls:
            df.drop(df.index, inplace=True)
            response = requests.get(url)
            if response.ok:
                soup = BeautifulSoup(response.text, 'lxml')
                name_cat=url.replace('http://books.toscrape.com/catalogue/category/books/','').split('_')[0]
            with open('%s_urls.txt' %name_cat,'r') as file:
                list_urls = [row.strip() for row in file]
                 #Extraire données
                for url in list_urls :
                    books_data=extraire_données.extraire_donnees(url)
                    books_data.update(books_data)
                    df=pd.concat([df, pd.DataFrame([books_data])],ignore_index=True) #On ajoute dans le DF vide toutes les lignes correspondant à chaque URL sans ré-écrire l'index à chaque fois
                    os.chdir('Catégories/%s' %name_cat) #On se place dans le dossier correspondant à la catégorie
                    df.to_csv ('data_books.csv', index=False) #On créer le fichier .csv correspondant au DF
                    os.chdir(os.pardir) #On sort du dossier de la catégorie
                    os.chdir(os.pardir) #On sort du dossier catégorie
print(time.time()-start)
 
 
with open('all_cat_urls.txt','r') as file:
        list_urls = [row.strip() for row in file]
        for url in list_urls:
            all_pictures.pictures_by_category(url)
print(time.time()-start)      
for name in name_cat:
    os.remove('%s_urls.txt' %name_cat) #Permet de supprimer les fichiers .txt de chaque catégorie

print(time.time()-start)