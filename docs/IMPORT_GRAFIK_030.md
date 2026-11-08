# Import grafik 0.3.0 — ZAKOŃCZONY

**Data:** 8 listopada 2026. Import został wykonany automatycznie przez asystenta na GitHubie. Użytkownik **nie musi** przesyłać plików BP030.part01–part03 ani uruchamiać dawnego importera.

**Wynik GitHub Actions:** [run #42506140283 — SUCCESS](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42506140283)

**Commit importu:** `ead68f63b19907d994dac7c9292fe09ad7df214c`

## Potwierdzona zawartość

- 28 nowych ilustracji świąt, 3 zatwierdzone objawienia bogów.
- 31 plików DDS 1592×848 DXT1/BC1.
- 31 plików źródłowych w `source_artwork_030/`.
- Cztery stare warianty DDS (`gromnica_02`, `stado_03`, `kupala_03`, `perun_03`) usunięto; ich identyfikatory teł kierują do odpowiednich tekstur nowej serii.
- Oddzielne tła `bp_scene_deity_weles_2020`, `bp_scene_deity_perun_9110`, `bp_scene_deity_mokosh_3010`.
- Statyczne walidacje PASS. **Nie wykonano testu CK3**.

## Pobranie aktualizatora

1. Na [stronie zakończonego zadania](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42506140283) pobierz artefakt `Gniew-i-Laska-Bogow-0.3.0-DEV-NADPISZ`.
2. Rozpakuj pobrany ZIP, a następnie znajdujący się w nim plik `GNIEW_I_LASKA_BOGOW_0.3.0_DEV_NADPISZ.zip`.
3. **Wyłącz CK3.** Uruchom `AKTUALIZUJ_030.bat` w rozpakowanej zawartości drugiego ZIP.
4. Instalator szuka dotychczasowej instalacji, tworzy kopię bezpieczeństwa, nadpisuje ten sam mod i weryfikuje SHA-256. Nie tworzy drugiego wpisu w launcherze.
5. Pierwszy test przeprowadź na kopii zapisu gry. Sprawdź trzy wydarzenia bogów, ikony i `error.log`.

Wykonanie importu i zbudowanie paczki **nie oznacza** jeszcze weryfikacji działania wydarzeń w CK3.

## Archiwalne informacje

Wcześniejszy plan ręcznego przesłania trzech plików `BP030.part01`–`part03` został zastąpiony wykonanym importem bezpośrednim. Ten plan nie jest już potrzebny.
