import pygame
import time
import random
from ship import Ship
from button import Button
from button import Game_Over
import game_functions as gf
from settings import Settings
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from scoreboard import Quit_State

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Set FPS
	FPS = 60
	clock = pygame.time.Clock()

	# Make a ship, a group of bullets, and a group of aliens.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	enemy_bullets = Group()
	aliens = Group()

	# Create an instance to store game statistics, a quit statement and create a scoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	qs = Quit_State(ai_settings, screen)

	# Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Make the Play and Game Over button.
	play_button = Button(ai_settings, screen, "PRESS ENTER")
	game_over = Game_Over(ai_settings, screen, "GAME OVER")

	# Load the high score.
	gf.load_score(stats)
	sb.prep_high_score()
	sb.show_score()

	# Start the main loop for the game.
	while True:
		clock.tick(FPS)
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb, enemy_bullets )
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb,
			 ship, aliens, bullets)
			gf.update_enemy_bullets(ai_settings, screen, stats, sb, ship, aliens, enemy_bullets)
			gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets, enemy_bullets, game_over)
		if not stats.game_active:
			game_over.draw_button()
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, qs, enemy_bullets, game_over)

run_game()