import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	"""A class to report scoring information."""

	def __init__(self, ai_settings, screen, stats):
		"""Initialize scorekeeping attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		# Font settings for scoring information.
		self.text_color = (200, 200, 200)
		self.font = pygame.font.Font('font/invasion.TTF', 30)

		# Prepare the initial score images.
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()


	def prep_score(self):
		"""Turn the score into a rendered image."""
		rounded_score = int(round(self.stats.score, -1))
		score_str = "SCORE: " + "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

		# Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.left = self.screen_rect.left + 20
		self.score_rect.top = 20

	def prep_high_score(self):
		"""Turn the high score into a rendered image."""
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "HIGH SCORE: " + "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

		# Center the high score at the top fo the screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		"""Turn the level into a rendered image."""
		level = "LEVEL: " + str(self.stats.level)
		self.level_image = self.font.render(level, True, self.text_color, self.ai_settings.bg_color)

		# Position the level below the score.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.left = self.score_rect.left
		self.level_rect.top = self.score_rect.bottom + 5

	def prep_ships(self):
		"""Show how many ships are left."""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left + 1):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = self.ai_settings.screen_width - ship.rect.width - ship_number * ship.rect.width - 10
			ship.rect.y = 10
			self.ships.add(ship)


	def show_score(self):
		"""Draw scores and ships to the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)


class Quit_State():
	def __init__(self, ai_settings, screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings

		# Font settings for scoring information.
		self.text_color = (0, 0, 0)
		self.font = pygame.font.Font('font/invasion.TTF', 40)

		self.quit_statement(ai_settings)

	def quit_statement(self, ai_settings):
		quit_state = "'q' to quit"
		self.font = pygame.font.Font('font/invasion.TTF', 20)
		self.quit_state = self.font.render(quit_state, True, self.text_color, (71, 230, 44))
		self.quit_rect = self.quit_state.get_rect()
		self.quit_rect.center = self.screen_rect.center
		self.quit_rect.centery = self.screen_rect.centery + 135
		# self.quit_rect.center = self.screen_rect.right - 20
		# self.quit_rect.top = 20

	def show_quit(self):
		self.screen.blit(self.quit_state, self.quit_rect)
