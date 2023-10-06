#Packages importés

import requests
from bs4 import BeautifulSoup
import os



#Définition d'une fonction permettant de créer un dossier Catégories dans lequel on crée des sous dossiers par catégories



def create_folder_category(url) :

    try:
        response = requests.get(url)
        response.raise_for_status()
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
                        if not os.path.exists('%s' %name_cat) :  
                            os.makedirs('%s' %name_cat)
    except requests.exceptions.RequestException as error :
        print("Une erreur s'est produite :{error}")


def create_folder_one_category(url) :

    url=url.replace('\n','')
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.ok:
            soup = BeautifulSoup(response.text, 'lxml')
            if response.ok :
                soup = BeautifulSoup(response.text, 'lxml')
                div = soup.find('div', class_='page-header action') #permet de trouver les ul de la class indiquée
                name_cat=div.find('h1').get_text().replace(" ","-").lower() #Permet de trouver les ul compris dans la liste totale des ul = suppression du premier ul contenu dans a href
                if not os.path.exists('%s' %name_cat) :  
                    os.makedirs('%s' %name_cat)
    except requests.exceptions.RequestException as error :
        print("Une erreur s'est produite :{error}")

def create_folder_one_book(url) :

    url=url.replace('\n','')
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.ok:
            soup = BeautifulSoup(response.text, 'lxml')
            if response.ok :
                soup = BeautifulSoup(response.text, 'lxml')
                name_cat= soup.find(class_='breadcrumb').find_all('li')[-2].get_text().replace('\n','').lower() #Permet de trouver les li de la classe indiquée : 4 élements - on ne garde que le 2ème
                if not os.path.exists('%s' %name_cat) :  
                    os.makedirs('%s' %name_cat)
    except requests.exceptions.RequestException as error :
        print("Une erreur s'est produite :{error}")

