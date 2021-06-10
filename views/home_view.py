class HomeView(object):
    def __init__(self, controller=None):
        self.controller = controller


    def navigate_to_menu(self, message):
        """
        Cette fonction permet de récupérer l'option saisie par un utilisateur et ensuite
        d'utiliser de naviger vers le menu correspondant à cette option
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
        Bienvenue sur l'application de gestion des tournois d'échecs\n
        Voici les actions possibles depuis ce menu : \n
        [1]: Gérer les tournois\n
        [2]: Gérer les joueurs\n
        [3]: Gérer les tournées\n
        [0]: Retourner au menu parent (pas encore implémenté)\n
        [X]: Sortir de l'application (pas encore implémenté)\n
        """
        self.navigate_to_menu(message)

