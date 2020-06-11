# Dla zadanego dowiązania symbolicznego zweryfikuj, czy cała ścieżka do obiektu przez niego wskazanego znajduje
# się w obrębie zadanego drzewa katalogów (wszystkie pośrednie katalogi i dowiązania występujące w ścieżce).
# Uwaga: weryfikacja ma sprawdzić ścieżkę zapisaną w dowiązaniu, a nie przerobioną do postaci kanonicznej (bo to nie jest to samo).

#!/usr/bin/python3

import os
import sys

# Sprawdzenie czy zdano poprawna liczbe argumentow
if (len(sys.argv) != 3):
    print("Niepoprawna liczba argumentów!")
    sys.exit() 

# Sprawdzenie czy zadany katalog istnieje
if (not os.path.islink(sys.argv[1])):
    print("Zadany symlink nie istnieje!")
    sys.exit()

print(os.readlink(sys.argv[1]))
check = False

for root, dirs, files in os.walk(sys.argv[2]):
    for name in files:
        if os.readlink(sys.argv[1]) == os.path.join(root, name):
            check = True

print(check)