import pygame
import datetime

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Activity of the Day")

bg_image = pygame.image.load(r"C:\Users\OMOMON073\Desktop\Sindhu DP\l4\bg4.jpg")
bg_rect = bg_image.get_rect()
#colors
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)
GREEN = (0, 150, 150)
RED = (255, 0, 0)

#fonts
font_large = pygame.font.SysFont("Arial", 48)
font_medium = pygame.font.SysFont("Arial", 36)
font_small = pygame.font.SysFont("Arial", 24)

# Activities data (for simplicity, using two days' worth of data)
activities = [
    {
        "Wish":"Good Morning!! Have a great day!!",
        "name": "Morning Exercise",
        #"description":"A simple routine to feel brighter, happier, and healthier!"
        "place": "Living Room",
        "time": "7:00 AM",
        "duration": "30 minutes"
    },
    {
       # "title":
        "name": "BreakFast Time",
        "place": "Dining Room",
        "time": "9:30 PM",
        "duration": "45 minutes"
    },
    {
        "name": "Lunch Time :)",
        "place": "Dining Room",
        "time": "1:00 PM",
        "duration": "45 minutes"
    },
    {
        "name": "Have a Lil Nap!!",
        "place": "Garden",
        "time": "2:00 PM",
        "duration": "40 minutes"
    },
    {
        "name": "It's time for Evening Walk",
        "place": "Garden",
        "time": "3:00 PM",
        "duration": "40 minutes"
    },
    {
        "name": "Dinner",
        "place": "Dining Room",
        "time": "6:00 PM",
        "duration": "60 minutes"
    },
]

#current day 
current_day = 0

# Function to display the activity information
def display_activity(activity):
    # Background
    #screen.fill(LIGHT_BLUE)
    screen.blit(bg_image, bg_rect)

    # Activity Name
    name_text = font_large.render(f"Activity: {activity['name']}", True, BLACK)
    screen.blit(name_text, (50, 50))

    # Place
    place_text = font_medium.render(f"Location: {activity['place']}", True, BLACK)
    screen.blit(place_text, (50, 150))

    # Time
    time_text = font_medium.render(f"Time: {activity['time']}", True, BLACK)
    screen.blit(time_text, (50, 250))

    # Duration
    duration_text = font_medium.render(f"Duration: {activity['duration']}", True, BLACK)
    screen.blit(duration_text, (50, 350))

    # Instructions text
    #instructions_text = font_small.render("Click 'Next Activity' to see the next activity", True, GREEN)
    #screen.blit(instructions_text, (50, 450))

    # Display the current date
    current_date = datetime.date.today()
    date_text = font_small.render(f"Today's Date: {current_date}", True, BLACK)
    screen.blit(date_text, (50, 450))

    pygame.display.flip()

# Function to draw a "Next Activity" button
def draw_next_activity_button():
    button_width = 100
    button_height = 50
    button_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT - 100, button_width, button_height)
    pygame.draw.rect(screen, GREEN, button_rect)
    text = font_medium.render(">>", True, WHITE)
    screen.blit(text, (button_rect.x + (button_width - text.get_width()) // 2, button_rect.y + (button_height - text.get_height()) // 2))
    return button_rect

# Main game loop
def main():
    global current_day
    clock = pygame.time.Clock()
    running = True

    # Display the current activity
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
                    if button_rect.collidepoint(event.pos):  # If clicked on "Next Activity" button
                        # Move to the next day, wrapping around if necessary
                        current_day = (current_day + 1) % len(activities)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
