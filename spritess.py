import pygame
import random


class Ufo(pygame.sprite.Sprite):
    """Создание спрайта с НЛО"""
    def __init__(self, filename, group):
        super().__init__()
        self.coo_x = random.randint(0, 800)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(self.coo_x, 0))
        self.mask = pygame.mask.from_surface(self.image)
        self.add(group)

    def update(self):
        """Перемещение НЛО"""
        if self.rect.y < 533:
            self.rect.y += 5
        else:
            self.kill()


class Plane(pygame.sprite.Sprite):
    """Создание спрайта с самолетом"""
    def __init__(self, filename, coo_x, coo_y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.plane_image = pygame.image.load(filename).convert_alpha()
        self.rect = self.plane_image.get_rect(center=(coo_x, coo_y))
        self.mask = pygame.mask.from_surface(self.plane_image)
        self.speed = speed

    def update(self, posi):
        """Перемещение самолета"""
        if posi == 'left' and 0 < self.rect.x:
            self.rect.x -= self.speed
        elif posi == 'right' and self.rect.x < 780:
            self.rect.x += self.speed
