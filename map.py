import pygame
import pytmx
from pytmx.util_pygame import load_pygame
import pyscroll

class MapManager:

    def __init__(self, screen_size):
        self.tmx_data = load_pygame('assets/map/map.tmx') 
        self.map_layer = pyscroll.BufferedRenderer(
            pyscroll.data.TiledMapData(self.tmx_data),
            screen_size
        )
        self.map_layer.zoom = 2 

    def add(self, sprite):
        self.group.add(sprite)

    def render(self, surface, center):
        self.map_layer.center(center)
        rect = surface.get_rect()
        self.map_layer.draw(surface, rect)