import pygame
import sys
from spritess import Ufo, Plane  # Импортируем классы спрайтов


clock = pygame.time.Clock()
FPS = 60


def end_window(points):
    """Создание окна проигрыша"""
    pygame.init()
    # Задаем размер, цвет
    size = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('End')
    screen.fill((28, 2, 194))

    # Создание надписей
    font1 = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 40)
    text_fail = font1.render('Вы проиграли', True, (255, 255, 255))
    text_point = font1.render(f'Ваш счет составляет {points * 100} очков', True, (255, 255, 255))
    text_again1 = font1.render('Уровень 1', True, (255, 255, 255))
    text_again2 = font1.render('Уровень 2', True, (255, 255, 255))
    text_end = font2.render('Завершить', True, (255, 255, 255))
    text_start = font2.render('Начало', True, (255, 255, 255))

    # Визуализация кнопок
    pygame.draw.rect(screen, (166, 249, 255), (45, 280, 325, 150), 8)
    pygame.draw.rect(screen, (166, 249, 255), (425, 280, 325, 150), 8)
    pygame.draw.rect(screen, (166, 249, 255), (45, 450, 325, 100), 8)
    pygame.draw.rect(screen, (166, 249, 255), (425, 450, 325, 100), 8)

    # Добавление текста
    screen.blit(text_fail, (270, 120))
    screen.blit(text_point, (170, 180))
    screen.blit(text_again1, (135, 350))
    screen.blit(text_again2, (515, 350))
    screen.blit(text_end, (130, 483))
    screen.blit(text_start, (534, 483))

    # Запуск цикла
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Считывание координат при нажатии клавиш мышки
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coords = pygame.mouse.get_pos()
                # Нажание на кнопку уровня 1
                if (45 <= coords[0] <= 370) and (280 <= coords[1] <= 430):
                    first_level()
                # Нажание на кнопку уровня 2
                elif (425 <= coords[0] <= 750) and (280 <= coords[1] <= 430):
                    second_level()
                # Нажание на кнопку завершения программы
                elif (45 <= coords[0] <= 370) and (450 <= coords[1] <= 550):
                    running = False
                    break
                # Нажание на кнопку возвращения на начальный экран
                elif (425 <= coords[0] <= 750) and (450 <= coords[1] <= 550):
                    running = False
                    main()

        pygame.display.flip()

    pygame.quit()

    print(points)


def first_level():
    """Создание экрана для первого уровня"""
    pygame.init()
    points = 0

    # Загрузка звука
    bomm = pygame.mixer.Sound('images/взрыв.mp3')

    # Создание группы спрайтов с НЛО
    ufos = pygame.sprite.Group()

    # Задаем параметры для фона
    size = 800, 533
    backgrount = pygame.image.load('images/window.jpg')
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Level 1')
    screen.blit(backgrount, (0, 0))

    # Создание персонажа - самолета
    plane = Plane('images/plane.jpg', 390, 475, 15)
    screen.blit(plane.plane_image, plane.rect)
    ufo_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ufo_timer, 2000)

    running = True
    while running:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False

            # Проверка нажатий клавиш для управления самолетом
            if keys[pygame.K_LEFT]:
                plane.update('left')
            elif keys[pygame.K_RIGHT]:
                plane.update('right')

            # Вывод НЛО
            if event.type == ufo_timer:
                ufos.add(Ufo('images/UFO.png', ufos))
                points += 1

        # Проверка столкновений
        for ufo in ufos:
            if pygame.sprite.collide_mask(ufo, plane):
                bomm.play()
                running = False
                end_window(points)

        # Обновление экрана
        screen.blit(backgrount, (0, 0))
        ufos.draw(screen)
        ufos.update()
        screen.blit(plane.plane_image, plane.rect)
        pygame.display.update()
        clock.tick(30)

    pygame.quit()


def second_level():
    """Создание экрана для второго уровня"""
    points = 0
    pygame.init()

    # Загрузка звука
    bomm = pygame.mixer.Sound('images/взрыв.mp3')

    # Создание группы спрайтов с НЛО
    ufos = pygame.sprite.Group()

    # Задаем параметры для фона
    size = 800, 533
    backgrount = pygame.image.load('images/window.jpg')
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Level 1')
    screen.blit(backgrount, (0, 0))

    # Создание персонажа - самолета
    plane = Plane('images/plane.jpg', 390, 475, 25)
    screen.blit(plane.plane_image, plane.rect)
    ufo_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ufo_timer, 1500)

    running = True
    while running:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False

            # Проверка нажатий клавиш для управления самолетом
            if keys[pygame.K_LEFT]:
                plane.update('left')
            elif keys[pygame.K_RIGHT]:
                plane.update('right')

            # Вывод НЛО
            if event.type == ufo_timer:
                ufos.add(Ufo('images/UFO.png', ufos))
                points += 1

        # Проверка столкновений
        for ufo in ufos:
            if pygame.sprite.collide_mask(ufo, plane):
                bomm.play()
                running = False
                end_window(points)

        # Обновление экрана
        screen.blit(backgrount, (0, 0))
        ufos.draw(screen)
        ufos.update()
        screen.blit(plane.plane_image, plane.rect)
        pygame.display.update()
        clock.tick(30)

    pygame.quit()


def main():
    # Создание вводного экрана
    size = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Go Plane')
    screen.fill((28, 2, 194))
    #  Создание надписей
    font1 = pygame.font.Font(None, 40)
    text_rules = font1.render('Go Plane', True, (255, 255, 255))
    screen.blit(text_rules, (330, 80))
    text_rules1 = font1.render('C помощью стрелок управляйте самолетом,', True, (255, 255, 255))
    text_rules2 = font1.render("чтобы избежать НЛО", True, (255, 255, 255))
    #  Созданеи кнопок
    screen.blit(text_rules1, (120, 130))
    screen.blit(text_rules2, (200, 170))
    pygame.draw.rect(screen, (166, 249, 255), (50, 300, 325, 200), 8)
    pygame.draw.rect(screen, (166, 249, 255), (425, 300, 325, 200), 8)
    pygame.draw.line(screen, (166, 249, 255), (0, 20), (800, 20), width=8)
    pygame.draw.line(screen, (166, 249, 255), (0, 580), (800, 580), width=8)
    text_level1 = font1.render("Уровень 1", True, (255, 255, 255))
    screen.blit(text_level1, (140, 390))
    text_level2 = font1.render("Уровень 2", True, (255, 255, 255))
    screen.blit(text_level2, (515, 390))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Считывание координат при нажатии клавиш мышки
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coords = pygame.mouse.get_pos()
                # Нажание на кнопку уровня 1
                if (50 <= coords[0] <= 375) and (300 <= coords[1] <= 500):
                    running = False
                    first_level()
                # Нажание на кнопку уровня 2
                elif (425 <= coords[0] <= 750) and (300 <= coords[1] <= 500):
                    running = False
                    second_level()

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    sys.exit(main())
