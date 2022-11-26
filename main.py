import pygame as p


# Initializing pygame
p.init()


# Declaring global constants - Making our dimension for the game
WIDTH, HEIGHT = 800, 500
win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Hangman Game!")


# Load images
images = []
for i in range(7):
    image = p.image.load("images/hangman" + str(i) + ".png")
    images.append(image)


# Game variables
hangman_status = 0

# colors
WHITE = (255, 255, 255)

# Set up game loop
# Defining our speed
FPS = 60
clock = p.time.Clock()


# Running the clock 
run = True
while run:
    clock.tick(FPS)

    # Making the background and update the display
    win.fill(WHITE)
    win.blit(images[hangman_status], (150, 100)) # Override the surface
    p.display.update()

    # If someone clicks the red button, it closes
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    # Get position of the mouse
        elif event.type == p.MOUSEBUTTONDOWN:
            pos = p.mouse.get_pos()
            run = print(pos)
        


p.quit()
