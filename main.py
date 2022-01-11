import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = 5
        self.rect.center = (self.rect.width / 2, self.rect.height / 2)

FPS = 30

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("Igra huli")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player1 = Player((0, 255, 0))
player1.rect.x = 100
player1.rect.y = 440
all_sprites.add(player1)
player2 = Player((255, 0, 0))
player2.rect.x = 1340
player2.rect.y = 440
all_sprites.add(player2)


running = True

moving1 = 0
moving2 = 0

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving2 = 1
            elif event.key == pygame.K_RIGHT:
                moving2 = 2
            elif event.key == pygame.K_UP:
                moving2 = 3
            elif event.key == pygame.K_DOWN:
                moving2 = 4

            if event.key == pygame.K_a:
                moving1 = 1
            elif event.key == pygame.K_d:
                moving1 = 2
            elif event.key == pygame.K_w:
                moving1 = 3
            elif event.key == pygame.K_s:
                moving1 = 4
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_w or event.key == pygame.K_d or event.key == pygame.K_s:
                moving1 = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
                moving2 = 0

        if moving1 == 1:
            player1.rect.x -= player1.velocity
        elif moving1 == 2:
            player1.rect.x += player1.velocity
        elif moving1 == 3:
            player1.rect.y -= player1.velocity
        elif moving1 == 4:
            player1.rect.y += player1.velocity

        if moving2 == 1:
            player2.rect.x -= player2.velocity
        elif moving2 == 2:
            player2.rect.x += player2.velocity
        elif moving2 == 3:
            player2.rect.y -= player2.velocity
        elif moving2 == 4:
            player2.rect.y += player2.velocity

    screen.fill((255, 255, 255))
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()