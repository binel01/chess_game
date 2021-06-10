import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from models.player_model import Player
from views.home_view import HomeView
from views.player_view import PlayerView

class PlayerController(object):
    def __init__(self, parent_view):
        # A la création du controleur, on peut le lier à son modèle et sa vue
        self.model = Player()
        self.view = PlayerView(self)
        self.parent_view = parent_view


    def save_player(self, player):
        new_player = self.model(player.nom, player.prenom, player.date_naissance, player.sexe, 
                player.sexe, player.classement)
        return new_player.save()


    def display_home(self):
        """
        Permet l'affichage de la page de gestion des joueurs
        """
        return self.view.display_home()


    def go_to_menu(self, menu_option):
        """
        Fonction permettant de gérer la navigation entre les pages d'une vue
        """
        if menu_option == "0":
            return self.parent_view.display_home()
        elif menu_option == "1":
            all_players = self.model.get_all()
            return self.view.display_players_list(all_players)
        elif menu_option == "2":
            message = "Désolé, ce menu n'est pas encore implémenté !\nVeuillez réessayer : "
            return self.view.navigate_to_menu(message)
        elif menu_option == "3":
            message = "Désolé, ce menu n'est pas encore implémenté !\nVeuillez réessayer : "
            return self.view.navigate_to_menu(message)
        elif menu_option == "4":
            message = "Désolé, ce menu n'est pas encore implémenté !\nVeuillez réessayer : "
            return self.view.navigate_to_menu(message)
        elif menu_option == "X":
            return self.view.display_home()
        elif menu_option == "Z":
            return self.parent_view.display_home()


