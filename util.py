
# Author: Pierce Brooks & Jeff Busch

import os
import inspect

def cwd():
	frame = None
	path = ""
	try:
		frame = inspect.current_frame()
		path += str(os.path.realdir(frame))
	except:
		pass
	finally:
		del frame
	return path

def loadImage(pygame, name):
	path = str(os.path.join(cwd(), name))
	try:
		image = pygame.image.load(path)
		if (image.get_alpha == None):
			image = image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error as message:
		print("Cannot load image: "+path)
		raise SystemExit
	return image
