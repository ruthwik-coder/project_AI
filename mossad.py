# import random
#
# #
# #
# # a=random.randint(1,250)
# #
# # print(a)(random.randint(1,255), random.randint(1,255), random.randint(1,255))
# # Creates a list containing 5 lists, each of 8 items, all set to 0
# # w, h = 8, 5
# # Matrix = [[1 for x in range(w)] for y in range(h)]
# # print (Matrix)
# # import pygame
# # import sys
# #
# # pygame.font.init()
# #
# # class ui_Checkbox:
# #     def __init__(self, surface, x, y, idnum, color=(230, 230, 230), caption="", outline_color=(0, 0, 0), check_color=(0, 0, 0), font_size=22,
# #                  font_color=(0, 0, 0), text_offset=(28, 1), font='Arial', isChecked=False):
# #         self.surface = surface
# #         self.x = x
# #         self.y = y
# #         self.color = color
# #         self.caption = caption
# #         self.oc = outline_color
# #         self.cc = check_color
# #         self.fs = font_size
# #         self.fc = font_color
# #         self.to = text_offset
# #         self.ft = font
# #
# #         # identification for removal and reorganization
# #         self.idnum = idnum
# #
# #         # checkbox object
# #         self.font = pygame.font.SysFont(self.ft, self.fs)
# #         self.font_surf = self.font.render(self.caption, True, self.fc)
# #         w, h = self.font.size(self.caption)
# #
# #         self.checkbox_obj = pygame.Rect(self.x + w + 24, self.y + 4, 12, 12)
# #         self.checkbox_outline = self.checkbox_obj.copy()
# #
# #         # variables to test the different states of the checkbox
# #         self.checked = isChecked
# #
# #     def _draw_button_text(self):
# #         w, h = self.font.size(self.caption)
# #         self.font_pos = (self.x, self.y + 12 / 2 - h / 2 + self.to[1])
# #         self.surface.blit(self.font_surf, self.font_pos)
# #
# #     def render_checkbox(self):
# #         self._draw_button_text()
# #         if self.checked:
# #             pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
# #             pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
# #             w, h = self.font.size(self.caption)
# #             pygame.draw.circle(self.surface, self.cc, (self.x + w + 30, self.y + 10), 4)
# #         elif not self.checked:
# #             pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
# #             pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
# #
# #     def _update(self, event_object):
# #         x, y = pygame.mouse.get_pos()
# #         px, py, w, h = self.checkbox_obj
# #         if px < x < px + w and py < y < py + h:
# #             if event_object.type == pygame.MOUSEBUTTONDOWN:
# #                 self.checked = not self.checked
# #
# #     def update_checkbox(self, event_object):
# #         self._update(event_object)
# #
# # def main():
# #     # Initialize Pygame
# #     pygame.init()
# #
# #     # Screen setup
# #     screen_width = 400
# #     screen_height = 300
# #     screen = pygame.display.set_mode((screen_width, screen_height))
# #     pygame.display.set_caption("Checkbox Demo")
# #
# #     # Background color
# #     background_color = (255, 255, 255)
# #
# #     # Create checkboxes
# #     checkboxes = [
# #         ui_Checkbox(screen, 50, 50, 1, caption="Option 1"),
# #         ui_Checkbox(screen, 50, 100, 2, caption="Option 2", isChecked=True),
# #         ui_Checkbox(screen, 50, 150, 3, caption="Option 3")
# #     ]
# #
# #     # Main game loop
# #     running = True
# #     clock = pygame.time.Clock()
# #
# #     while running:
# #         # Event handling
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 running = False
# #
# #             # Update checkboxes
# #             for checkbox in checkboxes:
# #                 checkbox.update_checkbox(event)
# #
# #         # Fill screen with background color
# #         screen.fill(background_color)
# #
# #         # Render checkboxes
# #         for checkbox in checkboxes:
# #             checkbox.render_checkbox()
# #
# #         # Update display
# #         pygame.display.flip()
# #
# #         # Control frame rate
# #         clock.tick(60)
# #
# #     # Quit Pygame
# #     pygame.quit()
# #     sys.exit()
#
# #!/usr/bin/env python3
#
# from PIL import Image
# import numpy as np
#
# # Open the maze image and make greyscale, and get its dimensions
# im = Image.open('images/maze3.png').convert('L')
# w, h = im.size
#
# # Ensure all black pixels are 0 and all white pixels are 1
# binary = im.point(lambda p: p > 128 and 1)
#
# # Resize to half its height and width so we can fit on Stack Overflow, get new dimensions
# binary = binary.resize((w,h),Image.NEAREST)
# w, h = binary.size
#
# # Convert to Numpy array - because that's how images are best stored and processed in Python
# nim = np.array(binary)
#
# # Print that puppy out
# for r in range(h):
#     for c in range(w):
#         poop=nim[r,c]
#         if poop==1:
#             poop=0
#         else:
#             poop=1
#         print(poop,end='')
#     print()
#
import pygame, sys, time

pygame.init()
pygame.display.set_caption("Towers of Hanoi")
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

game_done = False
framerate = 60

# game vars:
steps = 0
n_disks = 3
disks = []
towers_midx = [120, 320, 520]
pointing_at = 0
floating = False
floater = 0

# colors:
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
gold = (239, 229, 51)
blue = (78, 162, 196)
grey = (170, 170, 170)
green = (77, 206, 145)


def blit_text(screen, text, midtop, aa=True, font=None, font_name=None, size=None, color=(255, 0, 0)):
    if font is None:  # font option is provided to save memory if font is
        font = pygame.font.SysFont(font_name, size)  # already loaded and needs to be reused many times
    font_surface = font.render(text, aa, color)
    font_rect = font_surface.get_rect()
    font_rect.midtop = midtop
    screen.blit(font_surface, font_rect)


def menu_screen():  # to be called before starting actual game loop
    global screen, n_disks, game_done
    menu_done = False
    while not menu_done:  # every screen/scene/level has its own loop
        screen.fill(white)
        blit_text(screen, 'Towers of Hanoi', (323, 122), font_name='sans serif', size=90, color=grey)
        blit_text(screen, 'Towers of Hanoi', (320, 120), font_name='sans serif', size=90, color=gold)
        blit_text(screen, 'Use arrow keys to select difficulty:', (320, 220), font_name='sans serif', size=30,
                  color=black)
        blit_text(screen, str(n_disks), (320, 260), font_name='sans serif', size=40, color=blue)
        blit_text(screen, 'Press ENTER to continue', (320, 320), font_name='sans_serif', size=30, color=black)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    menu_done = True
                    game_done = True
                if event.key == pygame.K_RETURN:
                    menu_done = True
                if event.key in [pygame.K_RIGHT, pygame.K_UP]:
                    n_disks += 1
                    if n_disks > 6:
                        n_disks = 6
                if event.key in [pygame.K_LEFT, pygame.K_DOWN]:
                    n_disks -= 1
                    if n_disks < 1:
                        n_disks = 1
            if event.type == pygame.QUIT:
                menu_done = True
                game_done = True
        pygame.display.flip()
        clock.tick(60)


def game_over():  # game over screen
    global screen, steps
    screen.fill(white)
    min_steps = 2 ** n_disks - 1
    blit_text(screen, 'You Won!', (320, 200), font_name='sans serif', size=72, color=gold)
    blit_text(screen, 'You Won!', (322, 202), font_name='sans serif', size=72, color=gold)
    blit_text(screen, 'Your Steps: ' + str(steps), (320, 360), font_name='mono', size=30, color=black)
    blit_text(screen, 'Minimum Steps: ' + str(min_steps), (320, 390), font_name='mono', size=30, color=red)
    if min_steps == steps:
        blit_text(screen, 'You finished in minumum steps!', (320, 300), font_name='mono', size=26, color=green)
    pygame.display.flip()
    time.sleep(2)  # wait for 2 secs
    pygame.quit()  # pygame exit
    sys.exit()  # console exit


def draw_towers():
    global screen
    for xpos in range(40, 460 + 1, 200):
        pygame.draw.rect(screen, green, pygame.Rect(xpos, 400, 160, 20))
        pygame.draw.rect(screen, grey, pygame.Rect(xpos + 75, 200, 10, 200))
    blit_text(screen, 'Start', (towers_midx[0], 403), font_name='mono', size=14, color=black)
    blit_text(screen, 'Finish', (towers_midx[2], 403), font_name='mono', size=14, color=black)


def make_disks():
    global n_disks, disks
    disks = []
    height = 20
    ypos = 397 - height
    width = n_disks * 23
    for i in range(n_disks):
        disk = {}
        disk['rect'] = pygame.Rect(0, 0, width, height)
        disk['rect'].midtop = (120, ypos)
        disk['val'] = n_disks - i
        disk['tower'] = 0
        disks.append(disk)
        ypos -= height + 3
        width -= 23


def draw_disks():
    global screen, disks
    for disk in disks:
        pygame.draw.rect(screen, blue, disk['rect'])
    return


def draw_ptr():
    ptr_points = [(towers_midx[pointing_at] - 7, 440), (towers_midx[pointing_at] + 7, 440),
                  (towers_midx[pointing_at], 433)]
    pygame.draw.polygon(screen, red, ptr_points)
    return


def check_won():
    global disks
    over = True
    for disk in disks:
        if disk['tower'] != 2:
            over = False
    if over:
        time.sleep(0.2)
        game_over()


def reset():
    global steps, pointing_at, floating, floater
    steps = 0
    pointing_at = 0
    floating = False
    floater = 0
    menu_screen()
    make_disks()


menu_screen()
make_disks()
# main game loop:
while not game_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                reset()
            if event.key == pygame.K_q:
                game_done = True
            if event.key == pygame.K_RIGHT:
                pointing_at = (pointing_at + 1) % 3
                if floating:
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 100)
                    disks[floater]['tower'] = pointing_at
            if event.key == pygame.K_LEFT:
                pointing_at = (pointing_at - 1) % 3
                if floating:
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 100)
                    disks[floater]['tower'] = pointing_at
            if event.key == pygame.K_UP and not floating:
                for disk in disks[::-1]:
                    if disk['tower'] == pointing_at:
                        floating = True
                        floater = disks.index(disk)
                        disk['rect'].midtop = (towers_midx[pointing_at], 100)
                        break
            if event.key == pygame.K_DOWN and floating:
                for disk in disks[::-1]:
                    if disk['tower'] == pointing_at and disks.index(disk) != floater:
                        if disk['val'] > disks[floater]['val']:
                            floating = False
                            disks[floater]['rect'].midtop = (towers_midx[pointing_at], disk['rect'].top - 23)
                            steps += 1
                        break
                else:
                    floating = False
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 400 - 23)
                    steps += 1
    screen.fill(white)
    draw_towers()
    draw_disks()
    draw_ptr()
    blit_text(screen, 'Steps: ' + str(steps), (320, 20), font_name='mono', size=30, color=black)
    pygame.display.flip()
    if not floating: check_won()
    clock.tick(framerate)
