import os
import pygame


def load_image(file_path, colorkey=None):
    """Loads an image from a file and optionally sets a colorkey."""
    full_path = os.path.join(os.getcwd(), file_path)
    try:
        image = pygame.image.load(full_path)
    except pygame.error as e:
        print(f"Unable to load image '{file_path}': {e}")
        raise SystemExit
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image
