
# Authors: Pierce Brooks, Amalie Brooks, & Jeff Busch

import sys
import piece
import importlib

def run(pygame, arguments):
	resolution = [800, 600]
	pygame.display.init()
	screen = pygame.display.set_mode(tuple(resolution))
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))
	clock = pygame.time.Clock()
	objects = []
	objects.append(piece.Piece([resolution[0]/2, resolution[1]/2]))
	
	quit = False
	while not (quit):
		#update
		background.fill((0, 0, 0))
		deltaTime = float(clock.tick())/1000.0
		for object in objects:
			print(object)
			object.update(pygame, screen, background, deltaTime)
		screen.blit(background, (0, 0))
		
		#input
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				quit = True
		if (quit):
			break
		
		#render
		pygame.display.flip()
	
	pygame.display.quit()
	return 0

if (__name__ == "__main__"):
	arguments = sys.argv
	pygame = importlib.import_module("pygame")
	run(pygame, arguments)
