import requests
from bs4 import BeautifulSoup
import urllib
import os

#Objectif : récuperer les images des livres d'une catégorie

#Définition des listes et dictionnaires nécessaires pour le fonctionnement du programme


def pictures_by_category(url) :

    book_image=[]
    data_book={}


    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
    #    name_cat=url.replace('http://books.toscrape.com/catalogue/category/books/','').split('_')[0]  #Trouve le nom de la catégorie : on enlève la première partie de l'URL + on sépare le nom restant pour supprimer le numéro associé
    #    for name in name_cat:
    #    if not os.path.exists('%s/Images' %name_cat) :   #On vérifie si le dossier est déjà créer ou non
    #        os.mkdir('%s/Images' %name_cat)           # si dossier inexistant : création des dossiers par nom de catégories
    #    os.chdir('%s/Images' %name_cat)                  #on se place dans le dossier de la catégorie

        div = soup.find('div', class_='item active') #permet de trouver les div de la class indiquée
        img=div.find('img').get('src').replace('../../','') #Permet de trouver le lien html de chaque image / supprime les premiers caractères
        book_image='http://books.toscrape.com/'+img #rajoute l'url de base du site au lien qu'on vient de trouver
        name_img=url.replace('http://books.toscrape.com/catalogue/','').replace('/index.html','').split('_')[0].replace('-',' ') # permet de de ne garder que le nom du livre
        data_book={ name_img : book_image}  #Création d'un dictionnaire avec en keys le nom de l'image et en value son url associée     
        for key in data_book.keys() :   #pour chacune des key du dictionnaire :
                pict=urllib.request.urlretrieve(book_image,'%s.jpeg' %name_img)  #Télécharger l'image couverture du livre avec pour nom le nom du livre
        #os.chdir(os.pardir) # on sort du dossier Images
        
               