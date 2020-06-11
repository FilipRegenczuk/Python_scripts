# W zadanym pliku tekstowym należy znaleźć i wylistować na ekran wszystkie liczby zmiennoprzecinkowe o 
# formacie: cyfry części całkowitej, znak kropki dziesiętnej, cyfry części ułamkowej. Nie należy listować
# liczb z nieznaczącymi zerami na początku lub końcu, ani liczb nie mających żadnej cyfry przed znakiem kropki.

#!/usr/bin/python3

import sys
import os
import re

# Sprawdzenie czy zdano poprawna liczbe argumentow
if (len(sys.argv) != 2):
    print("Niepoprawna liczba argumentów!")
    sys.exit() 

# Sprawdzenie czy zadany plik istnieje
if (not os.path.isfile(sys.argv[1])):
    print("Zadany plik nie istnieje!")
    sys.exit()


dir_path = os.path.abspath(sys.argv[1])

with open(dir_path, 'r') as file:
    file_content = file.read()

pattern = '[1-9]\d*\.\d*[1-9]|0\.\d*[1-9]'    # gdy wiecej liczb przed . lub [1-9].xxx, lub sytuacja gdy 0.xxx

float_numbers = re.findall(pattern, file_content)
for x in float_numbers:
    print(x)