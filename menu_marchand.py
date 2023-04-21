import pygame,sys
from save import *

class Menu_Marchand:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.save_data = SaveData('save.json')
   

    def run(self):

        largeur_bouton = 400
        bouton_potion = pygame.Rect((self.screen.get_width() - largeur_bouton) / 2, 700, largeur_bouton, 50)
        


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_potion.collidepoint(pygame.mouse.get_pos()):
                        items_old = self.save_data.load_inventory()
                        num_pieces = items_old.count("Piece")
                        if num_pieces >= 1:
                            self.save_data.remove_item_from_inventory("Piece")
                            items = self.save_data.load_inventory()
                            items.append("potion")
                            self.save_data.save_inventory(items)
                            return
                    else:
                        return
                
                        
                        
                
            self.screen.fill((0, 0, 0))
            font_grand = pygame.font.Font('graphics/font/Enchanted_Land.otf', 50)
            texte_bienvenue = font_grand.render("Bienvenue chez le marchand", True, (255, 255, 255))
            self.screen.blit(texte_bienvenue, ((self.screen.get_width() - texte_bienvenue.get_width()) / 2, 50))
            

            pygame.draw.rect(self.screen, (255, 255, 255), bouton_potion)
            pygame.draw.rect(self.screen, (255, 0, 0), bouton_potion, 3)
            image = pygame.image.load("graphics/potions/potion_heal.png")
            self.screen.blit(image, ((self.screen.get_width() - image.get_width()) / 2, 100))
            font = pygame.font.Font(None, 30)
            texte_potion = font.render("1 potion pour 1 piece", True, (0, 0, 0))
            self.screen.blit(texte_potion, (bouton_potion.x + 10, bouton_potion.y + 10))
            
            pygame.display.flip()
