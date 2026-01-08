import time


f1 = "fortnite-win-tracker/data/npulsive.txt" # TODO: have names as environment variables
f2 = "fortnite-win-tracker/data/dogeous.txt"


def read_stats(file_path):
    with open(file_path, "r") as f:
        return [int(x) for x in f.read().split(",")]


def write_stats(file_path, solos, duos, squads):
    with open(file_path, "w") as f:
        f.write(f"{solos}, {duos}, {squads}")


def print_stats():
    account_1_wins = read_stats(f1)
    account_2_wins = read_stats(f2)

    print()
    print("Npulsive")
    time.sleep(0.1)
    print(f" {account_1_wins[0]} solos")
    time.sleep(0.1)
    print(f" {account_1_wins[1]} duos")
    time.sleep(0.1)
    print(f" {account_1_wins[2]} squads")
    time.sleep(0.1)

    print("Dog")
    time.sleep(0.1)
    print(f" {account_2_wins[0]} solos")
    time.sleep(0.1)

    print("TOTAL")
    time.sleep(0.1)
    total_solos = account_1_wins[0] + account_2_wins[0]
    print(f" {total_solos} solos")
    time.sleep(0.1)
    total_wins = total_solos + account_1_wins[1] + account_1_wins[2]
    print(f" {total_wins} wins")


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

            if gamemode not in [1, 2, 3]:
                print("Invalid input.")
                continue
        
            n = int(input("Wins to add: "))
            account_1_wins = read_stats(f1)
            new_wins = account_1_wins[gamemode - 1] + n

            if gamemode == 1:
                if n == 0:
                    print(f"[Npulsive] Bruh you still have {new_wins} solo wins.")
                else:
                    write_stats(f1, new_wins, account_1_wins[1], account_1_wins[2])
                    if n < 0:
                        print(f"[Npulsive] Bruh you're back at {new_wins} solo wins.")
                    else:
                        print(f"[Npulsive] You now have {new_wins} solo wins!")
            
            elif gamemode == 2:
                write_stats(f1, account_1_wins[0], new_wins, account_1_wins[2])
                print(f"[Npulsive] You now have {new_wins} duo wins!")
            
            elif gamemode == 3:
                write_stats(f1, account_1_wins[0], account_1_wins[1], new_wins)
                print(f"[Npulsive] You now have {new_wins} squad wins!")
        
        elif acc == 2:
            n = int(input("Wins to add: "))
            account_2_wins = read_stats(f2)
            new_wins = account_2_wins[0] + n
            write_stats(f2, new_wins, 0, 0)
            print(f"[Dogeous] You now have {new_wins} solo wins!")
        
        else:
            print("Invalid input.")
    
    else:
        print("Invalid input.")
    
    print()
