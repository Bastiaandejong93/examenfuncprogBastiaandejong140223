from prettytable import PrettyTable
gidsen ={"1":{"naam":"Anass","leeftijd":23, "geslacht": "man", "loon":2500,"steden":["Amsterdam", "Londen","Rome"]},
"2":{"naam":"Bastiaan", "geslacht": "man","leeftijd":23, "loon":2300,"steden": ["Singapore","Shanghai","Denpasar"]},
"3":{"naam":"Orlando", "geslacht": "man","leeftijd":23,"loon":2300,"steden": ["Lissabon","Rome","Budapest"]},
"4":{"naam":"Toon", "geslacht": "man","leeftijd":23, "loon":3000,"steden": ["Amsterdam","Londen","Rome"]},
"5":{"naam":"Dario","geslacht":"man","leeftijd":23, "loon": 2500,"steden": ["Londen","Rome","Parijs"]}}
admins = {"admin":"admin"}

def toon_menu():
        print('1: Toon gidsen')
        print('2: Voeg gids toe')
        print('3: Voeg een stad toe aan een gids')
        print('4: Verwijder een gids')
        print('5: Voeg een stad toe aan alle gidsen')
        print('6: Verander het wachtwoord van admin')
        print('7: Gebruik filter')
def toon_gidsen():
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Naam", "Geslacht", "Leeftijd", "Loon", "Steden"]
        for key, value in gidsen.items():
                tabel.add_row([key, value["naam"], value["geslacht"], value["leeftijd"], value["loon"], value["steden"]])
        print(tabel)
def voeg_gids_toe():
        nieuwe_ID = str(len(gidsen) + 1)
        naam = input("Geef een naam in: ")
        geslacht = input("Geef een geslacht in: ")
        loon = input("Geef een loon in: ")
        leeftijd = input("Geef een leeftijd in: ")
        steden = input("Geef een stad in: ")
        gidsen[nieuwe_ID] = {"naam": naam, "geslacht": geslacht, "loon": loon, "leeftijd": leeftijd, "steden": [steden]}
        print(naam,"is toegevoegd")
def voeg_stad_toe():
        toon_gidsen()
        ID = input("Aan wie wil je een stad toevoegen? gebruik ID: ")
        nieuwe_stad = input("Geef een stad in: ")
        gidsen[ID]["steden"].append(nieuwe_stad)
        print(nieuwe_stad, "is toegevoegd aan de lijst van", gidsen[ID]["naam"])
def verwijder_gids():
        username = input("Geef een gebruikersnaam in: ")
        wachtwoord = input("Geef een wachtwoord in: ")
        while username not in admins or wachtwoord != admins[username]:
                print("Gebruikersnaam of wachtwoord is niet correct")
                username = input("Geef een gebruikersnaam in: ")
                wachtwoord = input("Geef een wachtwoord in: ")
        if username in admins and wachtwoord == admins[username]:
                toon_gidsen()
                ID = input("Geef een ID in welke je wilt verwijderen: ")
                gidsen.pop(ID)
                print("Gids is verwijderd")
def voeg_stad_toe_aan_alle_gidsen():
        stad = input("Geef een stad in: ")
        for key, value in gidsen.items():
                gidsen[key]["steden"].append(stad)
        print("Stad is toegevoegd aan alle gidsen")
def verander_wachtwoord():
        username= input("Geef een gebruikersnaam in: ")
        oud_wachtwoord = input("Geef een wachtwoord in: ")
        while username not in admins and oud_wachtwoord != admins[username]:
                print("Gebruikersnaam of wachtwoord is niet correct")
                username = input("Geef een gebruikersnaam in: ")
                oud_wachtwoord = input("Geef een wachtwoord in: ")
                if username in admins and oud_wachtwoord == admins[username]:
                        nieuw_wachtwoord = input("Geef een nieuw wachtwoord in: ")
                        bevestig_wachtwoord = input("Bevestig het wachtwoord: ")
                        if nieuw_wachtwoord == bevestig_wachtwoord:
                                admins["admin"] = nieuw_wachtwoord
                                print("Wachtwoord is veranderd")
                                break
def filter():
        print("1: Filter Man/Vrouw")
        print("2: Filter op Stad")
        print("3: Alle gidsen met een hoger loon dan x")
        print("4: Alle Mannen/Vrouwen die een bepaalde stad gidsen")
        keuze = input("Geef een keuze in: ")
        if keuze == "1":
                geslacht = input("Geef een geslacht in: ")
                for key, value in gidsen.items():
                        if value["geslacht"] == geslacht:
                                tabel = PrettyTable()
                                for key,value in gidsen.items():
                                        tabel.field_names = ["ID", "Naam", "Geslacht", "Leeftijd", "Loon", "Steden"]
                                        tabel.add_row([key, value["naam"], value["geslacht"], value["leeftijd"], value["loon"], value["steden"]])
                                        print(tabel)

        elif keuze == "2":
                stad = input("Geef een stad in: ")
                for key, value in gidsen.items():
                        if stad in value["steden"]:
                                tabel = PrettyTable()
                                for key,value in gidsen.items():
                                        tabel.field_names = ["ID", "Naam", "Geslacht", "Leeftijd", "Loon", "Steden"]
                                        tabel.add_row([key, value["naam"], value["geslacht"], value["leeftijd"], value["loon"], value["steden"]])
                                        print(tabel)


        elif keuze == "3":
                loon = int(input("Geef een loon in: "))
                for key, value in gidsen.items():
                        if int(value["loon"]) > loon:
                                tabel = PrettyTable()
                                for key,value in gidsen.items():
                                        tabel.field_names = ["ID", "Naam", "Geslacht", "Leeftijd", "Loon", "Steden"]
                                        tabel.add_row([key, value["naam"], value["geslacht"], value["leeftijd"], value["loon"], value["steden"]])
                                        print(tabel)
        elif keuze == "4":
                geslacht = input("Geef een geslacht in: ")
                stad = input("Geef een stad in: ")
                for key, value in gidsen.items():
                        if value["geslacht"] == geslacht and stad in value["steden"]:
                                tabel = PrettyTable()
                                for key,value in gidsen.items():
                                        tabel.field_names = ["ID", "Naam", "Geslacht", "Leeftijd", "Loon", "Steden"]
                                        tabel.add_row([key, value["naam"], value["geslacht"], value["leeftijd"], value["loon"], value["steden"]])
                                        print(tabel)
                                        break
        else:
                print("Keuze is niet correct")


##################################################################################################################

toon_menu()
keuze = input("Geef een keuze in: ")
while not keuze.lower() == "stop":
        if keuze == "1":
                toon_gidsen()
                toon_menu()
                keuze = input("Geef een keuze in: ")

        elif keuze == "2":
                voeg_gids_toe()
                toon_menu()
                keuze = input("Geef een keuze in: ")
        elif keuze == "3":
                voeg_stad_toe()
                toon_menu()
                keuze = input("Geef een keuze in: ")
        elif keuze == "4":
                verwijder_gids()
                toon_menu()
                keuze = input("Geef een keuze in: ")
        elif keuze == "5":
                voeg_stad_toe_aan_alle_gidsen()
                toon_menu()
                keuze = input("Geef een keuze in: ")
        elif keuze == "6":
                verander_wachtwoord()
                toon_menu()
                keuze = input("Geef een keuze in: ")
        elif keuze == "7":
                filter()
                toon_menu()
                keuze = input("Geef een keuze in: ")
        else:
                print("Keuze is niet correct")
                keuze = input("Geef een keuze in: ")
                toon_menu()