import pygame
import datetime

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Activity of the Day")

bg_image = pygame.image.load(r"C:\Users\OMOMON073\Desktop\Sindhu DP\l4\bg.jpg")
bg_rect = bg_image.get_rect()

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
        "duration": "30 minutes"
    },
    {
        "wish": "It's breakfast time! Fuel up for the day ahead!",
        "name": "Breakfast Time",
        "description": "Enjoy a nutritious meal to kickstart your day!",
        "place": "Dining Room",
        "time": "9:30 AM",
        "duration": "45 minutes"
    },
    {
        "wish": "Time for a delicious lunch!",
        "name": "Lunch Time :)",
        "description": "A hearty meal to keep you energized for the afternoon!",
        "place": "Dining Room",
        "time": "1:00 PM",
        "duration": "45 minutes"
    },
    {
        "wish": "Relax and recharge!",
        "name": "Have a Lil Nap!!",
        "description": "A short nap to refresh your mind and body!",
        "place": "Bedroom",
        "time": "2:00 PM",
        "duration": "40 minutes"
    },
    {
        "wish": "Enjoy the fresh air and stay active!",
        "name": "It's time for Evening Walk",
        "description": "A gentle walk to boost your mood and health!",
        "place": "Garden",
        "time": "3:00 PM",
        "duration": "40 minutes"
    },
    {
        "wish": "End the day with a satisfying meal!",
        "name": "Dinner",
        "description": "A delicious dinner to wrap up the day!",
        "place": "Dining Room",
        "time": "6:00 PM",
        "duration": "60 minutes"
    },
]

# Current activity index
current_day = 0

# Function to display the activity information
def display_activity(activity):
    # Background
    screen.blit(bg_image, bg_rect)

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
    button_width = 150
    button_height = 50
    button_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT - 100, button_width, button_height)
    pygame.draw.rect(screen, GREEN, button_rect)
    text = font_medium.render("Next Activity", True, WHITE)
    screen.blit(text, (button_rect.x + (button_width - text.get_width()) // 2, button_rect.y + (button_height - text.get_height()) // 2))
    return button_rect

# Main game loop
def main():
    global current_day
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

if __name__ == "__main__":
    main()
