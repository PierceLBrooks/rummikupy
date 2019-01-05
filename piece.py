
# Author: Pierce Brooks & Jeff Busch

# import obj
import util
import random
import pygame

class Piece(pygame.sprite.Sprite):
	def __init__(self, position):
		super(Piece, self).__init__()
		self.position = position
		self.scale = [1.0, 1.0]
		self.image = None
		self.imageWidth = None
		self.imageHeight = None
		self.imageWidthMaximum = 1280
		self.imageHeightMaximum = 1280
		self.imagePositionX = self.position[0]
		self.imagePositionY = self.position[1]
		self.imageScaleX = self.scale[0]
		self.imageScaleY = self.scale[1]
		self.rect = None
		
	def update(self, pygame, screen, background, deltaTime):
		if (self.image == None):
			self.image = util.loadImage(pygame, "piece.png")
			self.imageWidth = self.image.get_width()
			self.imageHeight = self.image.get_height()

		# range = 500
		# self.position[0] += int(deltaTime*float(random.randint(-range, range)))
		# self.position[1] += int(deltaTime*float(random.randint(-range, range)))
		
		if ((self.imageScaleX != self.scale[0]) or (self.imageScaleY != self.scale[1])):
			scaleX = 1.0+(self.scale[0]-self.imageScaleX)
			scaleY = 1.0+(self.scale[1]-self.imageScaleY)
			scaleX = int(scaleX*float(self.imageWidth))
			scaleY = int(scaleY*float(self.imageHeight))
			if ((scaleX < self.imageWidthMaximum) and (scaleY < self.imageHeightMaximum)):
				self.image = pygame.transform.smoothscale(self.image, (scaleX, scaleY))
			
		self.rect = self.image.get_rect(x=(self.position[0]), y=(self.position[1]))
		
		self.imagePositionX = self.position[0]
		self.imagePositionY = self.position[1]
		self.imageScaleX = self.scale[0]
		self.imageScaleY = self.scale[1]
		
		background.blit(self.image, tuple(self.position))
		
	def setPosition(self, position):
		self.position = position
		
	def setScale(self, scale):
		self.scale = scale
		
	def getPosition(self):
		return self.position
		
	def getScale(self):
		return self.scale
