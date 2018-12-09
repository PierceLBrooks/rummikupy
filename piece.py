
# Author: Pierce Brooks & Jeff Busch

import obj
import util

class Piece(obj.Object):
	def __init__(self, position):
		self.position = position
		self.image = util.loadImage("piece.png")
		
	def update(self, pygame, screen, background, deltaTime):
		screen.blit(background, self.image, self.position)
