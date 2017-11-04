import sys
sys.path.insert(0, "../lib")
import Leap
import math

import pygame
from pygame.locals import *

# useful constants
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# initialise leap motion
controller = Leap.Controller()

# initialise pygame
pygame.init()

# initialise the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
pygame.display.set_caption("sock puppets!")

# initialise the clock
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30

def on_event_key( event ):
	print "on_event_key: " + str(event)

def clamp( value, min_value, max_value ):
	return min( max_value, max( min_value, value) )

done = False
while not done:
	# control framerate
	clock.tick(FRAMES_PER_SECOND)

	# handle input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif not hasattr(event, 'key'):
			# ignore anything that is not a key press
			continue
		else:
			on_event_key( event )

	# update leap motion
	frame = controller.frame()
	hands = frame.hands

	# clear the backbuffer
	screen.fill(BLACK)
	
	# render to the backbuffer
	#pygame.draw.rect(screen, RED, [10,10,30,20])
	#pygame.draw.ellipse(screen, BLUE, [10,40,40,60])

	for index, hand in enumerate(hands):
		g = hand.grab_strength		#	0.0 -> 1.0
		g = clamp(g, 0.1, 1.0)
		inv_g = 1 - g

		wrist = hand.wrist_position
		direction = hand.direction

		max_radius = 40

		# left/right turn - by just using x component
		x_turn = clamp(int(100*direction.x), -50, 50)

		# left/right turn - by measuring angle on xz plane from 0,0,1
		# note: need to sort out the math here..
		#cos_angle = Leap.Vector(0,0,-1).dot( Leap.Vector(direction.x, 0, direction.y))
		#angle = math.acos(cos_angle)
		#x_turn = max(-50, min(50, int(angle * 100)))

		pygame.draw.circle(screen, RED, [(index+1)*300 + x_turn, 500 - int(wrist.y)], int(max_radius * inv_g))

	# flip the backbuffer to the front buffer
	pygame.display.flip()

pygame.quit()

