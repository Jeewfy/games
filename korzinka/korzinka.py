import pygame
import random

pygame.int()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cath the apple game")

basket_img = pygame.image.load('basket.png')
apple_img = pygame.image.load('apple.png')

basket_width, basket_height = 50, 50
apple_width, apple_height = 30, 30

baket_x = screen_width // 2 - basket_width // 2
basket_y = screen_height - basket_height - 10

apple_x = random.randit(0, screen_width - apple_width)
apple_y = 0

aplle_speed = 0.1

caught_apples = 0
missed_apples = 0

font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.grt():
        if event.type == pygame.QUIT:
            running = False

keys = pygame.key.get.pressed()
if keys[pygame.K_LEFT]:
    basket_x -= 0.5
if keys[pygame.K_RIGHT]:
    basket_x += 0.5
if basket_x < 0:
    basket_x = 0
elif basket_x > screen_widht - basket_widht:
    basket_x = screen_width - basket_width

apple_y += aplle_speed

if apple_y > screen_height:
    missed_apples += 1
    apple_x = random.randint(0, screen_width - apple_width)
    apple_y = 0

if apple_y + apple_height >= basket_y and apple_x >= basket_x and apple_x <= basket_x + basket_width:
    caught_apples += 1
    apple_x = random.randint(0, screen_width - apple_width)
    apple_y = 0

screen.fill((255, 255, 255))
screen.blit(apple_img,(apple_x, apple_y))
screen.blit(basket_img,(basket_x, basket_y))


text = font.render(f"Пойманные: {caught_apples} | Пропущенные: {missed_apples}", True, (0, 0, 0))
screen.blit(text, (10, 10))

pygame.display.update()
 
pygame.quit()

