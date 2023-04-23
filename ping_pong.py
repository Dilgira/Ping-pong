from pygame import *

# константы
img_ball = 'tenis_ball.png'

# класс который будем использовать для всех спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#игровая сцена:
back = (200, 255, 255) #цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

# Персонажи
ball = GameSprite(img_ball, 200, 200, 50, 50, 7)

#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
   for e in event.get():
       if e.type == QUIT:
           game = False

   if finish != True:
       window.fill(back)
       ball.reset()

   display.update()
   clock.tick(FPS)
