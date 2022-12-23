def ui(userput):
    match userput:
        case "w":
            return "North"
        case "a":
            return "West"
        case "s":
            return "South"
        case "d":
            return "East"
        case "e":
            return "Shoot"
        case "":
            return "Bye"
while True:
    userput = input("Enter tank command:")
    print(ui(userput))
    if userput == "":
        break
    else:
        continue