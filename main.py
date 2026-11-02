
#boucle du jeu:
    #le menu du jeu s'affiche
    #on demande au user de faire un choix valide entre démarrer, voir le classement, ou quitter
    #le choix est éxecuté 


#afficher le menu:
#header
#menu des choix 

#choix valide:
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


#composition de l'équipe: 
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
#vérifier les pvs de chaque joueur 
    #on lance une vague
    #score +1
#défaite retour au menu principal

#vérifier les pv des persos: 
#les pvs sont supéreurs à 0

#vérifier les pvs de l'équipe:
#vérifier les pvs de chaque membre de l'équipe 
#si un héro a des pvs 

#vague:
#on récupère un monstre alétoire depuis la bdd
#vérifier les pvs du monstre: 
    #chaque perso de l'équipe attaque le monstre et ses pvs réduisent à chaque fois
    #le monstre attaque un perso aléatoire
    #il subit des dégats 
#victoire du joueur