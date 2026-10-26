# Sesja testowa v0.1.9 ALPHA: przygotowanie do testu w CK3

**Status:** OCZEKUJE NA TEST UŻYTKOWNIKA  
**Wydanie źródeł:** `v0.1.9-alpha`  
**Wynik kontroli importu na GitHub:** 110/110 ścieżek obecnych. Nie jest to dowód poprawnego działania moda w grze.

## Zasady bezpieczeństwa

- Test wyłącznie na **kopii zapisu**, nie na głównej kampanii.
- Przed uruchomieniem zachowaj kopię aktualnej instalacji moda.
- Zanotuj wersję CK3, używany zestaw modów oraz ewentualne odstępstwa od `supported_version="1.20.*"`.
- Zachowaj świeży plik `Documents\Paradox Interactive\Crusader Kings III\logs\error.log` w razie nieoczekiwanego działania. Nie kasuj wcześniejszych logów bez kopii.

## Etap A: krótka kontrola uruchomienia

- [ ] Mod jest rozpoznawany przez launcher i można wczytać testowy zapis.
- [ ] Decyzja debug `[TEST] Bogowie pamiętają` jest dostępna w trybie debug.
- [ ] Ścieżka testowa `bp_test.9001 → bp_test.9002 → bp_test.9005` otwiera cztery nowe święta.
- [ ] Ścieżka `bp_test.9005 → bp_test.9006` pozwala podejrzeć cztery zapowiedzi bez angażowania mechanik święta.
- [ ] Widać właściwe tła Peruna, Plonów, Dziadów jesiennych i Szczodrych Godów; portrety nie zasłaniają istotnych elementów.
- [ ] Nie ma brakujących tłumaczeń (surowych kluczy lokalizacji), pustych przycisków ani błędów w oknach wydarzeń.
- [ ] Nie wystąpił crash ani oczywisty błąd w logu.

## Etap B: mechanika do osobnych prób

| Element | Oczekiwane zachowanie według projektu | Wynik |
| --- | --- | --- |
| Perun podczas wojny | Trzy próby, błogosławieństwo związane z osobistym dowodzeniem, ograniczone czasowo | Nie testowano |
| Perun w pokoju | Możliwość zachowania łaski i aktywacji po wybuchu wojny | Nie testowano |
| Święto Plonów | Premia dotyczy stolicy; sprawdzić kumulację z premią Mokoszy | Nie testowano |
| Dziady jesienne | Niespłacony dynastyczny dług Welesa blokuje wielką łaskę | Nie testowano |
| Szczodre Gody | Święto rozpoczęte w grudniu nie resetuje się 1 stycznia | Nie testowano |
| Powrót po roku | Święto znów jest dostępne w następnym sezonie | Nie testowano |

Pełny scenariusz i wymagane daty opisuje [PLAN_TESTOW_019.md](PLAN_TESTOW_019.md). Nie trzeba wykonywać wszystkich prób w jednej sesji.

## Dziennik zgłoszenia błędu

Gdy wystąpi problem, zapisać:

- Data testu i data w grze:
- Wersja CK3 / system:
- Aktywne mody i kolejność:
- Co uruchomiono / która opcja:
- Oczekiwany rezultat:
- Co faktycznie się wydarzyło:
- Powtarzalność błędu:
- Screen, `error.log` i ewentualnie kopia zapisu:
- Priorytet: blokujący / istotny / kosmetyczny.

Nie uznawać wersji za przetestowaną przed uzupełnieniem wyników. Zmiany mechaniki i nowe pomysły wymagają osobnego wpisu planu produkcji, bez modyfikowania stabilnego snapshotu.
