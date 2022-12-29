import random
import time

class Enemy:
    def __init__(self):
        self.ecordinates = self.generate_cord()

    def generate_cord(self):
        while True:
            ecordinates = (random.randint(-10, 10), random.randint(-10, 10))
            if ecordinates == (0, 0) or ecordinates == (1, 1) or ecordinates == (-1, -1) or ecordinates == (
            -1, 1) or ecordinates == (1, -1):
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

    def gen_bullet(self, d, cx, cy):
        if d == "UP":
            bullet = (cy + (11 - cy), cy + 11)
            return bullet
        if d == "DOWN":
            bullet = (cy - 11, cy - (11 + cy))
            return bullet
        if d == "LEFT":
            bullet = (cx - 11, cx - (11 + cx))
            return bullet
        if d == "RIGHT":
            bullet = (cx + (11 - cx), cx + 11)
            return bullet

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

    def check_hit(self, ec, bullet):
        ecx = ec[0]
        ecy = ec[1]
        bp = bullet[0]
        bn = bullet[1]

        def hit(d, tankc, enemyc, quadrant):
            if d == "UP" or d == "RIGHT":
                ran = range(tankc, quadrant)
            if d == "DOWN" or d == "LEFT":
                ran = range(tankc, quadrant, -1)
            for shot in ran:
                time.sleep(0.5)
                if shot == enemyc:
                    return True
                else:
                    print(".")
                    continue

        if self.direction == "UP" and self.cordinateX == ecx and ecy >= self.cordinateY:
            if self.cordinateY >= 0 and abs(ecy - self.cordinateY) <= 10:
                return hit(self.direction, self.cordinateY, ecy, bp)
            if self.cordinateY < 0 and abs(ecy - self.cordinateY) <= 10:
                return hit(self.direction, self.cordinateY, ecy, bn)
        if self.direction == "DOWN" and self.cordinateX == ecx and ecy <= self.cordinateY:
            if self.cordinateY >= 0 and abs(ecy - self.cordinateY) <= 10:
                return hit(self.direction, self.cordinateY, ecy, bp)
            if self.cordinateY < 0 and abs(ecy - self.cordinateY) <= 10:
                return hit(self.direction, self.cordinateY, ecy, bn)
        if self.direction == "LEFT" and self.cordinateY == ecy and ecx <= self.cordinateX:
            if self.cordinateX >= 0 and abs(ecx - self.cordinateX) <= 10:
                return hit(self.direction, self.cordinateX, ecx, bp)
            if self.cordinateX < 0 and abs(ecx - self.cordinateX) <= 10:
                return hit(self.direction, self.cordinateX, ecx, bn)
        if self.direction == "RIGHT" and self.cordinateY == ecy and ecx >= self.cordinateX:
            if self.cordinateX >= 0 and abs(ecx - self.cordinateX) <= 10:
                return hit(self.direction, self.cordinateX, ecx, bp)
            if self.cordinateX < 0 and abs(ecx - self.cordinateX) <= 10:
                return hit(self.direction, self.cordinateX, ecx, bn)
        else:
            for hit in range(0, 8):
                time.sleep(0.5)
                print(".")
            return False
    def info(self):
        print(f"Gas left: {self.gas}")
        print(f"Tank Cordinates:{(self.cordinateX, self.cordinateY)}")
        print(f"Direction: {self.direction}")
        print(self.shelldc)



