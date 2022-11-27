import pygame

def check_win():
    for r in range(row):
        if mas[0][r] == "x" and mas[1][r] == "x" and mas[2][r] == "x":
            return "x"
        if mas[0][r] == "o" and mas[1][r] == "o" and mas[2][r] == "o":
            return "o"

pygame.init()
clock = pygame.time.Clock()
size_block = 100  # размеры блоков
margin = 10  # пространство между блоками

row = col = 3  # количество ячеек по горизонтали и вертикали
mas = [[0] * row for i in range(col)]  # создание матрицы поля
width = height = size_block * row + margin * (col + 1)  # размеры окна в зависимости от поля
size_window = (width, height)
screen = pygame.display.set_mode(size_window)
RED = (255, 0, 0)
GREEN = (0,255,0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)

mas = [[0]*row for i in range(col)]

turn = 0

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            x_col = x_mouse//(size_block+margin)
            y_row = y_mouse//(size_block+margin)
            if mas[x_col][y_row] == 0:
                if turn%2 == 0:
                    mas[x_col][y_row] = "x"
                else:
                    mas[x_col][y_row] = "o"
                turn += 1


    # вывод поля по строкам
    for r in range(row):
        for c in range(col):
            if mas[c][r] == "x":
                color = RED
            elif mas[c][r] == "o":
                color = GREEN
            else:
                color = WHITE
            x = 0 + c * size_block + margin * (c + 1)  # координата нового блока меняется в зависимости от номера колонки
            y = 0 + r * size_block + margin * (r + 1)  # координата нового блока меняется в зависимости от номера строки
            pygame.draw.rect(screen, color, (x, y, size_block, size_block))  # вывод ячейки белого цвета
            if color == RED:
                pygame.draw.line(screen,WHITE,(x,y),(x+size_block,y+size_block),5)
                pygame.draw.line(screen,WHITE,(x,y+size_block),(x+size_block,y),5)
            elif color == GREEN:
                pygame.draw.circle(screen,WHITE,(x+size_block//2,y+size_block//2),size_block//2,5)
    if check_win() == "x":
        screen.fill(BLACK)
        font = pygame.font.SysFont("Times New Roman ",80)
        text = font.render("win - x",1,RED,BLACK)
        text_cor = text.get_rect()
        text_x = screen.get_width()/2 - text_cor.width/2
        text_y = screen.get_height()/2 - text_cor.height/2
        screen.blit(text,[text_x,text_y])
    if check_win() == "o":
        screen.fill(BLACK)
        print("o - win")
    pygame.display.update()