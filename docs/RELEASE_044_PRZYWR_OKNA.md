# Gniew i Łaska Bogów 0.4.4 DEV — przywrócenie poprawnych okien

**Przyczyna wydania:** wersja 0.4.3 nie zatrzymywała czasu, a użytkownik zgłosił dodatkowy błąd komunikatu. Eksperymentalne `letter_event` i puste `opening` zostały wycofane.

**Status:** 9 listopada 2026, osobna gałąź `feature/0.4.4-przywrocenie-okien-diagnostyka-pauzy`. Testy CI [#42624169723](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42624169723) **SUCCESS**. [Pobierz aktualizator 0.4.4 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42624169723/artifacts/13677079913).

## Wykonane
- W 12 oknach obrzędów, 12 oknach fabularnych, 3 osobistych objawieniach oraz 2 wydarzeniach zemsty przywrócono standardowe `type = character_event`; usunięto `window = character_event`, `sender = root`, `opening = bp_043_empty_opening`.
- Zachowano oprawę wszystkich 31 obrazów, układ **12 świąt × dokładnie 2 okna**, polskie i angielskie teksty, wszelkie koszty, premie, krwawe wybory oraz 16 wyników prób.
- Nie wrócono do powiadomień o nadejściu święta — pozostawiono wyłącznie komunikaty z rzeczywistym skutkiem decyzji.
- Testy automatyczne sprawdziły komplet 29 poprawionych okien, strukturę wydarzeń, teksty wyników, obrazy, kalendarz i wymuszoną liczbę okien.
- Test Windows PowerShell 5.1 z powodzeniem nadpisał **próbną instalację 0.4.3 na 0.4.4** i zachował prawidłową kopię zapasową.

## Czego NIE wykonano i co wymaga testu

**Automatyczna pauza nie jest naprawiona.** Cofnięcie błędnego formatu okien nie jest równoznaczne z wymuszeniem zatrzymania czasu. Potrzebujemy jeszcze ustalić mechanizm, który faktycznie zatrzymuje zegar w bieżącym CK3, i ewentualne konflikty z ustawieniami gry lub innymi modami. Testy GitHub Actions nie uruchamiają CK3.

W celach diagnostycznych CK3 dostarcza udokumentowaną komendę konsoli `pause_on bp_gaik.5001`; można ją sprawdzić w trybie debugowania, lecz nie jest ona zwykłym poleceniem zdarzeń możliwym do umieszczenia bezpośrednio w skrypcie. Pełne instrukcje: [Diagnostyka pauzy](DIAGNOSTYKA_PAUZY_044.md).

## Instalacja

1. Zamknij CK3 i przygotuj kopię zapisu gry.
2. Pobierz [0.4.4 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42624169723/artifacts/13677079913) — GitHub Actions artifact.
3. Rozpakuj pobrany ZIP, a następnie znajdujący się w nim `GNIEW_I_LASKA_BOGOW_0.4.4_DEV_NADPISZ.zip`.
4. Uruchom `AKTUALIZUJ_044.bat` i poczekaj na potwierdzenie ukończenia. Aktualizator tworzy kopię i nadpisuje **ten sam** mod, nie tworząc drugiej pozycji w launcherze.
5. Po uruchomieniu gry sprawdź wygląd świąt i błąd komunikatu; następnie zweryfikuj, czy zwykłe wydarzenia CK3 pauzują w tej konfiguracji.

Nie przedstawiamy wydania jako wersji ze sprawną pauzą. Kryterium takiej poprawki to **obserwacja zatrzymanego zegara CK3 w chwili otwarcia pierwszego okna** i brak problemów z kolejką wydarzeń.
