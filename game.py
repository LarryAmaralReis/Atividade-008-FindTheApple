import pygame
import sys
from config import *
from map import Map


class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
		pygame.display.set_caption('FindTheApple')
		self.clock = pygame.time.Clock()
		self.back_img = pygame.image.load('images/background.png').convert()
		self.map = Map()
	
	def main_loop(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			self.screen.blit(self.back_img, (0, 0))
			self.map.run()
			pygame.display.update()
			self.clock.tick(FPS)
