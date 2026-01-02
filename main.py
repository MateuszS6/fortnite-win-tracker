import time


f1 = "fortnite-win-tracker/data/npulsive.txt"
f2 = "fortnite-win-tracker/data/dogeous.txt"


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
        mainAcc = open(f1,"r")
        for line in mainAcc:
            fields = line.strip().split(",")
        mainSolos = fields[0]
        mainDuos = fields[1]
        mainSquads = fields[2]
        mainAcc.close()

        print()
        print("Npulsive")
        time.sleep(0.1)
        print(f" {mainSolos} solos")
        time.sleep(0.1)
        print(f" {mainDuos} duos")
        time.sleep(0.1)
        print(f" {mainSquads} squads")
        time.sleep(0.1)

        otherAcc = open(f2,"r")
        for line in otherAcc:
            fields = line.strip().split(",")
        otherSolos = fields[0]
        otherAcc.close()

        print("Dog")
        time.sleep(0.1)
        print(f" {fields[0]} solos")
        time.sleep(0.1)
        print("TOTAL")
        time.sleep(0.1)
        tSolos = int(mainSolos) + int(otherSolos)
        print(f" {str(tSolos)} solos")
        time.sleep(0.1)
        tWins = tSolos + int(mainDuos) + int(mainSquads)
        print(f" {str(tWins)} wins")
    
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
            i_mode = int(input("Select gamemode: "))
        
            if i_mode == 1:
                i_solos = input("Wins to add: ")
                mainAcc = open(f1,"r+")
                for line in mainAcc:
                    fields = line.strip().split(",")
                nSolos = str(int(fields[0]) + int(i_solos))
                if i_solos == "0":
                    print(f"[Npulsive] Bruh you still have {nSolos} solo wins.")
                else:
                    oDuos = str(fields[1])
                    oSquads = str(fields[2])
                    mainAcc.truncate(0)
                    mainAcc.seek(0)
                    mainAcc.write(nSolos + "," + oDuos + "," + oSquads)
                    mainAcc.close()
                    if int(i_solos) < 0:
                        print(f"[Npulsive] Bruh you're back at {nSolos} solo wins.")
                    else:
                        print(f"[Npulsive] You now have {nSolos} solo wins!")
            
            elif i_mode == 2:
                i_duos = input("Wins to add: ")
                mainAcc = open(f1,"r+")
                for line in mainAcc:
                    fields = line.split(", ")
                oSolos = str(fields[0])
                nDuos = str(int(fields[1]) + int(i_duos))
                oSquads = str(fields[2])
                mainAcc.truncate(0)
                mainAcc.seek(0)
                mainAcc.write(f"{oSolos}, {nDuos}, {oSquads}")
                mainAcc.close()
                print(f"[Npulsive] You now have {nDuos} duo wins!")
            
            elif i_mode == 3:
                i_squads = input("Wins to add: ")
                mainAcc = open(f1,"r+")
                for line in mainAcc:
                    fields = line.strip().split(",")
                oSolos = str(fields[0])
                oDuos = str(fields[1])
                nSquads = str(int(fields[2]) + int(i_squads))
                mainAcc.truncate(0)
                mainAcc.seek(0)
                mainAcc.write(f"{oSolos}, {oDuos}, {nSquads}")
                mainAcc.close()
                print(f"[Npulsive] You now have {nSquads} squad wins!")
            
            else:
                print("Invalid input.")
        
        elif acc == 2:
            ii_solos = input("Wins to add: ")
            otherAcc = open(f2,"r+")
            for line in otherAcc:
                fields = line.strip().split(",")
            nSolos = str(int(fields[0]) + int(ii_solos))
            oDuos = str(fields[1])
            oSquads = str(fields[2])
            otherAcc.truncate(0)
            otherAcc.seek(0)
            otherAcc.write(f"{nSolos}, {oDuos}, {oSquads}")
            otherAcc.close()
            print(f"[Dogeous] You now have {nSolos} solo wins!")
        
        else:
            print("Invalid input.")
    
    else:
        print("Invalid input.")
    
    print()
