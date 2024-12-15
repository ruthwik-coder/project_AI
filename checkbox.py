# checkbox.py
import pygame

pygame.font.init()


class ui_Checkbox:
    def __init__(self, surface, x, y, idnum, color=(230, 230, 230), caption="", outline_color=(0, 0, 0),
                 check_color=(0, 0, 0), font_size=14, font_color=(0, 0, 0), text_offset=(28, 1),
                 font='Arial Black', isChecked=False):
        eyed  =1
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.caption = caption
        self.oc = outline_color
        self.cc = check_color
        self.fs = font_size
        self.fc = font_color
        self.to = text_offset
        self.ft = font
        self.idnum = idnum

        # Initialize font and text
        self.font = pygame.font.SysFont(self.ft, self.fs)
        self.font_surf = self.font.render(self.caption, True, self.fc)
        self.text_width, self.text_height = self.font.size(self.caption)

        # Position checkbox after text
        self.checkbox_obj = pygame.Rect(self.x + self.text_width + 10, self.y, 20, 20)
        self.checkbox_outline = self.checkbox_obj.copy()

        self.checked = isChecked

    def _draw_button_text(self):
        self.surface.blit(self.font_surf, (self.x, self.y + self.to[1]))

    def render_checkbox(self):
        self._draw_button_text()
        pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
        pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)

        if self.checked:
            pygame.draw.circle(self.surface, self.cc,
                               (self.checkbox_obj.centerx, self.checkbox_obj.centery), 8)


    def update_checkbox(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.checkbox_obj.collidepoint(mouse_pos):
                self.checked = not self.checked

                return True
        return False