import pygame
import sys
import os
from TestCode import *
from Card import *
from Settings import *
import ctypes

class Game:
    def __init__(self):
        pygame.init()
        WIDTH, HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Poker Stars")
        self.clock = pygame.time.Clock()
        self.hand = Hand()
        
        self.display_surface = pygame.display.get_surface()
        background_image = pygame.image.load(os.path.join("table.jpeg")).convert()
        self.scaled_background = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        Deck_card = pygame.image.load(os.path.join("default.png")).convert()
        self.scaled_Deck_card = pygame.transform.scale(Deck_card, (50, 70))
        
        

    def run(self):
        mouse_down = False
        self.start_time = pygame.time.get_ticks()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        mouse_down = True
                
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  
                        if mouse_down:
                            mouse_down = False
                            self.hand()
                            #self.hand.update()
            
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            self.screen.blit(self.scaled_background, (0, 0))
            self.screen.blit(self.scaled_Deck_card, (230, 265))
            self.hand.update()
            pygame.display.update()
            self.clock.tick(60)

            

if __name__ == '__main__':
    game = Game()
    game.run()
