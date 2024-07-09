import pygame
class Ship:
    # کلاسی برای مدیریت جنگنده
    def __init__(self, ai_game) -> None:
        # تنظیم مکان اولیه 
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # پردازش تصویر 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # جنگنده جدید در پایین گنجره ایجاد شود
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        # کشیدن جنگنده در مکان واقعی
        self.screen.blit(self.image, self.rect)
