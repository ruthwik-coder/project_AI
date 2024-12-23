import math
import checkbox
import pygame
import time
import random
import astar
#from mossad import ui_Checkbox

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1024,512
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h =128,64
Matrix = [[1 for x in range(w)] for y in range(h)]
Matrix[88][32]=2
Matrix[89][32]=2
Matrix[88][33]=2
Matrix[89][33]=2
m_c=0
# //path0= [[0 for p123 in range(w)] for q123 in range(h)]
# //po=path0[m_c]
path0= [[1 for p123 in range(w)] for q123 in range(h)]
src=[0,0]
dest=[88,32]
mflag=True
l=0
clicked=False
pathu=[]
checkboxes = [
        checkbox.ui_Checkbox(WIN, 50, 50,1, caption="monsters"),
    checkbox.ui_Checkbox(WIN, 50, 100, 2, caption="walls"  ),#, isChecked=True)
checkbox.ui_Checkbox(WIN, 50, 150, 3, caption="DONE^_^"  )#, isChecked=True)

    ]
def draw(l,elapsed_time):
    font = pygame.font.SysFont("comicsans", 30)
    time_text = font.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    text_surface =font.render(f"Level: {l}", False, "pink")
    WIN.blit(text_surface, (50, 50))
def drawpath():

    pathu=astar.haha(Matrix,src,dest)
    if mflag == False:
        for lp in pathu:
            BG = pygame.transform.scale(pygame.image.load("images/monster1.png"), (8, 8))
            pygame.time.delay(1000)
            WIN.blit(BG, lp * 8)
    print("lol")


def main():
    global clicked, m_c
    run =True
    l=0
    clock = pygame.time.Clock()
    start_time = time.time()
    star_count = 0
    elapsed_time = 0
    while run:
        ev = pygame.event.get()
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        for event in ev:
            if event.type == pygame.QUIT or l==4:
                run = False
                break
            # In main game loop:

            for checkbox in checkboxes:
                checkbox.update_checkbox(event)
            if event.type==pygame.MOUSEBUTTONDOWN :
                clicked=True
            if event.type==pygame.MOUSEBUTTONUP :
                clicked=False


            for checkbox2 in checkboxes:

                if clicked==True and checkbox2.idnum == 2 and checkbox2.checked:
                 print("poop")
                 x,y=pygame.mouse.get_pos()
                 #print(x,y)
                 u,m=int(math.floor(x / 8.0)) ,int(math.floor(y / 8.0))
                 print(u,m)
                 Matrix[u][m]=0
                 path0[u][m]=0
                 p,q=int(math.floor(x / 8.0)) * 8,int(math.floor(y / 8.0)) * 8

                if  clicked==True and checkbox2.idnum == 1 and checkbox2.checked:
                    x, y = pygame.mouse.get_pos()
                    print("454")
                    # print(x,y)
                    u, m = int(math.floor(x / 8.0)), int(math.floor(y / 8.0))
                    #Matrix[u][m] = -1
                    src=[u,m]


                    p, q = int(math.floor(x / 8.0)) * 8, int(math.floor(y / 8.0)) * 8
                if clicked==True and checkbox2.idnum == 3 and checkbox2.checked:
                    mflag=False
                    drawpath()

        if int(elapsed_time) // 10 > l:
            l=l+1
            #rijngr
            draw(l, elapsed_time)

        WIN.fill((121, 168, 157))
        for i in range(h):
         for j in range(w):
                if Matrix[i][j] == -1  :
                    m_c=m_c+1
                    BG = pygame.transform.scale(pygame.image.load("images/monster1.png"), (8, 8))
                    WIN.blit(BG, (i * 8, j * 8))
                elif Matrix[i][j] == 0 :
                    BG = pygame.transform.scale(pygame.image.load("images/pixilart-drawing.png"), (8, 8))
                    WIN.blit(BG, (i * 8, j * 8))
                elif Matrix[i][j] == 2  :
                    BG=pygame.transform.scale(pygame.image.load("images/house.png"), (16, 16))
                    WIN.blit(BG, (704,256))


                else:
                    pygame.draw.rect(WIN, (121,168,157), (i * 8, j * 8, 8, 8))


        # Draw and update
         for checkbox in checkboxes:

            checkbox.render_checkbox()

        draw(l, elapsed_time)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()