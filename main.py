import pygame as p
import math


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


# Fonts
LETTER_FONT = p.font.SysFont('Arial', 15)

# Making the buttons using this eq: (width - (gap + radius * 2) * 13) // 2
RADIUS = 20
GAP = 15
letters = []
start_x = round((WIDTH - ((RADIUS * 2) + GAP) * 13) / 2)
start_y = 400
A = 65

for i in range(26):
    """
    i % 13 is to calculate the rows
    Each buttons distance = radius * 2 (Diameter) + Gap
    GAP * 2, gap between right and left side of the screen
    """
    x = start_x + (GAP * 2) + (((RADIUS * 2) + GAP) * (i % 13))

    """
    Integer division excludes the decimals, we are taking the whole number
    """
    y = start_y + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Game variables
hangman_status = 0

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up game loop
# Defining our speed
FPS = 60
clock = p.time.Clock()


# Draw function
def draw():
    # Making the background and update the display
    win.fill(WHITE)

    # Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        p.draw.circle(win, BLACK, (x, y), RADIUS, 3)
        text = LETTER_FONT.render(ltr, 1, BLACK)

        # Print the letters on the button and middle 
        win.blit(text, (x - text.get_width() / 1.5,y - text.get_width() / 1.5))

    win.blit(images[hangman_status], (150, 100)) # Override the surface
    p.display.update()

# Running the clock 
run = True
while run:
    clock.tick(FPS)

    draw()

    # If someone clicks the red button, it closes
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    # Get position of the mouse
        if event.type == p.MOUSEBUTTONDOWN:
            m_x, m_y = p.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                # The center of the button
                    distance = math.sqrt((x - m_x)**2 + (y-m_y)**2)
                    if distance < RADIUS:
                        letter[3] = False
        

p.quit()