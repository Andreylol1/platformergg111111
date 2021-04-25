#Создай собственный Шутер!
from random import *
from pygame import *
gg = 100,0,255
class GameSprite(sprite.Sprite):
#конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
#вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
#каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load('1.png'), (size_x, size_y))
        self.speed = player_speed
#каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
#метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
#метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
class Ball(GameSprite):
#метод "выстрел" (используем место игрока, чтобы создать там пулю)
win_width = 700
win_height = 700
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
#создание группы спрайтов-врагов
monsters = sprite.Group()
window.fill(gg)
man = Player("1.png", 5, 500 - 100, 40, 100, 10)
man1 = Player("1.png", 655, 500 - 100, 40, 100, 10)
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    man.reset()
    man1.reset()
    display.update()

    
