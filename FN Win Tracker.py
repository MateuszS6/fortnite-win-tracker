import time


f1 = "npulsive.txt"
f2 = "dog.txt"


while True:
    time.sleep(0.5)
    print(" > Fortnite Win Tracker")
    time.sleep(0.1)
    print("[1] View all stats")
    time.sleep(0.1)
    print("[2] Edit stats")
    time.sleep(0.1)
    options = input("Select option: ")

    if options == "1":
        mainAcc = open(f1,"r")
        for line in mainAcc:
            fields = line.split(", ")
        mainSolos = fields[0]
        mainDuos = fields[1]
        mainSquads = fields[2]
        mainAcc.close()
        print()
        print("Npulsive")
        time.sleep(0.1)
        print(" " + mainSolos + " solos")
        time.sleep(0.1)
        print(" " + mainDuos + " duos")
        time.sleep(0.1)
        print(" " + mainSquads + " squads")
        time.sleep(0.1)
        broAcc = open(f2,"r")
        for line in broAcc:
            fields = line.split(", ")
        broSolos = fields[0]
        broAcc.close()
        print("Dog")
        time.sleep(0.1)
        print(" " + fields[0] + " solos")
        time.sleep(0.1)
        print("TOTAL")
        time.sleep(0.1)
        tSolos = int(mainSolos) + int(broSolos)
        print(" " + str(tSolos) + " solos")
        time.sleep(0.1)
        tWins = tSolos + int(mainDuos) + int(mainSquads)
        print(" " + str(tWins) + " wins")
    
    elif options == "2":
        print("[1] Npulsive")
        time.sleep(0.1)
        print("[2] Dog")
        time.sleep(0.1)
        acc = input("Select account: ")

        if acc == "1":
            print("[1] Solo")
            time.sleep(0.1)
            print("[2] Duo")
            time.sleep(0.1)
            print("[3] Squad")
            time.sleep(0.1)
            i_mode = input("Select gamemode: ")
            
            if i_mode == "1":
                i_solos = input("Wins to add: ")
                mainAcc = open(f1,"r+")
                for line in mainAcc:
                    fields = line.split(", ")
                nSolos = str(int(fields[0]) + int(i_solos))
                if i_solos == "0":
                    print("[Npulsive] Bruh you still have " + nSolos + " solo wins.")
                else:
                    oDuos = str(fields[1])
                    oSquads = str(fields[2])
                    mainAcc.truncate(0)
                    mainAcc.seek(0)
                    mainAcc.write(nSolos + "," + oDuos + "," + oSquads)
                    mainAcc.close()
                    if int(i_solos) < 0:
                        print("[Npulsive] Bruh you're back at " + nSolos + " solo wins.")
                    else:
                        print("[Npulsive] You now have " + nSolos + " solo wins!")
            
            elif i_mode == "2":
                i_duos = input("Wins to add: ")
                mainAcc = open(f1,"r+")
                for line in mainAcc:
                    fields = line.split(", ")
                oSolos = str(fields[0])
                nDuos = str(int(fields[1]) + int(i_duos))
                oSquads = str(fields[2])
                mainAcc.truncate(0)
                mainAcc.seek(0)
                mainAcc.write(oSolos + "," + nDuos + "," + oSquads)
                mainAcc.close()
                print("[Npulsive] You now have " + nDuos + " duo wins!")
            
            elif i_mode == "3":
                i_squads = input("Wins to add: ")
                mainAcc = open(f1,"r+")
                for line in mainAcc:
                    fields = line.split(", ")
                oSolos = str(fields[0])
                oDuos = str(fields[1])
                nSquads = str(int(fields[2]) + int(i_squads))
                mainAcc.truncate(0)
                mainAcc.seek(0)
                mainAcc.write(oSolos + ", " + oDuos + ", " + nSquads)
                mainAcc.close()
                print("[Npulsive] You now have " + nSquads + " squad wins!")
            
            else:
                print("Invalid input.")
        
        elif acc == "2":
            ii_solos = input("Wins to add: ")
            broAcc = open(f2,"r+")
            for line in broAcc:
                fields = line.split(", ")
            nSolos = str(int(fields[0]) + int(ii_solos))
            oDuos = str(fields[1])
            oSquads = str(fields[2])
            broAcc.truncate(0)
            broAcc.seek(0)
            broAcc.write(nSolos + ", " + oDuos + ", " + oSquads)
            broAcc.close()
            print("[Dog] You now have " + nSolos + " solo wins!")
        
        else:
            print("Invalid input.")
    
    else:
        print("Invalid input.")
    
    print()
