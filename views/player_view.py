class PlayerView(object):
    def __init__(self, controller):
        self.controller = controller


    def navigate_to_menu(self, message):
        """
        Cette fonction permet de récupérer l'option saisie par un utilisateur et ensuite
        d'utiliser de naviger vers le menu correspondant à cette
        """
        # On récupère l'option saisie par le client
        # La récupération de l'option doit être améliorée pour gérer les cas d'erreur de saisie
        option = input(message)
        # Une fois qu'on a récupéré l'option, on navigue vers la page suggérée
        self.controller.go_to_menu(option)


    def display_home(self):
        """
        Affiche les options pour gérer les joueurs
        """
        message = """
        Ce menu permet de gérer les joueurs de l'application\n
        Voici les actions possibles depuis ce menu : \n
        [1]: Afficher tous les joueurs\n
        [2]: Ajouter un nouveau joueur\n
        [3]: Modifier un joueur (pas encore implémenté)\n
        [4]: Supprimer un joueur (pas encore implémenté)\n
        [0]: Retourner au menu parent (pas encore implémenté)\n
        [X]: Aller au menu précédent (pas encore implémenté)\n
        [Z]: Sortir de l'application (pas encore implémenté)\n
        """
        self.navigate_to_menu(message)
        

    def display_player(self, player):
        """
        Affiche les détails d'un joueur
        """
        message = """
        Informations sur le joueur :\n
        Nom : {0}\n
        Prenom: {1}\n
        Date de naissance: {2}\n
        Sexe: {3}\n
        Classement: {4}\n
        
        Vous pouvez retourner au menu de gestion des joueurs en saisissant l'option [0]\n
        Ou bien vous pouvez sortir du programme en saisissant l'option [X]\n
        """.format(player.nom, player.prenom, player.date_naissance, player.sexe, player.classement)
        self.navigate_to_menu(message)


    def display_players_list(self, players_list):
        """
        Affiche la liste de joueurs
        """
        message = ""

        if len(players_list) == 0:
            message = "La liste de joueurs est vide !\n"    

        for player in players_list:
            message += player.__str__() + '\n'

        message += """
        Vous pouvez retourner au menu de gestion des joueurs en saisissant l'option 0\n
        Ou bien vous pouvez sortir du programme en saisissant l'option X\n
        """
        
        self.navigate_to_menu(message)


    def display_create_player(self):
        """
        Affiche le menu de création d'un joueur
        """
        message = "Vueillez entrer les informations du nouveau joueur : \n"
        print(message)
        nom = input("\nVeuillez entrer le nom : ")
        prenom = input("\nVeuillez entrer le prenom : ")
        date_naissance = input("\nVeuillez entrer la date de naissance (dd/mm/yyyy) : ")
        sexe = input("\nVeuillez entrer le sexe du joueur : ")

        player = {
            "nom": nom,
            "prenom": prenom,
            "date_naissance": date_naissance,
            "sexe": sexe
        }

        result = self.controller.save_player(player)

        if result == {}:
            print("Une erreur s'est produite lors de l'enregistrement du joueur !")
        
        message += """Le joueur a bien été créé et sauvegardé en base de données\n
                Vous pouvez retourner au menu de gestion des joueurs en saisissant l'option 0\n
                Ou bien vous pouvez sortir du programme en saisissant l'option X\n"""
        
        self.navigate_to_menu(message)


