import pygame
from pygame.sprite import Sprite
import random

class Bullet(Sprite):
	""" A class to manage bullets fired from the ship"""

	def __init__(self, ai_settings, screen, ship):
		"""Create a bullet object at the ship's current position"""
		super().__init__()
		self.screen = screen

		# Create a bullet rect at (0, 0) and then set correct position.
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#Store the bullet's position as a decimal value.
		self.y = float(self.rect.y)

		# Bullet properties
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor


	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal position of the bullet.
		self.y -= self.speed_factor
		# Update the rect position
		self.rect.y = self.y
		

	def draw_bullet(self):
		"""Draw the bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)

class Enemy_Bullet(Sprite):
	""" A class to manage bullets fired from the alien"""

	def __init__(self, ai_settings, screen, aliens):
		"""Create a bullet object at the alien's current position"""
		super().__init__()
		self.screen = screen

		# Create a bullet rect at (0, 0) and then set correct position.
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		enemies = []
		for alien in aliens:
			enemies.append(alien)
			alien = random.choice(enemies)
		self.rect.centerx = alien.rect.centerx
		self.rect.bottom = alien.rect.bottom

		# Store the bullet's position as a decimal value.
		self.y = float(self.rect.y)

		self.color = ai_settings.enemy_bullet_color
		self.speed_factor = ai_settings.enemy_bullet_speed_factor


	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal position of the bullet.
		self.y += self.speed_factor
		# Update the rect position
		self.rect.y = self.y

	def draw_enemy_bullet(self):
		"""Draw the bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
