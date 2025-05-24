import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Flappy Bird")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Bird parameters
bird_x = 50
bird_y = height // 2
bird_speed_x = 0
bird_speed_y = 0
bird_size = 30
bird_width = 50
bird_height = 30

# Pipes
pipes = []
pipe_width = 10
pipe_height = 10
pipe_spacing = 20

# Game over condition
game_over = False

# Function to draw the bird
def draw_bird():
    pygame.draw.rect(screen, green, (bird_x, bird_y, bird_width, bird_height))

# Function to draw the pipes
def draw_pipes():
    for i in range(len(pipes)):
        pygame.draw.rect(screen, blue, (pipes[i][0], pipes[i][1], pipe_width, pipe_height))

# Function to handle bird movement
def move_bird():
    global bird_x, bird_y
    bird_x += bird_speed_x
    bird_y += bird_speed_y

    # Keep bird within bounds
    if bird_x < 0:
        bird_x = 0
    elif bird_x > width:
        bird_x = width - bird_width
    
    # Keep bird within bounds
    if bird_y < 0:
        bird_y = 0
    elif bird_y > height - bird_height:
        bird_y = height - bird_height

# Function to handle pipe movement
def move_pipes():
    global pipes
    for i in range(len(pipes)):
        pipes[i][1] -= 1  # Move pipes to the left
        if pipes[i][1] < 0:
            pipes[i][1] = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                move_bird()

    # Game logic
    if not game_over:
        # Update game state
        move_bird()
        move_pipes()

    # Draw everything
    screen.fill(white)  # Clear the screen
    draw_bird()
    draw_pipes()
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()