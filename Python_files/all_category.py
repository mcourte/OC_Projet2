#Packages importés
import requests
from bs4 import BeautifulSoup


#Definition d'une fonction permettant de récupérer les URL de chaque catégorie

def all_cat_urls(url):
    a_list=[]
    a=[]
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.ok:
            soup = BeautifulSoup(response.text, 'lxml')
            if response.ok :
                soup = BeautifulSoup(response.text, 'lxml')
                ul = soup.find('ul', class_='nav nav-list') #permet de trouver les ul de la class indiquée
                cat_ul=ul.find('ul') #Permet de trouver les ul compris dans la liste totale des ul = suppression du premier ul contenu dans a href
                list_cat=cat_ul.findAll('li') #permet de lister tous les li compris dans la liste des ul précédemments sélectionnés
                for li in list_cat:
                    a=li.find('a')['href'].replace("index.html","")  #permet de récupérer le href de chacun des a
                    a_list.append(url + a)  #permet de concaténer l'url de base + les href qu'on a récupéré
    except requests.exceptions.RequestException as error :
        print(f"Une erreur s'est produite :{error}")               
        
    return a_list  
    


