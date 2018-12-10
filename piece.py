
# Author: Pierce Brooks & Jeff Busch

import obj
import util
import random

class Piece(obj.Object):
	def __init__(self, position):
		self.position = position
		self.image = None
		self.imageX = None
		self.imageY = None
		self.rect = None
		
	def update(self, pygame, screen, background, deltaTime):
		if (self.image == None):
			self.image = util.loadImage(pygame, "piece.png")
		
		#Not sure if this is where this should be but it seems to work.
		self.imageX = self.image.get_width()
		self.imageY = self.image.get_height()
		self.rect = pygame.Rect(self.position[0], self.position[1], self.imageX, self.imageY)

		# range = 500
		# self.position[0] += int(deltaTime*float(random.randint(-range, range)))
		# self.position[1] += int(deltaTime*float(random.randint(-range, range)))
		
		background.blit(self.image, tuple(self.position))
