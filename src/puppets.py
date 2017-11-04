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
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
WHITE = (255, 255, 255)

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

def draw_puppet( index, screen, x, y, mouth_open, eyes_direction_x, eyes_direction_y):
	
	PUPPET_COLOUR_FACE = RED
	PUPPET_COLOUR_NOSE = GREEN

	if index == 1:
		# 2nd puppet
		PUPPET_COLOUR_FACE = BLUE
		PUPPET_COLOUR_NOSE = YELLOW

	# face (/main rectangle)
	PUPPET_RADIUS = 80
	PUPPET_DIAMETER = 2 * PUPPET_RADIUS

	pygame.draw.rect(screen, PUPPET_COLOUR_FACE, [x-PUPPET_RADIUS, y-PUPPET_RADIUS, PUPPET_DIAMETER, PUPPET_DIAMETER])

	# nose
	PUPPET_NOSE_WIDTH = 20
	PUPPET_NOSE_HEIGHT = 40

	pygame.draw.rect(screen, PUPPET_COLOUR_NOSE, [x-(PUPPET_NOSE_WIDTH/2),y-(PUPPET_NOSE_HEIGHT/2), PUPPET_NOSE_WIDTH, PUPPET_NOSE_HEIGHT])

	# mouth
	mouth_x = x
	mouth_y = y + 40

	PUPPET_MOUTH_WIDTH = 100
	PUPPET_MOUTH_HEIGHT = int(60 * mouth_open)

	pygame.draw.rect(screen, BLACK, [mouth_x - (PUPPET_MOUTH_WIDTH/2), mouth_y - (PUPPET_MOUTH_HEIGHT/2), PUPPET_MOUTH_WIDTH, PUPPET_MOUTH_HEIGHT])

	# eyes
	for eye_index in range(2):
		PUPPET_EYE_RADIUS = 20
		PUPPET_EYE_DIAMETER = 2 * PUPPET_EYE_RADIUS

		eye_x = x + (( (eye_index*2)-1) * 40)
		eye_y = y - 40

		pygame.draw.rect(screen, WHITE, [eye_x-PUPPET_EYE_RADIUS,eye_y-PUPPET_EYE_RADIUS,PUPPET_EYE_DIAMETER, PUPPET_EYE_DIAMETER])

		PUPPET_EYE_DOT_WIDTH = 20
		PUPPET_EYE_DOT_HEIGHT = 30

		eye_dot_x = eye_x + clamp(40 * eyes_direction_x, -20, 20)
		eye_dot_y = eye_y + clamp(40 * eyes_direction_y, -20, 20)

		pygame.draw.rect(screen, BLACK, [eye_dot_x-PUPPET_EYE_DOT_WIDTH/2, eye_dot_y-PUPPET_EYE_DOT_HEIGHT/2, PUPPET_EYE_DOT_WIDTH, PUPPET_EYE_DOT_HEIGHT])




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

	# render a puppet for each hand
	for index, hand in enumerate(hands):
		g = hand.grab_strength		#	0.0 -> 1.0
		g = clamp(g, 0.1, 1.0)
		inv_g = 1 - g

		wrist = hand.wrist_position
		direction = hand.direction

		# mouth_open: 0 = closed, 1 = open
		mouth_open = inv_g

		# eyes_direction_x: -1 = left, 0 = straight ahead, 1 = right
		eyes_direction_x = clamp(direction.x, -1, 1)

		# eyes_direction_y: -1 = up, 0 = straight ahead, 1 = down
		eyes_direction_y = 1 - clamp(direction.y, -1, 1)

		x = (index+1) * 300
		y = 500 - clamp( int(wrist.y), 0, 400 )

		draw_puppet( index, screen, x, y, mouth_open, eyes_direction_x, eyes_direction_y )

	# flip the backbuffer to the front buffer
	pygame.display.flip()

pygame.quit()

