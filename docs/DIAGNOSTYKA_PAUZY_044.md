# Diagnostyka pauzy wydarzeń CK3 — Gniew i Łaska Bogów

## Dlaczego wersje 0.4.2 i 0.4.3 nie działały?

W 0.4.2 dodaliśmy banery z własnym filtrem `auto_pause`. Gra wyświetlała je, ale nie przerywała czasu. To nie jest pewna metoda zatrzymania otwartego okna wydarzenia, a ustawienia filtra mogą zostać nadpisane przez gracza. Banery usunięto.

W 0.4.3 próbowaliśmy `type = letter_event` oraz `window = character_event`. W praktyce **to również nie zatrzymało rozgrywki** i wywołało nową regresję komunikatu (zgłoszenie użytkownika). Kod 0.4.4 cofa tę nietrafioną zmianę, przywracając `type = character_event` w 29 istotnych oknach.

**Brak pauzy nadal nie został naprawiony.** Wersja 0.4.4 jest naprawą regresji wyświetlania, nie obietnicą automatycznej pauzy.

## Udokumentowane polecenie do testu: pause_on

CK3 oferuje w konsoli debugowania polecenie `pause_on`. **To polecenie konsolowe, a nie efekt skryptowy wydarzenia**, dlatego nie należy go wpisywać do `events/*.txt` jako `pause_on = ...`.

Sprawdzenie dla Gaiku:

1. Uruchom CK3 w trybie debugowania — na dotychczasowych zrzutach widać, że jest aktywny.
2. Przed nadejściem Gaiku otwórz konsolę klawiszem `~`, `§` albo odpowiednią kombinacją zależną od układu klawiatury.
3. Wpisz: `pause_on bp_gaik.5001`.
4. Zamknij konsolę i uruchom grę na szybkości 5. Sprawdź, czy w dniu święta **pierwsze okno pojawia się przy zatrzymanym czasie**.
5. Na osobnym teście można analogicznie spróbować `pause_on bp_dziady.6001` lub `pause_on bp_stado.7001`.

Polecenie może działać jednokrotnie i nie jest dostępnym graczu standardowym bez debugowania rozwiązaniem na cały cykl dwunastu świąt. Ma **tylko ustalić, czy silnik rozpoznaje konkretne wydarzenie i potrafi w tym miejscu wymusić pauzę**.

Można też w konsoli wpisać `help pause_on`, aby zweryfikować obsługę i składnię polecenia w dokładnej wersji gry.

## Co sprawdzić przed kolejną próbą modowania

- Czy dowolne **zwykłe wydarzenie CK3**, niezwiązane z naszym modem, automatycznie zatrzymuje rozgrywkę na tej instalacji?
- Czy inny mod w playsecie nie zmienia obsługi pauzy lub okien wydarzeń? Dla testu wyłącz tylko mody odpowiedzialne za interfejs/pauzę, a sam mod Bogów pozostaw aktywny.
- Sprawdź w menu gry ustawienia komunikatów i automatycznej pauzy (wprowadzone od CK3 1.13).
- Zajrzyj do `Dokumenty\Paradox Interactive\Crusader Kings III\logs\error.log` oraz `database_conflicts.log` (jeśli występuje). Są szczególnie ważne w przypadku błędu komunikatu i konflików modów.
- Przetestuj jedno zdarzenie `event bp_gaik.5001` w konsoli i upewnij się, że wyświetla się w natywnym oknie z prawidłową lokalizacją.

Przy tym typie wydarzenia (`character_event`) dokumentacja skryptów CK3 nie wskazuje odrębnego, uniwersalnego parametru `pause = yes`. Flaga `should_pause_time = yes` występuje w bloku `court_scene` wydarzeń dworskich (`court_event`), którego **nie można bez sprawdzenia bezpiecznie skopiować do zwykłego wydarzenia**. W przeciwieństwie do tych flag `pause_on` jest udokumentowaną komendą konsolową.

## Gwarancje bezpieczeństwa wersji 0.4.4

- Dwustopniowa struktura 12 świąt, terminy, grafiki i ryzykowne rozstrzygnięcia **bez zmian**.
- 29 okien wraca na standardowy typ, bez pustego `opening = bp_043_empty_opening`.
- Zero dodatkowych banerów przy otwarciu; pozostają komunikaty o istotnych wynikach po decyzjach.
- Instalator nadpisuje istniejącego moda i wykonuje kopię bezpieczeństwa.

**Ważne: dopóki nie zobaczymy, że gra rzeczywiście się zatrzymuje, nie należy oznaczać żadnej dalszej wersji jako „naprawiona pauza”.**
