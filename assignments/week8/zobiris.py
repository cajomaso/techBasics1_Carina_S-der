import pygame
import random

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

Colours = [(250,0,50),#red
           (28,134,238),#blue
           (158,186,195),#silver
           (0,39,0)]#green

# Activate the pygame library
pygame.init()

# Create the display surface object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the pygame window name
pygame.display.set_caption('zobiris')

try:
    img = pygame.image.load("ruby.png").convert_alpha()
    img = pygame.transform.scale(img, (70, 100))
except:
    print("ruby not found")

try:
    img2 = pygame.image.load("zobiris.jpg").convert()
    img2 = pygame.transform.scale(img2, (1200, 700))
except:
    print("zobiris not found")


class Ruby:
    def __init__(self, positioning):
        self.original_image = img.copy()

        # Choose a random color and blend it onto the surface
        color_choosing = random.choice(Colours)
        self.original_image.fill(color_choosing, special_flags=pygame.BLEND_ADD)

        self.image = self.original_image
        self.positioning = positioning

        # different positions so the rubies dont lay over zobiris
        if positioning == "left":
            self.x = random.randint(0, 90)
            self.y = random.randint(0, SCREEN_HEIGHT - 100)
        elif positioning == "middle":
            self.x = random.randint(300, 450)
            self.y = random.randint(0, 300)
        elif positioning == "right":
            self.x = random.randint(1050, 1130)
            self.y = random.randint(0, SCREEN_HEIGHT - 100)
        else:
            print("Invalid positioning")

        # gemini helped with rotating
        # Store the center coordinate of the ruby to rotate around its own center pivot
        self.center = (self.x + 35, self.y + 50)  # half of width(70) and height(100)
        self.rect = self.image.get_rect(center=self.center)

        # SIMPLIFIED ROTATION PROPERTIES:
        # Start at a random angle between our wiggle limits
        self.max_angle = random.randint(20, 40)
        self.angle = random.randint(-self.max_angle, self.max_angle)

        # Determine rotation speed in degrees per frame
        self.speed = random.uniform(0.2, 1.0)
        self.direction = random.choice([-1, 1])  # -1 for clockwise, 1 for counter-clockwise

    def show(self):
        screen.blit(self.image, self.rect)

    def move(self):
        # 1. Update the angle by adding or subtracting the speed
        self.angle += self.speed * self.direction

        # 2. Reverse direction if the angle goes past the maximum limits
        if abs(self.angle) >= self.max_angle:
            self.direction *= -1

        # 3. Rotate the clean original image by our updated angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        # 4. Recalculate the bounding box (rect) to keep the rotated image perfectly centered
        self.rect = self.image.get_rect(center=self.center)


# Create a list to hold multiple instances of Ruby
rubies = []
num_rubies = random.randint(3, 7)

# Populate the ruby list across the different zones
for n in range(num_rubies):
    rubies.append(Ruby("left"))

for n in range(num_rubies):
    rubies.append(Ruby("middle"))

for n in range(num_rubies):
    rubies.append(Ruby("right"))

# Init the clock
clock = pygame.time.Clock()

flag = True
while flag:
    # Ticking the clock to run at 60 FPS
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    screen.blit(img2, (0, 0))

    for single_ruby in rubies:
        single_ruby.move()  # Calculate the new rotation
        single_ruby.show()  # Draw it centered

    pygame.display.flip()

pygame.quit()
exit(0)