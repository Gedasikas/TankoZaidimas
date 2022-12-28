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
            ecordinates = (random.randint(0, 1), random.randint(3, 10))  #PAKEIST
            if ecordinates == (self.cordinateX, self.cordinateY) or ecordinates == (self.cordinateX + 1, self.cordinateY + 1) or ecordinates == (self.cordinateX -1, self.cordinateY -1) or ecordinates == (
            self.cordinateX -1, self.cordinateY +1) or ecordinates == (self.cordinateX +1, self.cordinateY -1):
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
            bullet = self.cordinateY + 20
            print("SHOT TO NORTH")
            if self.cordinateX != self.ecordinates[0]:
                for hit in range(0, 5):
                    time.sleep(0.5)
                    print(".")
                print("MISS HIT, WRONG X COORDINATES")
            if self.cordinateX == self.ecordinates[0]:
                for hit in range(self.cordinateY, bullet):
                    time.sleep(0.5)
                    print(".")
                    if hit == self.ecordinates[1]:
                        print("HIT")
                        self.ecordinates = self.generate_cord()
                        break
                if self.ecordinates[1] < self.cordinateY:
                        print("MISS HIT, WRONG DIRECTION")





        if self.direction == "LEFT":
            self.shelldc["Shot to West"] += 1
            bullet = self.cordinateX - 20
            print("SHOT TO WEST")
            return bullet
        if self.direction == "DOWN":
            self.shelldc["Shot to South"] += 1
            bullet = self.cordinateY - 20
            print("SHOT TO SOUTH")
            if self.cordinateX != self.ecordinates[0]:
                print("MISS HIT, WRONG X COORDINATES")
            else:
                for hit in range(self.cordinateY, bullet):
                    if hit == self.ecordinates[1]:
                        print("HIT")
                        self.ecordinates = self.generate_cord()
                        break
                    else:
                        print(".")
                        continue
        if self.direction == "RIGHT":
            self.shelldc["Shot to East"] += 1
            bullet = self.cordinateX + 20
            print("SHOT TO EAST")
            return bullet

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
