# Gniew i Łaska Bogów 0.4.6 DEV: poprawki interfejsu i lokalizacji
**Data:** 9 listopada 2026
**Gałąź:** `feature/0.4.6-hotfix-ikona-alerty-teksty`
**Baza:** 0.4.5 DEV. **Status:** poprawka R2 na podstawie rzeczywistego `error.log`; oczekuje testu CK3. Testy kodu i instalatora wymagają uruchomienia CI dla R2.

## 3 poprawki
1. **Weles:** `bp_weles.2004.t` ma tytuł "Cena ofiary" (EN "The Price of Sacrifice").
2. **Znak Pierwszego Ognia:** **R2:** zdiagnozowano w `error.log` pewną przyczynę znaku zapytania. CK3 próbował otworzyć `gfx/interface/icons/traits/gfx/interface/icons/traits/bp_gods_mark_1_v020.dds` (podwójny prefiks), ponieważ definicja cechy podawała pełną ścieżkę. Usunięto parametr `icon = ...`, więc silnik używa domyślnego pliku `gfx/interface/icons/traits/bp_gods_mark_1_v020.dds`. Przywrócono oryginalny zatwierdzony DDS 120x120 z 7 mipmapami (identyczny plik jak w 0.4.5). Usunięto też nieobsługiwane `can_lose = yes` i nadano plikowi definicji UTF-8 BOM. **Rzeczywisty test ikony w grze nadal jest wymagany**.
3. **Kalendarz:** dwanaście decyzji świątecznych ma `should_create_alert = { always = no }` przy zachowaniu istniejących awaryjnych `effect`. Zaktualizowano PL/EN: tytuł Welesa, opisy decyzji, cztery zapisy uczestnictwa, osiem wpisów kroniki i wspólny status pozostałych świąt. Nie ma sugestii, że gracz musi uruchamiać święta ręcznie.

## Bezpieczna instalacja
- Zamknij CK3 i launcher.
- Pobierz ZIP z GitHub Actions tej gałęzi, wypakuj wewnętrzny `GNIEW_I_LASKA_BOGOW_0.4.6_DEV_NADPISZ.zip` i uruchom `AKTUALIZUJ_046.bat`.
- Skrypt sprawdza pliki, tworzy backup i nadpisuje dotychczasowy mod bez tworzenia drugiej pozycji.
- Graj na kopii zapisu. Ustawienia pauzy i skrypty 12 świąt pozostawiono bez zmian.

## Czyszczenie cache
W `Dokumenty/Paradox Interactive/Crusader Kings III`, po zamknięciu gry, można tymczasowo zmienić nazwę folderu `shadercache` na `shadercache_stary` oraz folderu `cache` na `cache_stary`, jeśli istnieją. Nie ruszać `save games` ani `mod`.

## Nadal otwarte
- Potwierdzić w CK3 naprawę ikony oraz zanik alertów. `error.log` z 9 listopada zawierał dokładnie jeden błąd VFS brakującej tekstury cechy; R2 usuwa jego przyczynę. Pauza działa w wersji 0.4.5 według testu gracza, jej kod bez zmian w 0.4.6.
- Naprawić sześć fabuł z nieuzasadnionym losowaniem dworzan, osobno `bp_040_blood_events.txt`.
- Przegląd jakości wszystkich 12 świąt i obrazów; `main` pozostaje nietknięte do zaliczenia testów.
