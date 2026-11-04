
from pymongo import MongoClient
#initialiser la bdd

#   Importer la db et s'y connecter ---
client = MongoClient(host='localhost', port=27017)
db = client.jeu
#   -----

#   Menu------
def display_game_menu():
    print_header()
    print("1.Démarrer une nouvelle partie \n 2. Voir le classement \n 3. Quitter")
def print_header():
    print('_'*50)
    print("Bienvenue sur le jeu !")
    print('_'*50)
#   --------


#   Choice handling------
def is_valid(choice, min, max):
    if not choice.isdigit():
        return False
    choice = int(choice)
    if choice>max and choice<min:
        return False

def print_error():
    print('Veuillez entrer un choix valide.')

def get_valid_choice(min,max):
    while True:
        choice= input('Entrez votre choix')
        if is_valid(choice,min,max):
            return choice
        else:
            print_error()
#   ----------


#   Running options----
def run_valid_choice(choice):
    if choice==1:
        run_new_game()
    elif choice==2:
        run_ranking()
    elif choice==3:
        run_quit()
#   --------


#   Récupérer toutes les données nécessaires de la db

def get_heroes_from_db():
    heroes=list(db.perso.find())
    return heroes

def get_monsters_from_db():
    monsters=list(db.monstre.find())
    return monsters

#   Chocix 1----

#       Get valid username-----

def is_username_valid(username, min, max):
    if username>max and username<min:
        return False

def get_valid_username():
    while True:
        username=input("Veuillez entrer un nom d'utilisateur de minimum 3 caractères")
        if is_username_valid(username,4,15):
            return username
        else:
            print_error()
#        -------

#       Create the team------

def print_infos(list):
    for i,p in enumerate(list):
        print(f"{i+1}. {p['name']} \033[1m ATK : \033[0m {p['ATK']} \033[1m DEF: \033[0m {p['DEF']} \033[1m PV : \033[0m {p['PV']}")
    
max_team_length=3

def create_team(): 
    user_team=[]
    available_heroes=get_heroes_from_db()
    while len(user_team)<max_team_length:
        print_infos(available_heroes)
        choice=get_valid_choice(1, len(available_heroes))
        user_team.append(available_heroes[choice-1])
        available_heroes.pop(choice-1)
    print_infos(user_team)
    return user_team
#       ----------
#       Run a round -----

def run_round(username,user_team):
    score =0
    while is_team_alive(user_team):
        run_wave()
        if is_team_alive(user_team):
            score+=1
    defeat(username,score)


def defeat(username, score):
    insert_ranked_player(username, score)
    display_score(score)
    classement()
    


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

def run_new_game():
    username=get_valid_username()
    user_team=create_team()
    run_round(username,user_team)

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
    # 
def main():
    while True:
        display_game_menu()
        choice=get_valid_choice(1,3)
        run_valid_choice(choice)