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
p=51
if p%5==0:
    print("grg")
