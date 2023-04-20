import pygame, time, sys

def run():
    screen = pygame.display.get_surface()
    
    font = pygame.font.Font(None, 40)
    text = "Ray Sist: The Quest-ionable Heroe (A Fantasy Of A 40-Year-Old Virgin) est un RPG dans un monde de fantaisie où les joueurs incarnent le personnage de Ray Sist, un homme de 40 ans qui n'a jamais eu de relation amoureuse ou sexuelle.L'histoire commence lorsque Ray Sist décide de partir en quête pour trouver l'amour et perdre sa virginité. Il se rend dans un monde fantastique rempli de magie et de créatures étranges, où il doit vaincre des ennemis, explorer des donjons et résoudre des énigmes pour avancer dans sa quête.Au fur et à mesure que le joueur progresse, Ray Sist rencontre différents personnages, certains amicaux et d'autres hostiles, qui l'aideront ou chercheront à l'empêcher dans sa quête. Le joueur doit prendre des décisions importantes qui affectent le déroulement de l'histoire et l'issue de la quête de Ray Sist.\n\nAu-delà de sa quête personnelle, Ray Sist se retrouve impliqué dans une conspiration plus grande qui menace le monde fantastique. Le joueur doit aider Ray Sist à sauver le monde en combattant des ennemis puissants et en révélant les secrets cachés.Le jeu propose un système de combat en temps réel, où le joueur doit utiliser des compétences spéciales et des attaques pour vaincre les ennemis. Il existe également un système de crafting pour créer des armes et des armures, ainsi qu'un système de relations avec les personnages non-joueurs qui affecte le déroulement de l'histoire."
    text_surface = font.render(text, True, '#ffff00')
    text_x = 900
    text_y = 900 // 2 - text_surface.get_height() // 2

    scroll_speed = 2

    running = True
    while running:

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_e or event.key == pygame.K_SPACE:
                    running = False

        screen.fill('#000000')

        text_x -= scroll_speed
        if text_x < -text_surface.get_width():
            text_x = screen.get_size()[0]

        screen.blit(text_surface, (text_x, text_y))

        pygame.display.flip()

        time.sleep(0.01)

    pygame.quit()