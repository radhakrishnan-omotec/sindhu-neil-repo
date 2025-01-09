import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Things and Places")
background = pygame.image.load('images/background.png')

def load_and_resize_image(image_path, size):
    image = pygame.image.load(image_path)
    return pygame.transform.scale(image, size)

keys = load_and_resize_image('images/keys.jpg', (135, 130))
glasses = load_and_resize_image('images/glasses.jpg', (135, 125))
wallet = load_and_resize_image('images/wallet.jpg', (135, 125))
medicines = load_and_resize_image('images/medicines.jpg', (135, 125))

k_holder = load_and_resize_image("images/key holder.jpg", (135, 125))
organiser = load_and_resize_image('images/organiser.jpg', (135, 125))
medi_cabinet = load_and_resize_image('images/Medicine-cabinet.jpg', (135, 125))
drawer = load_and_resize_image('images/drawer.jpg', (135, 125))

row1 = [keys, glasses, wallet, medicines]
row2 = []  
row3 = [k_holder, organiser, medi_cabinet, drawer]

correct_sequence = [k_holder, organiser, drawer, medi_cabinet]

dragging = False
dragged_image = None
original_row = None
original_index = -1
game_completed = False

def draw_columns():
    cell_width = 145
    cell_height = 155

    for index, img in enumerate(row1):
        screen.blit(img, (50 + index * cell_width, 50))

    for index, img in enumerate(row2):
        screen.blit(img, (50 + index * cell_width, 200))

    for index, img in enumerate(row3):
        screen.blit(img, (50 + index * cell_width, 450))

def get_image_at_position(x, y, row, row_offset):
    for index, img in enumerate(row):
        img_rect = img.get_rect(topleft=(50 + index * 145, row_offset))
        if img_rect.collidepoint(x, y):
            return index
    return None

def check_level_complete():
    return row2 == correct_sequence

def display_congratulations():
    font = pygame.font.SysFont('Arial', 36)
    text = font.render("Congratulations! You completed the level!", True, (255, 255, 0))
    screen.blit(text, (WIDTH //8, HEIGHT // 2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                if game_completed:
                    continue
                index = get_image_at_position(event.pos[0], event.pos[1], row3, 450)
                if index is not None:
                    dragging = True
                    dragged_image = row3[index]
                    original_row = row3  
                    original_index = index  
                    row3.pop(index)  
                else:
                    index = get_image_at_position(event.pos[0], event.pos[1], row2, 200)
                    if index is not None:
                        dragging = True
                        dragged_image = row2[index]
                        original_row = row2  
                        original_index = index  
                        row2.pop(index)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and dragging:
                if not game_completed:
                    if 200 < event.pos[1] < 325:  
                        row2.append(dragged_image)
                    elif 450 < event.pos[1] < 575:  
                        row3.append(dragged_image)
                    else:
                        original_row.insert(original_index, dragged_image)
                    dragging = False
                    dragged_image = None
                    original_row = None
                    original_index = -1
                if check_level_complete():
                    game_completed = True
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    draw_columns()
    if dragging and dragged_image:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(dragged_image, (mouse_x, mouse_y))
    if game_completed:
        display_congratulations()
    pygame.display.flip()
