#Packages importés

import requests
from bs4 import BeautifulSoup
import urllib

#Objectif : récuperer les images des livres d'une catégorie


def pictures_by_category(url) :
    '''La fonction permet de récupérer l'image de chaque livre & lui donner le nom du livre'''
    book_image=[]
    data_book={}

    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.ok:
            soup = BeautifulSoup(response.content, 'lxml')
            div = soup.find('div', class_='item active') #permet de trouver les div de la class indiquée
            img=div.find('img').get('src').replace('../../','') #Permet de trouver le lien html de chaque image / supprime les premiers caractères
            book_image='http://books.toscrape.com/'+img #rajoute l'url de base du site au lien qu'on vient de trouver
            name_img=url.replace('http://books.toscrape.com/catalogue/','').replace('/index.html','').split('_')[0].replace('-',' ') # permet de de ne garder que le nom du livre
            name_img=name_img[:255] #limite la longueur du nom du fichier a 255 caractère
            data_book={ name_img : book_image}  #Création d'un dictionnaire avec en keys le nom de l'image et en value son url associée     
            for key in data_book.keys() : 
                    pict=urllib.request.urlretrieve(book_image,'%s.jpeg' %name_img)  #Télécharger l'image couverture du livre avec pour nom le nom du livre
        else : print('Erreur')
    except requests.exceptions.RequestException as error :
        print(f"Une erreur s'est produite :{error}")  
               