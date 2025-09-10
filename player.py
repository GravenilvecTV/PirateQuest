import pygame

class Player:

    def __init__(self, map_width, map_height):
        # charger l'image du joueur (spritesheet)
        self.spritesheet = pygame.image.load('assets/spritesheets/characters.png')
        # stocker chaque morceau (frames)
        self.frames = []
        self.size = 64

        for i in range(3):
            frame = self.spritesheet.subsurface(pygame.Rect(i * 32, 32, 32, 32))
            frame = pygame.transform.scale(frame, (self.size , self.size ))
            self.frames.append(frame)

    def draw(self, surface, screen_size): 
        # centre de l'ecran
        pos = (
            screen_size[0] // 2 - self.size // 2, 
            screen_size[1] // 2 - self.size // 2 
        )
        # recuperer quelle frame
        frame = self.frames[0]
        # dessiner le joueur
        surface.blit(frame, pos)