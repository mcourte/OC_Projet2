# Package importés
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

#Objectif : récuperer tous les informations d'un livre


#Listes - création de liste vide pour récuperer les infos stockés dans des tables ou liste

td_list=[]
th_list=[]
li_list=[]

def extraire_donnees(elements):
    resultat=[]
    for element in elements:
        resultat.append(element.get_text())

    return resultat

#Adresse URL

url ='http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

#Début programme

response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, "lxml")

# Récupérer informations du Titre
title=soup.find('h1').get_text()   #get_text() permet de récupérer le texte sans les balises

# Récupérer informations UPC, Price(excl.tax), Price(incl. tax), Availability
tds=soup.find_all('th')   #findAll permet de récupérer TOUS les élements 'th' du code. Choisit ici car les tr de la table n'ont pas de classes
th_list= extraire_donnees(tds)
del th_list[1] #supprime la catégorie "Product type" 
del th_list[3] #supprime la catégorie "Tax" 
del th_list[4] #supprime la catégorie "Number of review"

tds=soup.find_all('td')   #findAll permet de récupérer TOUS les élements 'td' du code. Choisit ici car les tr de la table n'ont pas de classes
td_list= extraire_donnees(tds)
del td_list[1] #supprime la catégorie "Product type" 
del td_list[3] #supprime la catégorie "Tax" 
del td_list[4] #supprime la catégorie "Number of review"

#Création d'un dictionnaire avec les th en clé et les td en valeur pour récuper les infos situées dans le tableau
product_informations = {th_list[i]: td_list[i] for i in range(len(th_list))}
    
# Récupérer informations sur la "Catégorie du livre"
category=soup.find(class_='breadcrumb').findAll('li') #Permet de choisir tous les li qui appartient à la class breadcrumb de div
li_list= extraire_donnees(category)
category=li_list[-2] #Permet de garder uniquement la partie Category)

#Récupérer informations sur "Review Rating"
rating_dict={       #mise en place d'un dictionnaire pour le review rating pour passer les chiffres en numéraire
    'One' :'1',
    'Two' :'2',
    'Three' :'3',
    'Four' :'4',
    'Five' :'5',
    }

review_rating=soup.find('p', class_='star-rating').get('class')[1] #récupère uniquement le dernier mot de la classe qui correspont au nombre d'étoile
review_rating=''.join(rating_dict[ele] for ele in review_rating.split()) #permet de transformer les nombres écrits en numéraire


#Récupérer la description du livre
description=soup.find(class_="product_page").findAll('p')[-1].get_text() #récupère le dernier élement p de la class product_page

#Création d'un dictionnaire pour stocker l'ensemble des éléments à récupérer

book_data = {
    "Categorie" : category,
    "URL": url,
    "Titre": title,
    "Description" : description,
    "Note /5": review_rating,
    }

book_data.update(product_informations) #utilisation de la fonction update pour joindre le dictionnaire des élements contenu dans product_informations 



#Création fichier .csv, avec comme nom "booktoscrape.csv", en utilisant un dataframe
df = pd.DataFrame(book_data, index=[0])
df=df.reindex(('URL','UPC','Titre','Price (incl. tax)','Price (excl. tax)','Availability','Description','Categorie','Note /5'),axis=1)  #permet de réorganiser la liste des colonnes (axis =0 : lignes , axis=1 : colonnes)
df.to_csv (r'booktoscrape.csv', index=False, header=True)  #index = False : ici, je n'ai pas de "titre" de ligne, header=True : je veux afficher les en-têtes des colonnes





