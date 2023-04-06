import pygame

class Inventaire:
    """inventaire = Inventaire()
    inventaire.draw()"""
    def __init__(self, resolution, screen):
        # Définition des dimensions de l'écran
        self.resolution = resolution

        # Couleur de fond de l'écran
        self.bg_color = 'ffffff'

        # Variables pour l'inventaire
        self.inventory_open = False

        self.font = pygame.font.Font(None, 24)  # Utiliser la police Arial avec une taille de caractère de 24

        # Création de l'écran Pygame
        self.screen = screen
        # Définir le titre de la fenêtre Pygame
        pygame.display.set_caption("Inventaire")

    def open_inventory(self):
        self.inventory_open = True
        
    def draw_inventory(self):
        # Exemple de bloc de code indenté
        if self.inventory_open:
            # Dessiner l'inventaire
            inventory_rect = pygame.Rect(100, 100, 200, 300)  # Coordonnées et dimensions du rectangle
            pygame.draw.rect(self.screen, (0, 0, 0), inventory_rect)  # Dessiner le rectangle en noir
            inventory_text = self.font.render("Inventory", True, (255, 255, 255))  # Créer un texte "Inventory"
            self.screen.blit(inventory_text, (110, 110))  # Dessiner le texte à l'intérieur du rectangle
        else:
            # Dessiner le texte pour indiquer que l'inventaire est fermé
            closed_text = self.font.render("Press 'i' to open inventory", True, (0, 0, 0))
            self.screen.blit(closed_text, (100, 100))