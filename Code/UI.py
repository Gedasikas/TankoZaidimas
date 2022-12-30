from Code.Logic import Tank, Enemy, Plain
import time
Tank001 = Tank(0, 0, "UP", {"Shot to North": 0, "Shot to West": 0, "Shot to South": 0, "Shot to East": 0, }, 1000)
Enemy001 = Enemy()
Plain001 = Plain(10, 10)
#----------
Tank001.info()
print(f"Enemy cordinates: {Enemy001.ecordinates}")
print()
#___________
while True:
    if Tank001.gas <= 0:
        Tank001.info()
        print(f"Enemy cordinates: {Enemy001.ecordinates}\n")
        print(f"Targets hit: {Tank001.hittarget}  Targets missed: {Tank001.missedtarget}")
        print("OUT OF GAS\n###GAME OVER###")
        break
    else:
        userput = input("Enter tank command:")
        match userput:
            case "w":
                print()
                if Tank001.cordinateY != Plain001.ymax:
                    Tank001.move("n")
                if Tank001.cordinateY == Plain001.ymax:
                    print("REACHED THE MAP BORDER")
                Tank001.loose_gas("n")
                print()
            case "a":
                print()
                if Tank001.cordinateX != Plain001.xmin:
                    Tank001.move("w")
                if Tank001.cordinateX == Plain001.xmin:
                    print("REACHED THE MAP BORDER")
                Tank001.loose_gas("w")
                print()
            case "s":
                print()
                if Tank001.cordinateY != Plain001.ymin:
                    Tank001.move("s")
                if Tank001.cordinateY == Plain001.ymin:
                    print("REACHED THE MAP BORDER")
                Tank001.loose_gas("s")
                print()
            case "d":
                print()
                if Tank001.cordinateX != Plain001.xmax:
                    Tank001.move("e")
                if Tank001.cordinateX == Plain001.xmax:
                    print("REACHED THE MAP BORDER")
                Tank001.loose_gas("e")
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
                if Tank001.check_hit(Enemy001.ecordinates) == True:
                    print("HIT")
                    Tank001.target_hit()
                    Tank001.gain_gas()
                    Enemy001.ecordinates = Enemy001.generate_cord()
                    time.sleep(0.75)
                    print()
                    Tank001.info()
                    print(f"Enemy cordinates: {Enemy001.ecordinates}")
                else:
                    print("MISS HIT")
                    Tank001.target_missed()
                    Tank001.loose_gas("e")
                print()
            case "c":
                print()
                Tank001.loose_gas("c")
                Tank001.info()
                print(f"Enemy cordinates: {Enemy001.ecordinates}")
                print()
            case "/":
                print("Bye")
                break
