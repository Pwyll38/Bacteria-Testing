import pygame

pygame.init()

WIN_HEIGHT = 540
WIN_WIDTH = 960
WINDOW_SIZE = (WIN_WIDTH,WIN_HEIGHT)
CLOCK = pygame.time.Clock()

pygame.display.set_caption("Bacterias")
window = pygame.display.set_mode(WINDOW_SIZE, 0, 0)    

GROWTH_FACTOR = 4

def mainloop():
    window.fill((255,255,255))

    bac = 0.6
    x_axis = 0
    
    running = True
    while(running):
        
        x_axis+=0.1


        event_list =  pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                if event.key == pygame.K_ESCAPE:
                    running = False


        bac = GROWTH_FACTOR * bac * (1 - bac)
        print(bac)
        pygame.draw.circle(window, (0,155,155), (x_axis, WIN_HEIGHT*bac), 1, 0)


        pygame.display.update()
        CLOCK.tick(1000)

mainloop()
    
