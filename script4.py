# W zadanym katalogu przerób wszystkie dowiązania symboliczne wskazujące na pliki regularne
# (do których wykonujący skrypt nie ma prawa zapisu), tak aby ścieżki w dowiązaniach były bezwzględne.


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

dir_path = os.path.abspath(sys.argv[1])

for file in os.listdir(dir_path):
    path = dir_path + "/" + str(file)

    if (os.path.islink(path) and os.readlink(path) != (dir_path + "/" + os.path.basename(os.readlink(path)))):      # Sprawdzenie czy plik jest symlinkiem i czy nie ma juz dowiazania bezwzglednego
        new_path = dir_path + "/" + os.readlink(path)    # Dolaczenie CWD do sciezki wzglednej -> uzyskanie sciezki bezwzglednej
        os.unlink(path)                                  # Usuniecie starej sciezki
        os.symlink(new_path, path)                       # Dodanie nowej sciezki do symlinku
