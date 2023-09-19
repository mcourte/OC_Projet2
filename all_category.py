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
        ul = soup.find('ul', class_='nav nav-list') #permet de trouver les ul de la class indiquée
        cat_ul=ul.find('ul') #Permet de trouver les ul compris dans la liste totale des ul = suppression du premier ul contenu dans a href
        list_cat=cat_ul.findAll('li') #permet de lister tous les li compris dans la liste des ul précédemments sélectionnés
        for li in list_cat:
            a=li.find('a')['href']  #permet de récupérer le href de chacun des a
            a_list.append(url + a)  #permet de concaténer l'url de base + les href qu'on a récupéré


#Création d'un fichier texte avec l'ensemble des URLS des catégories
with open('all_urls.txt', 'w') as file:
    for a in a_list:
        file.write(a +'\n')   #le +'\n` permet de passer à la ligne entre chaque nouveau lien      
       

