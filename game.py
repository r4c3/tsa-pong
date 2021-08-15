import pygame, sys, math

#pygame init
pygame.init()
clock = pygame.time.Clock()
tick_rate = 144

#window init
screen_width = 1140
screen_height = 820
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("HCTSA Pong")
windowIcon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(windowIcon)

#game objects
ball = pygame.Rect(screen_width / 2 - 12, screen_height / 2 - 12, 24, 24)
left_player = pygame.Rect(8, screen_height / 2 - 57, 14, 114)
right_player = pygame.Rect(screen_width - 22, screen_height / 2 - 57, 14, 114)

#logic init
ball_velocity_x, ball_velocity_y, left_player_velocity_y, right_player_velocity_y = 0, 0, 0, 0
def resetBall():
    global ball_velocity_x, ball_velocity_y, left_player_velocity_y, right_player_velocity_y
    pygame.time.wait(300)
    ball_velocity_x = 4
    ball_velocity_y = 4
    left_player_velocity_y = 0
    right_player_velocity_y = 0
resetBall()

#game init
left_player_score = 0
right_player_score = 0

#event loop
def Game():
    game = True
    global ball_velocity_x, ball_velocity_y, left_player_velocity_y, right_player_velocity_y
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


        #logic
        left_player.y += left_player_velocity_y
        right_player.y += right_player_velocity_y

        if left_player.top <= 0:
            left_player.top = 0
        if left_player.bottom >= screen_height:
            left_player.bottom = screen_height
        if right_player.top <= 0:
            right_player.top = 0
        if right_player.bottom >= screen_height:
            right_player.bottom = screen_height

        ball.x += ball_velocity_x
        ball.y += ball_velocity_y

        if ball.top <= 0 or ball.bottom >= screen_height:
            ball_velocity_y *= -1
            clank.play()
        if ball.left <= 0:
            left_player_score += 1
            coin.play()
            resetBall()
        if ball.right >= screen_width:
            right_player_score += 1
        if ball.colliderect(left_player) or ball.colliderect(right_player):
            ball_velocity_x *= -1.02
            hitmarker.play()

        #display
        screen.fill(grey)
        pygame.draw.rect(screen, blue, left_player)
        pygame.draw.rect(screen, red, right_player)
        pygame.draw.ellipse(screen, white, ball)


        #refresh
        pygame.display.flip()
        clock.tick(tick_rate)