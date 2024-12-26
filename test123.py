import math
import checkbox
import pygame
import time
import random
import astar2

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 1024, 512
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

w, h = 128, 64
Matrix = [[0 for x in range(w)] for y in range(h)]
m_c = -1  # Start from -1 so first monster will be 0
path0 = [[1 for p123 in range(w)] for q123 in range(h)]
clicked = False
monster_move_timer = 0
MONSTER_MOVE_INTERVAL = 5 # Milliseconds between moves

checkboxes = [
    checkbox.ui_Checkbox(WIN, 50, 50, 1, caption="monsters"),
    checkbox.ui_Checkbox(WIN, 50, 100, 2, caption="walls"),
    checkbox.ui_Checkbox(WIN, 50, 150, 3, caption="DONE^_^")
]


def draw(l, elapsed_time):
    font = pygame.font.SysFont("comicsans", 30)
    time_text = font.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    text_surface = font.render(f"Level: {l}", False, "pink")
    WIN.blit(text_surface, (50, 50))


def main():
    MAX_MONSTERS = 200
    monsters = []  # Start with empty list
    monster_active = [False] * MAX_MONSTERS  # Track which monsters are active
    player = pygame.Rect(704, 256, 16, 16)
    global clicked, m_c
    monsters_moving = False

    run = True
    l = 0
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    last_move_time = pygame.time.get_ticks()

    while run:
        current_time = pygame.time.get_ticks()
        ev = pygame.event.get()
        clock.tick(60)
        elapsed_time = time.time() - start_time
        monster_image = pygame.transform.scale(pygame.image.load("images/monster1.png"), (8, 8))
        player_image = pygame.transform.scale(pygame.image.load("images/house.png"), (16, 16))

        for event in ev:
            if event.type == pygame.QUIT or l == 20:
                run = False
                break

            for checkbox in checkboxes:
                checkbox.update_checkbox(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False

            for checkbox2 in checkboxes:
                if clicked and checkbox2.idnum == 2 and checkbox2.checked:
                    x, y = pygame.mouse.get_pos()
                    u, m = int(x // 8), int(y // 8)
                    Matrix[m][u] = 1

                if clicked and checkbox2.idnum == 1 and checkbox2.checked:
                    m_c += 1
                    if m_c < MAX_MONSTERS:
                        x, y = pygame.mouse.get_pos()
                        u, m = int(x // 8), int(y // 8)
                        monsters.append(pygame.Rect(u * 8, m * 8, 16, 16))
                        monster_active[m_c] = True

                if clicked and checkbox2.idnum == 3 and checkbox2.checked:
                    monsters_moving = True

        # Move monsters if DONE was pressed and enough time has passed
        if monsters_moving and current_time - last_move_time >= MONSTER_MOVE_INTERVAL:
            last_move_time = current_time

            for i, monster in enumerate(monsters):
                if not monster_active[i]:
                    continue

                # Calculate path from monster to player
                start_x = int(monster.x // 8)
                start_y = int(monster.y // 8)
                end_x = int(player.x // 8)
                end_y = int(player.y // 8)

                # Ensure coordinates are within bounds
                start_x = max(0, min(w - 1, start_x))
                start_y = max(0, min(h - 1, start_y))
                end_x = max(0, min(w - 1, end_x))
                end_y = max(0, min(h - 1, end_y))

                path = astar2.haha(Matrix, (start_y, start_x), (end_y, end_x))

                if path and len(path) > 1:
                    next_pos = path[1]
                    monster.x = next_pos[1] * 8
                    monster.y = next_pos[0] * 8

                # Check collision with player
                if monster.colliderect(player):
                    run = False
                    print("Game Over!")
                    break

        # Drawing
        WIN.fill((121, 168, 157))

        # Draw walls
        for i in range(h):
            for j in range(w):
                if Matrix[i][j] == 1:
                    wall_img = pygame.transform.scale(pygame.image.load("images/pixilart-drawing.png"), (8, 8))
                    WIN.blit(wall_img, (j * 8, i * 8))

        # Draw active monsters
        for i, monster in enumerate(monsters):
            if monster_active[i]:
                WIN.blit(monster_image, monster)

        # Draw player
        WIN.blit(player_image, player)

        # Draw checkboxes
        for checkbox in checkboxes:
            checkbox.render_checkbox()

        draw(l, elapsed_time)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()