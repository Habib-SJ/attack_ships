import sys
import pygame

class AttackShips:
    # کلاسی برای مدیریت چیزهایی که داریم و رفتار بازی
    def __init__(self) -> None:
        # راه اندازی اولیه بازی 
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("ATTACK_SHIPS")
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.bg_color)



            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    atsh = AttackShips()
    atsh.run_game()