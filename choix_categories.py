import dict_category




def choix(url_base):
        category=dict_category.dict_cat(url_base)
        cat=list(category.keys())
        for i , categorie in enumerate(cat, start=1) : 
            print(f"{i}.{categorie}")
        cat_choisie = None  # Initialisez la variable à None pour entrer dans la boucle
        while True:
           try:
            choice = input("Entrez le numéro de la catégorie que vous souhaitez extraire : ")
            choix=int(choice) -1
            if 1<= choix <= len(cat):
                cat_choisie=cat[choix]
                print(f"Vous avez choisi d'extraire la catégorie : {cat_choisie}")
                url=list(category.values())
                url_cat=url[choix]
            else:
                  print("Numéro de catégorie invalide.")
            return url_cat

           except ValueError:
              print("Veuillez entrer un numéro valide.")


