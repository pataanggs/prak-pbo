import pygame
import random

WINDOW = pygame.display.set_mode((800, 550))
FPS = 60
pressed = False
visible_bugs = []
visible_blocks = []
visible_bombs = []
level = 0

class Shooter:

    def __init__(self, colour, x_pos, y_pos, width, height):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.colour = colour
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self):
        pygame.draw.rect(WINDOW, self.colour, self.rect)

    def left(self):
        self.rect.x -= 6

    def right(self):
        self.rect.x += 6

    def up(self):
        self.rect.y -= 6

    def down(self):
        self.rect.y += 6


class Bombs:

    def __init__(self, colour, x_pos, y_pos, width, height):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.colour = colour
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.visible = False

    def draw(self):
        pygame.draw.rect(WINDOW, self.colour, self.rect)

    def move(self):
        self.rect.y -= 8


class Bugs:

    def __init__(self, colour, x_pos, y_pos, width, height, speed):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.colour = colour
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.visible = True
        self.speed = speed

    def draw(self):
        pygame.draw.rect(WINDOW, self.colour, self.rect)

    def down(self):
        self.rect.y += 11

class Blocks:

    def __init__(self, colour, x_pos, y_pos, width, height):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.colour = colour
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.visible = False
        self.hits = 0
        self.hit = False

    def draw(self):
        pygame.draw.rect(WINDOW, self.colour, self.rect)


class Bonus:

    def __init__(self, colour, x_pos, y_pos, width, height, speed):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.colour = colour
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.visible = False
        self.speed = speed
        self.vert_speed = 2
        self.hit = False

    def draw(self):
        pygame.draw.rect(WINDOW, self.colour, self.rect)

    def pos(self, x_pos, y_pos):
        self.rect.x = x_pos
        self.rect.y = y_pos


def handle_shooter(shooter, keys_pressed):
    global visible_bombs
    global pressed
    # draw shooter
    shooter.draw()
    # move shooter
    if shooter.rect.y < 470:
        if keys_pressed[pygame.K_s]:
            shooter.down()

    if shooter.rect.y > 375:
        if keys_pressed[pygame.K_w]:
            shooter.up()

    if shooter.rect.x > 0:
        if keys_pressed[pygame.K_a]:
            shooter.left()

    if shooter.rect.x < 780:
        if keys_pressed[pygame.K_d]:
            shooter.right()
    # shoot bombs
    if keys_pressed[pygame.K_SPACE]:
        if pressed == False:
            bomb = Bombs((0, 30, 140), shooter.rect.x + 10,
                         shooter.rect.y - 10, 6, 20)
            visible_bombs.append(bomb)
            bomb.visible = True
            pressed = True

    else:
        pressed = False

    for bomb in visible_bombs:
        if bomb.visible == True:
            bomb.draw()
            bomb.move()

        if bomb.rect.y < 0:
            visible_bombs.remove(bomb)


def handle_blocks():

    global visible_blocks
    global visible_bombs
    global visible_bugs

    for block in visible_blocks:
        block.draw()

    for bomb in visible_bombs:
        for bug in visible_bugs:
            if bomb.rect.colliderect(
                    bug.rect) and bug.visible == True and bomb.visible == True:
                block = Blocks((255, 100, 0), bug.rect.x, bug.rect.y, 24, 10)
                visible_blocks.append(block)
                visible_bugs.remove(bug)
                if bomb in visible_bombs:
                    visible_bombs.remove(bomb)

        for block in visible_blocks:
            if bomb.rect.colliderect(block.rect) and bomb.visible == True:
                if block.hit == False:
                    bomb.visible = False
                    block.hit = True
                    block.hits = block.hits + 1
                    block.colour = (50, 0, 255)

            else:
                block.hit = False

            if block.hits == 2:
                block.colour = (100, 60, 255)

            if block.hits == 3:
                block.colour = (200, 0, 127)

            if block.hits == 4:
                visible_blocks.remove(block)


def handle_bugs():
    global bug_speed
    global visible_bugs
    global visible_blocks
    for bug in visible_bugs:
        if bug.visible == True:
            bug.draw()

            bug.rect.x += bug.speed
            if bug.rect.x >= 780:
                bug.speed *= -1
                bug.down()
            if bug.rect.x <= 0:
                bug.speed *= -1
                bug.down()

            if bug.rect.y >= 480:
                visible_bugs.remove(bug)

            for block in visible_blocks:
                if bug.rect.colliderect(block.rect):
                    bug.speed *= -1
                    bug.down()


def handle_bonus(shooter, bonus):
    global visible_bugs
    global visible_bombs
    if len(visible_bugs) <= 7 and bonus.hit == False:
        bonus.visible = True

    if bonus.visible == False:
        bonus.pos(800, 450)

    if bonus.visible == True:
        bonus.draw()

        if shooter.rect.x < bonus.rect.x and bonus.visible == True:
            bonus.rect.x -= bonus.speed

        if shooter.rect.x > bonus.rect.x and bonus.visible == True:
            bonus.rect.x += bonus.speed

        bonus.rect.y += bonus.vert_speed
        if bonus.rect.y == 400 or bonus.rect.y == 510:
            bonus.vert_speed *= -1

    for bomb in visible_bombs:
        if bomb.rect.colliderect(
                bonus.rect
        ) and bomb.visible == True and bonus.visible == True and bonus.hit == False:
            visible_bombs.remove(bomb.rect)
            bonus.hit = True
            bonus.visible = False

        if bonus.rect.colliderect(shooter.rect) and bonus.visible == True:
            pygame.quit()

    if len(visible_bugs) > 7:
        bonus.hit = False


def add_bugs():
    global level
    global visible_bugs
    global visible_blocks
    for block in visible_blocks:
        a = block.colour
    q = 300
    if len(visible_bugs) == 0:
        for t in range(14):
            visible_bugs.append(Bugs((255, 0, 50), q, 4, 24, 10, 6))
            q += 30

        for block in visible_blocks:
            if block.hits == 0:
                visible_blocks.remove(block)
        for s in range(18):
            visible_blocks.append(
                Blocks((a), 11 * random.randint(4, 70),
                       (11 * random.randint(4, 40)) - 7, 24, 10))

        level += 1


def level_function(shooter):
    global level
    global visible_blocks
    global visible_bugs
    if level == 0 and len(visible_bugs) == 0:
        for block in visible_blocks:
            block.colour = (255, 100, 0)
    if level == 1:
        shooter.colour = (0, 0, 95)
        for bug in visible_bugs:
            bug.colour = (255, 0, 150)
        for block in visible_blocks:
            if block.hits == 0:
                block.colour = (255, 150, 0)

    if level == 2:
        shooter.colour = (0, 0, 135)
        for bug in visible_bugs:
            bug.colour = (255, 0, 190)
        for block in visible_blocks:
            if block.hits == 0:
                block.colour = (0, 0, 140)

    if level == 3:
        shooter.colour = (0, 0, 175)
        for bug in visible_bugs:
            bug.colour = (255, 0, 230)
        for block in visible_blocks:
            if block.hits == 0:
                block.colour = (0, 0, 240)

    if level == 4:
        shooter.colour = (0, 0, 215)
        for bug in visible_bugs:
            bug.colour = (255, 15, 255)
        for block in visible_blocks:
            if block.hits == 0:
                block.colour = (255, 255, 15)

    if level == 5:
        shooter.colour = (70, 0, 0)
        for bug in visible_bugs:
            bug.colour = (0, 60, 170)
        for block in visible_blocks:
            if block.hits == 0:
                block.colour = (0, 180, 0)

    if level == 6:
        shooter.colour = (100, 0, 0)
        for bug in visible_bugs:
            bug.colour = (0, 80, 210)
        for block in visible_blocks:
            if block.hits == 0:
                block.colour = (0, 220, 0)

    if level == 7:
        shooter.colour = (0, 255, 255)
        for bug in visible_bugs:
            bug.colour = (0, 255, 255)
        for block in visible_blocks:
            if block.hits == 0:
                block.colour = (0, 255, 255)

    if level == 8:
        pygame.quit()


def draw_window():
    WINDOW.fill((0, 0, 10))
    pygame.draw.rect(WINDOW, (255, 50, 0), (0, 500, 800, 4))


def main():
    pygame.display.set_caption("Centipede")
    global visible_bugs
    shooter = Shooter((0, 0, 55), 400, 470, 20, 27)
    visible_bombs = []

    bonus = Bonus((0, 0, 255), 800, 470, 30, 10, 3)

    q = 300
    for t in range(14):
        visible_bugs.append(Bugs((255, 0, 50), q, 4, 24, 10, 6))
        q += 30

    for s in range(36):
        visible_blocks.append(
            Blocks((255, 100, 0), 11 * random.randint(4, 70),
                   (11 * random.randint(4, 40)) - 7, 24, 10))

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bug in visible_bugs:
            if bug.rect.colliderect(shooter.rect):
                pygame.quit()

        draw_window()
        handle_shooter(shooter, keys_pressed)
        handle_bugs()
        handle_blocks()
        add_bugs()
        handle_bonus(shooter, bonus)
        level_function(shooter)
        pygame.display.update()

    pygame.quit()


main()