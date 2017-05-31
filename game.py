import random, pygame
from pygame.locals import *


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer

        self.image = pygame.image.load('img/ship.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.15)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def collis(self, target):
        box = self.rect.inflate(-50, -100)
        return box.colliderect(target.rect)


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
        self.speed = random.randint(3, 10)


def displayText(displayText, wSize, background):
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render(displayText, 5, (255, 255, 255))
        textpos = text.get_rect(centerx=wSize[0] / 2, centery=wSize[1] / 2)
        background.blit(text, textpos)


def main():
    pygame.init()
    wSize = 800, 600
    screen = pygame.display.set_mode(wSize)
    pygame.display.set_caption('Spaceship')

    # background = pygame.Surface(screen.get_size())
    background = pygame.image.load('img/background.png').convert_alpha()

    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    ship = Ship()
    asteroid = []
    asteroid_count = 10
    for i in range(asteroid_count):
        asteroid.append(Asteroid())
    allsprites = pygame.sprite.RenderPlain(ship, asteroid)
    going = True
    over = False
    while going:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False
        print(screen)
        for i in range(asteroid_count):
            if ship.collis(asteroid[i]):
                over = True
                displayText("GAME OVER - Press Esc to quit.", wSize, background)


        if over != True: allsprites.update()

        screen.blit(background, (0, 0))
        if over != True:
            allsprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
