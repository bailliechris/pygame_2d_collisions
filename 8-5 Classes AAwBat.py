import pygame, random
 
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

sw = 900
sh = 650
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([sw, sh])
 
# This sets the name of the window
pygame.display.set_caption('Collisions with Multiple Objects')
 
clock = pygame.time.Clock()

cubeAmount = random.randrange(25,100)

# Set game variables
class cube():
    x = 250
    y = 250

    colour = [255, 255, 255]

    speedx = 0
    speedy = 0

    size = 5

    def physics(self):
        if self.y < 0 or self.y > sh:
            self.speedy = self.speedy * -1
        if self.x < 0 or self.x > sw:
            self.speedx = self.speedx * -1
        
    def move(self):
        self.x = self.x + self.speedx
        self.y = self.y + self.speedy

    def physicsBat(self, x, y, l, w):
        if self.x > x and self.x < (x + w):
            if self.y > y and self.y < (y + l):
                self.speedx = self.speedx * -1
                self.speedy = self.speedy * -1
        

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.size, self.size])

class bat():
    x = 300
    y = 300

    w = 200
    h = 200

    colour = [255, 255, 255]

    def move(self):
        pos = pygame.mouse.get_pos()
        self.x = pos[0]
        self.y = pos[1]

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.w, self.h])

#Create cube
cubeList = [ cube() for i in range(cubeAmount)]

bat1 = bat()

done = False

# Start program

for i in range(cubeAmount):
    cubeList[i].speedx = random.randrange(-10,10)
    cubeList[i].speedy = random.randrange(-10,10)
    cubeList[i].x = random.randrange(10,770)
    cubeList[i].y = random.randrange(10,570)
    cubeList[i].colour = [random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)]
    cubeList[i].size = random.randrange(4,20)
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
             
    # Clear screen
    screen.fill(BLACK)

    # Move Bat
    bat1.move()

    # Update cube
    for i in range(cubeAmount):
        cubeList[i].physics()
        cubeList[i].physicsBat(bat1.x, bat1.y, bat1.w, bat1.h)
        cubeList[i].move()
        cubeList[i].draw(screen)

    bat1.draw(screen)

    pygame.display.flip()
 
    clock.tick(30)
 
pygame.quit ()
