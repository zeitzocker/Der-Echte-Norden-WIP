import pygame                   # importiert das vorab installierte Paket pygame
import os
from sys import exit
from playerattributes import PlayerComplete
from enemyattributes import EnemyComplete

#################################################################################################################################################################################################
'General Settings'
#################################################################################################################################################################################################

working_dictionary = os.getcwd()
pygame.init()           # initialisiert das pygame modul, wird benoetigt um alle Bestandteile des pygame Packages zu nutzen
origin = 0
width_frame = 1280
height_frame = 720
gameRunning = True
screen = pygame.display.set_mode((width_frame, height_frame))
pygame.display.set_caption("Jelly Plague")
fps = 60
clock = pygame.time.Clock()
gameStart = True

#################################################################################################################################################################################################
'Surfaces and Images'
#################################################################################################################################################################################################
big_font = pygame.font.Font(working_dictionary + '/Fonts/Atop.ttf', 50)
medium_font = pygame.font.Font(working_dictionary + '/Fonts/Atop.ttf', 30)
small_font = pygame.font.Font(working_dictionary + '/Fonts/Atop.ttf', 20)

background_surface_x = 0
background_surface_y = 0
background_surface = pygame.image.load(os.path.join(working_dictionary, 'Graphics', 'Background_Ocean.png')).convert()
                                                # convert() wandelt png um, damit Python schneller damit arbeiten kann.
explanation_surface_x = width_frame / 2
explanation_surface_y = height_frame / 2
explanation_surface = pygame.image.load(os.path.join(working_dictionary, 'Graphics', 'explanation.png')).convert()
explanation_surface_rect = explanation_surface.get_rect(center=(explanation_surface_x, explanation_surface_y))

lives_surface_x = width_frame - 200
lives_surface_y = 20
lives_surface = pygame.image.load(os.path.join(working_dictionary, 'Graphics', 'lives.png')).convert_alpha()
lives_surface_rect_1 = lives_surface.get_rect(center=(lives_surface_x, lives_surface_y))
lives_surface_rect_2 = lives_surface.get_rect(center=(lives_surface_x + 35, lives_surface_y))
lives_surface_rect_3 = lives_surface.get_rect(center=(lives_surface_x + 70, lives_surface_y))


lives_text_surface_x = width_frame - 250
lives_text_surface_y = 28
lives_text_surface = small_font.render('Lives: ', False, 'White')
lives_text_surface_rect = lives_text_surface.get_rect(midbottom=(lives_text_surface_x, lives_text_surface_y))

text_surface_x = width_frame / 2
text_surface_y = 90
text_surface = big_font.render('Jelly Plague', False, 'White')
text_surface_rect = text_surface.get_rect(midbottom=(text_surface_x, text_surface_y))

score_surface_x = 40
score_surface_y = 28
score_surface = small_font.render('Score :', False, 'White')
score_surface_rect = score_surface.get_rect(midbottom=(score_surface_x, score_surface_y))

score_value_surface_x = 120
score_value_surface_y = 28
score_value_rect = score_surface.get_rect(midbottom=(score_value_surface_x, score_value_surface_y))

restart_surface_x = 650
restart_surface_y = 290
restart_surface = medium_font.render(' Restart (Press: Enter) / Quit (Press: Escape) ', False, 'White')
restart_surface_rect = restart_surface.get_rect(midbottom=(restart_surface_x, restart_surface_y))

winning_surface_x = 650
winning_surface_y = 290
winning_surface = big_font.render('Congratulations! You Win !', False, 'White')
winning_surface_rect = winning_surface.get_rect(midbottom=(winning_surface_x, winning_surface_y))

victory_message_surface_x = 650
victory_message_surface_y = 450
victory_message_surface = medium_font.render('You saved the ocean from the evil Jellys !', False, 'White')
victory_message_surface_rect = victory_message_surface.get_rect(midbottom=(victory_message_surface_x, victory_message_surface_y))

#################################################################################################################################################################################################
'Functions section'
#################################################################################################################################################################################################


def initialize_game():
    global player, player_shots, player1, enemy1_group, enemy1_bullets, enemy1_1, enemy1_2, enemy1_3, enemy3_1, \
        enemy1_4, enemy1_5, enemy2_1, enemy2_2, enemy2_3, enemy2_4, enemy2_5, enemy2_6, score_per_enemy, player_lives, \
        score_value, gameOn, gameWin, gameLost, timer, time_control

# # reset variables
    gameOn = True
    gameWin = False
    gameLost = False
    timer = 60
    time_control = int(pygame.time.get_ticks() / 1000)

# # define the player
    player = pygame.sprite.GroupSingle()
    player_shots = pygame.sprite.Group()
    player1 = PlayerComplete(100, height_frame, 5, origin, width_frame, height_frame, player_shots)
    player.add(player1)
    player_lives = 3

# # define enemies
    enemy1_group = pygame.sprite.Group()
    enemy1_bullets = pygame.sprite.Group()

    enemy1_1 = EnemyComplete((width_frame - 840), 240, 5, 150, 2000, height_frame,
                             enemy1_bullets, player_shots, 'orange_jelly.png')
    enemy1_2 = EnemyComplete((width_frame - 420), 300, 5, 150, 2000, height_frame,
                             enemy1_bullets, player_shots, 'orange_jelly.png')
    enemy1_3 = EnemyComplete((width_frame - 900), 300, 5, 150, 2000, height_frame,
                             enemy1_bullets, player_shots, 'orange_jelly.png')
    enemy1_4 = EnemyComplete((width_frame - 660), 300, 5, 150, 2000, height_frame,
                             enemy1_bullets, player_shots, 'orange_jelly.png')
    enemy1_5 = EnemyComplete((width_frame - 600), 240, 5, 150, 2000, height_frame,
                             enemy1_bullets, player_shots, 'orange_jelly.png')

    enemy2_1 = EnemyComplete((width_frame - 540), 300, 3, 150, 1000, height_frame,
                             enemy1_bullets, player_shots, 'pink_jelly.png')
    enemy2_2 = EnemyComplete((width_frame - 720), 240, 3, 150, 1000, height_frame,
                             enemy1_bullets, player_shots, 'pink_jelly.png')
    enemy2_3 = EnemyComplete((width_frame - 780), 300, 3, 150, 1000, height_frame,
                             enemy1_bullets, player_shots, 'pink_jelly.png')
    enemy2_4 = EnemyComplete((width_frame - 360), 240, 3, 150, 1000, height_frame,
                             enemy1_bullets, player_shots, 'pink_jelly.png')
    enemy2_5 = EnemyComplete((width_frame - 480), 240, 3, 150, 1000, height_frame,
                             enemy1_bullets, player_shots, 'pink_jelly.png')
    enemy2_6 = EnemyComplete((width_frame - 960), 240, 3, 150, 1000, height_frame,
                             enemy1_bullets, player_shots, 'pink_jelly.png')

    enemy3_1 = EnemyComplete(width_frame / 2, 160, 12, width_frame / 2 - 60, 2000, height_frame,
                             enemy1_bullets, player_shots, 'boss_jelly.png')

    enemy1_group.add(enemy1_1, enemy1_2, enemy1_3, enemy1_4, enemy1_5, enemy2_1, enemy2_2, enemy2_3, enemy2_4,
                     enemy2_5, enemy2_6, enemy3_1)

# # set score counter
    score_per_enemy = []
    for enemy in EnemyComplete.list:
        score_per_enemy.append(enemy.point_per_kill)
    score_value = 0


# # decrease timer
def update_timer():
    global timer, time_control
    current_ticks = int(pygame.time.get_ticks()/1000)
    if current_ticks > time_control:
        timer -= 1
        time_control = int(pygame.time.get_ticks() / 1000)


# # add points per killed enemy
def update_score():
    global score_per_enemy
    score_per_enemy = [enemy1_1.point_per_kill, enemy1_2.point_per_kill, enemy1_3.point_per_kill,
                       enemy1_4.point_per_kill, enemy1_5.point_per_kill, enemy2_1.point_per_kill,
                       enemy2_2.point_per_kill, enemy2_3.point_per_kill, enemy2_4.point_per_kill,
                       enemy2_5.point_per_kill, enemy2_6.point_per_kill, enemy3_1.point_per_kill]


# # check for player hits
def collision_sprite_player():
    if pygame.sprite.spritecollide(player1, enemy1_bullets, True):
        return True
    else:
        return False


#################################################################################################################################################################################################
'Game loop and game initialization'
#################################################################################################################################################################################################
initialize_game()

while gameRunning:
    for event in pygame.event.get():            # Wir rufen die pygame.event Bibliothek auf und mit den passenden keys
        if event.type == pygame.QUIT:
            pygame.quit()
            gameOn = False
            gameRunning = False
            exit()

    if gameStart:
        gameOn = False
        screen.blit(explanation_surface, explanation_surface_rect)

        pygame.display.update()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            gameStart = False
            gameOn = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            gameOn = False
            gameRunning = False
            exit()

    if gameLost:

        screen.blit(background_surface, (background_surface_x, background_surface_y))
        screen.blit(restart_surface, restart_surface_rect)

        final_score_font = pygame.font.Font(working_dictionary + '/Fonts/Atop.ttf', 40)
        final_score_value_surface = final_score_font.render(f'Highscore: {score_value}', False, 'White')
        screen.blit(final_score_value_surface, score_surface.get_rect(midbottom=(550, 190)))

        pygame.display.update()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            initialize_game()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            gameOn = False
            gameRunning = False
            exit()

    if gameWin:
        screen.blit(background_surface, (background_surface_x, background_surface_y))

        screen.blit(winning_surface, winning_surface_rect)
        screen.blit(victory_message_surface, victory_message_surface_rect)
        screen.blit(restart_surface, (width_frame / 4 - 50, height_frame - 80))

        final_score_font = pygame.font.Font(working_dictionary + '/Fonts/Atop.ttf', 40)
        final_score_value_surface = final_score_font.render(f'Highscore: {score_value}', False, 'White')
        screen.blit(final_score_value_surface, score_surface.get_rect(midbottom=(540, 190)))

        pygame.display.update()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            gameOn = False
            gameRunning = False
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            initialize_game()

    if gameOn:
        screen.blit(background_surface, (background_surface_x, background_surface_y))

        screen.blit(text_surface, text_surface_rect)
        screen.blit(lives_text_surface, lives_text_surface_rect)

        screen.blit(score_surface, score_surface_rect)
        score_value_surface = small_font.render(f'{score_value}', False, 'White')
        screen.blit(score_value_surface, score_value_rect)

        time_surface = small_font.render(f'Time: {timer}', False, 'White')
        screen.blit(time_surface, time_surface.get_rect(midbottom=((width_frame - 60), 28)))

        enemy1_group.update()
        enemy1_bullets.update()
        enemy1_group.draw(screen)
        enemy1_bullets.draw(screen)

        update_score()
        score_value = sum(score_per_enemy)

        player.update()
        player_shots.update()
        player.draw(screen)
        player_shots.draw(screen)

        update_timer()

        ###
        if collision_sprite_player():
            player_lives -= 1

        if player_lives == 3:
            screen.blit(lives_surface, lives_surface_rect_1)
            screen.blit(lives_surface, lives_surface_rect_2)
            screen.blit(lives_surface, lives_surface_rect_3)
        if player_lives == 2:
            screen.blit(lives_surface, lives_surface_rect_1)
            screen.blit(lives_surface, lives_surface_rect_2)
        else:
            screen.blit(lives_surface, lives_surface_rect_1)

        if (player_lives == 0) or (timer == 0):
            gameOn = False
            gameLost = True
        if not enemy3_1.alive():
            gameOn = False
            gameWin = True

        ###

        pygame.display.update()             # Nimmt "screen" und aktualisiert es staendig, solange gameOn "True" ist.
        clock.tick(fps)                     # Es werden 60 bilder pro sekunde projiziert.
