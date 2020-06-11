# W zadanym katalogu utwórz pliki regularne o nazwach pokrywających się z kolejnymi liniami w zadanym pliku
# (tworzyć również pliki ze spacjami w nazwie). Jeżeli plik o takiej nazwie już istnieje, to zmień prawa jego
# dostępu na „read only”. Jeżeli obiekt o takiej nazwie istnieje, a nie jest plikiem regularnym, to wyświetl 
# ostrzeżenie i nie zmieniaj go.

#!/usr/bin/python3

import os
import sys
import stat

# Sprawdzenie czy zdano poprawna liczbe argumentow
if (len(sys.argv) != 3):
    print("Niepoprawna liczba argumentów!")
    sys.exit() 

# Sprawdzenie czy zadany katalog istnieje
if (not os.path.isdir(sys.argv[1])):
    print("Zadany katalog nie istnieje!")
    sys.exit()

# Sprawdzenie czy zadany plik istnieje
if (not os.path.isfile(sys.argv[2])):
    print("Zadany plik nie istnieje!")
    sys.exit()


with open(sys.argv[2], 'r') as file:
    names = file.read().splitlines()

for name in names:
    path = str(sys.argv[1]) + "/" + str(name)
    if os.path.exists(path):
        if os.path.isfile(path):
            os.chmod(path, stat.S_IRUSR|stat.S_IRGRP|stat.S_IROTH)
        else:
            print("Plik nie jest plikiem regularnym")

    else:
        new_file = open(path, "w+")
        new_file.close()
