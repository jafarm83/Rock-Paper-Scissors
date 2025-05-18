# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import base64
import zlib
import time
import random
import pygame
import importlib.util
from io import BytesIO

# ███████╗ ██████╗ ██╗   ██╗██████╗ ███████╗
# ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝
# █████╗  ██║   ██║██║   ██║██████╔╝█████╗  
# ██╔══╝  ██║   ██║██║   ██║██╔══██╗██╔══╝  
# ██║     ╚██████╔╝╚██████╔╝██║  ██║███████╗
# ╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# Rock Paper Scissors - Ultimate Self-contained Edition

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

# Check if pygame is installed
def check_module_installed(module_name):
    return importlib.util.find_spec(module_name) is not None

# Install a module via pip
def install_module(module_name):
    print(f"[+] Installing required module: {module_name}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        print(f"[+] Successfully installed {module_name}")
    except Exception as e:
        print(f"[-] Failed to install {module_name}: {e}")
        sys.exit(1)

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

# Base64 encoded images (Embedded assets)
ASSETS = {
    "rock.png": """
iVBORw0KGgoAAAANSUhEUgAAAGQAAAA...
""",
    "paper.png": """
iVBORw0KGgoAAAANSUhEUgAAAGQAAAA...
""",
    "scissors.png": """
iVBORw0KGgoAAAANSUhEUgAAAGQAAAA...
"""
}

# Decode and write image files
def extract_assets():
    for name, data in ASSETS.items():
        try:
            img_data = base64.b64decode(data)
            with open(name, "wb") as f:
                f.write(img_data)
        except Exception as e:
            print(f"[-] Error extracting asset {name}: {e}")

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

# Initialize Pygame and run the game
def run_game():
    pygame.init()
    pygame.font.init()

    WIDTH, HEIGHT = 1000, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rock Paper Scissors - Ultimate Edition")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 200, 0)
    RED = (200, 0, 0)
    BLUE = (0, 150, 255)
    GRAY = (200, 200, 200)

    # Fonts
    title_font = pygame.font.SysFont("Arial", 60, bold=True)
    font = pygame.font.SysFont("Arial", 40)
    small_font = pygame.font.SysFont("Arial", 28)

    # Load images
    try:
        rock_img = pygame.image.load("rock.png")
        paper_img = pygame.image.load("paper.png")
        scissors_img = pygame.image.load("scissors.png")
    except pygame.error as e:
        print(f"Error loading image: {e}")
        sys.exit(1)

    BUTTON_SIZE = 150
    rock_img = pygame.transform.scale(rock_img, (BUTTON_SIZE, BUTTON_SIZE))
    paper_img = pygame.transform.scale(paper_img, (BUTTON_SIZE, BUTTON_SIZE))
    scissors_img = pygame.transform.scale(scissors_img, (BUTTON_SIZE, BUTTON_SIZE))

    # Game variables
    score = {"player": 0, "computer": 0}
    result_text = ""
    show_result_time = 0

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        rect = textobj.get_rect(center=(x, y))
        surface.blit(textobj, rect)

    def get_computer_choice():
        return random.choice(["ROCK", "PAPER", "SCISSORS"])

    def animate_computer_choice(computer_choice):
        choices = ["ROCK", "PAPER", "SCISSORS"]
        start_time = pygame.time.get_ticks()
        duration = 1000
        while pygame.time.get_ticks() - start_time < duration:
            screen.fill(WHITE)
            draw_text("Computer is choosing...", font, GRAY, screen, WIDTH // 2, 100)

            current = random.choice(choices)
            img = {"ROCK": rock_img, "PAPER": paper_img, "SCISSORS": scissors_img}[current]
            screen.blit(img, (WIDTH // 2 - img.get_width() // 2, HEIGHT // 2 - 50))

            pygame.display.update()
            pygame.time.wait(100)

        return computer_choice

    def display_result(player, computer):
        nonlocal result_text, show_result_time
        if player == computer:
            result_text = "Tie!"
        elif (
            (player == "ROCK" and computer == "SCISSORS") or
            (player == "PAPER" and computer == "ROCK") or
            (player == "SCISSORS" and computer == "PAPER")
        ):
            result_text = "You Win!"
            score["player"] += 1
        else:
            result_text = "You Lose!"
            score["computer"] += 1

        show_result_time = pygame.time.get_ticks()

    def main_menu():
        while True:
            screen.fill(WHITE)
            draw_text("Rock Paper Scissors", title_font, BLACK, screen, WIDTH // 2, 80)

            rock_rect = screen.blit(rock_img, (150, 300))
            paper_rect = screen.blit(paper_img, (425, 300))
            scissors_rect = screen.blit(scissors_img, (700, 300))

            draw_text("Click your choice!", font, GRAY, screen, WIDTH // 2, 600)
            draw_text(f"Score: You {score['player']} - Computer {score['computer']}", small_font, BLACK, screen, WIDTH // 2, 650)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if rock_rect.collidepoint(pos):
                        return "ROCK"
                    elif paper_rect.collidepoint(pos):
                        return "PAPER"
                    elif scissors_rect.collidepoint(pos):
                        return "SCISSORS"

            pygame.display.update()

    def show_result_screen(player, computer):
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 3000:
            screen.fill(WHITE)

            draw_text(f"You: {player}", font, BLACK, screen, WIDTH // 2 - 200, 150)
            draw_text(f"Computer: {computer}", font, BLACK, screen, WIDTH // 2 + 200, 150)

            screen.blit({"ROCK": rock_img, "PAPER": paper_img, "SCISSORS": scissors_img}[player], (150, 250))
            screen.blit({"ROCK": rock_img, "PAPER": paper_img, "SCISSORS": scissors_img}[computer], (650, 250))

            color = GREEN if "Win" in result_text else RED if "Lose" in result_text else BLUE
            draw_text(result_text, title_font, color, screen, WIDTH // 2, 500)

            pygame.display.update()

    while True:
        player_choice = main_menu()
        computer_choice = animate_computer_choice(get_computer_choice())
        display_result(player_choice, computer_choice)
        show_result_screen(player_choice, computer_choice)

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

if __name__ == "__main__":
    print("🚀 Rock Paper Scissors - Ultimate Self-contained Edition\n")

    if not check_module_installed("pygame"):
        install_module("pygame")

    extract_assets()

    try:
        run_game()
    finally:
        # Clean up temporary files
        for name in ASSETS.keys():
            if os.path.exists(name):
                os.remove(name)