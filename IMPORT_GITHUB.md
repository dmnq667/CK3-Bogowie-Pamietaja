# Jednorazowy import wersji 0.1.9 ALPHA

**Stan:** automatyczny importer został zainstalowany. Do jego uruchomienia trzeba przesłać do katalogu głównego repozytorium dokładnie dwa pliki:

- `BP019.part01` (23 068 672 B)
- `BP019.part02` (16 166 544 B)

Pliki są częściami jednego archiwum `Bogowie_Pamietaja_v0.1.9_import.zip`.

## Co zrobić na stronie GitHuba

1. Otworzyć główny katalog repozytorium, nie folder `Bogowie_Pamietaja`.
2. Wybrać **Add file → Upload files**.
3. Przeciągnąć jednocześnie oba pliki `BP019.part01` i `BP019.part02`.
4. Zatwierdzić **Commit changes**.

GitHub Actions uruchomi workflow `.github/workflows/import-bogowie-019.yml`. Ten workflow sprawdza sumę kontrolną archiwum, weryfikuje pliki na podstawie manifestu, odtwarza foldery `Bogowie_Pamietaja`, `docs`, `source_artwork`, usuwa tymczasowe fragmenty ZIP i zapisuje commit oraz tag `v0.1.9-alpha`.

**Kontrolna suma SHA-256 pełnego archiwum:** `8b7d33b7d40b47c81041273abc9705fb13272cfbd066af427e366d7f0b9be7e6`.

## Gdy coś pójdzie nie tak

Stan wykonania: zakładka [Actions](../../actions), zadanie **Import Bogowie Pamietaja v0.1.9**. Czerwony wynik oznacza, że repozytorium nie zostało jeszcze uzupełnione. Nie usuwać ani nie nadpisywać wówczas plików samodzielnie, tylko sprawdzić komunikat zadania.

Po zielonym wyniku szczegóły importu i wyniki walidacji archiwum zostaną zapisane w `SYNC_STATUS.md`. Weryfikacja działania wewnątrz CK3 pozostaje osobnym krokiem.
