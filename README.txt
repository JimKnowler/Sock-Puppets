Sock Puppets
==============================================

A quick hack to enjoy playing with PyGame and LeapMotion at HackHorsham Nov 2017

REQUIREMENTS
==============================================

- Windows

- Python2.7

- PyGame

- LeapMotion Controller

- LeapMotion Python SDK 3.2 (Orion)
  https://developer.leapmotion.com/documentation/python/index.html

Getting Started
==============================================

- connect + activate your LeapMotion controller

- start the main python script
  xx/sock_puppets/src$ python puppets.py

- Up to two hands are detected
  - The first hand that the leap motion detects will drive the RED puppet on the left
  - The second hand that the leap motion detects will drive the GREEN puppet on the right

- Each puppet is controlled by your hand, as if you were controlling a sock puppet
  - Hold your fingers together, 
  - Raise your hand up/down to move your puppet up/down
  - turn your hand left/right/up/down to move your puppet's eyes left/right/up/down
  - each puppet makes a different sound effect when you open its' mouth fully


FUTURE IDEAS
================================================= 

- add hats to each puppet

- add tongue to each puppet

- particle effects
  - emitted from an open mouth

- speech bubbles 
  - created when mouth is opened
  - animate fading / rising away from puppet 

- improve the sounds played when opening mouths
  - set volume of sound, every frame, by how open the puppet's mouth is
  - play different / multiple sounds

- improve accuracy of eye tracking
  - do some 3D math to calculate pitch / yaw angles
  - support resetting the 'forward' direction that angles are calculated from

- record puppet movements to play back later

- 