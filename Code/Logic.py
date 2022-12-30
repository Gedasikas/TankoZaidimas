import random
import time

class Plain:
    pass

class Enemy:
    def __init__(self):
        self.ecordinates = self.generate_cord()

    def generate_cord(self):
        while True:
            ecordinates = (random.randint(-10, 10), random.randint(-10, 10))
            if ecordinates == (0, 0):
                continue
            else:
                return ecordinates


class Tank:
    def __init__(self, cordinateX, cordinateY, direction, shelldc, gas):
        self.cordinateX = cordinateX
        self.cordinateY = cordinateY
        self.direction = direction
        self.shelldc = shelldc
        self.gas = gas
        self.hittarget = 0
        self.missedtarget = 0

    def loose_gas(self, action):
        if action in ("w",  "d", "s", "a", "e"):
            self.gas -= 10
        if action in ("-", "+", "c"):
            self.gas -= 5

    def gain_gas(self):
        self.gas += 50

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

    def turn_turret(self, turn):
        if turn == "+":
            if self.direction == "UP":
                self.direction = "RIGHT"
            elif self.direction == "RIGHT":
                self.direction = "DOWN"
            elif self.direction == "DOWN":
                self.direction = "LEFT"
            else:
                self.direction = "UP"
        elif turn == "-":
            if self.direction == "UP":
                self.direction = "LEFT"
            elif self.direction == "LEFT":
                self.direction = "DOWN"
            elif self.direction == "DOWN":
                self.direction = "RIGHT"
            else:
                self.direction = "UP"

    def shoot(self):
        if self.direction == "UP":
            self.shelldc["Shot to North"] += 1
            print("SHOT TO NORTH")
        if self.direction == "LEFT":
            self.shelldc["Shot to West"] += 1
            print("SHOT TO WEST")
        if self.direction == "DOWN":
            self.shelldc["Shot to South"] += 1
            print("SHOT TO SOUTH")
        if self.direction == "RIGHT":
            self.shelldc["Shot to East"] += 1
            print("SHOT TO EAST")

    def check_hit(self, ec):
        ecx = ec[0]
        ecy = ec[1]

        def hit(d, tankc, enemyc):
            if d == "UP" or d == "RIGHT":
                ran = range(tankc, tankc+11)
            if d == "DOWN" or d == "LEFT":
                ran = range(tankc, tankc-11, -1)
            for shot in ran:
                time.sleep(0.5)
                if shot == enemyc:
                    return True
                else:
                    print(".")
                    continue

        if self.direction == "UP" and self.cordinateX == ecx and ecy >= self.cordinateY:
            return hit(self.direction, self.cordinateY, ecy)
        if self.direction == "DOWN" and self.cordinateX == ecx and ecy <= self.cordinateY:
                return hit(self.direction, self.cordinateY, ecy)
        if self.direction == "LEFT" and self.cordinateY == ecy and ecx <= self.cordinateX:
                return hit(self.direction, self.cordinateX, ecx)
        if self.direction == "RIGHT" and self.cordinateY == ecy and ecx >= self.cordinateX:
                return hit(self.direction, self.cordinateX, ecx)
        else:
            for hit in range(0, 10):
                time.sleep(0.5)
                print(".")
            return False

    def target_hit(self):
        self.hittarget += 1
    def target_missed(self):
        self.missedtarget += 1

    def info(self):
        print(f"GAS LEFT: {self.gas}")
        print(f"Tank Cordinates:{(self.cordinateX, self.cordinateY)}")
        print(f"Direction: {self.direction}")
        print(self.shelldc)