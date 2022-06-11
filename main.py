import pygame
pygame.init()#程式初始化
screen = pygame.display.set_mode((500,600))#螢幕顯示
running = True
while running:
    for event in pygame.event.get():#取得玩家輸入
        if event.type == pygame.QUIT:
            running = False#跳出迴圈

pygame.quit()