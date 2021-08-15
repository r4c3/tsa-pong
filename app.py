import pygame, sys, random

#pygame init
pygame.init()
clock = pygame.time.Clock()
tick_rate = 60

#window init
screen_width = 1140
screen_height = 820
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("HCTSA Pong")
windowIcon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(windowIcon)

#font init
font = pygame.font.Font("assets/ebm.ttf", 12)

#sfx init

#color init
grey = pygame.Color(22, 22, 22)
blue = pygame.Color(0, 45, 114)
red = pygame.Color(203, 44, 48)
white = pygame.Color(230, 230, 230)

main_menu, game = True, False

def Main_Menu():
    #music init
    songs = ["accordion.wav", "curls.wav", "deepfriedfrenz.wav", "supervillaintheme.wav", "knishes.wav", "caniwatch.wav"]
    song_number = random.randint(0, len(songs))
    random.shuffle(songs)
    pygame.mixer.music.load("assets/music/" + songs[song_number])
    pygame.mixer.music.set_volume(0.03)
    pygame.mixer.music.play(1)
    for index, song in enumerate(songs):
        if index == song_number:
            continue
        pygame.mixer.music.queue("assets/music/" + song)
    
    #main menu loop
    while 1:
        #user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(grey)
        
        pygame.display.flip()
        clock.tick(tick_rate)

def Game():
    #objects init
    ball = pygame.Rect(screen_width / 2 - 12, screen_height / 2 - 12, 24, 24)
    left_player = pygame.Rect(8, screen_height / 2 - 57, 14, 114)
    right_player = pygame.Rect(screen_width - 22, screen_height / 2 - 57, 14, 114)

    #physics init
    ball_velocity_x = 4
    ball_velocity_y = 4
    left_player_velocity_y = 0
    right_player_velocity_y = 0
    left_player_score = 0
    right_player_score = 0

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
            ball_velocity_x *= -1.02

        #draw frame
        screen.fill(grey)
        pygame.draw.rect(screen, blue, left_player)
        pygame.draw.rect(screen, red, right_player)
        pygame.draw.ellipse(screen, white, ball)


        #render frame
        pygame.display.flip()
        clock.tick(tick_rate)


Main_Menu()