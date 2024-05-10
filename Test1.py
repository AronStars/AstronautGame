import 

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

def displayImage(astro, loc, counter, orientation):
    if counter % 2 == 0:
        counter += 1
        print(counter)
        return dis.blit(orientation, loc)
    else:
        counter += 1
        if astro == "astroleft":
            print("walkright")
            orientation = "astrowalkleft"
            return dis.blit(orientation, loc)
        else:
            print("walkleft")
            orientation = "astrowalkright"
            return dis.blit(orientation, loc)
        

def displayMessage(msg, loc, colour=(0, 0, 0)):
    dis.blit(comicSans.render(msg, True, colour), loc)

inviswall = pygame.Rect(0, 700, 1000, 1)  # Update the dimensions of the invisible wall

pos = [500, 350]
clock = pygame.time.Clock()
astronaut = createImage(orientation + ".png", [500, 500])
astronaut.get_rect(center=(500, 350))


game_over = False
target = False

# Variables to track key states
move_up = False
move_down = False
move_left = False
move_right = False

while not game_over:
    dis.fill(black)
    x_mouse, y_mouse = pygame.mouse.get_pos()
    displayImage(astronaut, pos, counter, orientation)
    counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_s:
                move_down = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False

    #if astronaut.colliderect(inviswall):
        #move_up = False
        #move_down = False
        #move_left = False
        #move_right = False
    #else:
        if move_up:
            pos[1] -= 10
        if move_down:
            pos[1] += 10
        if move_left:
            pos[0] -= 10
            orientation = "astroleft"
        if move_right:
            pos[0] += 10
            orientation = "astroright"

    clock.tick(30)
    pygame.display.update()

pygame.quit()
quit()
