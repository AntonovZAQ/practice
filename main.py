import pygame
import random

clock =  pygame.time.Clock()
pygame.init()
screen =  pygame.display.set_mode((1080, 608))
pygame. display.set_caption("GamePractice")
icon =  pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)

# player
bg =  pygame.image.load('images/bg.png').convert_alpha()

walk_left = [
    pygame.image.load('images/player_left/left_1.png').convert_alpha(),
    pygame.image.load('images/player_left/left_2.png').convert_alpha(),
    pygame.image.load('images/player_left/left_3.png').convert_alpha(),
    pygame.image.load('images/player_left/left_4.png').convert_alpha(),
    pygame.image.load('images/player_left/left_5.png').convert_alpha(),
    pygame.image.load('images/player_left/left_6.png').convert_alpha(),

] 
walk_right = [
    pygame.image.load('images/player_right/right_1.png').convert_alpha(),
    pygame.image.load('images/player_right/right_2.png').convert_alpha(),
    pygame.image.load('images/player_right/right_3.png').convert_alpha(),
    pygame.image.load('images/player_right/right_4.png').convert_alpha(),
    pygame.image.load('images/player_right/right_5.png').convert_alpha(),
    pygame.image.load('images/player_right/right_6.png').convert_alpha(),
   
] 



#rock

rock = pygame.image.load('images/rock.png').convert_alpha()

rock_x = 50
rock_y = 320
rock_timer = pygame.USEREVENT + 1 
pygame.time.set_timer(rock_timer, 5000)
rock_list_in_game = []




gameplay = True

player_anim_count = 0
bg_x = 0

player_speed = 25
player_x = 50
player_y = 320

is_jump = False
jump_count = 10
# экран Проигрыша
label = pygame.font.Font('fonts/Oswald-Bold.ttf', 40)
lose_label = label.render('ВЫ ПРОИГРАЛИ!', False, (193, 196, 199))
restart_label = label.render('Играть заново', False, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft=(420,250))
 
score = 0
jumps = 0


def display_score():
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score) + " Jumps: " + str(jumps), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

gameplay = True
running = True
while True: 
    
    
    #фоновое изображение 
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x+1080, 0))
    
    # рандом камней
    

    # экран проигрыша
    if gameplay:


        player_rect = walk_left[0].get_rect(topleft=(player_x,player_y))
        
        if rock_list_in_game:
            for (i, el) in enumerate (rock_list_in_game):
                screen.blit(rock, el)
                el.x -= 10
                
                if el.x < -10: 
                    rock_list_in_game.pop(i)

                    score += 20
                    jumps += 1
                    


                if player_rect.colliderect(el):
                    gameplay = False
      

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x,  player_y))
        else: 
            screen.blit(walk_right[player_anim_count], (player_x,  player_y))




        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 675:
            player_x += player_speed

        if not is_jump:                                         #Прыжок
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -10:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10


        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -1080: 
            bg_x = 0

    else:
        screen.fill((87, 88, 90))
        screen.blit(lose_label, (400,190))
        screen.blit(restart_label, restart_label_rect)
  
        
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 50
            rock_list_in_game.clear()
            score = 0
            jumps = 0
            
   
    display_score()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            pygame.quit()

        if event.type == rock_timer:
            rock_list_in_game.append(rock.get_rect(topleft=(1000,350)))

  

    clock.tick(20)
