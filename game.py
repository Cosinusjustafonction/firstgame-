import pygame
from random import randrange
import math
pygame.init()
white = (255, 255, 255)
red = (139, 0, 0)
screen = pygame.display.set_mode((800, 800))
floor = pygame.image.load("floor.png").convert_alpha()
clock = pygame.time.Clock()
blue = (135, 206, 250)

font = pygame.font.Font('freesansbold.ttf',32)

font = pygame.font.Font('freesansbold.ttf',32)

#def create_cube(x, y) :
	#cube = pygame.draw.rect(screen, red, (x, y, 50, 50))
	#return cube
def gameLoop() :
	over = False
	running = False
	obs_x = 900
	obs2_x = 1300
	collision = False
	x_cube = 150
	y_cube = 450
	cubey_change = 0
	gravity = 0.3
	obs_y = randrange(350, 430)
	obs_x = 900
	obs2_x = 1300
	obs2_y = randrange(350, 430)
	x_floor = 0
	y_floor = 500
	floor_change = 3
	player_rect = pygame.Rect(x_cube, y_cube, 100, 100)
	def draw_floor() :
		screen.blit(floor, (x_floor, y_floor))
		screen.blit(floor, (x_floor + 800, y_floor))
	while  running == False :
		clock.tick(184)
		while over == True :
			screen.fill(white)
			x_cube = 2000
			x_floor = 2000
			obs_x = 1300
			obs2_x = 1300
			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					running = False
					pygame.quit()
				if event.type == pygame.KEYDOWN :
					if event.key == pygame.K_r :
						gameLoop()
					if event.key == pygame.K_i :
						running = False
						pygame.quit()

			pygame.display.update()


		screen.fill(white)
		#creat_obstacle(obs_x, obs_y)
		#creat_obstacle2(obs2_x, obs2_y)
		obstcle_1 = pygame.draw.rect(screen, blue, (obs_x, obs_y, 50, 400))
		obstcle_2 = pygame.draw.rect(screen, blue, (obs2_x, obs2_y, 50, 400))
		diff = obs2_x - obs_x
		cubey_change += gravity
		y_cube += cubey_change
		x_floor -= floor_change
		obs_x -= 3
		obs2_x -= 3

		if obs_x < -50 :
			obs_y = randrange(350, 430)
			obs_x = 900
		if obs2_x < -50 :
			obs2_y = randrange(350, 430)
			obs2_x =     1300
		if x_floor <= -800 :
			x_floor = 0
		draw_floor()
		if y_cube >= 450 :
			y_cube = 450

		if y_cube == 450 :
			jump = True
		if y_cube != 450 :
			jump = False

		if diff > 400 :
			obs2_x = 1300
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				running = True
				pygame.quit()
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_SPACE :
					if jump :
						cubey_change = 0
						cubey_change -= 12
					print('hola')

		#create_cube(x_cube, y_cube)
		cube = pygame.draw.rect(screen, red, (x_cube, y_cube, 50, 50))
		if cube.colliderect(obstcle_1) :
			over = True
		if cube.colliderect(obstcle_2) :
			over = True

		pygame.display.update()




gameLoop()
