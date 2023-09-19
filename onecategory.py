#Packages importés

import requests
from bs4 import BeautifulSoup
import pandas as pd



import onebook_lien_fixe #Permet d'importer le script book sans avoir à recopier le code. Avantage : si modifications sur le script onebook, elles seront prises en compte
from onebook_lien_fixe import extraire_donnees #Permet d'importer la fonction extraire_donnees de onebook


#Objectif : récuperer tous les livres d'une catégorie 

links=[]

for i in range(10) :
    url_cat= 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-' +str(i) +'.html'
    response_cat = requests.get(url_cat)
    if response_cat.ok :
        soup = BeautifulSoup(response_cat.text, 'lxml')
        h3s = soup.findAll('h3')
        for h3 in h3s :
            a=h3.find('a')   #on cherche tous les liens compris dans les "h3"
            link= a['href'].replace("../../../","")   #permet de supprimer les "../.." en début de chaque lien contenu dans h3
            links.append('http://books.toscrape.com/catalogue/' + link)   #rajoute à la liste links, le début fixe des URL + la partie que l'on vient de récupérer
            


with open('urls.txt', 'w') as file:
    for link in links:
        file.write(link +'\n')   #le +'\n` permet de passer à la ligne entre chaque nouveau lien





