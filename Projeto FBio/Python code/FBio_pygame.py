import pygame
from sys import exit
from random import randint


pygame.init()
screen = pygame.display.set_mode((800,400)) #(largura, altura)
pygame.display.set_caption('Jetpack Trip') #nome do jogo
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = True

score = 0


#-----------Game aspect------------------------

sky_surface = pygame.Surface((800,300))
sky_surface.fill('cadetblue1')

ground_surface = pygame.Surface((800,50))
ground_surface.fill('chocolate4')

ceiling_surface = pygame.Surface((800,50))
ceiling_surface.fill('gray')

grass_surface = pygame.Surface((800,10))
grass_surface.fill('chartreuse3')

text_suface = test_font.render('Jetpack Trip', False, 'Black')

score_surface = test_font.render(str(score), False, 'Black')


#-------------Enemys----------------------------

enemy_surface = pygame.Surface((50,50))
enemy_rect = enemy_surface.get_rect(topleft = (1200,300))

enemy2_surface = pygame.Surface((50,50))
#enemy2_surface = pygame.image.load('C:\\Users\\Maria (escola)\\Documents\\Python\\Projeto FBio\\Imagens\\saw-blade.png').convert()
enemy2_rect = enemy2_surface.get_rect(topleft = (800,200))
down2 = True

enemy3_surface = pygame.Surface((50,50))
enemy3_rect = enemy3_surface.get_rect(topleft = (1800,150))


#-------------Coins----------------------------
coin_surface = pygame.Surface((30, 30))
coin_surface.fill('chartreuse3')
coin_rect = coin_surface.get_rect(topleft = (1000, 200))


#-------------Players--------------------------

player_surface = pygame.Surface((50,80))
player_surface.fill('lightgoldenrod1')
player_rect = player_surface.get_rect(topleft = (20, 270))

jetpack_active = False
player_velocity = 0
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jetpack_active = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jetpack_active = False
            

    if game_active:
        screen.blit(sky_surface,(0,50))
        screen.blit(ground_surface,(0,350))
        screen.blit(ceiling_surface,(0,0))
        screen.blit(grass_surface,(0,350))
        screen.blit(text_suface,(300,10))
        screen.blit(score_surface,(100,10))

        enemy_rect.x -= 3
        if enemy_rect.right <= 0:
            enemy_rect.left = 1000
        screen.blit(enemy_surface,enemy_rect)

        enemy2_rect.x -= 3
        if enemy2_rect.x < -100:
            enemy2_rect.x = 1200
        if enemy2_rect.y >= 300:
            down2 = False
        if enemy2_rect.y <= 100:
            down2 = True
        if down2:
            enemy2_rect.y += 1
        else:
            enemy2_rect.y -= 1
        screen.blit(enemy2_surface,enemy2_rect)

        enemy3_rect.x -= 3
        if enemy3_rect.right <= 0:
            enemy3_rect.left = 2000
        screen.blit(enemy3_surface,enemy3_rect)

        coin_rect.x -= 3
        if coin_rect.right <= 0:
                coin_rect.x = 1000
        screen.blit(coin_surface, coin_rect)



        if jetpack_active:
            player_velocity = -3
        else:
            player_velocity += 0.5

        player_rect.y += player_velocity

        if player_rect.bottom >= 350:
            player_rect.bottom = 350
        if player_rect.top <= 50:
            player_rect.top = 50

        screen.blit(player_surface,(player_rect))

        if coin_rect.colliderect(player_rect):
            score += 1
            score_surface = test_font.render(str(score), False, 'Black')
            coin_rect.x = 1000
            if score == 25:
                game_active = False

        if enemy_rect.colliderect(player_rect) or enemy2_rect.colliderect(player_rect) or enemy3_rect.colliderect(player_rect):
            game_active = False
            
    else:
        screen.fill('yellow')
        if score < 25:
            score_surface = test_font.render(str(score), False, 'Black')
        else:
            score_surface = test_font.render('WINNER!', False, 'Black')
        screen.blit(score_surface,(350,150))
        #fazer aqui pontuações de 4 jogadores


    pygame.display.update()
    clock.tick(60)

    

        