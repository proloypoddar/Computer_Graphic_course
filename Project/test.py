import pygame
import sys

# Setup
pygame.init()
pygame.joystick.init()

# Set up window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fantech Controller Tester")

font = pygame.font.Font(None, 30)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

# Connect to first joystick
if pygame.joystick.get_count() == 0:
    print("No controller found.")
    pygame.quit()
    sys.exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Using Controller: {joystick.get_name()}")

clock = pygame.time.Clock()

# Main loop
while True:
    screen.fill(BLACK)
    pygame.event.pump()

    # Draw axes
    for i in range(joystick.get_numaxes()):
        axis_val = joystick.get_axis(i)
        text = font.render(f"Axis {i}: {axis_val:.2f}", True, WHITE)
        screen.blit(text, (50, 30 + i * 30))

        # Show bar
        pygame.draw.rect(screen, GREEN, (300, 30 + i * 30, int(axis_val * 100), 20))

    # Draw buttons
    for i in range(joystick.get_numbuttons()):
        button_val = joystick.get_button(i)
        color = RED if button_val else WHITE
        pygame.draw.circle(screen, color, (600 + (i % 4) * 50, 100 + (i // 4) * 50), 20)
        btn_text = font.render(f"{i}", True, BLACK)
        screen.blit(btn_text, (590 + (i % 4) * 50, 90 + (i // 4) * 50))

    # Draw D-Pad (hat)
    for i in range(joystick.get_numhats()):
        hat_val = joystick.get_hat(i)
        text = font.render(f"Hat {i}: {hat_val}", True, WHITE)
        screen.blit(text, (50, 400 + i * 30))

    pygame.display.flip()
    clock.tick(60)
