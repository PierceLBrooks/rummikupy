
# Author: Pierce Brooks & Jeff Busch

import obj
import util

class Piece(obj.Object):
	def __init__(self, position):
		self.position = position
		self.image = None
		
	def update(self, pygame, screen, background, deltaTime):
		if (self.image == None):
			self.image = util.loadImage(pygame, "piece.png")
		screen.blit(background, self.image, self.position)
