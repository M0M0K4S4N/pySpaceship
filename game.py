import random, pygame
from pygame.locals import *


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer

        self.image = pygame.image.load('img/ship.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.25)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer

        self.loaded_image = pygame.image.load('img/asteroid.png')
        self.initialize()

    def update(self):
        self.rect = self.rect.move((-self.speed, 0))
        if self.rect.center[0] < -10:
            self.initialize()

    def initialize(self):
        self.size = random.uniform(0.2, 0.7)
        self.image = self.loaded_image.convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, self.size)

        self.rect = self.image.get_rect()

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.center = random.randint(900, 1500), random.randint(-100, 900)
        self.speed = random.randint(1, 10)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Spaceship')

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    ship = Ship()
    asteroid = []
    for i in range(10):
        asteroid.append(Asteroid())
    allsprites = pygame.sprite.RenderPlain(ship, asteroid)
    going = True

    while going:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False

        allsprites.update()

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
