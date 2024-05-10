import pygame, time

# FINAL BOSS MUST BE WARING

pygame.init()
dis = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Untitled space game 1')

pygame.font.init()
comicSans = pygame.font.SysFont('Comic Sans MS', 15)

blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
orientation = "astroright"
global counter
counter = 0

def createImage(image, size):
    imp = pygame.image.load(image)
    imp = pygame.transform.scale(imp, size)
    return imp

def displayMessage(msg, loc, colour=(0, 0, 0)):
    dis.blit(comicSans.render(msg, True, colour), loc)

pos = [500, 350]
velocity = [0, 0]
gravity = 0.5
jump_power = 10  # Increased jump power
acceleration = 0.8
friction = 0.2  
max_speed = 50

clock = pygame.time.Clock()

game_over = False
target = False

move_up = False
move_down = False
move_left = False
move_right = False

while not game_over:
    dis.fill(black)
    x_mouse, y_mouse = pygame.mouse.get_pos()
    counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if not move_down and not move_up: 
                    move_up = True
                    starttime = time.time()
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_up = False
                move_down = True  
            if event.key == pygame.K_s:
                move_down = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
    if move_up:
        elapsedtime = time.time() - starttime
        if elapsedtime > 0.5:  # Delay before resetting the move_up flag
            move_up = False
        else:
            velocity[1] -= jump_power
    if move_down:
        velocity[1] += acceleration
    velocity[1] += gravity # Add gravity to the velocity
    if move_left:
        velocity[0] -= acceleration
        orientation = "astroleft"
    if move_right:
        velocity[0] += acceleration
        orientation = "astroright" # Change the orientation of the astronaut
    velocity[0] *= (1 - friction)
    velocity[1] *= (1 - friction)
    velocity[0] = min(max_speed, max(-max_speed, velocity[0]))
    velocity[1] = min(max_speed, max(-max_speed, velocity[1]))
    pos[0] += velocity[0]
    pos[1] += velocity[1] # Calculate the new position of the astronaut
    astronaut = createImage(orientation + ".png", [300, 300])
    astronaut_rect = astronaut.get_rect(center=(pos[0], pos[1]))
    if pos[1] >= 700:
        velocity[1] = 0
        pos[1] = 700
        move_down = False 
    dis.blit(astronaut, astronaut_rect)
    clock.tick(60)
    pygame.display.update()

pygame.quit()
quit()
