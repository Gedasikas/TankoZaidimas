class Tank:
    def __init__(self, cordinateX, cordinateY, direction, shelldc):
        self.cordinateX = cordinateX
        self.cordinateY = cordinateY
        self.direction = direction
        self.shelldc = shelldc

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


Tank001 = Tank(0, 0, "UP", {"Shot to North": 0, "Shot to West": 0, "Shot to South": 0, "Shot to East": 0, })

while True:
    userput = input("Enter tank command:")
    match userput:
        case "w":
            Tank001.move("n")
        case "a":
            Tank001.move("w")
        case "s":
            Tank001.move("s")
        case "d":
            Tank001.move("e")
        case "e":
            Tank001.shoot()
        case "c":
            print(f"Tank Cordinates:{(Tank001.cordinateX, Tank001.cordinateY)}")
            print(f"Direction: {Tank001.direction}")
            print(Tank001.shelldc)
        case "":
            print("Bye")
            break
