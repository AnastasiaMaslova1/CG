import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Параметры окна
width, height = 800, 600

# Функция для ввода данных от пользователя
def get_user_input():
    def input_float(prompt, low, high):
        while True:
            try:
                value = float(input(prompt))
                if low <= value <= high:
                    return value
                else:
                    print(f"Ошибка: значение должно быть в диапазоне от {low} до {high}")
            except ValueError:
                print("Ошибка: введите числовое значение")
    
    cube_width = input_float("Введите ширину куба (положительное число): ", 0.1, float('inf'))
    cube_height = input_float("Введите высоту куба (положительное число): ", 0.1, float('inf'))
    cube_length = input_float("Введите длину куба (положительное число): ", 0.1, float('inf'))
    transparency = input_float("Введите коэффициент прозрачности (от 0.0 до 1.0): ", 0.0, 1.0)

    return cube_width, cube_height, cube_length, transparency

# Углы поворота куба
angle_x = 0
angle_y = 0

# Инициализация OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glDisable(GL_LIGHTING)  # Освещение отключено для более ясного понимания прозрачности
    #glEnable(GL_LIGHTING)  # Включаем освещение
    #glEnable(GL_LIGHT0)    # Включаем источник света 0
    #glEnable(GL_LIGHT1)    # Включаем источник света 1

#def setup_lighting():
    # Настройки источника света 0
    #light_ambient0 = [0.1, 0.1, 0.1, 1.0]
    #light_diffuse0 = [1.0, 1.0, 1.0, 1.0]
    #light_position0 = [1.0, 1.0, 1.0, 0.0]
    
    #glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient0)
    #glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse0)
    #glLightfv(GL_LIGHT0, GL_POSITION, light_position0)
    
    # Настройки источника света 1
    #light_ambient1 = [0.1, 0.1, 0.1, 1.0]
    #light_diffuse1 = [0.5, 0.5, 0.5, 1.0]
    #light_position1 = [-1.0, -1.0, -1.0, 0.0]
    
    #glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient1)
    #glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse1)
    #glLightfv(GL_LIGHT1, GL_POSITION, light_position1)
    
# Настройка проекции
def setup_projection():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspect_ratio = width / height
    glOrtho(-aspect_ratio * 10, aspect_ratio * 10, -10, 10, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

# Рисование куба
def draw_cube(cube_width, cube_height, cube_length, transparency):
    glColor4f(0.5, 0.5, 0.5, transparency)  # Серый цвет, прозрачность устанавливается здесь
    glBegin(GL_QUADS)
    # Координаты куба
    # Передняя грань
    glVertex3f(-cube_width / 2, -cube_height / 2, cube_length / 2)
    glVertex3f(cube_width / 2, -cube_height / 2, cube_length / 2)
    glVertex3f(cube_width / 2, cube_height / 2, cube_length / 2)
    glVertex3f(-cube_width / 2, cube_height / 2, cube_length / 2)
    # Задняя грань
    glVertex3f(-cube_width / 2, -cube_height / 2, -cube_length / 2)
    glVertex3f(cube_width / 2, -cube_height / 2, -cube_length / 2)
    glVertex3f(cube_width / 2, cube_height / 2, -cube_length / 2)
    glVertex3f(-cube_width / 2, cube_height / 2, -cube_length / 2)
    # Левый бок
    glVertex3f(-cube_width / 2, -cube_height / 2, cube_length / 2)
    glVertex3f(-cube_width / 2, cube_height / 2, cube_length / 2)
    glVertex3f(-cube_width / 2, cube_height / 2, -cube_length / 2)
    glVertex3f(-cube_width / 2, -cube_height / 2, -cube_length / 2)
    # Правый бок
    glVertex3f(cube_width / 2, -cube_height / 2, cube_length / 2)
    glVertex3f(cube_width / 2, cube_height / 2, cube_length / 2)
    glVertex3f(cube_width / 2, cube_height / 2, -cube_length / 2)
    glVertex3f(cube_width / 2, -cube_height / 2, -cube_length / 2)
    # Верхняя грань
    glVertex3f(-cube_width / 2, cube_height / 2, cube_length / 2)
    glVertex3f(cube_width / 2, cube_height / 2, cube_length / 2)
    glVertex3f(cube_width / 2, cube_height / 2, -cube_length / 2)
    glVertex3f(-cube_width / 2, cube_height / 2, -cube_length / 2)
    # Нижняя грань
    glVertex3f(-cube_width / 2, -cube_height / 2, cube_length / 2)
    glVertex3f(cube_width / 2, -cube_height / 2, cube_length / 2)
    glVertex3f(cube_width / 2, -cube_height / 2, -cube_length / 2)
    glVertex3f(-cube_width / 2, -cube_height / 2, -cube_length / 2)
    
    glEnd()

# Отображение сцены
def display(cube_width, cube_height, cube_length, transparency):
    global angle_x, angle_y
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    setup_projection()
    #
    #setup_lighting()
    
    glTranslatef(0.0, 0.0, -10)
    glRotatef(angle_x, 1, 0, 0)
    glRotatef(angle_y, 0, 1, 0)

    draw_cube(cube_width, cube_height, cube_length, transparency)
    pygame.display.flip()

def main():
    global angle_x, angle_y
    cube_width, cube_height, cube_length, transparency = get_user_input()

    pygame.init()
    screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D Convex Shape")

    init()
    
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            angle_y -= 1
        if keys[K_RIGHT]:
            angle_y += 1
        if keys[K_UP]:
            angle_x -= 1
        if keys[K_DOWN]:
            angle_x += 1

        display(cube_width, cube_height, cube_length, transparency)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
