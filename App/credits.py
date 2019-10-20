def credits():
    import pygame

    pygame.init()

    WIDHT_credits = 400
    HEIGHT_credits = 580
    win1 = pygame.display.set_mode((WIDHT_credits, HEIGHT_credits))
    pygame.display.set_caption("Clear the space!!!")
    background = pygame.image.load('image/credits_bgr.png')

    buttons_size = (1, 1)
    exit_plus = pygame.Surface(buttons_size)
    exit_plus_rect = exit_plus.get_rect()
    #exit_plus = pygame.image.load('image/exit_button.png')
    exit_plus_rect = exit_plus_rect.move((150,450))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False

        if pygame.mouse.get_pressed()[0] == 1:
            if (exit_plus_rect.right > pygame.mouse.get_pos()[0] > exit_plus_rect.left) and (exit_plus_rect.top < pygame.mouse.get_pos()[1] < exit_plus_rect.bottom):

                run = False
        win1.blit(background,(0,0))
        win1.blit(exit_plus, (exit_plus_rect.left,exit_plus_rect.top))
        pygame.time.delay(25)
        #print(pygame.mouse.get_pressed())
        pygame.display.update()
