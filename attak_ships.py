import sys
import pygame
from settings import Settings
from ship import Ship

class AttackShips:
    # کلاسی برای مدیریت چیزهایی که داریم و رفتار بازی
    def __init__(self) -> None:
        # راه اندازی اولیه بازی 
        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("ATTACK_SHIPS")
        self.ship = Ship(self)
        #self.bg_color = self.settings.bg_color
    
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


            pygame.display.flip()
            self.clock.tick(60)
    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()


if __name__ == '__main__':
    atsh = AttackShips()
    atsh.run_game()