import pygame

pygame.init()


screen = pygame.display.set_mode((1920,1080))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.draw.rect(screen,(0, 0, 255), pygame.Rect(70, 90, 60, 60))
            
        pygame.display.flip()