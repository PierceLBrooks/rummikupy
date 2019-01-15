
# Author: Pierce Brooks & Jeff Busch

import os
import inspect

def cwd():
	frame = None
	path = ""
	try:
		frame = inspect.currentframe()
		path += str(os.path.dirname(os.path.abspath(inspect.getfile(frame))))
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

def addVector(vector, number):
	result = []
	for i in range(len(vector)):
		result.append(vector[i]+number)
	return result

def subtractVector(vector, number):
	result = []
	for i in range(len(vector)):
		result.append(vector[i]-number)
	return result

def multiplyVector(vector, number):
	result = []
	for i in range(len(vector)):
		result.append(vector[i]*number)
	return result

def divideVector(vector, number):
	result = []
	for i in range(len(vector)):
		result.append(vector[i]/number)
	return result

def addVectors(vector, other):
	result = []
	if (len(vector) < len(other)):
		return None
	for i in range(len(vector)):
		result.append(vector[i]+other[i])
	return result

def subtractVectors(vector, other):
	result = []
	if (len(vector) < len(other)):
		return None
	for i in range(len(vector)):
		result.append(vector[i]-other[i])
	return result

def multiplyVectors(vector, other):
	result = []
	if (len(vector) < len(other)):
		return None
	for i in range(len(vector)):
		result.append(vector[i]*other[i])
	return result

def divideVectors(vector, other):
	result = []
	if (len(vector) < len(other)):
		return None
	for i in range(len(vector)):
		result.append(vector[i]/other[i])
	return result
