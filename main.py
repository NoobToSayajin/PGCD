import lib

def Init():
    N0 = int(input("Entrez un premier nombre entier non nul\n"))
    N1 = int(input("Entrez un second nombre entier non nul\n"))

    lib.PGCD(N0, N1)

Init()

while(True):
    Restart = str(input("Relancer ? Y/N\n"))

    if Restart == "Y" or Restart == "y":
        Init()
    else:
        break