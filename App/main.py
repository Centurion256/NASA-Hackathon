from App import *

class Main(object):

    def __init__(self):
        pygame.init()
        self.mainloop()


    # def transparent_window(self):

    #     fuchsia = (255, 255, 255)
    #     hwnd = pygame.display.get_wm_info()["window"]
    #     win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
    #                            win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    #     win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
    
    def on_mouse_down(self, event):
        for ball in self.balls:
            ball.mouse_collision(event.pos)

    def mainloop(self):

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10, 50)
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.set_colorkey(pygame.Color(15, 255, 0))
        #Чого воно підсвічує?
        background = pygame.transform.scale(pygame.image.load(f"Data/{BACKGROUND_IMAGE}.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        iss = ISS()
        self.balls = []
        healthbar = Healthbar(iss)
        for i in range(10):
            ball_pos = random.choice([[random.randint(0, SCREEN_WIDTH),0], [random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT], 
                                      [0, random.randint(0, SCREEN_HEIGHT)], [SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT)]])
            ball = Rubbish(1, random.randint(20, 40), ball_pos, [random.randint(-10, 10), random.randint(-10, 10)])
            self.balls.append(ball)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.on_mouse_down(event)

            screen.blit(background, (0,0))

            for ball in self.balls:
                ball.render(screen)
                ex = ball.move()
                col = ball.ISS_colision(iss)
                if(ex == -1 or col == -1):
                    # side = random.randchoise([(1,0), (0, 1), (-1, 0), (0, -1)])
                    ball.coords = random.choice([[random.randint(0, SCREEN_WIDTH),0], [random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT], 
                                      [0, random.randint(0, SCREEN_HEIGHT)], [SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT)]])
                if col == -1:
                    iss.hp -= ball.size//4
                if iss.hp < 0:
#                   screen.blit(pygame.image.load("Data/lose.png"))
                    time.sleep(3)
                    exit()
            iss.render(screen)

            healthbar.render(screen)

            pygame.display.flip()
            
            time.sleep(0.03)


main = Main()
