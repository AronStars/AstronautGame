import pygame

pygame.init()
scrn = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

#player size, player x and y, player speed
Psize = 20
Px, Py = 300 - (Psize / 2), 200 - (Psize / 2)
speed = 5

#falling/jumping variables
verticalchange = 0

fallspeed = 0.5
maxfallspeed = Psize

jumping = False
jumpspeed = 3
maxjumpspeed = jumpspeed
minjumpspeed = fallspeed

#tilemap stored in 2D array
grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

#converting tilemap into an array of rect objects
blocksize = Psize * 2
blocks = []
for y, row in enumerate(grid):
    for x, space in enumerate(row):
        if row[x] == 1:
            blocks.append(pygame.Rect(x * blocksize, y * blocksize, blocksize, blocksize))

#gameloop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #movement
    keys = pygame.key.get_pressed()
    #move left
    if keys[pygame.K_LEFT]:
        move = True
        for block in blocks:
            if pygame.Rect(Px - speed, Py, Psize, Psize).colliderect(block):
                move = False
        if move == True:
            for x, block in enumerate(blocks):
                blocks.pop(x)
                blocks.insert(x, pygame.Rect.move(block, speed, 0))
    
    #move right
    if keys[pygame.K_RIGHT]:
        move = True
        for block in blocks:
            if pygame.Rect(Px + speed, Py, Psize, Psize).colliderect(block):
                move = False
        if move == True:
            for x, block in enumerate(blocks):
                blocks.pop(x)
                blocks.insert(x, pygame.Rect.move(block, -speed, 0))
                
    #falling and jumping
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
        #swap the line above with the 3 lines of code below this to add vertical camera movement
        #for x, block in enumerate(blocks):
            #blocks.pop(x)
            #blocks.insert(x, pygame.Rect.move(block, 0, -verticalchange))
        
    #updating the player each frame
    player = pygame.Rect(Px, Py, Psize, Psize)
    
    #displaying the game
    scrn.fill("black")
    pygame.draw.rect(scrn, "yellow", player)
    for block in blocks:
        pygame.draw.rect(scrn, "blue", block)
    pygame.display.flip()
    
    #capping the frame rate at 60
    clock.tick(60)
    
pygame.quit()
