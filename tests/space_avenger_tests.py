import unittest
from unittest.mock import Mock
import pygame
from src.space_avenger.space_avenger import Player, Bullet, Explosion, Enemy

class TestPlayer(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.player = Player()
        self.player.frames = [Mock(), Mock()]  # Mock frames for the player
        self.player.rect = pygame.Rect(100, 100, 50, 50)  # Initial position

    def test_player_movement_left(self):
        self.player.update({pygame.K_LEFT: True})
        self.assertTrue(self.player.rect.x < 100)


class TestBullet(unittest.TestCase):
    def setUp(self):
        self.bullet = Bullet(100, 100)

    def test_bullet_movement(self):
        old_y = self.bullet.rect.y
        self.bullet.update()
        self.assertTrue(self.bullet.rect.y < old_y)

    def test_bullet_disappear(self):
        for _ in range(100):
            self.bullet.update()
        self.assertTrue(self.bullet.rect.y < 0)

class TestExplosion(unittest.TestCase):
    def setUp(self):
        self.explosion = Explosion(Mock())
        self.explosion.frames = [Mock(), Mock(), Mock()]  # Mock frames for the explosion

class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy("flyer", False)
        self.enemy.frames = [Mock(), Mock()]  # Mock frames for the enemy
        self.enemy.rect = pygame.Rect(100, 50, 50, 50)  # Initial position

    def test_enemy_movement(self):
        old_y = self.enemy.rect.y
        self.enemy.update()
        self.assertTrue(self.enemy.rect.y > old_y)

    def test_enemy_bounce(self):
        self.enemy.rect.x = 1  # Position near left edge
        self.enemy.advanced_movement = True
        self.enemy.update()
        self.assertTrue(self.enemy.x_speed > 0)  # Speed should have flipped to positive

if __name__ == '__main__':
    unittest.main()
