
# Authors: Pierce Brooks, Amalie Brooks, & Jeff Busch

import sys
import util
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
	sprites = pygame.sprite.Group()
	sprites.add(piece.Piece([resolution[0]/2, resolution[1]/2]))
	#grid = g.makeGrid(pygame, resolution[0], resolution[1], 40, 40)
	clock = pygame.time.Clock()
	

	rectangle_draging = False
	mouse_down = False
	mouse_pos = None
	dragger = None
	set_down = []
	repositioned = []
	offset_x = 0
	offset_y = 0
	mouse_x = 0
	mouse_y = 0
	
	quit = False
	while not (quit):
		#update
		background.fill((0, 0, 0))
		deltaTime = float(clock.tick())/1000.0
		#background.blit(grid, (0,0))
		for sprite in sprites:
			sprite.update(pygame, screen, background, deltaTime)
			if (mouse_down):
				if rectangle_draging:
					if (dragger == sprite):
						mouse_x, mouse_y = mouse_pos
						sprite.position[0] = mouse_x + offset_x
						sprite.position[1] = mouse_y + offset_y

				elif sprite.rect.collidepoint(mouse_pos):
					if (dragger == None):
						rectangle_draging = True
						dragger = sprite
						mouse_x, mouse_y = mouse_pos
						offset_x = sprite.position[0] - mouse_x
						offset_y = sprite.position[1] - mouse_y
				for num, sprite in enumerate (repositioned):
					if sprite.rect.collidepoint(mouse_pos):
						del repositioned[num]
						break


		screen.blit(background, (0, 0))
		
		"""
		if not (dragger == None):
			dragger.setScale(util.multiplyVector(dragger.getScale(), 1.0+(deltaTime*25.0)))
		"""
		
		#input
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				quit = True
			if (quit):
				break
		
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:
					sprites.add(piece.Piece([resolution[0]/2, resolution[1]/2]))
					print(sprites)
					
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:            
					mouse_down = True
					mouse_pos = event.pos

			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:            
					mouse_down = False
					rectangle_draging = False
					if not (dragger == None):
						if	dragger not in set_down:
							set_down.append(dragger)
						for sprite in set_down:	
							if not (sprite == dragger):
								if pygame.sprite.collide_rect(sprite, dragger):
									sprite.position[0] = 0
									sprite.position[1] = 600 - sprite.image.get_height()
									sprite.update(pygame, screen, background, deltaTime)
									if (len(repositioned) <= 1):
										repositioned.append(sprite)
										break
									break
						if (len(repositioned) > 1):
							if pygame.sprite.collide_rect(sprite, repositioned[0]):
								# for sprite in repositioned:
									sprite.position[0] += repositioned[-1].rect.right
									repositioned.append(sprite)
									dragger = None
									break
									
					dragger = None
					
			elif event.type == pygame.MOUSEMOTION:
				mouse_pos = event.pos
		
		#render
		pygame.display.flip()
	
	pygame.display.quit()
	return 0

if (__name__ == "__main__"):
	arguments = sys.argv
	pygame = importlib.import_module("pygame")
	run(pygame, arguments)
