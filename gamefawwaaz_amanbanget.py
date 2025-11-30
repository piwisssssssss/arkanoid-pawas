import pygame
import os

pygame.init()

# === SETUP DASAR ===
back = (200, 255, 255)
window = pygame.display.set_mode((500, 500))
window.fill(back)
clock = pygame.time.Clock()

# === TITIK PLATFORM ===
platform_x = 200
platform_y = 330

# === STATUS GAME ===
game_over = False

# === KELAS AREA ===
class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color if color else back

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


# === KELAS GAMBAR (SPRITE CUSTOM) ===
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=50, height=50):
        super().__init__(x, y, width, height)
        self.load_image(filename, width, height)

    def load_image(self, filename, width, height):
        """Muat sprite custom, fallback ke kotak warna abu-abu jika tidak ada."""
        if os.path.exists(filename):
            image = pygame.image.load(filename).convert_alpha()
            self.image = pygame.transform.scale(image, (width, height))
        else:
            print(f"[⚠️] File '{filename}' tidak ditemukan, pakai placeholder.")
            self.image = pygame.Surface((width, height))
            self.image.fill((180, 180, 180))

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# === LABEL TEKS ===
class Label(Area):
    def set_text(self, text, fsize=20, text_color=(0, 0, 0)):
        font = pygame.font.SysFont('Verdana', fsize)
        self.image = font.render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


# === BUAT OBJEK ===
ball = Picture("ball.png", 160, 200, 40, 40)
platform = Picture("platform.png", platform_x, platform_y, 100, 30)

# === BUAT MONSTER ===
start_x = 5
start_y = 5
n = 9
monster = []

for j in range(3):
    y = start_y + (55 * j)
    x = start_x + (27 * j)
    for i in range(n):
        enemy = Picture("enemy.png", x, y, 50, 50)
        monster.append(enemy)
        x += 55
    n -= 1

# === VARIABEL GERAK ===
move_right = False
move_left = False
bola_x = 3
bola_y = 3

# === LOOP UTAMA ===
while not game_over:
    window.fill(back)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False

    # Gerakkan platform
    if move_right and platform.rect.right < 500:
        platform.rect.x += 5
    if move_left and platform.rect.left > 0:
        platform.rect.x -= 5

    # Gerakkan bola
    ball.rect.x += bola_x
    ball.rect.y += bola_y

    # Pantulan dinding
    if ball.rect.y < 0:
        bola_y *= -1
    if ball.rect.x > 460 or ball.rect.x < 0:
        bola_x *= -1

    # Kalah
    if ball.rect.y > 480:
        label = Label(100, 200, 300, 100)
        label.set_text("YOU LOSE!", 60, (255, 0, 0))
        label.draw()
        pygame.display.update()
        pygame.time.wait(2000)
        game_over = True

    # Menang
    if len(monster) == 0:
        label = Label(100, 200, 300, 100)
        label.set_text("YOU WIN!", 60, (0, 200, 0))
        label.draw()
        pygame.display.update()
        pygame.time.wait(2000)
        game_over = True

    # Pantulan dari platform
    if ball.rect.colliderect(platform.rect):
        bola_y *= -1

    # Cek tabrakan dengan monster
    for m in monster[:]:
        if m.rect.colliderect(ball.rect):
            monster.remove(m)
            bola_y *= -1
        else:
            m.draw()

    # Gambar platform dan bola
    platform.draw()
    ball.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()