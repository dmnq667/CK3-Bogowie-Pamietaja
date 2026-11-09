# Gniew i Łaska Bogów — 0.4.3 DEV: Pauza bez zbędnych komunikatów

**Status:** wersja testowa, 9 listopada 2026.  
**Repozytorium:** [feature/0.4.3-pauza-bez-banerow](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/tree/feature/0.4.3-pauza-bez-banerow).  
**[Pobierz aktualizator 0.4.3 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42617710356/artifacts/13672913095)**.  
**Testy:** [GitHub Actions #42617710356](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42617710356) — analiza skryptów **PASS**, instalator Windows PowerShell 5.1 0.4.2 → 0.4.3 i backup **PASS**. Rzeczywista pauza w grze **nie jest jeszcze potwierdzona**.

## Zgłoszenie i wyjaśnienie

Dwa zrzuty ekranu potwierdziły, że wersja 0.4.2 wyświetlała na górze komunikaty „Rozstrzygnięcie święta” i „Nadeszło słowiańskie święto”, ale nie zatrzymywała rozgrywki. Przy szybkim biegu czasu wydarzenia z **Gaiku (30.04)** i **Dziadów wiosennych (2.05)** mogły następować prawie jednocześnie.

**Przyczyna dotychczasowego niepowodzenia:** `send_interface_toast` tylko wyświetlał powiadomienie. Filtr z `auto_pause = yes` nie gwarantował pauzy na komputerze gracza i dodatkowo zaśmiecał ekran. Nie ma potwierdzonego parametru `pause = yes` do dodania do `character_event`.

## Nowy wariant pauzy

W wersji 0.4.3 zmieniono **29 widocznych okien**: 12 scen obrzędowych, 12 scen fabularnych, osobiste objawienia Welesa, Peruna i Mokoszy oraz dwa wydarzenia zemsty rodowej.

W obrębie każdego z tych okien zastosowano:

```txt
type = letter_event
window = character_event
sender = root
opening = bp_043_empty_opening
```

Mechanizm opiera się na natywnym zatrzymywaniu czasu przez **wydarzenia typu listowego** (`letter_event`), a parametr `window = character_event` nakazuje zachować znane, duże okno wydarzenia. Puste `opening` zapobiega pojawieniu się dodatkowego powitania. Zostają te same ilustracje, właściwe treści i przyciski.

**To wariant eksperymentalny.** Sam fakt, że CK3 akceptuje tę składnię, nie dowodzi, iż w obecnej wersji gry zachowa zarazem pauzę i dokładnie ten sam wygląd; dopiero próba w działającym CK3 może to potwierdzić.

## Usunięcie komunikatów

- Całkowicie usunięto otwierające powiadomienia „Nadeszło słowiańskie święto”, „Rozstrzygnięcie święta” i „Bogowie upominają się o swoje”.
- Wyłączono poprzedni, nieskuteczny mechanizm wymuszania pauzy w filtrze komunikatów.
- Zachowano wyłącznie **16 istotnych powiadomień o rozstrzygnięciu próby** — po wyborze gracza, np. „Ocaleni z wód Kupały” lub „Śmierć w świętym gaju”.
- **Nie przybyło żadnego nowego okna do przeklikania.**

## Nie zmieniono

- **Terminów wszystkich 12 świąt** ani ich kolejności;
- struktury **jedno okno edukacyjne + jedno okno fabularne** na święto;
- **31 zatwierdzonych grafik** i ich przypisania;
- bonusów za udział, siedmiu losowań grożących śmiercią, 16 opisów wyników, odroczonych konsekwencji i właściwych postaci.

## Testy

Weryfikator `tools/validate_story_043.py` potwierdza:

- **29/29** wydarzeń używa wskazanego typu i oryginalnego szablonu;
- **12/12** świąt ma dokładnie dwa widoczne okna;
- **0** banerów przy otwarciu;
- **16** komunikatów o prawdziwym wyniku losowania, siedem potencjalnie śmiertelnych łańcuchów;
- pozostawiono bez zmian zatwierdzone pliki graficzne;
- test Windows instalatora **PASS** — poprawna podmiana i zachowanie poprzedniej wersji w kopii.

**Testy nie uruchamiają silnika CK3**, więc nie stanowią potwierdzenia rzeczywistego automatycznego zatrzymania czasu.

## Instalacja

1. Zamknij CK3.
2. Pobierz [paczę 0.4.3 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42617710356/artifacts/13672913095) z GitHub Actions.
3. Rozpakuj pobrany ZIP, następnie znajdujący się w nim `GNIEW_I_LASKA_BOGOW_0.4.3_DEV_NADPISZ.zip`.
4. Uruchom `AKTUALIZUJ_043.bat`. Aktualizator nadpisuje istniejący mod bez drugiej pozycji w launcherze i najpierw tworzy kopię.
5. Uruchom **kopię zapisu gry** i sprawdź przy szybkości 4–5 przejście Gaik → Dziady wiosenne oraz późniejsze Stado. **Gdy tylko pojawi się pierwsze okno święta, spójrz na datę i stan pauzy; czas nie może dalej biec do kliknięcia.**
6. Sprawdź również, czy otwierają się dwie sceny z dotychczasowymi grafikami, a górne banery nie wracają.

Jeśli gra nie zatrzymuje się mimo `letter_event`, to znaczy, że silnik CK3 nie honoruje tego sposobu z zachowanym szablonem na aktualnej wersji. Wtedy nie będziemy powtarzać kolejnych ustawień banerów; konieczne będzie rozwiązanie oparte na kontrolowanym sposobie otwierania/priorytetyzacji wydarzeń albo użycie natywnej komendy `pause_on` do diagnostyki.

**Kryterium przyjęcia:** komplet oryginalnych ilustracji + pierwsze okno zatrzymuje czas samoczynnie + drugi etap nie jest gubiony + brak górnych banerów przy rozpoczęciu wydarzenia.
