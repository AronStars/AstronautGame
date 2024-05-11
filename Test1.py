import pygame, time

# FINAL BOSS MUST BE WARING
#test

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
gravity = 20
jump_power = 100
acceleration = 20
friction = 0.2  
max_speed = 100
jump_acceleration = 20
jump_deceleration = 10

clock = pygame.time.Clock()

game_over = False
target = true

player_state = {
    "move_up": False,
    "move_down": False,
    "move_left": False,
    "move_right": False
}

astronaut = createImage(orientation + ".png", [300, 300])
astronaut_rect = astronaut.get_rect(center=(pos[0], pos[1]))

while not game_over:
    dis.fill(black)
    x_mouse, y_mouse = pygame.mouse.get_pos()
    counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if not player_state["move_down"] and not player_state["move_up"]: 
                    player_state["move_up"] = True
                    starttime = time.time()
            if event.key == pygame.K_a:
                player_state["move_left"] = True
            if event.key == pygame.K_d:
                player_state["move_right"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_state["move_up"] = False
                player_state["move_down"] = True  
            if event.key == pygame.K_s:
                player_state["move_down"] = False
            if event.key == pygame.K_a:
                player_state["move_left"] = False
            if event.key == pygame.K_d:
                player_state["move_right"] = False
    
    if player_state["move_up"]:
        elapsedtime = time.time() - starttime
        if elapsedtime > 0.5: 
            player_state["move_up"] = False
        else:
            velocity[1] -= jump_power
            velocity[1] -= jump_acceleration
    else:
        player_state["move_down"] = True
    
    if player_state["move_down"]:
        velocity[1] += acceleration
    
    velocity[1] += gravity
    
    if player_state["move_left"]:
        velocity[0] -= acceleration
        orientation = "astroleft"
    
    if player_state["move_right"]:
        velocity[0] += acceleration
        orientation = "astroright"  
    
    velocity[0] *= (1 - friction)
    velocity[1] *= (1 - friction)
    velocity[0] = min(max_speed, max(-max_speed, velocity[0]))
    velocity[1] = min(max_speed, max(-max_speed, velocity[1]))
    
    dt = clock.tick(60) / 1000.0 
    
    pos[0] += velocity[0] * dt
    pos[1] += velocity[1] * dt  
    
    if pos[1] >= 600:
        velocity[1] = 0
        pos[1] = 600
        player_state["move_down"] = False 
    
    astronaut_rect.center = (pos[0], pos[1])
    
    dis.blit(astronaut, astronaut_rect)
    pygame.display.update()

pygame.quit()
quit()