# Stan produkcji: Bogowie Pamiętają

**Aktualizacja:** 26.10.2026  
**Wersja:** 0.1.9 ALPHA, 12 świąt  
**Stan GitHub:** PEŁNA SYNCHRONIZACJA ŹRÓDEŁ, TESTY W CK3 OCZEKUJĄ.

## Potwierdzony import GitHub

- Import automatyczny ukończono commitem `d31a6809a21d0322d9bdd3ca4ce5250913305033`.
- Utworzono tag odtwarzalnej wersji źródeł: `v0.1.9-alpha`.
- Archiwum importowe przeszło kontrolę SHA-256; importer zweryfikował indywidualnie 110 plików na podstawie `IMPORT_MANIFEST_SHA256.json`.
- Dodatkowa kontrola listy plików w repozytorium: **110/110 ścieżek manifestu obecnych**, bez braków.
- Repozytorium zawiera 64 pliki w `Bogowie_Pamietaja/`, w tym 16 plików wydarzeń i 32 tekstury DDS; ponadto 32 oryginalne JPG w `source_artwork/` oraz 13 dokumentów wydania w `docs/`. Są również dokumenty służące do prowadzenia repozytorium.
- Wcześniejsze instrukcje o brakujących plikach lub oczekującym imporcie w archiwalnych komunikatach nie są już aktualne.

**Uwaga:** sprawdzenie integralności archiwum i obecności plików nie zastępuje uruchomienia moda w Crusader Kings III.

## Materiał źródłowy

- Archiwum wyjściowe: `Bogowie_Pamietaja_v0.1.9_ALPHA_12_SWIAT(1).zip`
- SHA-256 archiwum wyjściowego: `98ac06b79946907fe36fb01d3a3d10c5a6ab5da24b9bd103fdce26ab4e66a9f4`
- SHA-256 archiwum importowego: `8b7d33b7d40b47c81041273abc9705fb13272cfbd066af427e366d7f0b9be7e6`
- Szczegóły: [SYNC_STATUS.md](SYNC_STATUS.md), [IMPORT_MANIFEST_SHA256.json](IMPORT_MANIFEST_SHA256.json)

## Kolejny etap produkcji

1. Sprawdzić działanie w bieżącej wersji CK3 oraz `error.log`, uwzględniając zgodność z innymi modami.
2. Przetestować cykl roczny wszystkich 12 świąt i warunki wywoływania wydarzeń.
3. Zweryfikować wybory i skutki: Perun (wojna/pokój), dług Welesa, Mokosz, Dziady jesienne i Szczodre Gody.
4. Sprawdzić lokalizacje PL/EN, 32 tekstury DDS i dopasowanie ilustracji.
5. Zapisać potwierdzone wyniki testów i błędy w repozytorium przed wydaniem następnej wersji.

## Procedury i bieżące testy

- [Standard importu przez GitHub Actions](docs/PROCEDURA_PUBLIKACJI_GITHUB.md): stosować przy większych paczkach, żeby nie wymagać ręcznego przesyłania katalogów.
- [Wieczorna sesja testowa 0.1.9](docs/SESJA_TESTOWA_019.md): przygotowana, nie została jeszcze przeprowadzona.
- Nowy mechanizm do wersji 0.2.0: [Cztery Sądy Bogów](docs/PROJEKT_CZTERY_SADY_BOGOW_020.md). **Zatwierdzony przez autora podział 2 / 4 / 3 / 3**, czyli sądy po 2., 6., 9. i 12. święcie. **Tylko drugi sąd, po Dziadach wiosennych, może warunkowo przyznać +1500 złota w ostatecznym rozliczeniu minionego roku, maksymalnie raz na rok obrzędowy.** Ten sam władca może otrzymać premię w następnych latach, po ponownym spełnieniu warunków. Pozostałe sądy bez nagrody pieniężnej, z konsekwencjami fabularnymi i możliwym rozwojem cechy. **To projekt, bez zmian w skryptach 0.1.9.**
- Stabilnej bazy 0.1.9 nie zmieniać przed wieczornymi testami i uzgodnieniem mechaniki.

## Zasady

GitHub jest źródłem stanu produkcji. Każde wydanie wymaga historii zmian, stanu testów i oznaczenia wersji. Nie mieszać z `CK3-The-Weight-of-Words`.
