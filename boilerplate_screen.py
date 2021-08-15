def Winner():
    global music_paused
    winner = True

    #timers init
    dt = 0

    #main menu loop
    while 1:
        #user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         if start_button.collidepoint(event.pos):
            #             Game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    if music_paused:
                        pygame.mixer.music.unpause()
                        music_paused = False
                    else:
                        music_paused = True
                        pygame.mixer.music.pause()
            
            

        #draw frame
        screen.fill(grey)

        #render frame
        pygame.display.flip()
        dt = clock.tick(tick_rate)