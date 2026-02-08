from random import randint
import os, sys
import pandas as pd
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#os.environ.setdefault("MPLCONFIGDIR", os.path.join(tempfile.gettempdir(), "mplconfig"))

#def resource_path(relative_path):
#    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
#    return os.path.join(base, relative_path)

font_path = os.getcwd()+"\\fonts\\NotoSansJP-Medium.ttf"

kanji_df=pd.read_excel(os.getcwd()+'\\kanji_bank.xlsx')
kanji_dict=dict()

for i in kanji_df.iterrows():
    kanji_dict[i[1]['Reading']]=i[1]['Kanji']

mode_setter=False
while mode_setter not in ['1','2']:
    mode_setter=input('["1" or "2"] Choose PERFORMANCE or REMINISCENCE modes')

if mode_setter=='1':
    kanji_dict_game={k:v for v,k in kanji_dict.copy().items()}
else:
    kanji_dict_game=kanji_dict.copy()


pygame.init()

WIDTH=1200
HEIGHT=720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
cpt="KANJI PERFORMANCE" if mode_setter=='1' else "KANJI REMINISCENCE"
pygame.display.set_caption(cpt)
running=True

while running:
    while kanji_dict_game:
        screen.fill(WHITE)

        choice=randint(a=0,b=len(kanji_dict_game)-1)
        answer=list(kanji_dict_game.keys())[choice]
        letter=list(kanji_dict_game.values())[choice]
        
        waiting=True
        conclude=False

        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    conclude=True
                    pygame.quit()
                    break
                if event.type == pygame.KEYDOWN:
                    waiting = False
            if conclude:
                break
            
            if mode_setter=='1':
                custom_font = pygame.font.Font(font_path, 30)
            else:
                custom_font = pygame.font.Font(font_path, 100)

            text=custom_font.render(letter,True,BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()
        
        if conclude:
            break

        kanji_dict_game.pop(answer)

        waiting=True
        while waiting:
            screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    conclude=True
                    pygame.quit()
                    break
                if event.type == pygame.KEYDOWN:
                    waiting = False
                
            if conclude:
                break

            if mode_setter=='1':
                custom_font = pygame.font.Font(font_path, 100)
            else:
                custom_font = pygame.font.Font(font_path, 30)

            text=custom_font.render(answer,True,BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()

        if conclude:
            break

    running=False

pygame.quit()