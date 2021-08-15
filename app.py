import pygame, sys, random

#pygame init
pygame.init()
clock = pygame.time.Clock()
tick_rate = 144

#window init
screen_width = 1140
screen_height = 820
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("HCTSA Pong")
windowIcon = pygame.image.load("assets/img/icon.png")
pygame.display.set_icon(windowIcon)

#font init
h1 = pygame.font.Font("assets/ebm.ttf", 90)
h3 = pygame.font.Font("assets/ebm.ttf", 62)
p = pygame.font.Font("assets/ebm.ttf", 42)

#sfx init

#color init
grey = pygame.Color(22, 22, 22)
blue = pygame.Color(0, 45, 114)
red = pygame.Color(203, 44, 48)
white = pygame.Color(245, 245, 245)

main_menu, game = True, False

def Main_Menu():
    #music init
    songs = ["accordion.wav", "curls.wav", "deepfriedfrenz.wav", "supervillaintheme.wav", "knishes.wav", "caniwatch.wav"]
    song_number = random.randint(0, len(songs) - 1)
    random.shuffle(songs)
    pygame.mixer.music.load("assets/music/" + songs[song_number])
    pygame.mixer.music.set_volume(0.03)
    pygame.mixer.music.play(1)
    for index, song in enumerate(songs):
        if index == song_number:
            continue
        pygame.mixer.music.queue("assets/music/" + song)
    
    #objects init
    title = h1.render("HCHS TSA PONG", True, white)
    title_rect = title.get_rect(center=(screen_width / 2, 80))

    blue_logo = pygame.image.load("assets/img/blue_logo.png")
    blue_logo = pygame.transform.scale(blue_logo, (160, 90))

    red_logo = pygame.image.load("assets/img/red_logo.png")
    red_logo = pygame.transform.scale(red_logo, (160, 90))

    start_button = pygame.Rect(screen_width / 2 - 210, screen_height - 80 - 65, 420, 90)

    start_text = h3.render("START GAME", True, red)
    start_text_rect = start_text.get_rect(center=(screen_width / 2, screen_height - 80 - 20))

    left_text_1 = p.render("player 1 (left):", True, blue)
    left_text_1_rect = left_text_1.get_rect(center=(180, 210))
    left_text_2 = p.render("\"q\" to move up", True, white)
    left_text_2_rect = left_text_2.get_rect(center=(180, 250))
    left_text_3 = p.render("\"a\" to move down", True, white)
    left_text_3_rect = left_text_3.get_rect(center=(180, 290))

    right_text_1 = p.render("player 2 (right):", True, red)
    right_text_1_rect = right_text_1.get_rect(center=(screen_width - 180, 210))
    right_text_2 = p.render("\"p\" to move up", True, white)
    right_text_2_rect = right_text_2.get_rect(center=(screen_width - 180, 250))
    right_text_3 = p.render("\";\" to move down", True, white)
    right_text_3_rect = right_text_3.get_rect(center=(screen_width - 180, 290))

    center_text_1 = p.render("gameplay:", True, white)
    center_text_1_rect = center_text_1.get_rect(center=(screen_width / 2, 370))
    center_text_2 = p.render("first to 11 wins", True, white)
    center_text_2_rect = center_text_2.get_rect(center=(screen_width / 2, 410))
    center_text_3 = p.render("both players hit their up buttons to start next point", True, white)
    center_text_3_rect = center_text_3.get_rect(center=(screen_width / 2, 450))
    center_text_4 = p.render("press \"m\" to toggle audio", True, white)
    center_text_4_rect = center_text_4.get_rect(center=(screen_width / 2, 490))

    #main menu loop
    while 1:
        #user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_button.collidepoint(event.pos):
                        Game()

        #draw frame
        screen.fill(grey)
        screen.blit(title, title_rect)
        screen.blit(blue_logo, (150, 35))
        screen.blit(red_logo, (screen_width - 150 - 160, 35))
        pygame.draw.rect(screen, white, start_button)
        screen.blit(start_text, start_text_rect)
        screen.blit(left_text_1, left_text_1_rect)
        screen.blit(left_text_2, left_text_2_rect)
        screen.blit(left_text_3, left_text_3_rect)
        screen.blit(right_text_1, right_text_1_rect)
        screen.blit(right_text_2, right_text_2_rect)
        screen.blit(right_text_3, right_text_3_rect)
        screen.blit(center_text_1, center_text_1_rect)
        screen.blit(center_text_2, center_text_2_rect)
        screen.blit(center_text_3, center_text_3_rect)
        screen.blit(center_text_4, center_text_4_rect)

        #render frame
        pygame.display.flip()
        clock.tick(tick_rate)

def Game():
    game = True
    pygame.mixer.music.pause()

    #score init
    left_player_score = 0
    right_player_score = 0

    #objects init
    ball = pygame.Rect(screen_width / 2 - 15, screen_height / 15 - 12, 30, 30)

    left_player = pygame.Rect(12, screen_height / 2 - 57, 24, 114)
    right_player = pygame.Rect(screen_width - 36, screen_height / 2 - 57, 24, 114)

    left_score_label = p.render("player 1 score:", True, blue)
    left_score_label_rect = left_score_label.get_rect(center=(100, 20))
    left_score_value = p.render(str(left_player_score), True, white)
    left_score_value_rect = left_score_value.get_rect(center=(180, 20))

    right_score_label = p.render("player 2 score:", True, red)
    right_score_label_rect = right_score_label.get_rect(center=(screen_width - 100, 20))
    right_score_value = p.render(str(right_player_score), True, white)
    right_score_value_rect = right_score_value.get_rect(center=(screen_width - 180, 20))

    #physics init
    ball_velocity_x = 4
    ball_velocity_y = 4
    left_player_velocity_y = 0
    right_player_velocity_y = 0

    #game loop
    while game:
        #user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    left_player_velocity_y -= 5
                if event.key == pygame.K_a:
                    left_player_velocity_y += 5
                if event.key == pygame.K_p:
                    right_player_velocity_y -= 5
                if event.key == pygame.K_SEMICOLON:
                    right_player_velocity_y += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    left_player_velocity_y += 5
                if event.key == pygame.K_a:
                    left_player_velocity_y -= 5
                if event.key == pygame.K_p:
                    right_player_velocity_y += 5
                if event.key == pygame.K_SEMICOLON:
                    right_player_velocity_y -= 5


        #apply player velocities
        left_player.y += left_player_velocity_y
        right_player.y += right_player_velocity_y

        #check and enforce player collisions
        if left_player.top <= 0:
            left_player.top = 0
        if left_player.bottom >= screen_height:
            left_player.bottom = screen_height
        if right_player.top <= 0:
            right_player.top = 0
        if right_player.bottom >= screen_height:
            right_player.bottom = screen_height

        #apply ball velocities
        ball.x += ball_velocity_x
        ball.y += ball_velocity_y

        #check and enforce ball collisions
        if ball.top <= 0 or ball.bottom >= screen_height:
            ball_velocity_y *= -1
        if ball.left <= 0:
            left_player_score += 1
        if ball.right >= screen_width:
            right_player_score += 1
        if ball.colliderect(left_player) or ball.colliderect(right_player):
            ball_velocity_x *= -1
            ball_velocity_y += random.choice([-0.3, 0.4, 2, 0.55, 0.2, -0.1, 0])

        #draw frame
        screen.fill(grey)

        screen.blit(left_score_label, left_score_label_rect)
        screen.blit(left_score_value, left_score_value_rect)
        screen.blit(right_score_label, right_score_label_rect)
        screen.blit(right_score_value, right_score_value_rect)

        pygame.draw.ellipse(screen, white, ball)
        pygame.draw.rect(screen, blue, left_player)
        pygame.draw.rect(screen, red, right_player)

        #render frame
        print(ball_velocity_x, ball_velocity_y)
        pygame.display.flip()
        clock.tick(tick_rate)

Main_Menu()