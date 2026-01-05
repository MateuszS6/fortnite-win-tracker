import time


f1 = "fortnite-win-tracker/data/npulsive.txt"
f2 = "fortnite-win-tracker/data/dogeous.txt"


def read_stats(file_path):
    data_file = open(file_path, "r")
    for line in data_file:
        wins = line.strip().split(",")
    data_file.close()
    return wins


def write_stats(file_path, solos, duos, squads):
    data_file = open(file_path, "r+")
    data_file.truncate(0)
    data_file.seek(0)
    data_file.write(f"{str(solos)}, {str(duos)}, {str(squads)}")
    data_file.close()


def print_stats():
    npulsive_wins = read_stats(f1)
    dogeous_wins = read_stats(f2)

    print()
    print("Npulsive")
    time.sleep(0.1)
    print(f" {npulsive_wins[0]} solos")
    time.sleep(0.1)
    print(f" {npulsive_wins[1]} duos")
    time.sleep(0.1)
    print(f" {npulsive_wins[2]} squads")
    time.sleep(0.1)

    print("Dog")
    time.sleep(0.1)
    print(f" {dogeous_wins[0]} solos")
    time.sleep(0.1)

    print("TOTAL")
    time.sleep(0.1)
    total_solos = int(npulsive_wins[0]) + int(dogeous_wins[0])
    print(f" {str(total_solos)} solos")
    time.sleep(0.1)
    total_wins = total_solos + int(npulsive_wins[1]) + int(npulsive_wins[2])
    print(f" {str(total_wins)} wins")


while True:
    time.sleep(0.5)
    print(" > Fortnite Win Tracker")
    time.sleep(0.1)
    print("[1] View all stats")
    time.sleep(0.1)
    print("[2] Edit stats")
    time.sleep(0.1)
    options = int(input("Select option: "))

    if options == 1:
        print_stats()
    
    elif options == 2:
        print("[1] Npulsive")
        time.sleep(0.1)
        print("[2] Dog")
        time.sleep(0.1)
        acc = int(input("Select account: "))

        if acc == 1:
            print("[1] Solo")
            time.sleep(0.1)
            print("[2] Duo")
            time.sleep(0.1)
            print("[3] Squad")
            time.sleep(0.1)
            gamemode = int(input("Select gamemode: "))
        
            if gamemode == 1:
                s = int(input("Wins to add: "))
                npulsive_wins = read_stats(f1)
                new_solos = int(npulsive_wins[0]) + s
                if s == 0:
                    print(f"[Npulsive] Bruh you still have {str(new_solos)} solo wins.")
                else:
                    write_stats(f1, new_solos, npulsive_wins[1], npulsive_wins[2])
                    if s < 0:
                        print(f"[Npulsive] Bruh you're back at {str(new_solos)} solo wins.")
                    else:
                        print(f"[Npulsive] You now have {str(new_solos)} solo wins!")
            
            elif gamemode == 2:
                d = int(input("Wins to add: "))
                npulsive_wins = read_stats(f1)
                new_duos = int(npulsive_wins[1]) + d
                write_stats(f1, npulsive_wins[0], new_duos, npulsive_wins[2])
                print(f"[Npulsive] You now have {str(new_duos)} duo wins!")
            
            elif gamemode == 3:
                sq = int(input("Wins to add: "))
                npulsive_wins = read_stats(f1)
                new_squads = int(npulsive_wins[2]) + sq
                write_stats(f1, npulsive_wins[0], npulsive_wins[1], new_squads)
                print(f"[Npulsive] You now have {str(new_squads)} squad wins!")
            
            else:
                print("Invalid input.")
        
        elif acc == 2:
            n = int(input("Wins to add: "))
            dogeous_wins = read_stats(f2)
            new_solos = int(dogeous_wins[0]) + n
            write_stats(f2, new_solos, 0, 0)
            print(f"[Dogeous] You now have {str(new_solos)} solo wins!")
        
        else:
            print("Invalid input.")
    
    else:
        print("Invalid input.")
    
    print()
