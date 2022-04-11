import pygame 
from config import *
from grass import Grass
from char import Char
from apple import Apple


class Map:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.all_sprites = pygame.sprite.Group()
		self.apple_sprites = pygame.sprite.Group()
		self.obstacle_sprites = pygame.sprite.Group()
		self.draw_map()

	def draw_map(self):
		for row_index, row in enumerate(MAP):
			for col_index, col in enumerate(row):
				x = col_index * GRASSSIZE
				y = row_index * GRASSSIZE
				if col == 'x':
					Grass((x, y), [self.all_sprites, self.obstacle_sprites])
				if col == 'a':
					Apple((x, y), [self.all_sprites, self.apple_sprites])
				if col == 'p':
					self.player = Char((x, y), [self.all_sprites], self.obstacle_sprites, self.apple_sprites)

	def run(self):
		self.all_sprites.draw(self.display_surface)
		self.all_sprites.update()
