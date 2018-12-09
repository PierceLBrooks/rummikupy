
# Authors: Pierce Brooks, Amalie Brooks, & Jeff Busch

import sys
import obj
import importlib

def run(pygame, arguments):
	resolution = (800, 600)
	pygame.display.init()
	screen = pygame.display.set_mode(resolution)
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))
	clock = pygame.time.Clock()
	objects = []
	objects.append(obj.Object())
	
	quit = False
	while not (quit):
		#update
		deltaTime = float(clock.tick())/1000.0
		for object in objects:
			print(object)
			object.update(pygame, screen, background, deltaTime)
		
		#input
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				quit = True
		if (quit):
			break
		
		#render
		pygame.display.flip()
		background.fill((0, 0, 0))
	
	pygame.display.quit()
	return 0

if (__name__ == "__main__"):
	arguments = sys.argv
	pygame = importlib.import_module("pygame")
	run(pygame, arguments)
