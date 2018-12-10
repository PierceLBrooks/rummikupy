
# Authors: Pierce Brooks, Amalie Brooks, & Jeff Busch

import sys
import piece
import importlib
import grid as g

def run(pygame, arguments):
	resolution = [800, 600]
	pygame.display.init()
	screen = pygame.display.set_mode(tuple(resolution))
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))
	objects = []
	objects.append(piece.Piece([resolution[0]/2, resolution[1]/2]))
	#grid = g.makeGrid(pygame, resolution[0], resolution[1], 40, 40)
	clock = pygame.time.Clock()
	
	# Is it ok to have this here?
	rectangle_draging = False
	
	quit = False
	while not (quit):
		#update
		background.fill((0, 0, 0))
		deltaTime = float(clock.tick())/1000.0
		#background.blit(grid, (0,0))
		for object in objects:
			object.update(pygame, screen, background, deltaTime)
		screen.blit(background, (0, 0))
		
		#input
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				quit = True
			if (quit):
				break
		
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:
					objects.append(piece.Piece([resolution[0]/2, resolution[1]/2]))
					print(objects)

		#I found this code on google. I modified it to work with our objects.
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:            
					if object.rect.collidepoint(event.pos):
						rectangle_draging = True
						mouse_x, mouse_y = event.pos
						offset_x = object.position[0] - mouse_x
						offset_y = object.position[1] - mouse_y

			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:            
					rectangle_draging = False

			elif event.type == pygame.MOUSEMOTION:
				if rectangle_draging:
					mouse_x, mouse_y = event.pos
					object.position[0] = mouse_x + offset_x
					object.position[1] = mouse_y + offset_y
		
		#render
		pygame.display.flip()
	
	pygame.display.quit()
	return 0

if (__name__ == "__main__"):
	arguments = sys.argv
	pygame = importlib.import_module("pygame")
	run(pygame, arguments)
