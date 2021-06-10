class Player(object):
    """
    This model is used to save data from one Player 
    """

    # Tableau à titre indicatif en attendant l'intégration de TinyDB
    players_list = []

    def __init__(self, nom="", prenom="", date_naissance="", sexe=""):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = 0

    def __str__(self):
        return self.nom + ' - ' + self.prenom + ' - ' + self.date_naissance + \
            ' - ' + self.sexe + ' - ' + self.classement

    
    def save(self):
        """
        Todo: Se connecter à la BD et enregistrer le joueur
        """
        # 1. on crée un objet Joueur
        player = {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance,
            "sexe": self.sexe,
            "classement": self.classement
        }

        # 2. On enregistre l'objet joueur
        self.players_list.append(player)
        return player


    def get_all(self):
        """
        Todo: Se connecter à la base de données et récupérer tous les joueurs 
        """
        return self.players_list

