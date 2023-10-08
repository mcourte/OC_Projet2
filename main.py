#Packages importés
import time

#Modules importés
import folder_by_categories
import extract_data
import extract_pict
import choix_categories


#Fonction permettant de convertir le temps d'exécution de secondes en HH:MM:SS
def convert(seconds):
    ''' La fonction permet de convertir les secondes en HH/MM/SS afin d'avoir un timing plus clair '''
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return '%d:%02d:%02d' % (hour, min, sec)


#Fonction principale du programme
def main ():
    url_base = "http://books.toscrape.com/"
    while True:
     print("\nMenu :")
     print("1. Extraire toutes les catégories avec les images")
     print("2. Extraire une catégorie spécifique avec les images")
     print("3. Extraire les données d'un livre et son image")
     print("4. Quitter")
     choice = input("Choisissez une option : ")
     if choice == "1":
        start=time.time()
        folder_by_categories.create_folder_category(url_base)
        extract_data.extract_donnees_all_cat(url_base)
        extract_pict.extract_pict_all_cat(url_base)
        print('Fin du programme')
        end_time=(time.time()-start)
        print(convert(end_time))

     elif choice == "2":
        start=time.time()
        url_cat=choix_categories.choix(url_base)
        folder_by_categories.create_folder_one_category(url_cat)
        extract_data.extract_donnees_one_cat(url_cat)
        extract_pict.extract_pict_one_cat(url_cat)
        print('Fin du programme')
        end_time=(time.time()-start)
        print(convert(end_time))

     elif choice == "3":
        start=time.time()
        url_book=input("Entrez l'url du livre choisi : ")
        folder_by_categories.create_folder_one_book(url_book)    
        extract_data.extract_donnees_one_book(url_book)
        extract_pict.extract_pict_one_book(url_book)
        print('Fin du programme')
        end_time=(time.time()-start)
        print(convert(end_time))

     elif choice == "4":
        print("Arrêt du programme ! A bientôt")
        break
     else:
      print("Choix invalide. Veuillez choisir une option valide.")


if __name__=="__main__":
   main()