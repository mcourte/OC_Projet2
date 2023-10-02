import requests
from bs4 import BeautifulSoup
import pandas as pd


# Fonction pour extraire les données d'une page
def extraire_donnees(url):
    td_list = []
    th_list = []
    books_data={}
    
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "lxml")

    # Récupérer les informations du Titre
    title = soup.find('h1').get_text()

    # Récupérer les informations UPC, Price(excl.tax), Price(incl. tax), Availability
    tds=soup.findAll('th')   #findAll permet de récupérer TOUS les élements 'th' du code. Choisit ici car les tr de la table n'ont pas de classes
    th_list = [th.get_text() for th in tds if th.get_text()] #Permet de récupérer le texte de chacun des "th" si celui-ci existe

    tds=soup.findAll('td')   
    td_list = [td.get_text() for td in tds if td.get_text()] #

    # Créer un dictionnaire avec les informations
    product_informations = {th_list[i]: td_list[i] for i in range(len(th_list))}
    del product_informations['Product Type'], product_informations['Tax'],  product_informations['Number of reviews']  #Permet de supprimer les items qui ne nous interessent pas 
    
    # Récupérer la Catégorie du livre
    category = soup.find(class_='breadcrumb').findAll('li')[-2].get_text() #Permet de trouver les li de la classe indiquée : 4 élements - on ne garde que le 2ème

    # Récupérer Review Rating
    rating_dict = {
        'One': '1',
        'Two': '2',
        'Three': '3',
        'Four': '4',
        'Five': '5',
    }

    review_rating = soup.find('p', class_='star-rating')['class'][1]   #Permet de récupérer le nom de la classe qui contient l'information cherchée. On ne garde que le 2ème élement qui correspont au nombre d'étoile
    review_rating = ''.join(rating_dict[ele] for ele in review_rating.split())  #Fonction permettant de transformer les chiffres écrits en lettres en numéraire

    # Récupérer la Description du livre
    if soup.find(class_="product_page").find('p', class_=None) is not None :
        description=soup.find(class_="product_page").find('p', class_=None).get_text()
    else :
        description=''


    #Récupérer l'URL de l'image du livre

    div = soup.find('div', class_='item active') #permet de trouver les ul de la class indiquée
    img=div.find('img').get('src').replace('../../','') #Permet de trouver les ul compris dans la liste totale des ul = suppression du premier ul contenu dans a href
    book_image='http://books.toscrape.com/'+img


    # Créer un dictionnaire pour stocker toutes les informations
    book_data = {
        "URL" : url,
        "Titre": title,
        "Description": description,
        "Categorie": category,
        "Note /5": review_rating,
        "Image URL" : book_image,
    }

    book_data.update(product_informations)
    books_data.update(book_data)    
    return books_data 

