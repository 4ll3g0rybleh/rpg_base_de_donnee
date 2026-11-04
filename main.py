

#initialiser la bdd

#se connecter à la bdd
#BOUCLE DU JEU:
    #afficher le menu du jeu
    #recuperer un choix valide
    #éxecuter le choix 


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
                #le convertir en int
                #doit être compris dans l'intervalle donnée
                    #retourner le choix
                #redemander un choix dans l'intervalle 
            #redemander un choix qui est un nombre getchoice()


#éxécuter le choix valide:
    #si le choix est 1 on lance le menu de la partie 
    #si le choix est 2 on lance l'affichage du classement 
    #si le choix est 3 on quitte le jeu 




#choix 1 menu de la partie:
    #on get_username()
    #on demande au user de create_team() qu'on récupère dans une var user_team
    #on lance le jeu(user team) 

#get username():
    #on récupere dans une variable username l'entrée utilisateur du nom
    #on retourne la var username


#get_heroes():
    #on récupere ds une liste tous les heros depuis la bdd
    #on en retourne la liste 

#get_available(list):
    #on récupère la liste en paramètre dans une variable liste "disponibles"
    #on retourne la liste "disponibles"

#print_infos():
    #on print la liste en paramètre


#create_team(): 
    #création d'une variable liste d'équipe vide 
    #on récupère get_heroes() dans une variable heros disponibles
    #on on affecte une max length à une variable team_max_length
    #boucle de la creation de l'équipe jusqu'à ce qu'elle atteigne team_max_length:
        #on print_infos la liste des héros disponibles
        #on demande au joueur de faire un choix valide pour ajouter un héro disponible à son équipe
            #le héro choisi est ajouté à l'équipe de l'utilisateur
            #le héro choisi est supprimé de la liste des héros disponibles 
    #la liste équipe est retournée 


#get_players_db():
    #récupérer joueurs présents dans la collection joueurs depuis la db ds une variable players 
    #retourner la variable players

#make_ranking():
    #recuperer get_players_db() dans une variable users_ranked
    #on trie la liste du plus petit au plus haut score 
    #on return la liste

#choix 2 affichage du classement:
    #on récupère le classement get_ranking() dans une var classement 
    #on print la variable classement

#choix 3 quitter:
    #on quitte le jeu




#jeu(user_team):
    #score = 0
    #tant que team_is_alive(user_team)
        #on lance une vague
        #si is_team_alive(user_team):
            #score+1
    #défaite()


#vague(user_team):
    #monstres=get_monsters()
    #on récupère dans une variable random_monster un monstre aléatoire pick_random_choice(monstres)
    #tant que random_monster n'est pas vivant
        #on récupère un monstre aleatoire dans la var random monster
    #tant que is_character_alive(random_monster) et is_team_alive(active_team) :
        #combat_phase(user_team, monstres)


#combat_phase(active_team, monstres):
    #team_on_monster(active_team, random_monster)
    #si is_alive(random_monster) 
        #monster_on_team(active_team, random_monster)


#team_on_monster(active_team, random_monster):
    #pour chaque perso de l'equipe 
        #si perso is_alive()   
            #dégâts(perso, random_monster)
            #print_attaque(perso, random_monster) 

#monster_on_team(active_team, random_monster):
    #si is_alive(random_monster)
        #alive_team = get_alive_entities(active_team)
        #on affecte pick_random_choice(alive_team) à une var target_hero
       
        #degats(monster, target_hero)
        #print_attaque(random_monster, target_hero)
        #on retourne le target_hero


#degats(character1, character2, active team, monster):
    #attk=attk_data(chara1, list1)
    #def_n_hp=def_n_hp_data(chara2, list2)
    #degats=def_n_hp-attk

#attk_data(chara1, list1):
    #attk= l'attaque du chara1 dans la list1
    #on retourne attk 

#def_n_hp_data(chara2, list2):
    #def= la defense du chara2 dans la list2
    #hp= les hp du chara2 dans la list2
    #def_n_hp=hp+def
    #on retourne def_n_hp 

#update_victim_hp(degats, chara2, list2)
    #



#is_character_alive(): 
    #si les pvs du character concerné (monstre/héro) sont supéreurs à 0 il est vivant

#is_team_alive(team):
    #is_alive() pr chaque membre
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

#insert_ranked_player: 
        #envoyer le joueur avec son score à la bdd  



#défaite():
    #insert_ranked_player()
    #affichage du score du joueur
    #classement()
    #retour au menu principal