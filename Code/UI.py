import random
import time


class Tank:
    def __init__(self, cordinateX, cordinateY, direction, shelldc):
        self.cordinateX = cordinateX
        self.cordinateY = cordinateY
        self.direction = direction
        self.shelldc = shelldc
        self.ecordinates = self.generate_cord()

    def generate_cord(self):
        while True:
            ecordinates = (random.randint(-10, 1), random.randint(-10, 10))  # PAKEIST
            if ecordinates == (self.cordinateX, self.cordinateY) or ecordinates == (
            self.cordinateX + 1, self.cordinateY + 1) or ecordinates == (
            self.cordinateX - 1, self.cordinateY - 1) or ecordinates == (
            self.cordinateX - 1, self.cordinateY + 1) or ecordinates == (
            self.cordinateX + 1, self.cordinateY - 1):
                continue
            else:
                return ecordinates

    def move(self, to):
        if to == "n":
            self.direction = "UP"
            self.cordinateY += 1
            print("MOVED NORTH")
        if to == "w":
            self.direction = "LEFT"
            self.cordinateX -= 1
            print("MOVED WEST")
        if to == "s":
            self.direction = "DOWN"
            self.cordinateY -= 1
            print("MOVED SOUTH")
        if to == "e":
            self.direction = "RIGHT"
            self.cordinateX += 1
            print("MOVED EAST")

    def shoot(self):
        if self.direction == "UP":
            self.shelldc["Shot to North"] += 1
            bulletp = self.cordinateY + (10-self.cordinateY)
            bulletm = self.cordinateY + 10
            print("SHOT TO NORTH")
            if self.cordinateX != self.ecordinates[0]:
                for hit in range(0, 5):
                    time.sleep(0.5)
                    print(".")
                print("MISS HIT, WRONG X COORDINATES")
            if self.cordinateX == self.ecordinates[0] and self.ecordinates[1] >= self.cordinateY and self.cordinateY >= 0 and abs(self.ecordinates[1]-self.cordinateY) <= 10:
                for hit in range(self.cordinateY, bulletp + 1):
                    time.sleep(0.5)
                    print(".")
                    if hit == self.ecordinates[1]:
                        print("HIT")
                        self.ecordinates = self.generate_cord()
                        break
                return
            if self.cordinateX == self.ecordinates[0] and self.ecordinates[1] >= self.cordinateY and self.cordinateY < 0 and abs(self.ecordinates[1]-self.cordinateY) <= 10:
                for hit in range(self.cordinateY, bulletm + 1):
                    time.sleep(0.5)
                    print(".")
                    if hit == self.ecordinates[1]:
                        print("HIT")
                        self.ecordinates = self.generate_cord()
                        break
                return
            if self.cordinateX == self.ecordinates[0] and ((self.ecordinates[1] < self.cordinateY or abs(self.ecordinates[1]-self.cordinateY) > 10)):
                for hit in range(0, 5):
                    time.sleep(0.5)
                    print(".")
                print("MISS HIT, WRONG DIRECTION OR NOT IN RANGE")


        if self.direction == "LEFT":
            self.shelldc["Shot to West"] += 1
            bulletp = self.cordinateX - 10
            bulletm = self.cordinateX - (10 + self.cordinateX)
            print("SHOT TO WEST")
            if self.cordinateY != self.ecordinates[1]:
                for hit in range(0, 5):
                    time.sleep(0.5)
                    print(".")
                print("MISS HIT, WRONG Y COORDINATES")
            if self.cordinateY == self.ecordinates[1] and self.ecordinates[0] <= self.cordinateX and self.cordinateX >=0 and abs(self.ecordinates[0] - self.cordinateX) <= 10:
                for hit in range(self.cordinateX, bulletp - 1, -1):
                    time.sleep(0.5)
                    print(".")
                    if hit == self.ecordinates[0]:
                        print("HIT")
                        self.ecordinates = self.generate_cord()
                        break
                return
            if self.cordinateY == self.ecordinates[1] and self.ecordinates[0] <= self.cordinateX and self.cordinateY < 0 and abs(self.ecordinates[0] - self.cordinateX) <= 10:
                for hit in range(self.cordinateX, bulletm - 1, -1):
                    time.sleep(0.5)
                    print(".")
                    if hit == self.ecordinates[0]:
                        print("HIT")
                        self.ecordinates = self.generate_cord()
                        break
                return
            if self.cordinateY == self.ecordinates[1] and ((self.ecordinates[0] > self.cordinateX or abs(self.ecordinates[0] - self.cordinateX) > 10)):
                for hit in range(0, 5):
                    time.sleep(0.5)
                    print(".")
                print("MISS HIT, WRONG DIRECTION OR NOT IN RANGE")

        if self.direction == "DOWN":
            self.shelldc["Shot to South"] += 1
            bulletp = self.cordinateY - 10
            bulletm = self.cordinateY - (10 + self.cordinateY)
            print("SHOT TO SOUTH")
            if self.cordinateX != self.ecordinates[0]:
                for hit in range(0, 5):
                    time.sleep(0.5)
                    print(".")
                print("MISS HIT, WRONG X COORDINATES")
            if self.cordinateX == self.ecordinates[0] and self.ecordinates[1] <= self.cordinateY and self.cordinateY >= 0 and abs(self.ecordinates[1] - self.cordinateY) <= 10:
                for hit in range(self.cordinateY, bulletp - 1, -1):
                    time.sleep(0.5)
                    print(".")
                    if hit == self.ecordinates[1]:
                        print("HIT")
                        self.ecordinates = self.generate_cord()
                        break
                return
            if self.cordinateX == self.ecordinates[0] and self.ecordinates[1] <= self.cordinateY and self.cordinateY < 0 and abs(self.ecordinates[1] - self.cordinateY) <= 10:
                for hit in range(self.cordinateY, bulletm - 1, -1):
                    time.sleep(0.5)
                    print(".")
                    if hit == self.ecordinates[1]:
                        print("HIT")
                        self.ecordinates = self.generate_cord()
                        break
                return
            if self.cordinateX == self.ecordinates[0] and ((self.ecordinates[1] > self.cordinateY or abs(self.ecordinates[1] - self.cordinateY) > 10)):
                for hit in range(0, 5):
                    time.sleep(0.5)
                    print(".")
                print("MISS HIT, WRONG DIRECTION OR NOT IN RANGE")

        if self.direction == "RIGHT":
            self.shelldc["Shot to East"] += 1
            bulletp = self.cordinateX - 10
            bulletm = self.cordinateX - (10 + self.cordinateX)
            print("SHOT TO EAST")
            if self.cordinateY != self.ecordinates[1]:
                for hit in range(0, 5):
                    time.sleep(0.5)
                    print(".")
                print("MISS HIT, WRONG Y COORDINATES")
            if self.cordinateY == self.ecordinates[1] and self.ecordinates[0] >= self.cordinateX and self.cordinateX >= 0 and abs(self.ecordinates[0]-self.cordinateX) <= 10:
                for hit in range(self.cordinateX, bulletp + 1):
                    time.sleep(0.5)
                    print(".")
                    if hit == self.ecordinates[0]:
                        print("HIT")
                        self.ecordinates = self.generate_cord()
                        break
                return
            if self.cordinateY == self.ecordinates[1] and self.ecordinates[0] >= self.cordinateX and self.cordinateX < 0 and abs(self.ecordinates[0]-self.cordinateX) <= 10:
                for hit in range(self.cordinateX, bulletm + 1):
                    time.sleep(0.5)
                    print(".")
                    if hit == self.ecordinates[0]:
                        print("HIT")
                        self.ecordinates = self.generate_cord()
                        break
                return
            if self.cordinateY == self.ecordinates[1] and ((self.ecordinates[0] < self.cordinateX or abs(self.ecordinates[0]-self.cordinateX) > 10)):
                for hit in range(0, 5):
                    time.sleep(0.5)
                    print(".")
                print("MISS HIT, WRONG DIRECTION OR NOT IN RANGE")

    def info(self):
        print(f"Tank Coordinates:{(Tank001.cordinateX, Tank001.cordinateY)}")
        print(f"Direction: {Tank001.direction}")
        print(Tank001.shelldc)
        print(f"Enemy Coordinates:: {self.ecordinates}")


Tank001 = Tank(0, 0, "UP", {"Shot to North": 0, "Shot to West": 0, "Shot to South": 0, "Shot to East": 0, })
while True:
    userput = input("Enter tank command:")
    match userput:
        case "w":
            print()
            Tank001.move("n")
            print()
        case "a":
            print()
            Tank001.move("w")
            print()
        case "s":
            print()
            Tank001.move("s")
            print()
        case "d":
            print()
            Tank001.move("e")
            print()
        case "e":
            print()
            Tank001.shoot()
            print()
        case "c":
            print()
            Tank001.info()
            print()
        case "":
            print("Bye")
            break
