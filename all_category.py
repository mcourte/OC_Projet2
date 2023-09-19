#Packages importés

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv

import onebook_lien_fixe #Permet d'importer le script book sans avoir à recopier le code. Avantage : si modifications sur le script onebook, elles seront prises en compte
from onebook_lien_fixe import extraire_donnees


#Objectif : récuperer les liens de toutes les catégories

#Définition des listes et dictionnaires nécessaires pour le fonctionnement du programme

links={}
a_list=[]
a=[]
#Adresse URL

url ='http://books.toscrape.com/'

#Début programme

response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    if response.ok :
        soup = BeautifulSoup(response.text, 'lxml')
        uls = soup.find_all('ul', class_='nav nav-list')
        for ul in uls:
            a=ul.find('a')['href']
        print(a)
       
#Création fichier .csv, avec comme nom "all_cat_urls.csv", en utilisant un dataframe
df = pd.DataFrame.from_dict(links) 
df.to_csv (r'all_cat_urls.csv', index=False, header=False)
