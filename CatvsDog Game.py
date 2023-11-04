import pygame
import random
import os
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dog vs. Cat Game")

images_dir = r"C:\Users\amogh\OneDrive\Documents\His exellency Amogh Singh\my world\Pictures For AI\DogVSCat"

dog_images = [pygame.image.load(os.path.join(images_dir, f)) for f in os.listdir(images_dir) if f.startswith("dog")]
cat_images = [pygame.image.load(os.path.join(images_dir, f)) for f in os.listdir(images_dir) if f.startswith("cat")]

current_image = None
correct_label = None
score = 0

game_over = False
game_over_start_time = None
game_over_duration = 2

def load_image():
    global current_image, correct_label
    image_type = random.choice(["dog", "cat"])
    if image_type == "dog":
        correct_label = "Dog"
        current_image = random.choice(dog_images)
    else:
        correct_label = "Cat"
        current_image = random.choice(cat_images)

load_image()

running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if correct_label == "Dog":
                    score += 1
                    load_image()
                else:
                    game_over = True
                    game_over_start_time = time.time()
            elif event.key == pygame.K_c:
                if correct_label == "Cat":
                    score += 1
                    load_image()
                else:
                    game_over = True
                    game_over_start_time = time.time()

    if game_over:
        if time.time() - game_over_start_time >= game_over_duration:
            running = False 
    window.fill((255, 255, 255))

    if not game_over:
        window.blit(current_image, (WIDTH // 2 - current_image.get_width() // 2, HEIGHT // 2 - current_image.get_height() // 2))
    else:
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, (255, 0, 0))
        window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    window.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()
