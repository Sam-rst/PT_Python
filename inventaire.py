class Inventaire:
    def __init__(self):
        self.objets = [] # La liste des objets collectés
    
    def ajouter_objet(self, objet):
        self.objets.append(objet)
    
    def supprimer_objet(self, objet):
        self.objets.remove(objet)
            
    def get_items(self):
        return self.objets