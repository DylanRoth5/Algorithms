import pygame

pygame.init()

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Enigma Machine')


# define font
font = pygame.font.SysFont('arialblack',20)
# define color
text_col = (255,255,255)


def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y)) 

run = True
while run:
    screen.fill((0,0,0))
    draw_text('hello',font,text_col,160,250)
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('pause') 
        # quit game
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
