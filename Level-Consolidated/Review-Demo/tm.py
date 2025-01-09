import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
width, height = 1200, 600
canvas = pygame.display.set_mode((width, height))
background_image = pygame.image.load("main_bg.jpg")
background_image = pygame.transform.scale(background_image, (width, height))
pygame.display.set_caption("Game Menu")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
button_color = (100, 150, 255)
hover_color = (150, 200, 255)

# Fonts
font = pygame.font.SysFont("Arial", 40)
button_font = pygame.font.SysFont("Arial", 30)
canvas.blit(background_image, (0, 0))
# Button class for easy button handling
class Button:
    def __init__(self, x, y, width, height, color, hover_color, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.action = action
    
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        
        # Draw the text
        text_surface = button_font.render(self.text, True, black)
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
                                  self.rect.y + (self.rect.height - text_surface.get_height()) // 2))
    
    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]
        if self.rect.collidepoint(mouse_pos) and mouse_click:
            return True
        return False

# Level 1 function (Placeholder for your level 1 game)
def level_1():
    pygame.init()
    
    # Screen setup
    width, height = 1200, 600
    canvas = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Breakfast")
    color = (255, 255, 255)
    canvas.fill(color)
    
    # Fonts and colors
    font = pygame.font.Font(None, 36)
    message_font = pygame.font.SysFont("Arial", 24)
    button_color = (200, 200, 200)
    hover_color = (150, 150, 150)
    message_color = (150, 150, 150)
    
    # Load images
    images = {
        "table": pygame.image.load('level1/level1/Images/kitchentable.png'),
        "bread": pygame.image.load('level1/level1/Images/bread.png'),
        "plate": pygame.image.load('level1/level1/Images/plate.png'),
        "cheese": pygame.image.load('level1/level1/Images/Cheeseslice.jpg'),
        "lettuce": pygame.image.load('level1/level1/Images/lettuce.png'),
        "onion": pygame.image.load('level1/level1/Images/Onion slice.png'),
        "tomato": pygame.image.load('level1/level1/Images/TomatoSlice.jpg'),
        "bread_layer": pygame.image.load('level1/level1/Images/breadsl.png'),
        "lettuce_layer": pygame.image.load('level1/level1/Images/lettuce2.png'),
        "cheese_layer": pygame.image.load('level1/level1/Images/Cheesesl.png'),
        "onion_layer": pygame.image.load('level1/level1/Images/OS.png'),
        "tomato_layer": pygame.image.load('level1/level1/Images/TS.png'),
        "plate_final": pygame.image.load('level1/level1/Images/plate2.png')
    }
    
    # Back button
    back_button = Button(850, 500, 100, 50, button_color, hover_color, "Back", return_to_menu)
    
    # Ingredient positions
    rows, cols = 3, 2
    cell_width, cell_height = 120, 120
    tab_width, tab_height = 820, 10
    ingredient_positions = {}
    row_col_to_image = [
        ("bread", (0, 0)),
        ("plate", (0, 1)),
        ("cheese", (1, 0)),
        ("lettuce", (1, 1)),
        ("onion", (2, 0)),
        ("tomato", (2, 1))
    ]
    for name, (row, col) in row_col_to_image:
        x = col * cell_width + tab_width
        y = row * cell_height + tab_height
        ingredient_positions[name] = (x, y)
    
    # Game state
    selected_sequence = []
    required_sequence = ["plate", "bread", "cheese", "lettuce", "onion", "tomato", "bread"]
    message = ""
    game_completed = False

    def draw_message(message_text):
        """Display a message on the bottom of the screen."""
        canvas.fill((255, 255, 255), (0, height - 50, width, 50))
        text = message_font.render(message_text, True, message_color)
        text_rect = text.get_rect(center=(width // 2, height - 25))
        canvas.blit(text, text_rect)

    while True:
        canvas.fill(color)
        canvas.blit(images["table"], (5, 5))
        
        # Draw ingredients
        for name, pos in ingredient_positions.items():
            canvas.blit(images[name], pos)
        
        # Draw back button
        back_button.draw(canvas)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif back_button.is_pressed():
                return_to_menu()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for name, rect_pos in ingredient_positions.items():
                    rect = images[name].get_rect(topleft=rect_pos)
                    if rect.collidepoint(event.pos):
                        if name == required_sequence[len(selected_sequence)]:
                            selected_sequence.append(name)
                            message = f"{name.capitalize()} added!"
                            if name == "bread" and len(selected_sequence) == len(required_sequence):
                                message = "Sandwich is ready! Enjoy!"
                                game_completed = True
                        else:
                            message = f"Wrong ingredient! Start over."
                            selected_sequence = []

        draw_message(message)
        pygame.display.flip()


# Level 2 function (Placeholder for your level 2 game)
def level_2():
    #def level_2(return_to_menu):
    import pygame
    import sys

    pygame.init()
    WIDTH, HEIGHT = 800, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Things and Places")
    background = pygame.image.load('./level2/images/background.png')

    button_color = (200, 200, 200)
    hover_color = (150, 150, 150)
    back_button = Button(50, 600, 150, 50, button_color, hover_color, "Back", return_to_menu)

    def load_and_resize_image(image_path, size):
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, size)

    keys = load_and_resize_image('./level2/images/keys.jpg', (135, 130))
    glasses = load_and_resize_image('./level2/images/glasses.jpg', (135, 125))
    wallet = load_and_resize_image('./level2/images/wallet.jpg', (135, 125))
    medicines = load_and_resize_image('./level2/images/medicines.jpg', (135, 125))

    k_holder = load_and_resize_image("./level2/images/key holder.jpg", (135, 125))
    organiser = load_and_resize_image('./level2/images/organiser.jpg', (135, 125))
    medi_cabinet = load_and_resize_image('./level2/images/Medicine-cabinet.jpg', (135, 125))
    drawer = load_and_resize_image('./level2/images/drawer.jpg', (135, 125))

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
        screen.blit(text, (WIDTH // 8, HEIGHT // 2))

    while True:
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        draw_columns()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    return_to_menu()
                    return
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

        if dragging and dragged_image:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.blit(dragged_image, (mouse_x - 67, mouse_y - 62))  # Adjusting for image center

        if game_completed:
            display_congratulations()

        back_button.draw(screen)
        pygame.display.flip()

# Level 3 function (Placeholder for your level 3 game)
import pygame


def level_3():
    # Initialize pygame
    pygame.init()

    # Screen setup
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pictures and Frames")

    # Load wall background
    wall_image = pygame.image.load("./level3/Images/wall.jpeg")
    wall_rect = wall_image.get_rect()

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    for_msg = (150, 150, 150)

    # Load and scale images
    occasion_images = {
        "birthday": pygame.image.load("./level3/Images/HB1.jpg"),
        "holiday": pygame.image.load("./level3/Images/vacay1.jpg"),
        "wedding": pygame.image.load("./level3/Images/Wed1.jpg"),
        "easter": pygame.image.load("./level3/Images/easter1.jpg"),
        "christmas": pygame.image.load("./level3/Images/christmas.jpg"),
        "friends": pygame.image.load("./level3/Images/friends21.png"),
    }
    image_size = (185, 130)
    for key in occasion_images:
        occasion_images[key] = pygame.transform.scale(occasion_images[key], image_size)

    # Frames and image positions
    frames = {
        "birthday": pygame.Rect(50, 50, 200, 150),
        "holiday": pygame.Rect(300, 50, 200, 150),
        "wedding": pygame.Rect(550, 50, 200, 150),
        "easter": pygame.Rect(50, 250, 200, 150),
        "christmas": pygame.Rect(300, 250, 200, 150),
        "friends": pygame.Rect(550, 250, 200, 150),
    }
    image_positions = {
        "birthday": pygame.Rect(50, 450, 185, 130),
        "holiday": pygame.Rect(150, 450, 185, 130),
        "wedding": pygame.Rect(250, 450, 185, 130),
        "easter": pygame.Rect(350, 450, 185, 130),
        "christmas": pygame.Rect(450, 450, 185, 130),
        "friends": pygame.Rect(550, 450, 185, 130),
    }

    # Dragging variables
    dragging = False
    dragged_image = None
    offset_x, offset_y = 0, 0
    message = ""
    font = pygame.font.SysFont("Arial", 24)

    # Back Button setup
    def return_to_menu():
        print("Returning to menu...")
        return  # Replace with your menu logic

    back_button = Button(700, 15, 50, 25, (200, 200, 200), (150, 150, 150), "<<", return_to_menu)

    def draw_frames():
        """Draw black rectangles for frames."""
        for frame in frames.values():
            pygame.draw.rect(screen, BLACK, frame, 6)

    def draw_images():
        """Draw images at their current positions."""
        for key, img in occasion_images.items():
            screen.blit(img, image_positions[key])

    def is_inside_frame(image_rect, frame_rect):
        """Check if an image is inside its corresponding frame."""
        return frame_rect.contains(image_rect)

    def draw_message(message_text):
        """Display a message at the bottom of the screen."""
        text = font.render(message_text, True, for_msg)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 50))

    # Main game loop
    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(wall_image, wall_rect)
        draw_frames()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if back_button.is_pressed():
                    #back_button.action()
                    return_to_menu()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    #running = False  # Exit level logic

                if event.button == 1:  # Left-click
                    for key, img_rect in image_positions.items():
                        if img_rect.collidepoint(event.pos):
                            dragging = True
                            dragged_image = key
                            offset_x = img_rect.x - event.pos[0]
                            offset_y = img_rect.y - event.pos[1]
                            break
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and dragging:
                    image_rect = image_positions[dragged_image]
                    if is_inside_frame(image_rect, frames[dragged_image]):
                        message = f"Correct! {dragged_image.capitalize()} picture placed."
                    else:
                        message = f"Wrong! {dragged_image.capitalize()} picture not placed correctly."
                    dragging = False
                    dragged_image = None
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_x, mouse_y = event.pos
                    image_positions[dragged_image].topleft = (mouse_x + offset_x, mouse_y + offset_y)

        draw_images()

        # Highlight dragged image
        if dragging:
            img_rect = image_positions[dragged_image]
            frame_rect = frames[dragged_image]
            color = GREEN if is_inside_frame(img_rect, frame_rect) else RED
            pygame.draw.rect(screen, color, img_rect, 2)

        # Draw Back Button
        back_button.draw(screen)

        # Display message
        draw_message(message)

        pygame.display.flip()

    pygame.quit()
# Level 4 function (Placeholder for your level 4 game)
def level_4():
    pygame.init()

    # Display setup
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Activity of the Day")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 150, 150)
    RED = (255, 0, 0)

    # Fonts
    font_large = pygame.font.SysFont("Arial", 48)
    font_medium = pygame.font.SysFont("Arial", 36)
    font_small = pygame.font.SysFont("Arial", 24)

    # Activities data
    activities = [
        # Example data as in the original code
        # (Use your original activity details here)
        # ...
    ]

    current_day = 0

    def display_activity(activity):
        screen.fill(WHITE)

        # Activity content
        wish_text = font_medium.render(activity['wish'], True, RED)
        screen.blit(wish_text, (50, 20))

        name_text = font_large.render(f"Activity: {activity['name']}", True, BLACK)
        screen.blit(name_text, (50, 80))

        description_text = font_medium.render(activity['description'], True, BLACK)
        screen.blit(description_text, (50, 140))

        place_text = font_medium.render(f"Location: {activity['place']}", True, BLACK)
        screen.blit(place_text, (50, 200))

        time_text = font_medium.render(f"Time: {activity['time']}", True, BLACK)
        screen.blit(time_text, (50, 260))

        duration_text = font_medium.render(f"Duration: {activity['duration']}", True, BLACK)
        screen.blit(duration_text, (50, 320))

        # Current date
        current_date = datetime.date.today()
        date_text = font_small.render(f"Today's Date: {current_date}", True, BLACK)
        screen.blit(date_text, (45, 380))

    def return_to_menu():
        print("Returning to menu...")
        return  # Replace with your menu logic

    # Buttons
    next_button = Button(WIDTH // 2 - 100, HEIGHT - 100, 200, 50, GREEN, (0, 200, 200), "Next Activity", None)
    back_button = Button(10, 10, 100, 50, (200, 200, 200), (150, 150, 150), "Back", return_to_menu)

    clock = pygame.time.Clock()
    running = True

    while running:
        # Get current activity
        activity = activities[current_day]

        # Display activity
        display_activity(activity)

        # Draw buttons
        next_button.draw(screen)
        back_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.is_pressed():
                    current_day = (current_day + 1) % len(activities)
                elif back_button.is_pressed():
                    back_button.action()
                    running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Main menu function
def main_menu():
    running = True
    level_buttons = [
        Button(100, 100, 200, 50, button_color, hover_color, "Level 1", start_level_1),
        Button(100, 200, 200, 50, button_color, hover_color, "Level 2", start_level_2),
        Button(100, 300, 200, 50, button_color, hover_color, "Level 3", start_level_3),
        Button(100, 400, 200, 50, button_color, hover_color, "Level 4", start_level_4),
    ]
    
    while running:
        
        #canvas.fill(white)

        # Draw title text
        title_text = font.render("Game Menu", True, black)
        canvas.blit(title_text, (width // 2 - title_text.get_width() // 2, 50))

        # Draw level selection buttons
        for button in level_buttons:
            button.draw(canvas)

        # Check if any button was pressed
        for button in level_buttons:
            if button.is_pressed():
                button.action()  # Start the corresponding level function

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Close the game
        
        pygame.display.update()

# Function to handle the transition from level to main menu
def return_to_menu():
    main_menu()  # Calls the main menu function again

# Functions to start each level
def start_level_1():
    level_1()

def start_level_2():
    level_2()

def start_level_3():
    level_3()

def start_level_4():
    level_4()

# Run the main menu
main_menu()
