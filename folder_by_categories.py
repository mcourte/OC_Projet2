#Packages importés

import requests
from bs4 import BeautifulSoup
import os



#Définition d'une fonction permettant de créer un dossier Catégories dans lequel on crée des sous dossiers par catégories



def create_folder_category(url) :

    if not os.path.exists('Categories'):
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
                a=li.find('a')['href'].replace('index.html','')  #permet de récupérer le href de chacun des a
                name_cat=a.replace('catalogue/category/books/','').split('_')[0] #permet de récupérer le nom de la catégorie
                for name in name_cat:                   #Pour chaque nom de catégorie : création d'un dossier si il n'est pas déjà existant
                    if not os.path.exists('Catégories/%s' %name_cat) :  
                        os.makedirs('Catégories/%s' %name_cat)



