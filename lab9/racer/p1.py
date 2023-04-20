import pygame
import random
import sys
import time

pygame.init()

FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5  # размер шагов
ENEMTY_STEP = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCORE = 0

clock = pygame.time.Clock()

score_font = pygame.font.SysFont("verdana", 20)  # шрифт

SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

wasted = pygame.image.load('images/wasted.jpg')
wasted = pygame.transform.scale(wasted, (400, 600))

bg = pygame.image.load("images/AnimatedStreet.png") # изображение дороги

pygame.mixer.music.load('sounds/background.wav')
pygame.mixer.music.play(-1)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):   # Класс Enemy представляет вражеские автомобили, которые движутся вниз по экрану
        super().__init__()
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self):  # создает "нового" врага когда он переходит границы
        self.rect.move_ip(0, ENEMTY_STEP)
        if (self.rect.bottom > SCREEN_HEIGHT):
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):  # движение нашей машины
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/coin.png")
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self):  # если монета переходит границы, дает ей новую позицию сверху("создает новую")
        self.rect.move_ip(0, 5)
        if (self.rect.bottom > SCREEN_HEIGHT):
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def spawn(self):  # дает случайную позицю сверху
        self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


P1 = Player()
E1 = Enemy()
C1 = Coin()
enemies = pygame.sprite.Group()
enemies.add(E1)
coin = pygame.sprite.Group()
coin.add(C1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    C1.update()
    E1.update()

    if pygame.sprite.spritecollideany(P1, enemies):  # если игрок коснется врага
        pygame.mixer.music.load('sounds/crash.wav')
        pygame.mixer.music.play()

        SURF.blit(wasted, (0, 0))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P1, coin):  # если игрок коснется монету
        SCORE += 1
        ENEMTY_STEP += 0.5
        C1.spawn()  # задает новую позицию

    SURF.blit(bg, (0, 0))

    E1.draw(SURF)
    C1.draw(SURF)
    P1.draw(SURF)

    score_img = score_font.render(str(SCORE), True, BLACK)
    SURF.blit(score_img, (10, 10))

    pygame.display.update()
    clock.tick(FPS)