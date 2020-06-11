# W zadanym drzewie katalogów znaleźć dowiązania symboliczne wskazujące na pliki regularne, 
# zmodyfikowane nie wcześniej niż 5 minut temu i nie później niż 1 minutę.


#!/usr/bin/python3

import os
import sys
import time
import datetime

# Sprawdzenie czy zdano poprawna liczbe argumentow
if (len(sys.argv) != 2):
    print("Niepoprawna liczba argumentów!")
    sys.exit() 

# Sprawdzenie czy zadany katalog istnieje
if (not os.path.isdir(sys.argv[1])):
    print("Zadany katalog nie istnieje!")
    sys.exit()
 
ctime = datetime.datetime.now()     # Czas obecny
hours = 1                           # Strefa czasowa
minutes = 40

dir_path = os.path.abspath(sys.argv[1])


for root, dirs, files in os.walk(dir_path):
    for name in files:
        filepath = os.path.join(root, name)

        if os.path.islink(filepath):

            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))     # Czas ostatniej modyfikacji
            hours_added = datetime.timedelta(hours=hours, minutes=minutes)          # Roznica godzinowa
            mtime = mtime + hours_added                                             # Korekta do czasu lokalnego

            difftime = ctime - mtime                                                # Roznica obecnego czasu i czasu modyfikacji linku
            difftime = datetime.timedelta(seconds=difftime.seconds).total_seconds()     # Konwersja do sekund

            if (difftime < 5*60 and difftime > 1*60):
                print(name)
            
                