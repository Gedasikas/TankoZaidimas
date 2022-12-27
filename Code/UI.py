class Tank():
    def __init__(self, cordinateX, cordinateY, direction):
        self.cordinateX = cordinateX
        self.cordinateY = cordinateY
        self.direction = direction
    def move(self, to):
        if to == "n":
            self.direction = "Up"
            self.cordinateY += 1
            print("Moved North")
        if to == "w":
            self.direction = "Left"
            self.cordinateX -= 1
            print("Moved West")
        if to == "s":
            self.direction = "Down"
            self.cordinateY -= 1
            print("Moved South")
        if to == "e":
            self.direction = "Right"
            self.cordinateX += 1
            print("Moved East")

    def shoot(self):
        print("Shot")


Tank001 = Tank(0, 0, "Up")

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
            print((Tank001.cordinateX, Tank001.cordinateY))
            print(Tank001.direction)
        case "":
            print ("Bye")
            break


