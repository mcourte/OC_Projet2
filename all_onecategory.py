#Packages importés

import requests
from bs4 import BeautifulSoup
import pandas as pd



import onebook_lien_fixe #Permet d'importer le script book sans avoir à recopier le code. Avantage : si modifications sur le script onebook, elles seront prises en compte
from onebook_lien_fixe import extraire_donnees #Permet d'importer la fonction extraire_donnees de onebook


#Objectif : récuperer tous les livres d'une catégorie 

links=[]
url_cats=[]
urls_onecat=[]

all_cat=open("all_urls.txt", "r")
lignes= all_cat.readlines()

for ligne in lignes:
    url_cat=  (str(ligne) +'page-').replace('\n','')
    url_cats.append(url_cat + '\n') 

    for i in range(10) :
        url_onecat= url_cat +str(i) +'.html'
        response_cat = requests.get(url_onecat)
        if response_cat.ok :
            urls_onecat.append(url_onecat)
            soup = BeautifulSoup(response_cat.text, 'lxml')
            h3s = soup.findAll('h3')
            for h3 in h3s :
                a=h3.find('a')   #on cherche tous les liens compris dans les "h3"
                link= a['href'].replace("../../../","")   #permet de supprimer les "../.." en début de chaque lien contenu dans h3
                links.append('http://books.toscrape.com/catalogue/' + link)   #rajoute à la liste links, le début fixe des URL + la partie que l'on vient de récupérer
                with open('test.txt', 'w') as file:
                    for link in links:
                        file.write(link +'\n')   #le +'\n` permet de passer à la ligne entre chaque nouveau lien


   





