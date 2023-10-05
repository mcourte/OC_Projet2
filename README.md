# Programme pour extraire les données et les images des livres de books.toscrape.com

## Etape 1 : Télécharger le code

Cliquer sur le bouton vert "<> Code" puis sur Download ZIP.  
Extraire l'ensemble des éléments dans le dossier dans lequel vous voulez stockez les datas qui seront téléchargées.  

## Etape 2 ; Installer Python et ouvrir le terminal de commande

Télécharger [Python](https://www.python.org/downloads/) et [installer-le](https://fr.wikihow.com/installer-Python)  

Ouvrir le terminal de commande :  
Pour les utilisateurs de Windows : [démarche à suivre ](https://support.kaspersky.com/fr/common/windows/14637#block0)  
Pour les utilisateurs de Mac OS : [démarche à suivre ](https://support.apple.com/fr-fr/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac)  
Pour les utilisateurs de Linux : ouvrez directement le terminal de commande   

## Etape 3 : Création de l'environnement virtuel

Se placer dans le dossier où l'on a extrait l'ensemble des documents grâce à la commande ``cd``  
Exemple :
```
cd home/magali/OpenClassrooms/Formation/Projet_2
```


Dans le terminal de commande, executer la commande suivante :
```
python3 -m venv env
```


Activez l'environnement virutel
```
source env/bin/activate
```
> Pour les utilisateurs de Windows, la commande est la suivante : 
> ``` env\Scripts\activate.bat ```

## Etape 4 : Télécharger les packages nécessaires au bon fonctionnement du programme

Dans le terminal, taper la commande suivante :
```
pip -r requierements.txt
```

## Etape 5 : Lancer le programme

Taper la commande suivante :
```
python3 main.py
```
Vous aurez alors un menu qui va s'afficher avec 3 choix :  
*Vous pouvez importer les datas de l'ensemble des livres de toutes les catégories  
*Vous pouvez importer les dates de l'ensemble des livres d'une seule catégorie  
*Vous pouvez importer les datas d'un seul livre :  
Pour cela, aller directement sur [books.toscrape](http://books.toscrape.com), choisissez un livre, et copier son URL dans le terminal  
Le programme va créer un dossier pour chaque catégorie de livre, qui sera composé d'un fichier data.csv et d'un dossier Images comprenant l'ensemble des couvertures des livres


### Informations diverses
Il est seulement nécessaire de lancer main.py pour que le code s'exécute entièrement.
* folder_by_categories.py permet de créer l'ensemble des dossiers de catégories
* all_categories.py permet de récupérer l'URL de chacune des catégories
* urls_by_categories.py permet de récupérer les URL de l'ensemble des livres d'une catégorie
* extraire_donnees.py permet d'extraire les données d'un livre
* all_pictures.py permet de télécharger les images et de créer un dossier Images pour chacune des catégories'
* les modules extract_data.py, extract_pict.py , dict_url_cat.py, dict_category.py regroupent des fonctions utilisant les fonctions décrites dans les 5 modules cités précedemment permettant de fluidifier la lecture du programme
* choix_categories.py permet de mettre en place le système de choix de catégories de l'option 2 du main.py'
