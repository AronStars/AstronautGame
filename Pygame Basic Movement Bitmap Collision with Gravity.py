import pygame

pygame.init()
scrn = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

#player size, playerx, playery, player speed
Psize = 20
Px, Py = 300 - (Psize / 2), 200 - (Psize / 2)
speed = 5

verticalchange = 0

fallspeed = 0.5
maxfallspeed = Psize

jumping = False
jumpspeed = 3
maxjumpspeed = jumpspeed
minjumpspeed = fallspeed

#bitmap stored in 2D array
grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,1,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

#converting bitmap into an array of rect objects
blocks = []
for y, row in enumerate(grid):
    for x, space in enumerate(row):
        if row[x] == 1:
            blocks.append(pygame.Rect(x * 40, y * 40, 40, 40))

#game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and Px - speed >= 0:
        move = True
        for block in blocks:
            if pygame.Rect(Px - speed, Py, Psize, Psize).colliderect(block):
                move = False
        if move == True:
            Px -= speed
            
    if keys[pygame.K_RIGHT] and Px + speed <= scrn.get_width() - Psize:
        move = True
        for block in blocks:
            if pygame.Rect(Px + speed, Py, Psize, Psize).colliderect(block):
                move = False
        if move == True:
            Px += speed
            
    #jumping and falling
    #falling
    falling = True
    for block in blocks:
        if pygame.Rect(Px, Py + verticalchange + 1, Psize, Psize).colliderect(block):
            falling = False
            verticalchange = 0

    if falling == True and fallspeed < maxfallspeed:
        verticalchange += fallspeed
        
    #jumping
    if keys[pygame.K_UP] and falling == False:
        jumping = True

    if jumping == True:
        verticalchange -= jumpspeed
        jumpspeed -= fallspeed
        if jumpspeed <= minjumpspeed:
            jumpspeed = maxjumpspeed
            jumping = False

    #moving the player vertically and managing vertical collision
    move = True
    for block in blocks:
        if pygame.Rect(Px, Py + verticalchange, Psize, Psize).colliderect(block):
            jumping = False
            move = False
    if move == True:
        Py += verticalchange
    
    #updating the player rect object each frame so that if Px or Py change it will me modified accordingly
    player = pygame.Rect(Px, Py, Psize, Psize)
    
    #displaying all
    scrn.fill("black")
    pygame.draw.rect(scrn, "green", player)
    for block in blocks:
        pygame.draw.rect(scrn, "red", block)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()