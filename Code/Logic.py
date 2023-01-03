import random
import time
import pickle


class Plain:
    def __init__(self, xmax, ymax):
        self.xmax = xmax
        self.ymax = ymax
        self.xmin = -xmax
        self.ymin = -ymax


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

    # def pickle_enemy(self):
    #     with open("enemy.pkl", 'wb') as file:
    #         pickle.dump(self.ecordinates, file)
    # def open_pickle_enemy(self):
    #     try:
    #         with open("enemy.pkl", 'rb') as file:
    #             enemy = pickle.load(file)
    #         return enemy
    #     except:
    #         pass


class Tank:
    def __init__(self, cordinateX, cordinateY, direction, shelldc, gas, hittarget, missedtarget):
        self.cordinateX = cordinateX
        self.cordinateY = cordinateY
        self.direction = direction
        self.shelldc = shelldc
        self.gas = gas
        self.hittarget = hittarget
        self.missedtarget = missedtarget

    # Kuras
    def loose_gas(self, action):
        if action in ("n", "w", "s", "e"):
            self.gas -= 10
        if action in ("-", "+", "c"):
            self.gas -= 5

    def gain_gas(self):
        self.gas += 50

    # Judėjimas
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

    # Pasisukimas nejudant iš vietos
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

    # Šūvis + šūvių skaičiavimas
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

    # Patikrina ar šūvis pataiko į priešą
    def check_hit(self, ec):
        ecx = ec[0]
        ecy = ec[1]

        def hit(d, tankc, enemyc):
            global ran
            if d == "UP" or d == "RIGHT":
                ran = range(tankc, tankc + 11)
            if d == "DOWN" or d == "LEFT":
                ran = range(tankc, tankc - 11, -1)
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

    # Pataiktmų ir NEpataikymų skaičiavimas
    def target_hit(self):
        self.hittarget += 1

    def target_missed(self):
        self.missedtarget += 1

    # Tanko info
    def info(self):
        print(f"GAS LEFT: {self.gas}")
        print(f"Tank Cordinates:{(self.cordinateX, self.cordinateY)}")
        print(f"Direction: {self.direction}")
        print(self.shelldc)

    # Pickle Hit record
    def pickle_get_hit(self):
        try:
            players = pickle.load(open("hit.pkl", "rb"))
            name = input("Name: ")
            if name in players:
                if players.get(name) < self.hittarget:
                    players[name] = self.hittarget
                    print("NEW personal best!")
                    with open("hit.pkl", 'wb') as file:
                        pickle.dump(players, file)
                else:
                    print(f"Personal best score to beat: {players[name]}")
            else:
                players[name] = self.hittarget
                print("NEW personal best!")
                with open("hit.pkl", 'wb') as file:
                    pickle.dump(players, file)
        except:
            pickle.dump({}, open("hit.pkl", "wb"))
            players = pickle.load(open("hit.pkl", "rb"))
            name = input("Name: ")
            players[name] = self.hittarget
            print("NEW personal best!")
            with open("hit.pkl", 'wb') as file:
                pickle.dump(players, file)

    def pickle_hit_count(self):
        try:
            with open("hit.pkl", 'rb') as file:
                record = pickle.load(file)
            return sorted(record.items(), key=lambda x: x[1], reverse=True)
        except:
            return ("No previous data")
# Pickle Resume game
# def pickle_tank(self):
#     with open("tank.pkl", 'wb') as file:
#         pickle.dump((self.cordinateX, self.cordinateY, self.direction, self.shelldc, self.gas, self.hittarget, self.missedtarget), file)
# def open_pickle_tank(self):
#     try:
#         with open("tank.pkl", 'rb') as file:
#             tank = pickle.load(file)
#             for item in tank:
#                 return item
#     except:
#         print("No previous game")
