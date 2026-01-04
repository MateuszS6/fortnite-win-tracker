import time


f1 = "fortnite-win-tracker/data/npulsive.txt"
f2 = "fortnite-win-tracker/data/dogeous.txt"


def view_stats():
    npulsive_data = open(f1,"r")
    for line in npulsive_data:
        wins = line.strip().split(",")
    solos = wins[0]
    duos = wins[1]
    squads = wins[2]
    npulsive_data.close()
    print()

    print("Npulsive")
    time.sleep(0.1)
    print(f" {solos} solos")
    time.sleep(0.1)
    print(f" {duos} duos")
    time.sleep(0.1)
    print(f" {squads} squads")
    time.sleep(0.1)

    dogeous_data = open(f2,"r")
    for line in dogeous_data:
        wins = line.strip().split(",")
    other_solos = wins[0]
    dogeous_data.close()

    print("Dog")
    time.sleep(0.1)
    print(f" {wins[0]} solos")
    time.sleep(0.1)

    print("TOTAL")
    time.sleep(0.1)
    total_solos = int(solos) + int(other_solos)
    print(f" {str(total_solos)} solos")
    time.sleep(0.1)
    total_wins = total_solos + int(duos) + int(squads)
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
        view_stats()
    
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
                npulsive_data = open(f1,"r+")
                for line in npulsive_data:
                    wins = line.strip().split(",")
                new_solos = str(int(wins[0]) + s)
                if s == 0:
                    print(f"[Npulsive] Bruh you still have {new_solos} solo wins.")
                else:
                    duos = str(wins[1])
                    squads = str(wins[2])
                    npulsive_data.truncate(0)
                    npulsive_data.seek(0)
                    npulsive_data.write(f"{new_solos}, {wins[1]}, {wins[2]}")
                    npulsive_data.close()
                    if s < 0:
                        print(f"[Npulsive] Bruh you're back at {new_solos} solo wins.")
                    else:
                        print(f"[Npulsive] You now have {new_solos} solo wins!")
            
            elif gamemode == 2:
                d = int(input("Wins to add: "))
                npulsive_data = open(f1,"r+")
                for line in npulsive_data:
                    wins = line.split(", ")
                new_duos = str(int(wins[1]) + d)
                npulsive_data.truncate(0)
                npulsive_data.seek(0)
                npulsive_data.write(f"{wins[0]}, {new_duos}, {wins[2]}")
                npulsive_data.close()
                print(f"[Npulsive] You now have {new_duos} duo wins!")
            
            elif gamemode == 3:
                sq = int(input("Wins to add: "))
                npulsive_data = open(f1,"r+")
                for line in npulsive_data:
                    wins = line.strip().split(",")
                new_squads = str(int(wins[2]) + sq)
                npulsive_data.truncate(0)
                npulsive_data.seek(0)
                npulsive_data.write(f"{wins[0]}, {wins[1]}, {new_squads}")
                npulsive_data.close()
                print(f"[Npulsive] You now have {new_squads} squad wins!")
            
            else:
                print("Invalid input.")
        
        elif acc == 2:
            n = int(input("Wins to add: "))
            dogeous_data = open(f2,"r+")
            for line in dogeous_data:
                wins = line.strip().split(",")
            new_solos = str(int(wins[0]) + n)
            dogeous_data.truncate(0)
            dogeous_data.seek(0)
            dogeous_data.write(f"{new_solos}, {wins[1]}, {wins[2]}")
            dogeous_data.close()
            print(f"[Dogeous] You now have {new_solos} solo wins!")
        
        else:
            print("Invalid input.")
    
    else:
        print("Invalid input.")
    
    print()
