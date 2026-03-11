import pygame

# Инициализация
pygame.init()
pygame.mixer.init()  # Инициализируем звук

# Загрузка и запуск музыки
# Файл должен лежать в папке с кодом
try:
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)  # -1 означает бесконечный повтор
except:
    print("Файл music.mp3 не найден!")

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

# Параметры игрока и препятствий (как в предыдущем примере)
player_rect = pygame.Rect(100, 310, 40, 40)
gravity = 0
is_jumping = False
obstacle = pygame.Rect(600, 310, 40, 40)
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                gravity = -15
                is_jumping = True

    # Гравитация и движение
    gravity += 1
    player_rect.y += gravity
    if player_rect.bottom >= 350:
        player_rect.bottom = 350
        is_jumping = False

    obstacle.x -= speed
    if obstacle.x < -40:
        obstacle.x = 800

    if player_rect.colliderect(obstacle):
        pygame.mixer.music.stop()  # Остановить музыку при проигрыше
        print("Игра окончена!")
        running = False

    # Отрисовка
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 200, 255), player_rect)
    pygame.draw.rect(screen, (255, 50, 50), obstacle)
    pygame.draw.line(screen, (255, 255, 255), (0, 350), (800, 350))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
