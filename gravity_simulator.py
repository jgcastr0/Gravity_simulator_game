import pygame


# Initializing Pygame
pygame.init()

# Screen settings
width, height = 700, 600    
screen = pygame.display.set_mode((width, height))

# Clock object to control FPS rate
clock = pygame.time.Clock()
fps = 60

class Universe:
    def __init__(self):
        # Colors
        self.BACKGROUND_COLOR:tuple = (0, 0, 0)

class Particle:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
        self.size = self.mass * 10
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def desenhar(self, tela):
        pygame.draw.circle(tela, self.color, (self.x, self.y), self.size)


def main():

    # Main loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        # Fill the screen with a color
        screen.fill(self.BACKGROUND_COLOR)

        # Updates the display
        pygame.display.flip()
        
        # FPS rate
        clock.tick(fps)


if __name__ == '__main__':
    main()
