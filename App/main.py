

from App import *

class Main(object):

    def __init__(self):
        pygame.init()
        self.mainloop()


    def transparent_window(self):

        fuchsia = (255, 255, 255)
        hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                               win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)


    def mainloop(self):

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10, 50)
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.set_colorkey(pygame.Color(15, 255, 0))

        iss = ISS()
        balls = []
        for i in range(10):
            ball = Rubbish(1, 50, [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)], [random.randint(-10, 10), random.randint(-10, 10)])
            balls.append(ball)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            screen.fill((255, 255, 255))
            for ball in balls:
                ball.render(screen)
                # ex = ball.move()
                # if ex == -1:
                #     ball.coords = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]
            iss.render(screen)
            pygame.display.flip()
            time.sleep(0.03)


main = Main()
