
# Author: Pierce Brooks & Jeff Busch

import obj
import util
import random

class Piece(obj.Object):
	def __init__(self, position):
		self.position = position
		self.image = None
		
	def update(self, pygame, screen, background, deltaTime):
		if (self.image == None):
			self.image = util.loadImage(pygame, "piece.png")
		range = 500
		self.position[0] += int(deltaTime*float(random.randint(-range, range)))
		self.position[1] += int(deltaTime*float(random.randint(-range, range)))
		background.blit(self.image, tuple(self.position))
