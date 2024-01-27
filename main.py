import pygame
import sys


def main():
    # Создание вводного экрана
    size = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Приветствие')
    screen.fill((15, 10, 80))
    #  Создание надписей
    font1 = pygame.font.Font(None, 40)
    text_rules = font1.render('Название', True, (255, 255, 255))
    screen.blit(text_rules, (330, 80))
    text_rules1 = font1.render('C помощью стрелок управляйте ...,', True, (255, 255, 255))
    text_rules2 = font1.render("чтобы избежать ...", True, (255, 255, 255))
    #  Созданеи кнопок
    screen.blit(text_rules1, (120, 130))
    screen.blit(text_rules2, (200, 170))
    pygame.draw.rect(screen, (210, 160, 0), (50, 300, 325, 200), 8)
    pygame.draw.rect(screen, (210, 160, 0), (425, 300, 325, 200), 8)
    pygame.draw.line(screen, (210, 160, 0), (0, 20), (800, 20), width=8)
    pygame.draw.line(screen, (210, 160, 0), (0, 580), (800, 580), width=8)
    text_level1 = font1.render("Уровень 1", True, (255, 255, 255))
    screen.blit(text_level1, (140, 390))
    text_level2 = font1.render("Уровень 2", True, (255, 255, 255))
    screen.blit(text_level2, (515, 390))

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    sys.exit(main())
