import pygame
import random
import sys

pygame.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Platformer")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 28)

player = pygame.Rect(100, 450, 40, 50)

velocity_y = 0
speed = 6
jump_power = -14
gravity = 0.7

on_ground = False

score = 0
lives = 3
game_over = False
win = False

platforms = [
    pygame.Rect(0, 550, 900, 50),
    pygame.Rect(100, 450, 150, 20),
    pygame.Rect(320, 380, 150, 20),
    pygame.Rect(550, 310, 150, 20),
    pygame.Rect(730, 230, 120, 20)
]

coins = [
    pygame.Rect(160, 410, 20, 20),
    pygame.Rect(380, 340, 20, 20),
    pygame.Rect(610, 270, 20, 20),
    pygame.Rect(770, 190, 20, 20)
]

enemies = [
    pygame.Rect(300, 510, 40, 40),
    pygame.Rect(500, 510, 40, 40),
    pygame.Rect(680, 510, 40, 40)
]

enemy_direction = [1, -1, 1]

goal = pygame.Rect(800, 180, 40, 50)


def reset_player():
    global velocity_y

    player.x = 100
    player.y = 450
    velocity_y = 0


def draw_text(text, x, y):
    image = font.render(text, True, (255, 255, 255))
    screen.blit(image, (x, y))


def restart_game():
    global score, lives, game_over, win

    score = 0
    lives = 3
    game_over = False
    win = False

    reset_player()

    coins.clear()
    coins.extend([
        pygame.Rect(160, 410, 20, 20),
        pygame.Rect(380, 340, 20, 20),
        pygame.Rect(610, 270, 20, 20),
        pygame.Rect(770, 190, 20, 20)
    ])


running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_r:
                restart_game()

            if event.key == pygame.K_SPACE and on_ground:
                velocity_y = jump_power

    if not game_over and not win:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += speed

        velocity_y += gravity
        player.y += velocity_y

        on_ground = False

        for platform in platforms:

            if player.colliderect(platform):

                if velocity_y > 0:
                    player.bottom = platform.top
                    velocity_y = 0
                    on_ground = True

                elif velocity_y < 0:
                    player.top = platform.bottom
                    velocity_y = 0

        if player.left < 0:
            player.left = 0

        if player.right > WIDTH:
            player.right = WIDTH

        for i, enemy in enumerate(enemies):

            enemy.x += enemy_direction[i] * 2

            if enemy.left <= 0 or enemy.right >= WIDTH:
                enemy_direction[i] *= -1

            if player.colliderect(enemy):

                lives -= 1
                reset_player()

                if lives <= 0:
                    game_over = True

        for coin in coins[:]:

            if player.colliderect(coin):

                coins.remove(coin)
                score += 10

        if player.colliderect(goal):

            if len(coins) == 0:
                win = True

        if player.y > HEIGHT:

            lives -= 1
            reset_player()

            if lives <= 0:
                game_over = True

    screen.fill((30, 30, 60))

    for platform in platforms:
        pygame.draw.rect(screen, (80, 180, 80), platform)

    for coin in coins:
        pygame.draw.circle(
            screen,
            (255, 215, 0),
            coin.center,
            10
        )

    for enemy in enemies:
        pygame.draw.rect(
            screen,
            (220, 60, 60),
            enemy
        )

    pygame.draw.rect(
        screen,
        (150, 80, 255),
        goal
    )

    pygame.draw.rect(
        screen,
        (50, 150, 255),
        player
    )

    draw_text(f"Score: {score}", 20, 20)
    draw_text(f"Lives: {lives}", 20, 55)

    if len(coins) == 0:
        draw_text("Goal unlocked!", 650, 20)
    else:
        draw_text(
            f"Coins left: {len(coins)}",
            650,
            20
        )

    if game_over:

        draw_text(
            "GAME OVER",
            350,
            250
        )

        draw_text(
            "Press R to restart",
            320,
            300
        )

    if win:

        draw_text(
            "YOU WIN!",
            370,
            250
        )

        draw_text(
            f"Final Score: {score}",
            340,
            300
        )

        draw_text(
            "Press R to play again",
            310,
            350
        )

    pygame.display.update()

pygame.quit()
sys.exit()