# Historia wydań

## 0.4.5 DEV — 9 listopada 2026

- Przywrócono dawny codzienny mechanizm wywoływania 12 świąt. W wersjach 0.4.x zegar wbrew wcześniejszym założeniom ograniczono do sądu, usuwając automatyczne obrzędy.
- Wywołanie prowadzi prosto do edukacyjnego okna z bonusem; przycisk uruchamia istniejącą historię fabularną. Liczba okien pozostała **dokładnie 2**.
- Dodano zapis zgłoszenia na 335 dni, który zapobiega ponownemu otwieraniu obrzędu na kolejne dni świątecznego okna, zwłaszcza Gaik → Dziady wiosenne.
- Zweryfikowano 3 rzeczywiste pliki DDS Szczodrych Godów i ich przypisanie. Okna korzystają ze standardowego `character_event`, a nie nieudanego `letter_event`.
- Bez zmian: kalendarz, 31 zaakceptowanych ilustracji, fabuła, premie, ryzyko śmierci i 16 wyników prób.
- **[0.4.5 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42632417532/artifacts/13682155682)** — walidacja skryptów PASS, próba aktualizacji na Windows i kopii bezpieczeństwa PASS. **Pauza czeka na sprawdzenie w grze.**

## 0.4.4 DEV — 9 listopada 2026

- Cofnięto `letter_event` + `opening = bp_043_empty_opening` w 29 widocznych wydarzeniach po zgłoszeniu braku pauzy i błędu komunikatu; przywrócono `character_event`.
- Pozostawiono 12 świąt × 2 okna, terminy, 31 ilustracji, wybory i 16 wyników groźnych prób; bez zbędnych banerów na starcie.
- Dodano [diagnostykę `pause_on`](docs/DIAGNOSTYKA_PAUZY_044.md) i wyraźnie zaznaczono, że automatyczna pauza nie działa jeszcze w sposób potwierdzony.
- [Paczka 0.4.4 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42624169723/artifacts/13677079913) z walidacją 29 okien i testem instalacji Windows z kopią zapasową — **PASS**.

## 0.4.3 DEV — 9 listopada 2026

- Usunięto wszystkie trzy rodzaje dodatkowych banerów przy wejściu w obrzęd, historię lub spotkanie z bogiem — nie zatrzymywały rozgrywki, więc były zbędne.
- W 29 ważnych oknach wykorzystano `letter_event` i jednocześnie `window = character_event`: próba systemowego zatrzymywania czasu bez utraty dotychczasowych ilustracji i układu.
- Dotychczasowy filtr `auto_pause` wyłączono dla powiadomień; zachowano 16 wyników ryzykownych prób, bez dodatkowych przycisków.
- Kalendarz bez zmian: **12 świąt, każde dokładnie dwa okna**. 31 zatwierdzonych grafik, premie i opcje bez zmian.
- **[0.4.3 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42617710356/artifacts/13672913095)** — walidator i aktualizacja Windows PASS. **Rzeczywista pauza w CK3 wciąż wymaga potwierdzenia w rozgrywce**.

## 0.4.2 DEV — 9 listopada 2026

- Naprawiono brak informacji o wyniku 25% ryzyka śmierci w Gaiku i Nocy Kupały: wyraźne komunikaty dla zgonu i przeżycia.
- Poprawiono analogiczne gałęzie próby Peruna, zemsty rodowej, ostatniej rozprawy, osobistego gniewu Peruna i Welesa; także wariant 50/50 ratunku dworzanina.
- Dodano 16 osobnych wyników z 42 kluczami lokalizacji w każdym języku. Zachowano faktyczne losowanie, premie i możliwość zgonu.
- Nowy natywny filtr komunikatów CK3 `auto_pause = yes` i powiadomienie przy otwarciu 24 okien świątecznych, 3 objawień i 2 wydarzeń zemsty.
- Kalendarz bez zmian. Dwustopniowa struktura 12 świąt i 31 zatwierdzonych grafik bez zmian.
- [0.4.2 DEV: pakiet przetestowany na Windowsie](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42573291604/artifacts/13654395511) — struktura i instalacja PASS; zachowanie pauzy w samej rozgrywce wymaga potwierdzenia.


## 0.4.1 DEV — 9 listopada 2026: obrzęd, dar i krwawa opowieść

- Wszystkie 12 świąt otrzymały **pierwsze okno edukacyjne** oraz **drugie okno fabularne**. Zachowano groźne wybory i odroczoną zemstę.
- Każdy udział w święcie daje +45 pobożności, -10 stresu i odpowiednie tematyczne błogosławieństwo na 90 dni; usunięto ryzyko podwójnego przyznania podstawowej premii.
- Stare zapowiedzi i wydarzenia podglądu zamieniono na niewidoczne przekaźniki; audyt **12/12 PASS, dokładnie 2 okna**.
- Naprawiono wyświetlanie surowych nazw 15 nowych modyfikatorów i 4 efektów opinii — pełne nazwy i opisy po polsku i angielsku.
- Poprawiono audyt identyfikatorów z cyframi w nazwie `bp_041`, aby nie ukrywał rzeczywistego łańcucha wydarzeń.
- Zachowano 31 zatwierdzonych tekstur, trzy osobiste objawienia bogów, stare wejścia z kalendarza i gałąź 0.4.0.
- Zbudowano [aktualizator 0.4.1 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42565179434/artifacts/13651276740) i **przetestowano na Windowsie** podmianę istniejącej instalacji z kopią bezpieczeństwa. Test CK3 dla 0.4.1 nadal oczekuje.



### Poprawka instalatora 0.4.0 DEV — 9 listopada 2026

- Usunięto błąd: kontrola skryptu `AKTUALIZUJ_040.ps1` oczekiwała wersji `0.3.0-dev`, mimo że paczka miała `0.4.0-dev`; instalator przerywał przed kopiowaniem.
- Dostosowano szukanie katalogów do komputerów bez dysku `H:`.
- Dodano automatyczny test na Windows PowerShell 5.1: **prawdziwa instalacja nadpisująca próbny mod 0.3.0, kontrola kopii i nowych plików — PASS**.
- Poprawiona paczka: [pobierz 0.4.0 DEV](https://github.com/dmnq667/CK3-Bogowie-Pamietaja/actions/runs/42556994466/artifacts/13648255623). Poprzedniej paczki nie używać.

## 0.4.0 DEV — 9 listopada 2026

- Całkowita przebudowa widocznych historii **12 świąt**: 12/12 PASS, najwyżej 2 okna z zapowiedzią.
- Koniec automatycznych cztero-, pięcio- i ośmiookienkowych obrzędów.
- 107 kluczy lokalizacji PL/EN, jasna stawka, łącznie z imiennymi dworzanami i ryzykiem śmierci.
- Rozgałęzione losy: łaska, krwawe egzekucje prawdziwych postaci, rody pamiętające wyroki, wieloletnie modyfikatory i odroczona zemsta.
- Sąd I przeliczany automatycznie w tle, bez nowego klikania.
- Zmieniono wejście w pakt Welesa i wycofywanie ofiary; 3 główne objawienia i cała nowa oprawa graficzna bez zmian.
- Statyczna kontrola automatyczna PASS. **Nie wykonano jeszcze testu gry, kompatybilności zapisów ani bilansu.**



## 0.3.0 DEV — w produkcji (08.11.2026)
- Nazwa: **Gniew i Łaska Bogów**.
- Wydarzenia Welesa 2020, Peruna 9110 i Mokoszy 3010: osobiste objawienia, pamięć czynów, rozgałęzienia charakteru i silne konsekwencje.
- Nowe tła i opisy PL/EN, podstawowe premie za uczestnictwo w części świąt, redakcja pierwszych scen wszystkich 12 obrzędów.
- 28 nowych scen świątecznych i 3 grafiki boskie przekonwertowane do DDS, **zaimportowane i zweryfikowane na GitHubie 08.11.2026**; automatycznie wygenerowano aktualizator 0.3.0 DEV.
- Test w CK3, zgodność z aktualną wersją gry i pełna redakcja lokalizacji: **oczekują**.


Historia odtworzona z zachowanej dokumentacji, nie z oryginalnych commitów.

## 0.1.9 ALPHA
- Rozszerzony kalendarz do 12 świąt.
- Święto Peruna, Święto Plonów, Dziady jesienne, Szczodre Gody.
- Grafiki wydarzeń i efekty związane z mechaniką religijną oraz długiem Welesa.
- Walidacja statyczna według dokumentacji wydania; test w CK3 oczekuje.

## 0.1.8 ALPHA
- Rozwój mechaniki dynastycznego długu Welesa.

## 0.1.7 ALPHA
- Mapowanie ilustracji i dokumentacja wersji.

## 0.1.6 ALPHA
- Wcześniejszy etap projektu, szczegóły w oryginalnym archiwum.
