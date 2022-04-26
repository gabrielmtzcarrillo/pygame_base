import pygame
import engine

def main () -> None:
    pygame.init()
    app = engine.Application()
    app.loop()

if __name__ == '__main__':
    main()