import pygame
from random import randint
import threading
def refresh():
    global running
    global no_ref
    while running:
        if not no_ref:
            pygame.display.flip()

def clean_buffer():
    global no_ref
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                no_ref = True
                running = False
                break

no_ref = False
t = threading.Thread(target=refresh)
t2 = threading.Thread(target=clean_buffer)
pygame.init()
width, height = 1536, 1536 # Stream through OBS to make fullscreen. Edit values if necessary for picture resolution
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("")
image_names = ["image (1).png", "image (2).png", "image (3).png", "image (4).png", "image (5).png"]  # Add your image names
images = [pygame.image.load(name) for name in image_names]
running = True
current_image_index = 0
t2.start()
t.start()

while running:
    # Clean up event buffer, check for QUIT actions(also done in a thread)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            no_ref = True
            running = False
    no_ref = True
    screen.fill((0, 0, 0))  # Clear the screen

    # Display the current image
    current_image = images[current_image_index]
    screen.blit(current_image, (0, 0)) # Show image on screen

    pygame.display.flip()  # Update the display
    non_ref = False
    pygame.time.delay(randint(1000, 5000))  # Delay random amounts to appear more natural

    # Move to a random image
    current_image_index = randint(0, len(images)-1)

pygame.quit()
raise SystemExit # Replaces "sys.exit()"
