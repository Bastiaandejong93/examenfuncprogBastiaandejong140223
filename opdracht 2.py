wordlist=["Appel","Peer","Banaan","Perzik","Watermeloen"]
worddict={}
worddictversleuteld={}
def toon_menu():
    print("1. Voeg woord toe")
    print("2. Verwijder woord")
    print("3. Toon woorden")
    print("4. Toon woorden versleuteld")
def Voeg_woord_toe():
    nieuw_woord = input("Geef een nieuw woord in: ")
    if nieuw_woord in wordlist:
        print("Dit woord zit al in de lijst")
    else:
        wordlist.append(nieuw_woord)
        print(nieuw_woord,"is toegevoegd")
def verwijder_woord():
    woord = input("Geef een woord in: ")
    if woord in wordlist:
        wordlist.remove(woord)
        print(woord,"is verwijderd")
    else:
        print("Het woord zit niet in de lijst")

def list_to_dict():
    for woord in wordlist:
        nieuwe_ID =("W"+str(wordlist.index(woord)+1))
        worddict.update({nieuwe_ID:woord})
def versleutel_dict():
    for woord in worddict.values():
          versleuteld_woord = ""
          for letter in woord:
                versleuteld_woord += chr(ord(letter)+4)
          worddictversleuteld.update({woord:versleuteld_woord})


############
#Hoofdprogramma
############
toon_menu()
keuze = input("Geef je keuze in: ")
while not keuze == "stop":
    if keuze == "1":
        Voeg_woord_toe()
    elif keuze == "2":
        verwijder_woord()
    elif keuze == "3":
        print(wordlist)
    elif keuze == "4":
        list_to_dict()
        versleutel_dict()
    else:
        print("Foute invoer")
    toon_menu()
    keuze = input("Geef je keuze in: ")

