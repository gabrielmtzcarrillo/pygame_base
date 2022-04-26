from datetime import datetime
import os

import pygame
import pygame.mixer

class Application():
    is_running:bool
    clock:pygame.time.Clock
    fps:int

    font:pygame.font.Font
    
    timer:int = 0
    timer_last:int = 0

    render_size:pygame.Vector2
    screen:pygame.Surface

    padding:pygame.Vector2

    sfx_camera = None

    def __init__(self, title:str  = "PyGame 2 Engine", w:int = 1280, h:int = 720) -> None:
        self.is_running = True
        
        self.clock = pygame.time.Clock()
        self.fps = 0
        
        self.render_size = pygame.Vector2(w,h)
        self.screen = pygame.display.set_mode(self.render_size)
        pygame.display.set_caption(title)
        
        self.padding = pygame.Vector2(4,4)

        # RESOURCES
        self.font = pygame.font.Font(pygame.font.get_default_font(), 16)

        self.sfx_camera = pygame.mixer.Sound("assets\\sfx\\camera.wav")

        # CHECK FOR DIRECTORIES
        if not os.path.exists("screenshots\\"):
            os.makedirs("screenshots\\")

    def loop(self) -> None:
        while self.is_running:
            self.timer = pygame.time.get_ticks()
            self.fps = self.clock.get_fps()
            
            self.update()

            if self.is_running:
                self.render()
            
            self.clock.tick(120)

    def scene_input(self) -> None:
        # HANDLE EVENTS
        for event in pygame.event.get():

            #ON KEYPRESS
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_F5:
                    self.screenshot()
                    continue

                if event.key == pygame.K_ESCAPE:
                    self.is_running = False
                    pygame.quit()
                    return

            #ON QUITTING
            if event.type == pygame.QUIT :
                self.is_running = False
                return

    def update(self) -> None:
        ## ENGINE LOGIC GOES HERE
        self.scene_input()

        # CALL 8 TIMES IN A SECOND
        if (self.timer - self.timer_last) > 125:
                self.timer_last = self.timer
                self.scene_tick()

    def scene_tick(self) -> None:
        # TICK LOGIC GOES HERE
        pass

    def render(self) -> None:
        # CLEAR SCREEN
        self.screen.fill((64,64,64))
        
        # DRAW FPS
        image = self.font.render(f"FPS: {self.fps:.2f}",True, (255,255,255))
        i_size = pygame.Vector2(image.get_size())
        self.screen.blit(image, self.render_size - self.padding - i_size)

        # DISPLAY SCREEN
        pygame.display.flip()
        
    def screenshot(self) -> None:
        now = datetime.now()
        pygame.image.save(self.screen,f"screenshots\\{now:%Y%m%d_%H%M%S}.png")
        pygame.mixer.Sound.play(self.sfx_camera)