import pygame
import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="chirananda", passwd="chirananda", database="record")

c = db.cursor()

try:
    # create database
    c.execute("CREATE DATABASE record")

    # create table to put high score
    c.execute(
        "CREATE TABLE col1 (hiscore smallint UNSIGNED, id int PRIMARY KEY AUTO_INCREMENT)")

    # added 1 element to the database; wich will be kept updating
    c.execute("INSERT INTO col1 (hiscore) VALUES(%s)", (0,))
    db.commit()
except:
    pass

pygame.init()

win = pygame.display.set_mode((500, 700))
pygame.display.set_caption("TETTRIS")

bg = pygame.image.load("bg2.jpg")


def lineCheck(bricks2, yList):

    global yVal

    for i in bricks2:

        yCount = 0

        for j in bricks2:

            if i.y == j.y:

                yCount += 1

        if yCount == 5:

            yList.append(i)
            yVal = i.y


class brick():

    def __init__(self, x1=200, y1=0):
        self.x = x1
        self.y = y1

    def draw(self, win):

        hitbox = (self.x, self.y, 100, 100)
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 100, 100))
        pygame.draw.rect(win, (0, 0, 0), hitbox, 2)


bricks = []
bricks2 = []
yList = []
bricks.append(brick())
font = pygame.font.SysFont('comicsans', 30, True)

# initializing variables
preScore = 0
yVal = 0
score = 0
left = True
right = True
maxY = 550
run = True


# main loop
while run:

    pygame.time.delay(100)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in bricks:

        for j in bricks2:
            if i.x < j.x and i.x + 100 > j.x or i.x > j.x and i.x < j.x + 100 or i.x == j.x:
                if maxY > j.y - 100:
                    maxY = j.y - 100

            if i.y + 100 > j.y and i.y < j.y + 100 or i.y == j.y:

                if i.x - 1 < j.x + 100 and i.x > j.x:
                    left = False

                else:
                    left = True

                if i.x + 101 > j.x and i.x < j.x:
                    right = False
                else:
                    right = True

        if i.y < maxY:

            if keys[pygame.K_LEFT] and left and i.x > 0:
                i.x -= 5
                maxY = 550

            print(left)

            if keys[pygame.K_RIGHT] and right and i.x + 100 < 500:
                i.x += 5
                maxY = 550

            if keys[pygame.K_DOWN]:
                i.y += 10

            else:
                i.y += 5

        elif maxY > 50:
            k = bricks.pop()
            bricks2.append(k)
            bricks.append(brick())

            lineCheck(bricks2, yList)

            for i in yList:
                bricks2.remove(i)
                score += 20

            yList = []

            if yVal != 0:
                for i in bricks2:
                    if i.y < yVal:
                        i.y += 100

            yVal = 0

            maxY = 550
            left = True
            right = True

    if maxY == 50:

        c.execute("UPDATE col1 SET hiscore = %s WHERE id = %s", (score, 1))
        db.commit()

    c.execute("SELECT hiscore FROM col1 WHERE id = 1")

    for i in c:
        preScore = i[0]

    win.blit(bg, (0, 0))

    for i in bricks:
        i.draw(win)

    for i in bricks2:
        i.draw(win)

    text1 = font.render("SCORE    : " + str(score), 1, (0, 0, 0))
    win.blit(text1, (300, 20))

    text2 = font.render("HI SCORE: " + str(preScore), 1, (0, 0, 0))
    win.blit(text2, (300, 50))

    pygame.display.update()


pygame.quit()
