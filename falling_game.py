

import pygame

import time

import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("IMG_7448.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5

BRICK_WIDTH = 10
BRICK_HEIGHT = 20
BRICK_VEL = 3

FONT = pygame.font.SysFont("arial", 30)


def draw(player, elapsed_time, bricks):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "orange")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "orange", player)

    for brick in bricks:
        pygame.draw.rect(WIN, "white", brick)

    pygame.display.update()

def main():
    run = True

    player  = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, 
                          PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    brick_add_increment = 2000
    brick_count = 0

    bricks = []
    hit = False

    while run: 
        brick_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if brick_count > brick_add_increment:
            for _ in range(3):
                brick_x = random.randint(0, WIDTH - BRICK_WIDTH)
                brick = pygame.Rect(brick_x, -BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT)
                bricks.append(brick)

            brick_add_increment = max(200, brick_add_increment - 50)
            brick_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL


        for brick in bricks[:]:
            brick.y += BRICK_VEL
            if brick.y > HEIGHT:
                bricks.remove(brick)
            elif brick.y + brick.height >= player.y and brick.colliderect(player):
                bricks.remove(brick)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "orange")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2,
                                  HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        

        draw(player, elapsed_time, bricks)
    pygame.quit()

if __name__ == "__main__":
    main()
