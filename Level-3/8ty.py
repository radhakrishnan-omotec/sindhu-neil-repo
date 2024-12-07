import pygame
import os
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drag and Drop Images onto Frames")

wall_image = pygame.image.load(r"C:\Users\OMOMON073\Desktop\Sindhu DP\l3\wall.jpeg")
wall_rect = wall_image.get_rect()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
for_msg= (150,150, 150)

# Load images of different occasions (6 images)
occasion_images = {
    "birthday": pygame.image.load(r"C:\Users\OMOMON073\Desktop\Sindhu DP\l3\HB1.jpg"),
    "holiday": pygame.image.load(r"C:\Users\OMOMON073\Desktop\Sindhu DP\l3\vacay1.jpg"),
    "wedding": pygame.image.load(r"C:\Users\OMOMON073\Desktop\Sindhu DP\l3\Wed1.jpg"),
    "easter": pygame.image.load(r"C:\Users\OMOMON073\Desktop\Sindhu DP\l3\easter1.jpg"),
    "christmas": pygame.image.load(r"C:\Users\OMOMON073\Desktop\Sindhu DP\l3\christmas.jpg"),
    "friends":pygame.image.load(r"C:\Users\OMOMON073\Desktop\Sindhu DP\l3\friends21.png"),
}

# Scale images to fit in the frame
image_size = (185, 130)
for key in occasion_images:
    occasion_images[key] = pygame.transform.scale(occasion_images[key], image_size)

# Define frames for each occasion (Reduced height of frames)
frames = {
    "birthday": pygame.Rect(50, 50, 200, 150),  # Reduced height of frames
    "holiday": pygame.Rect(300, 50, 200, 150),
    "wedding": pygame.Rect(550, 50, 200, 150),
    "easter": pygame.Rect(50, 250, 200, 150),
    "christmas": pygame.Rect(300, 250, 200, 150),
    "friends": pygame.Rect(550, 250, 200, 150)
}

# Neatly line up images in a single row below frames (Increase space below the frames for images)
image_positions = {
    "birthday": pygame.Rect(50, 400, 185, 130),
    "holiday": pygame.Rect(150, 400, 185, 130),
    "wedding": pygame.Rect(250, 400, 185, 130),
    "easter": pygame.Rect(350, 400, 185, 130),
    "christmas": pygame.Rect(450, 400, 185, 130),
    "friends": pygame.Rect(550, 400, 185, 130)
}

# Dragging variables
dragging = False
dragged_image = None
offset_x, offset_y = 0, 0
message = ""  
font = pygame.font.SysFont("Arial", 24)

#draw the frames
def draw_frames():
    for frame in frames.values():
        pygame.draw.rect(screen, BLACK, frame, 6)

#draw images
def draw_images():
    for key, img in occasion_images.items():
        screen.blit(img, image_positions[key])


def is_inside_frame(image_rect, frame_rect):
    return frame_rect.colliderect(image_rect)

# Function to display messages
def draw_message(message_text):
    text = font.render(message_text, True, for_msg)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 50))

# Main game loop
def main():
    global dragging, dragged_image, offset_x, offset_y, message
   # clock = pygame.time.Clock()

    # Running flag
    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(wall_image, wall_rect)
        draw_frames()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    for key, img_rect in image_positions.items():
                        if img_rect.collidepoint(event.pos):  # If click is on the image
                            dragging = True
                            dragged_image = key
                            offset_x = img_rect.x - event.pos[0]
                            offset_y = img_rect.y - event.pos[1]
                            break
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if dragging:
                        image_rect = image_positions[dragged_image]
                        frame_for_image = frames[dragged_image]  # Get the correct frame for the image

                        # Check if the image is inside its corresponding frame
                        if is_inside_frame(image_rect, frame_for_image):
                            message = f"Correct! {dragged_image.capitalize()} Image Placed."
                        else:
                            message = f"Wrong! {dragged_image.capitalize()} Image Not Placed Correctly."
                        dragging = False
                        dragged_image = None
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_x, mouse_y = event.pos
                    image_positions[dragged_image].topleft = (mouse_x + offset_x, mouse_y + offset_y)

        # Draw images
        draw_images()

       
        if dragging:
            current_image_rect = image_positions[dragged_image]
            frame_for_image = frames[dragged_image]
            if is_inside_frame(current_image_rect, frame_for_image):
                pygame.draw.rect(screen, GREEN, current_image_rect, 2)  # Green border if inside the correct frame
            else:
                pygame.draw.rect(screen, RED, current_image_rect, 2)  # Red border if outside the frame

        # Draw validation message
        draw_message(message)

        pygame.display.flip()
 

    pygame.quit()

# Run the program
if __name__ == "__main__":
    main()
