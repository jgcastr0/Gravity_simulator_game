import pygame
import math

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 500, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulação de gravidade")

# Configurações de cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Classe para as esferas (átomos)
class Sphere:
    def __init__(self, x, y, mass, fixed=False):
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = mass  # Vamos usar a massa como o raio para simplificação
        self.vx = 0
        self.vy = 0
        self.fixed = fixed  # Se a esfera é fixa ou não

    def draw(self, screen):
        color = YELLOW if self.fixed else WHITE
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), int(self.radius))

    def update(self, central_spheres):
        if not self.fixed:
            # Constante gravitacional (ajustável para a simulação)
            G = 3
            fx = 0
            fy = 0
            for central_sphere in central_spheres:
                dx = central_sphere.x - self.x
                dy = central_sphere.y - self.y
                dist = math.hypot(dx, dy)
                if dist > 0:
                    force = G * self.mass * central_sphere.mass / dist**2
                    fx += force * dx / dist
                    fy += force * dy / dist

            self.vx += fx / self.mass
            self.vy += fy / self.mass
            self.x += self.vx
            self.y += self.vy

# Função principal
def main():
    clock = pygame.time.Clock()
    central_spheres = []
    particles = []
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if event.button == 3:  # Botão direito do mouse
                    central_spheres.append(Sphere(x, y, 20, fixed=True))

        # Adicionar partículas ao segurar o botão do mouse
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            particles.append(Sphere(x, y, 3))

        screen.fill(BLACK)

        for central_sphere in central_spheres:
            central_sphere.draw(screen)
        
        for particle in particles:
            particle.update(central_spheres)
            particle.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
