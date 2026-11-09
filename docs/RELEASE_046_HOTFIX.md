# Gniew i Łaska Bogów 0.4.6 DEV: poprawki interfejsu i lokalizacji
**Data:** 9 listopada 2026
**Gałąź:** `feature/0.4.6-hotfix-ikona-alerty-teksty`
**Baza:** 0.4.5 DEV. **Status:** testy kodu / instalatora wymagają uruchomienia CI, test w CK3 niezaliczony.

## 3 poprawki
1. **Weles:** `bp_weles.2004.t` ma tytuł "Cena ofiary" (EN "The Price of Sacrifice").
2. **Znak Pierwszego Ognia:** oryginalne 120x120 DDS zostało osadzone bez przerysowania w przezroczystej 128x128 teksturze z 8 mipmapami. Nazwa i ścieżka bez zmian. Sprawdzić w CK3, czy znika znak zapytania.
3. **Kalendarz:** dwanaście decyzji świątecznych ma `should_create_alert = { always = no }` przy zachowaniu istniejących awaryjnych `effect`. Zaktualizowano PL/EN: tytuł Welesa, opisy decyzji, cztery zapisy uczestnictwa, osiem wpisów kroniki i wspólny status pozostałych świąt. Nie ma sugestii, że gracz musi uruchamiać święta ręcznie.

## Bezpieczna instalacja
- Zamknij CK3 i launcher.
- Pobierz ZIP z GitHub Actions tej gałęzi, wypakuj wewnętrzny `GNIEW_I_LASKA_BOGOW_0.4.6_DEV_NADPISZ.zip` i uruchom `AKTUALIZUJ_046.bat`.
- Skrypt sprawdza pliki, tworzy backup i nadpisuje dotychczasowy mod bez tworzenia drugiej pozycji.
- Graj na kopii zapisu. Ustawienia pauzy i skrypty 12 świąt pozostawiono bez zmian.

## Czyszczenie cache
W `Dokumenty/Paradox Interactive/Crusader Kings III`, po zamknięciu gry, można tymczasowo zmienić nazwę folderu `shadercache` na `shadercache_stary` oraz folderu `cache` na `cache_stary`, jeśli istnieją. Nie ruszać `save games` ani `mod`.

## Nadal otwarte
- Potwierdzić w CK3 naprawę ikony oraz zanik alertów. Pauza działa w wersji 0.4.5 według testu gracza, jej kod bez zmian w 0.4.6.
- Naprawić sześć fabuł z nieuzasadnionym losowaniem dworzan, osobno `bp_040_blood_events.txt`.
- Przegląd jakości wszystkich 12 świąt i obrazów; `main` pozostaje nietknięte do zaliczenia testów.
