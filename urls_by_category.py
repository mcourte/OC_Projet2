#Packages importés

import requests
from bs4 import BeautifulSoup
import pandas as pd
import all_categories






#Définition d'une fonction permettant de récupérer les URL de tous les livres d'une catégories et de l'enregistrer dans un fichier 

def url_by_category(url):
    name_cat=[]
    links=[]

 
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        name_cat=url.replace('http://books.toscrape.com/catalogue/category/books/','').split('_')[0]
        for name in name_cat:
            h3s = soup.findAll('h3')
            for h3 in h3s :
                a=h3.find('a')   #on cherche tous les liens compris dans les "h3"
                link= a['href'].replace("../../../","")   #permet de supprimer les "../.." en début de chaque lien contenu dans h3
                link_c='http://books.toscrape.com/catalogue/' + link
                while link_c not in links:
                    links.append(link_c)
            next_page = soup.find('li', class_='next')
            if next_page:
                next_url = next_page.find('a')['href']
                url = url.rsplit('/', 1)[0] + '/' + next_url  # Construire le nouvel URL de la page suivante
                response = requests.get(url)
                if response.ok:
                    soup = BeautifulSoup(response.text, "lxml")
                    h3s = soup.findAll('h3')
                    for h3 in h3s :
                        a=h3.find('a')   
                        link= a['href'].replace("../../../","")
                        link_c='http://books.toscrape.com/catalogue/' + link
                        while link_c not in links:
                            links.append(link_c)
        return links



