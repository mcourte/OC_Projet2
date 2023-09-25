#Packages importés

import requests
from bs4 import BeautifulSoup
import pandas as pd




#Objectif : récuperer tous les livres d'une catégorie 

links=[]
url_cats=[]
urls_onecat=[]
 
#URL

url= 'https://books.toscrape.com/catalogue/category/books/default_15/'

url_cat= url +'index.html'
response = requests.get(url_cat)
if response.ok :
        soup = BeautifulSoup(response.text, 'lxml')
        h3s = soup.findAll('h3')
        for h3 in h3s :
            a=h3.find('a')   #on cherche tous les liens compris dans les "h3"
            link= a['href'].replace("../../../","")   #permet de supprimer les "../.." en début de chaque lien contenu dans h3
            links.append('http://books.toscrape.com/catalogue/' + link)   #rajoute à la liste links, le début fixe des URL + la partie que l'on vient 
for i in range(2,10) :
    url_onecat= url +'page-'+ str(i) +'.html'
    response_cat = requests.get(url_onecat)
    if response_cat.ok :
        urls_onecat.append(url_onecat)
        soup = BeautifulSoup(response_cat.text, 'lxml')
        h3s = soup.findAll('h3')
        for h3 in h3s :
            a=h3.find('a')   #on cherche tous les liens compris dans les "h3"
            link= a['href'].replace("../../../","")   #permet de supprimer les "../.." en début de chaque lien contenu dans h3
            links.append('http://books.toscrape.com/catalogue/' + link)   #rajoute à la liste links, le début fixe des URL + la partie que l'on vient de récupérer
with open('urls.txt', 'w') as file:
    for link in links:
        file.write(link +'\n')   #le +'\n` permet de passer à la ligne entre chaque nouveau lien


   





