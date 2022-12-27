class Tank():
    def __init__(self):
        pass
    def move(self, to):
        if to == "n":
            print("Moved North")
        if to == "w":
            print("Moved West")
        if to == "s":
            print("Moved South")
        if to == "e":
            print("Moved East")

Tank001 = Tank()

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
            pass
        case "":
            print ("Bye")
            break


