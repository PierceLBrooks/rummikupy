
# Author: Pierce Brooks

from PIL import Image
import util

def makeGrid(pygame, width, height, widthGrid, heightGrid):
	name = "grid.png"
	image = Image.new("RGBA", (width, height), "black")
	pixels = image.load()
	other = None
	current = None
	for x in range(width):
		for y in range(height):
			check = False
			current = []
			current.append(int((float(x)/float(width))*float(widthGrid)))
			current.append(int((float(y)/float(height))*float(heightGrid)))
			for i in range(3):
				for j in range(3):
					other = []
					other.append(i-1)
					other.append(j-1)
					if not ((other[0] == 0) and (other[1] == 0)):
						other[0] = int((float(x+other[0])/float(width))*float(widthGrid))
						other[1] = int((float(y+other[1])/float(height))*float(heightGrid))
						if not ((other[0] == current[0]) and (other[1] == current[1])):
							check = True
							break
				if (check):
					break
			if (check):
				pixel = list(pixels[x, y])
				length = len(pixel)
				for i in range(length):
					if (i == length-1):
						break
					pixel[i] = 255-pixel[i]
				pixels[x, y] = tuple(pixel)
	image.save(name)
	return util.loadImage(pygame, name)
