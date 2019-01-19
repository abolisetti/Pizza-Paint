import pygame
import sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Flood Fill")

px = pygame.PixelArray(screen)

colours = {"w": 0xFFFFFF, "r": 0xFF0000, "g": 0x00FF00, "b": 0x0000FF, "y": 0xFFFF00, "p": 0xFF00FF}
colour = colours["w"]

class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def flood_fill(node, replacement_colour):
	current_colour = screen.get_at((x, y))

	q = []
	q.append(node)
	while q:
		n = q.pop()
		if screen.get_at((n.x, n.y)) == current_colour:
			px[n.x, n.y] = replacement_colour
			if n.x - 1 >= 0 and n.y - 1 >= 0 and n.x + 1 < 200 and n.y + 1 < 200:
				q += [Node(n.x-1, n.y), Node(n.x+1, n.y), Node(n.x, n.y-1), Node(n.x, n.y+1)]


middle_down = False
while True:
	if middle_down:
		x, y = pygame.mouse.get_pos()
		px[x, y] = 0x00FF00

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit(0)
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit(0)
			elif chr(event.key) in colours:
				colour = colours[chr(event.key)]
		elif event.type == MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			if event.button == 1:
				flood_fill(Node(x, y), colour)
			elif event.button == 2:
				middle_down = True
		elif event.type == MOUSEBUTTONUP:
			if event.button == 2:
				middle_down = False

	pygame.display.update()
	fpsClock.tick(60)
