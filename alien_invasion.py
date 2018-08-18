#coding=utf-8
# author: heimu
# 2018.8.18

import sys
import  pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
import game_functions as gf
from button import Button
from scoreboard import Scoreboard

def run_game():

    # 初始化游戏并创建一个屏幕对象

    pygame.init()   # 初始化背景设置
    ai_settings = Settings()    # 创建一个Settings实例
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # 指定屏幕尺寸
    pygame.display.set_caption("Alien Invasion")

    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,  aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)



run_game()