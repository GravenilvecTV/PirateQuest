import pygame
pygame.init()
from map import MapManager
from player import Player

# creer la fenetre du jeu
class Game:

    def __init__(self):
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("PirateQuest")
        self.map_manager = MapManager(self.screen_size)

        self.player = Player(
            self.map_manager.tmx_data.width,
            self.map_manager.tmx_data.height
        )
 
        self.running = True

    def run(self):
        while self.running:
            # evenements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # rafraichir les elements du jeu
            self.screen.fill((0, 0, 0))
            self.map_manager.render(self.screen, (0, 0))
            self.player.draw(self.screen, self.screen_size)  
            pygame.display.flip() 
            
 
        pygame.quit()

# creer une instance du jeu
game = Game()
game.run() 