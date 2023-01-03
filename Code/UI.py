from Code.Logic import Tank, Enemy, Plain, time
import os

Plain001 = Plain(10, 10)

while True:
    commandput = input("""Start new game: 1
Controls: 2
High scores: 3
Delete high scores: 4
Exit: 5
Input:""")
    match commandput:
        case "1":
            Tank001 = Tank(0, 0, "UP", {"Shot to North": 0, "Shot to West": 0, "Shot to South": 0, "Shot to East": 0, }, 100)
            Enemy001 = Enemy()
            print()
            Tank001.info()
            print(f"Enemy coordinates: {Enemy001.ecordinates}")
            print()
            while True:
                if Tank001.gas <= 0:
                    Tank001.info()
                    print(f"Enemy coordinates: {Enemy001.ecordinates}\n")
                    print(f"Targets hit: {Tank001.hittarget}  Targets missed: {Tank001.missedtarget}")
                    print("OUT OF GAS\n###GAME OVER###")
                    print()
                    Tank001.pickle_get_hit()
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
                                print(f"Enemy coordinates: {Enemy001.ecordinates}")
                            else:
                                print("MISS HIT")
                                Tank001.target_missed()
                                Tank001.loose_gas("e")
                            print()
                        case "c":
                            print()
                            Tank001.loose_gas("c")
                            Tank001.info()
                            print(f"Enemy coordinates: {Enemy001.ecordinates}")
                            print()
                        case "/":
                            print("Bye")
                            break
                        case other:
                            print()
                            print("COMMAND DOES NOT EXIST")
                            print()

        case "2":
            print()
            print("""Judėjimas: w a s arba d
Šauti: e maksimalus šūvio atstumas yra 10 kordinačių
Pasisukti 90 laipsnių prieš laikrodžio rodyklę: -
Pasisukti 90 laipsnių palei laikrodžio rodyklę: +
Info: c
Išeiti: /
Judėjimas ir šūvis kainuoja 10 kuro, pasisukimas ir info kainuoja 5.
Pataikymas duoda 50 kuro.""")
        case "3":
            print()
            Tank001 = Tank(0, 0, "UP", {"Shot to North": 0, "Shot to West": 0, "Shot to South": 0, "Shot to East": 0, }, 100)
            print("HIGH SCORES:")
            l = Tank001.pickle_hit_count()
            if l == "No previous data":
                print(l)
            else:
                for count, player in enumerate(l, 1):
                    print(f"{count}. {player}")
        case "4":
            try:
                file = 'hit.pkl'
                location = "C:/Users/admin/Documents/GitHub/TankoZaidimas/Code"
                path = os.path.join(location, file)
                os.remove(path)
                print()
                print("High score data removed")
            except:
                print()
                print("No saved data")
        case "5":
            print("Thanks for playing, bye")
            break
        case other:
            print("Command does not exist")
    print()




