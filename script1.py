# W zadanym katalogu przerób wszystkie dowiązania symboliczne wskazujące na pliki regularne
# (do których wykonujący skrypt nie ma prawa zapisu) znajdujące się w tym katalogu, tak aby
# ścieżki dowiązania miały postać ./plik.

#!/usr/bin/python3

import os
import sys

# Sprawdzenie czy zdano poprawna liczbe argumentow
if (len(sys.argv) != 2):
    print("Niepoprawna liczba argumentów!")
    sys.exit() 

# Sprawdzenie czy zadany katalog istnieje
if (not os.path.isdir(sys.argv[1])):
    print("Zadany katalog nie istnieje!")
    sys.exit()


for file in os.listdir(sys.argv[1]):
    path = str(sys.argv[1]) + "/" + str(file)
    dir_path = os.getcwd() + "/" + str(sys.argv[1])

    if (os.path.islink(path) and os.path.dirname(os.readlink(path)) == dir_path):       # Plik musi byc symlinkiem z dowiazaniem na plik w danym katalogu
        new_path = "./" + os.path.basename(os.readlink(path))       # Nowa sciezka na wzor "./plik"
        os.unlink(path)                                             # Usuniecie starej sciezki
        os.symlink(new_path, path)                                  # Dodanie nowej sciezki do symlinku
        
