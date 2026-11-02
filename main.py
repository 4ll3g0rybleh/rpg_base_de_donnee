

#initialiser la bdd

#boucle du jeu:
    #le menu du jeu s'affiche
    #on demande au user de faire un choix valide entre démarrer, voir le classement, ou quitter
    #le choix est éxecuté 


#afficher le menu:
#header
#menu des choix 

#recupérer choix valide:
#input utilisateur
#doit être un chiffre 
#doit être compris dans l'intervalle donnée

#éxécuter le choix valide:
#si le choix est 1 on lance le menu de la partie 
#si le choix est 2 on lance l'affichage du classement 
#si le choix est 3 on quitte le jeu 


#choix 1 menu de la partie:
    #demander le username 
    #on demande au user de créer son équipe
    #on lance le jeu 


#recuperer les heros:
#on récupere ds une liste les héros depuis la bdd

#composition de l'équipe: 
#création d'une variable équipe vide 
#boucle de la creation de l'équipe jusqu'à ce qu'elle soit complète:
    #on récupère de la bdd la collection héros dans une liste héross disponibles
    #on affiche la liste des héros disponibles avec leurs informations 
    #on demande au joueur de faire un choix valide pour ajouter un héro à son équipe
        #le héro choisi est ajouté à l'équipe de l'utilisateur
        #le héro choisi est supprimé de la liste à afficher 
#la liste des héros de l'équipe est retournée 

#choix 2 affichage du classement:
#on récupère les joueurs présents dans la collection joueurs dans la bdd dans une liste classement 
#on les trie du plus petit au plus haut score 
#on les affiche dans l'ordre 

#choix 3 quitter:
#on quitte le jeu

#le déroulement du jeu :
#on crée une équipe active qui contient l'équipe choisie  
#tant que les pvs de l'équipe sont pos
    #on lance une vague
#défaite
# affichage du score joueur et du classement
#vérifier si le score du joueur est plus élevé que celui de quelqu'un dans le classement
    #envoyer le joueur avec son score à la bdd 
#retour au menu principal

#vérifier les pv des persos: 
#les pvs sont supéreurs à 0

#vérifier les pvs de l'équipe:
#vérifier les pvs de chaque membre de l'équipe 
#si un héro a des pvs la fonction est vraie

#recupérer les monstres:
#on récupère les monstres dans une liste

#récupérer un choix aléatoire:
# on récupère un perso alétoire depuis une liste donnée
#on le retourne


#vague:
#on initialise un score à 0
#on récupère un monstre aléatoire
#tant que les pvs du monstre sont pos et les pvs de l'equipe sont pos: 
        #chaque perso de l'équipe attaque le monstre 
        #ses pvs réduisent à chaque fois
    #si les pvs du monstre sont pos
        #on choisit un héro target de l'équipe aléatoire
        #le monstre attaque 
        #le héro subit des dégats
    #vérifier si les pvs du héro target sont negatifs:
        #enlever le héro de l'équipe active
#le score prend +1
#victoire du joueur



