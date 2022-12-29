from Code.Logic import Tank, Enemy
Tank001 = Tank(0, 0, "UP", {"Shot to North": 0, "Shot to West": 0, "Shot to South": 0, "Shot to East": 0, }, 100)
Enemy001 = Enemy()
while True:
    if
    userput = input("Enter tank command:")
    match userput:
        case "w":
            print()
            Tank001.move("n")
            Tank001.loose_gas("w")
            print()
        case "a":
            print()
            Tank001.move("w")
            Tank001.loose_gas("a")
            print()
        case "s":
            print()
            Tank001.move("s")
            Tank001.loose_gas("s")
            print()
        case "d":
            print()
            Tank001.move("e")
            Tank001.loose_gas("d")
            print()
        case "+":
            print()
            Tank001.turn_turret("+")
            Tank001.loose_gas("+")
            print("TURNED CLOCKWISE")
            print()
        case "-":
            print()
            Tank001.turn_turret("-")
            Tank001.loose_gas("-")
            print("TURNED ANTI-CLOCKWISE")
            print()
        case "e":
            print()
            Tank001.shoot()
            if Tank001.check_hit(Enemy001.ecordinates,
                                 Tank001.gen_bullet(Tank001.direction, Tank001.cordinateX, Tank001.cordinateY)) == True:
                print("HIT")
                Enemy001.ecordinates = Enemy001.generate_cord()
            else:
                print("MISS HIT")
            print()
        case "c":
            print()
            Tank001.info()
            print(f"Enemy cordinates: {Enemy001.ecordinates}")
            print()
        case "/":
            print("Bye")
            break
