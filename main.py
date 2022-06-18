import pygame
FPS = 60
WHITE = (255,255,255)
WIDTH = 600
HEIGHT = 700

pygame.init()#程式初始化
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))#螢幕顯示
pygame.display.set_caption("Ryan's game")
running = True

class Player(pygame.sprite.Sprite):#不懂
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 600
        self.speedx = 8
    def update(self):#
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx


all_sprites = pygame.sprite.Group()#
player = Player()#

all_sprites.add(player)#

while running:
    clock.tick(FPS)#不懂
    for event in pygame.event.get():#取得玩家輸入
        if event.type == pygame.QUIT:
            running = False#跳出迴圈

    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()