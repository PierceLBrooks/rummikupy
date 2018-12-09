
# Author: Pierce Brooks & Jeff Busch

import os
import inspect

def cwd():
	frame = None
	path = ""
	try:
		frame = inspect.currentframe()
		path += str(os.path.realdir(frame))
	except:
		pass
	finally:
		del frame
	return path

def loadImage(pygame, name):
	path = os.path.join(cwd(), name)
	print(path)
	try:
		image = pygame.image.load(path)
		if (image.get_alpha == None):
			image = image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error as message:
		print("Cannot load image: "+str(path))
		print(message)
		raise SystemExit
	return image
