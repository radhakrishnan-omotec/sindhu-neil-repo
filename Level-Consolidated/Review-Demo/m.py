import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
width, height = 1200, 600
canvas = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Menu")
background_image = pygame.image.load("main_bg.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
button_color = (100, 150, 255)
hover_color = (150, 200, 255)

# Fonts
font = pygame.font.SysFont("Arial", 40)
button_font = pygame.font.SysFont("Arial", 30)
# Button class for easy button handling

class Button:
    def __init__(self, x, y, width, height, color, hover_color, text, action):
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
    position=(5,5)
    color=(255,255,255)
    width,height=1200,600
    canvas=pygame.display.set_mode((width,height))
    font = pygame.font.Font(None, 36)
    for_msg= (150,150, 150)
    
    #print("Level 1 Started!")
    button_color = (200, 200, 200)
    hover_color = (150, 150, 150)
    back_button = Button(1100, 15, 50, 25, (200, 200, 200), (150, 150, 150), "<<", return_to_menu)
    #back_button = Button(50, 500, 150, 50, button_color, hover_color, "Back", return_to_menu)

    plate2=pygame.image.load('level1/level1/Images/plate2.png')
    bread2=pygame.image.load('level1/level1/Images/breadsl.png')
    lettuce2=pygame.image.load('level1/level1/Images/lettuce2.png')
    cheese2=pygame.image.load('level1/level1/Images/Cheesesl.png')
    tomatosl=pygame.image.load('level1/level1/Images/TS.png')
    onionsl=pygame.image.load('level1/level1/Images/OS.png')
    image1 = pygame.image.load('level1/level1/Images/bread.png')
    b_rect=image1.get_rect()
    image2 = pygame.image.load('level1/level1/Images/plate.png')
    pl_rect=image2.get_rect()
    image3=pygame.image.load('level1/level1/Images/Cheeseslice.jpg')
    ch_rect=image3.get_rect()
    image4=pygame.image.load('level1/level1/Images/lettuce.png')
    lt_rect=image4.get_rect()
    image5=pygame.image.load('level1/level1/Images/Onion slice.png')
    sl_rect=image5.get_rect()
    image6=pygame.image.load('level1/level1/Images/TomatoSlice.jpg')
    ts_rect=image6.get_rect()

    rows, cols = 3, 2
    cell_width, cell_height = 120, 120

    pygame.display.set_caption("Breakfast")

    img=pygame.image.load('level1/level1/Images/kitchentable.png')

    rect1=img.get_rect()
    table_width,table_height=((rect1.width)/2,(rect1.height)/2)
    print(table_width,table_height)
    tabwidth=820
    tabheight=10
    exit=False
    foreground_position = False
    canvas.fill(color)
    canvas.blit(img,dest=position)
    message = ""  
    font = pygame.font.SysFont("Arial", 24)
    def draw_message(message_text):
        canvas.fill((255,255 , 255), (0, height - 50, width, 50))
        text = font.render(message_text, True, for_msg)
        message_area=canvas.blit(text, (width // 2 - text.get_width() // 2, height - 50))
        canvas.blit(text,message_area)
      
    br_fl=0
    ch_fl=0
    ts_fl=0
    os_fl=0
    lt_fl=0
    br_cntr=0
    pl_fl=0
        #def draw_table(tablearea,)
    for row in range(rows):
        for col in range(cols):
            x = col * cell_width+tabwidth
            y = row * cell_height+tabheight
            if row == 0 and col == 0:
                canvas.blit(image1,(x,y) )   
                b_rect.topleft=(x,y)
            elif row == 0 and col == 1:
                canvas.blit(image2, (x, y))
                pl_rect.topleft=(x,y)
            elif row==1 and col==0:
                canvas.blit(image3,(x,y))
                ch_rect.topleft=(x,y)
            elif row==1 and col==1:
                canvas.blit(image4,(x,y))
                lt_rect.topleft=(x,y)
            elif row==2 and col==0:
                canvas.blit(image5,(x,y))
                sl_rect.topleft=(x,y)
            elif row==2 and col==1:
                canvas.blit(image6,(x,y))
                ts_rect.topleft=(x,y)
            
    while not exit:
        #level_text = font.render("Level 1", True, black)
        #canvas.blit(level_text, (width // 2 - level_text.get_width() // 2, height // 3))

        # Draw Back Button
        back_button.draw(canvas)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    exit=True
            if back_button.is_pressed():
                return_to_menu()
                return
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    print("Clicked!")
                elif pl_rect.collidepoint(event.pos):
                    canvas.blit(plate2, (305,90))
                    pl_fl=1
                elif b_rect.collidepoint(event.pos):
                    if pl_fl==1 and br_cntr!=2:
                        canvas.blit(bread2, (355,173))
                        br_fl=1
                        br_cntr+=1
                    else:
                        message=f"Plate has to be taken first"
                elif  ch_rect.collidepoint(event.pos):
                    if br_fl==1:
                        canvas.blit(cheese2, (380,160))
                        ch_fl=1
                    else:
                        message=f"Bread has to selected"
                elif  lt_rect.collidepoint(event.pos):
                    if br_fl==1:
                        canvas.blit(lettuce2, (380,190))
                        lt_fl=1
                    else:
                        message=f"Bread has to selected"
                elif  sl_rect.collidepoint(event.pos):
                    if br_fl==1:
                        canvas.blit(onionsl, (395,170))
                        os_fl=1
                    else:
                        message=f"Bread has to selected"
                elif  ts_rect.collidepoint(event.pos):
                    if br_fl==1:
                        canvas.blit(tomatosl,(380,160))
                        ts_fl=1
                    else:
                        message=f"Bread has to selected"
                #if br_cntr!=2:
                #   print("it would be nice if bread is placed on top and at last too!")
                if br_cntr==2 and (ch_fl==1 or ts_fl==1 or os_fl==1 or lt_fl==1):
                    message=f"Sandwich is ready!!"
        draw_message(message)
        pygame.display.update()
    pygame.display.flip()
    pygame.quit()
    # Your code to start level 1

# Level 2 function (Placeholder for your level 2 game)
def level_2():
    import pygame
    import sys
    pygame.init()
    WIDTH, HEIGHT = 800, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Things and Places")
    background = pygame.image.load('./level2/images/background.png')
    
    button_color = (200, 200, 200)
    hover_color = (150, 150, 150)
    back_button = Button(700, 15, 50, 25, (200, 200, 200), (150, 150, 150), "<<", return_to_menu)
    
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
        screen.blit(text, (WIDTH //8, HEIGHT // 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if back_button.is_pressed():
                return_to_menu()
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
        back_button.draw(screen)
        pygame.display.flip()

# Level 3 function (Placeholder for your level 3 game)
def level_3():
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
    #def return_to_menu():
        #print("Returning to menu...")
        #return  # Replace with your menu logic

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
        #screen.fill(WHITE)
        screen.blit(wall_image, wall_rect)
        draw_frames()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if back_button.is_pressed():
                return_to_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #if back_button.is_pressed():
                 #   back_button.action()
                    #running = False  # Exit level logic
                  #  return_to_menu()
                    
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
    import pygame
    import datetime

    # Initialize pygame
    pygame.init()

    # Set up display
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Activity of the Day")

    exercise_image = pygame.image.load("./level4/Images/exercise.png")
    exercise_rect = exercise_image.get_rect()

    breakfast_image = pygame.image.load("./level4/Images/breakfast.jpg")
    breakfast_rect = breakfast_image.get_rect()

    lunch_image = pygame.image.load("./level4/Images/lunch.jpg")
    lunch_rect = lunch_image.get_rect()

    nap_image = pygame.image.load("./level4/Images/nap.jpg")
    nap_rect = nap_image.get_rect()

    walk_image = pygame.image.load("./level4/Images/walk.jpg")
    walk_rect = walk_image.get_rect()

    dinner_image = pygame.image.load("./level4/Images/dinner.jpg")
    dinner_rect = dinner_image.get_rect()


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
        {
            "wish": "Good Morning! Start your day with positivity!",
            "name": "Morning Exercise",
            "description": "A simple routine to feel brighter, happier, and healthier!",
            "place": "Living Room",
            "time": "7:00 AM",
            "duration": "30 minutes",
            "image": exercise_image,
            "rect": exercise_rect 
        },
        {
            "wish": "It's breakfast time! Fuel up for the day ahead!",
            "name": "Breakfast Time",
            "description": "Enjoy a nutritious meal to kickstart your day!",
            "place": "Dining Room",
            "time": "9:30 AM",
            "duration": "45 minutes",
            "image": breakfast_image,
            "rect": breakfast_rect 
        },
        {
            "wish": "Time for a delicious lunch!",
            "name": "Lunch Time :)",
            "description": "A hearty meal to keep you energized for the afternoon!",
            "place": "Dining Room",
            "time": "1:00 PM",
            "duration": "45 minutes",
            "image": lunch_image,
            "rect": lunch_rect 
        },
        {
            "wish": "Relax and recharge!",
            "name": "Have a Lil Nap!!",
            "description": "A short nap to refresh your mind and body!",
            "place": "Bedroom",
            "time": "2:00 PM",
            "duration": "40 minutes",
            "image": nap_image,
            "rect": nap_rect 
        },
        {
            "wish": "Enjoy the fresh air and stay active!",
            "name": "It's time for Evening Walk",
            "description": "A gentle walk to boost your mood and health!",
            "place": "Garden",
            "time": "3:00 PM",
            "duration": "40 minutes",
            "image": walk_image,
            "rect": walk_rect 
        },
        {
            "wish": "End the day with a satisfying meal!",
            "name": "Dinner",
            "description": "A delicious dinner to wrap up the day!",
            "place": "Dining Room",
            "time": "6:00 PM",
            "duration": "60 minutes",
            "image": dinner_image,
            "rect": dinner_rect 
        },
    ]

    # Current activity index
    current_day = 0

    # Function to display the activity information
    def display_activity(activity):
        # Background
        screen.blit(activity["image"], activity["rect"])

        # Wish
        wish_text = font_medium.render(activity['wish'], True, RED)
        screen.blit(wish_text, (50, 20))

        # Activity Name
        name_text = font_large.render(f"Activity: {activity['name']}", True, BLACK)
        screen.blit(name_text, (50, 80))

        # Description
        description_text = font_medium.render(activity['description'], True, BLACK)
        screen.blit(description_text, (50, 140))

        # Place
        place_text = font_medium.render(f"Location: {activity['place']}", True, BLACK)
        screen.blit(place_text, (50, 200))

        # Time
        time_text = font_medium.render(f"Time: {activity['time']}", True, BLACK)
        screen.blit(time_text, (50, 260))

        # Duration
        duration_text = font_medium.render(f"Duration: {activity['duration']}", True, BLACK)
        screen.blit(duration_text, (50, 320))

        # Display the current date
        current_date = datetime.date.today()
        date_text = font_small.render(f"Today's Date: {current_date}", True, BLACK)
        screen.blit(date_text, (45, 380))

        pygame.display.flip()

    # Function to draw a "Next Activity" button
    def draw_next_activity_button():
        button_width = 200
        button_height = 50
        button_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT - 100, button_width, button_height)
        pygame.draw.rect(screen, GREEN, button_rect)
        text = font_medium.render("Next Activity", True, WHITE)
        screen.blit(text, (button_rect.x + (button_width - text.get_width()) // 2, button_rect.y + (button_height - text.get_height()) // 2))
        return button_rect



    current_day
    clock = pygame.time.Clock()
    running = True

    while running:
            # Get the current activity data
        activity = activities[current_day]

            # Display the activity info
        display_activity(activity)

            # Draw the "Next Activity" button
        button_rect = draw_next_activity_button()

            # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if button_rect.collidepoint(event.pos): 
                        current_day = (current_day + 1) % len(activities)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


# Main game loop
def main_menu():
    running = True
    level_buttons = [
        Button(100, 400, 200, 50, button_color, hover_color, "Level 1", level_1),
        Button(350, 400, 200, 50, button_color, hover_color, "Level 2", level_2),
        Button(600, 400, 200, 50, button_color, hover_color, "Level 3", level_3),
        Button(850, 400, 200, 50, button_color, hover_color, "Level 4", level_4),
    ]
    
    while running:
        canvas.blit(background_image, (0, 0))
        
        # Draw title text
        title_text = font.render("Shattered Reflections", True, black)
        canvas.blit(title_text, (width // 2 - title_text.get_width() // 2, 75))
        
        # Draw buttons
        for button in level_buttons:
            button.draw(canvas)
        
        # Check if any button was pressed
        for button in level_buttons:
            if button.is_pressed():
                button.action()  # Start the corresponding level function
        
        # Handle quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()
    
    pygame.quit()
def return_to_menu():
    main_menu() 

#main menu
main_menu()
