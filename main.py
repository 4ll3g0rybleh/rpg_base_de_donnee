

#initialiser la bdd

#se connecter à la bdd
#BOUCLE DU JEU:
    #afficher le menu du jeu
    #recuperer un choix valide
    #éxecuter le choix 

#max_team_length=3

#afficher le menu():
    #afficherle header du jeu print_header()
    #afficher le menu des choix 

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
    #si le choix est 1,lancer le menu de la partie 
    #si le choix est 2, lancer l'affichage du classement 
    #si le choix est 3, quitter le jeu 



#choix 1 menu de la partie:
    #get_username()
    #user_team=create_team() 
    #lancer le jeu(user team) 


#get username():
    #username = valid_username()
    #retourner la var username

#valid_username(min, max):
    #boucle infinie:
        #demander un input dans une var username
            #la longueur du username doit être comprise dans l'intervalle donnée
                #retourner le username
            #redemander un username de la bonne longueur 
        #redemander un username

#get_heroes():
    #récuperer ds une liste tous les heros depuis la bdd
    #return la liste

#get_monsters_from_db:
    #on récupère les monstres dans une liste monstres depuis la db
    #on retourne la listre monstres    
    #retourner la liste 

#print_infos(liste):
    #on print la liste en paramètre


#create_team(): 
    #user_team=[]
    #available_heroes=get_heroes()
    #tant que la taille de user_team est plus petite que team_max_length:
        #on print_infos(available_heroes) la liste des héros disponibles
        #on demande au joueur de faire un choix valide pour ajouter un héro disponible à son équipe
            #le héro choisi est ajouté à l'équipe de l'utilisateur
            #le héro choisi est supprimé de la liste des héros disponibles 
    #la liste équipe est retournée 


#jeu(username, user_team):
    #score = 0
    #tant que team_is_alive(user_team)
        #on lance une vague
        #si is_team_alive(user_team):
            #score+1
    #défaite(username,score)


#défaite(username, score):
    #insert_ranked_player(username, score)
    #display_score(score)
    #classement()
    #afficher le menu principal


#vague(user_team):
    #monsters=get_monsters()
    #alive_monsters=get_alive_entities(monsters)
    #random_monster=pick_random_choice(monsters)
    #tant que is_character_alive(random_monster) et is_team_alive(active_team) :
        #combat_phase(user_team, monstres)


#combat_phase(active_team, monstres):
    #team_on_monster(active_team, random_monster)
    #si is_alive(random_monster) 
        #monster_on_team(active_team, random_monster)

#is_character_alive(): 
    #si les pvs du character concerné (monstre/héro) sont supéreurs à 0 il est vivant

#is_team_alive(team):
    #is_character_alive() pr chaque membre
    #si les pvs d'au moins un héro de l'équipe sont positifs l'équipe est vivante

#pick_random_choice(list):
    #on choisit un perso alétoire depuis une liste donnée
    #on le retourne

#team_on_monster(alive_team, random_monster):
    #pour chaque perso de l'equipe 
        #degats=dégâts(perso, random_monster)
        #update_victim_hp(degats,random_monster,alive_monsters)
        #print_attaque(perso, random_monster) 

#monster_on_team(user_team, random_monster):
    #si is_alive(random_monster)
        #alive_team = get_alive_entities(active_team)
        #target_hero=pick_random_choice(alive_team)
        #degats=degats(monster, target_hero)
        #update_victim_hp(degats,target_hero,alive_team)
        #print_attaque(random_monster, target_hero)
        #retourner le target_hero

#get_alive_entities(list):
    #alive_entities= liste vide
    #pour chaque entité de list 
        #si l'entité is_alive():
            #ajouter l'entité à alive_entities
    #retourner alive_entities

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
    #on met à jour les hp du chara 2 dans la list2 



#choix 2 affichage du classement:
    #on récupère le classement get_ranking() dans une var classement 
    #on print la variable classement

#get_players_db():
    #récupérer joueurs présents dans la collection joueurs depuis la db ds une variable players 
    #retourner la variable players

#make_ranking():
    #recuperer get_players_db() dans une variable users_ranked
    #on trie la liste du plus petit au plus haut score 
    #on return la liste

#insert_ranked_player: 
        #envoyer le joueur avec son score à la bdd  



#choix 3 quitter:
    #on quitte le jeu