from pygame import *

# константы
img_ball = 'tenis_ball.png'
img_racket = 'racket.png'

racket_size_x = 50
racket_size_y = 140

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
#класс-наследник Player для ракеток (суперкласс — GameSprite). Данный тип спрайта должен управляться пользователем с помощью стрелок клавиатуры и с помощью клавиш W и S
class Player(GameSprite):
    # метод для управления спрайтом клавишами W и S
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - racket_size_y - 5:
            self.rect.y += self.speed
    # метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - racket_size_y - 5:
            self.rect.y += self.speed


#игровая сцена:
back = (200, 255, 255) #цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

# Персонажи
ball = GameSprite(img_ball, 200, 200, 50, 50, 7)
racket1 = Player(img_racket, 10, 0, racket_size_x, racket_size_y, 6)
racket2 = Player(img_racket, win_width - racket_size_x - 10, 0, racket_size_x, racket_size_y, 6)

# Надписи
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))

#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

speed_x = 4
speed_y = 4

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        #Передвигаем спрайты
        racket1.update_l()
        racket2.update_r()
        # Автоматическое движение мяча
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        #Отрисовывем спрайты    
        racket1.reset()
        racket2.reset()
        ball.reset()

        # Блок условий
        # при столкновении с верхней и нижней границами сцены мяч будет отскакивать в противоположном направлении по оси y
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
         # при столкновении с ракетками мяч будет отскакивать в противоположном направлении по оси x, меняем знак скорости по оси x
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        #условие проигрыша 1 игрока
        if ball.rect.x < 0:
            window.blit(lose1, (200, 200))
            finish = True
        #условие проигрыша 2 игрока
        elif ball.rect.x > win_width - 50:
            window.blit(lose2, (200, 200))
            finish = True
    display.update()
    clock.tick(FPS)
