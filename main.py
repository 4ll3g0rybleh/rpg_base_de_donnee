

#initialiser la bdd

#BOUCLE DU JEU:
    #le menu du jeu s'affiche
    #on demande au user de faire un choix valide
    #le choix valide est éxecuté 


#afficher le menu():
#on affiche le header du jeu print_header()
#on affiche le menu des choix 

#get_choice():
#demander un input utilisateur dans une var chocie
#retourner le choice

#vérifier choix valide():
#boucle infinie:
    #recupérer get_choice() dans une variable choice
        #doit être un chiffre 
            #le convertir enint
            #doit être compris dans l'intervalle donnée
                #retourner le choix
            #redemander un choix dans l'intervalle 
        #redemander un choix qui est un nombre getchoice()


#éxécuter le choix valide:
#si le choix est 1 on lance le menu de la partie 
#si le choix est 2 on lance l'affichage du classement 
#si le choix est 3 on quitte le jeu 


#get username():
#on récupere dans une variable username l'entrée utilisateur du nom
#on retourne la var username

#choix 1 menu de la partie:
    #on get_username()
    #on demande au user de create_team() qu'on récupère dans une var user team
    #on lance le jeu(user team) 



#get_heroes():
#on récupere ds une liste tous les heros depuis la bdd
#on en retourne la liste 

#get_available():
#on récupère la liste en paramètre dans une variable liste "disponibles"
#on retourne la liste "disponibles"

#print_infos():
#on print la liste en paramètre


#create_team(): 
#création d'une variable liste d'équipe vide 
#on récupère get_all() dans une var all heroes
#on recupère get_available dans une var available heroes
#on on affecte une max length à une variable team_max_length
#boucle de la creation de l'équipe jusqu'à ce qu'elle atteigne team_max_length:
    #on print_infos la liste des héros disponibles
    #on demande au joueur de faire un choix valide pour ajouter un héro à son équipe
        #le héro choisi est ajouté à l'équipe de l'utilisateur
        #le héro choisi est supprimé de la liste des héros disponibles 
#la liste équipe est retournée 


#get_ranked_players_db():
#récupérer joueurs présents dans la collection joueurs depuis la db ds une variable players 
#retourner la variable players

#get_ranking():
#recuperer get_ranked_players_db() dans une variable users_ranked
#on trie la liste du plus petit au plus haut score 
#on return la liste

#choix 2 affichage du classement:
#on récupère le classement get_ranking() dans une var classement 
#on print la variable classement

#choix 3 quitter:
#on quitte le jeu

#is_character_alive(): 
#si les pvs du character concerné (monstre/héro) sont supéreurs à 0 il est vivant

#is_team_alive(team):
#vérifier les pvs de chaque membre de l'équipe 
#si les pvs d'au moins un héro de l'équipe sont positifs l'équipe est vivante



#get_monsters_from_db:
#on récupère les monstres dans une liste monstres depuis la db
#on retourne la listre monstres

#get_active_monsters():
#on récupère get_monsters_from_db dans une liste monstres_actifs
#on retourne la liste monstres_actifs

#pick_random_choice(list):
#on choisit un perso alétoire depuis une liste donnée
#on le retourne

#pick_monster_target(active_team):
#creer une variable target/cible qui contient un héro aléatoire de l'équipe active 
#retourner la variable target

#insert_ranked_player: 
#vérifier si il y a - de 3 utilisateurs dans la bdd
    #envoyer le joueur avec son score à la bdd  
#sinon vérifier si le score du joueur est plus élevé que celui de quelqu'un dans le classement
    #envoyer le joueur avec son score à la bdd  
    #supprimer de la bdd la personne avec le score le plus bas



#vague(active_team):
#on initialise un score à 0
#monstres=get_active_monsters()
#on récupère dans une variable random_monster un monstre aléatoire pick_random_choice(monstres) 
#tant que is_alive(random_monster) et is_team_alive(active_team) :
    #chaque perso de l'equipe active  
        #attaque le monstre 
        #lui afflige des dégats
    #si les pvs du monstre sont pos
        #on affecte pick_monster_target(active_team) à une var target_hero
        #le monstre l'attaque 
        #le target_hero subit des dégats
    #sinon:
        #on supprime le random_monster de la liste monstres
    #vérifier si les pvs du héro target sont negatifs:
        #on supprime le héro de l'équipe active
#le score prend +1
#victoire du joueur

#jeu(user_team):
#on affecte la liste user_team à une variable active_team

#tant que les pvs de l'équipe active sont pos
    #on lance une vague
#défaite
#insertion du score ds la bdd 
#affichage du score du joueur
#affichage du classement
#retour au menu principal


