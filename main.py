import pygame, time
from debug import debug
# from button import Button
from inventaire import Inventaire
from sys import exit



if __name__ == '__main__':
    pygame.init()
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    
    inventaire = Inventaire(resolution)
    inventaire.draw_inventory()
    
    previous_time = time.time()
    
    while True:
        dt = time.time() - previous_time
        previous_time = time.time()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    debug('Touche I appuyée')
                    inventaire.open_inventory()
        
        # debug("test")
        pygame.display.update()
        clock.tick(60)