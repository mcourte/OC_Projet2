#Packages importés

import requests
from bs4 import BeautifulSoup
import os



#Objectif : récuperer les liens de toutes les catégories

#Définition des listes et dictionnaires nécessaires pour le fonctionnement du programme

links={}
a_list=[]
a=[]
#Adresse URL

url ='http://books.toscrape.com/'

#Début programme
if not os.path.exists('Catégories') :
                    os.mkdir('Catégories')
response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    if response.ok :
        soup = BeautifulSoup(response.text, 'lxml')
        ul = soup.find('ul', class_='nav nav-list') #permet de trouver les ul de la class indiquée
        cat_ul=ul.find('ul') #Permet de trouver les ul compris dans la liste totale des ul = suppression du premier ul contenu dans a href
        list_cat=cat_ul.findAll('li') #permet de lister tous les li compris dans la liste des ul précédemments sélectionnés
        for li in list_cat:
            a=li.find('a')['href'].replace("index.html","")  #permet de récupérer le href de chacun des a
            name_cat=a.replace('catalogue/category/books/','').split('_')[0] 
            noms_categorie ={'nom' : name_cat}
            for value in noms_categorie.values():
                if not os.path.exists('Catégories/%s' %value) :
                    os.makedirs('Catégories/%s' %value)

