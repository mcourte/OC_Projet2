import requests
from bs4 import BeautifulSoup
import urllib
import os

import all_category

#Objectif : récuperer les images des livres d'une catégorie

#Définition des listes et dictionnaires nécessaires pour le fonctionnement du programme

book_image=[]
list_url=[]
name_img=[]
data_book={}

#

if not os.path.exists('Images') :
    os.mkdir('Images')
with open('urls.txt', 'r') as file:
    for row in file:
        row=row.replace('\n','')
        list_url.append(row)
    for url in list_url :        
        response = requests.get(url)
        if response.ok :
            soup = BeautifulSoup(response.text, 'lxml')
            div = soup.find('div', class_='item active') #permet de trouver les ul de la class indiquée
            img=div.find('img').get('src').replace('../../','') #Permet de trouver les ul compris dans la liste totale des ul = suppression du premier ul contenu dans a href
            book_image='http://books.toscrape.com/'+img
            name_img=url.replace('http://books.toscrape.com/catalogue/','').replace('/index.html','')
            data_book={ name_img : book_image}        
            for key in data_book.keys() :
                pict=urllib.request.urlretrieve(book_image,'Images/%s.jpeg' %name_img)  #Télécharger l'image couverture du livre