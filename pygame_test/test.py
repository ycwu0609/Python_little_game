import pygame
from pygame.locals import *
from sys import exit

#Set Sound Effect
def Glass_Effect():
    sound_effect = pygame.mixer.Sound("musics/glass3.wav")
    sound_effect.play()

#game's main code
def game_main():
    #Record pos
    broke_pos = []
    #Set bgm
    pygame.mixer.music.load("musics/If_I_Had_a_Chicken.mp3")
    pygame.mixer.music.play(10000)
    pygame.mixer.music.set_volume(0.5)
    
    my_font = pygame.font.SysFont("arial", 24)
    game_text = my_font.render("Press Mouse's Botton to hit, press R to refresh, and press space to back to index", True, (50, 50, 50), (255, 255, 255))
    
    while True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    
        "paste on the background image"
        screen.blit(game_main_background, (0,0))
        screen.blit(game_text, (10, 450), None, BLEND_RGB_MULT)
        for i in broke_pos:
            screen.blit(scar, i, None,BLEND_RGBA_SUB)
        
        "Deal with pressing mouse's button"
        if event.type == MOUSEBUTTONDOWN:
            "get mouse's current position"
            x, y = pygame.mouse.get_pos()
            x-=scar.get_width()/2
            y-=scar.get_height()/2
            screen.blit(scar, (x, y), None,BLEND_RGBA_SUB)
            broke_pos.append((x, y))
            Glass_Effect()
    
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                index_main()
            if event.key == K_r:
                del broke_pos[0:] 
        "update"
        pygame.display.update()
    
#index's main code
def index_main():
    pygame.mixer.music.load("musics/Spring_In_My_Step.mp3")
    pygame.mixer.music.play(10000)
    pygame.mixer.music.set_volume(0.5)
    
    my_font = pygame.font.SysFont("arial", 30)
    index_text = my_font.render("Press Mouse's Botton to Start.", True, (255, 255, 255), (0, 0, 0))
    
    while True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.blit(black, (0,0))        
        screen.blit(index_background, (0,0))
        screen.blit(index_text, (330, 450), None, BLEND_RGB_ADD)
        if event.type == MOUSEBUTTONDOWN:
            game_main()
        pygame.display.update()
    
        
if __name__ == '__main__':
    "assign image"
    game_background_image_filename = "images/percussion.jpg"
    index_background_image_filename = "images/GuaMiHaHa.png"
    scar_image_filename = "images/scar.png"
    black_image_filename = "images/black.png"
    glass_music_filename = "musics/broken.mp3"
    
    "Initialization"
    pygame.init()
    "create window"
    screen = pygame.display.set_mode((640, 480), 0, 32)
    "assign window's name"
    pygame.display.set_caption("878787878787")
    "import image"
    game_main_background = pygame.image.load(game_background_image_filename).convert()
    index_background = pygame.image.load(index_background_image_filename).convert()
    scar = pygame.image.load(scar_image_filename).convert()
    black = pygame.image.load(black_image_filename).convert()
    
   
    index_main()