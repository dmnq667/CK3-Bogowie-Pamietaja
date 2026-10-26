# 0.2.0, Gromnica: dwa czyny w jednym obrzędzie

**Status:** KOD WDROŻONY NA GAŁĘZI ROBOCZEJ, WALIDACJA STATYCZNA PASS. TEST W CK3: OCZEKUJE.
**Gałąź:** `feature/0.2.0-gromnica-dual-duty`
**Baza bez zmian:** `main` oraz tag `v0.1.9-alpha`.
**Decyzja autora:** umożliwić strzeżenie ognia **i** uratowanie ludzi podczas jednego przebiegu Gromnicy. Rozstrzygnięcie negatywne Sądu I zmienia nazwę na **„Gdy bogowie milczą”**.

## Jak działa nowy wybór

1. W dotychczasowym `bp_gromnica.1001` wybiera się jedno z trzech działań; treści i skutki pierwszej sceny nie zostały zmienione.
2. W drugim wydarzeniu, `bp_gromnica.1002`, można wykonać **drugi czyn**:
   - jeśli najpierw opłacono straże i ognie (35 złota), można jeszcze wysłać pomoc do północnych osad (50 prestiżu);
   - jeśli najpierw uratowano mieszkańców osad (50 prestiżu), można dodatkowo opłacić straże i ognie (35 złota).
3. Po drugim czynie gracz widzi trzecią scenę `bp_gromnica.1003`, roboczo „Dwa obowiązki”, z odrębnym opisem zależnym od kolejności działań. Wykorzystano istniejące tła Gromnicy, bez tworzenia nowych grafik.
4. Gra zapisuje **oba dotychczasowe znaczniki** `bp_gromnica_fire` i `bp_gromnica_village` oraz nowy, trwalszy `bp_gromnica_both_done_v020` (335 dni). Sąd I będzie mógł w wersji 0.2.0 zweryfikować faktycznie wykonane oba czyny; sąd nie został jeszcze zakodowany.
5. Dodatkowy czyn zwiększa przychylność jednego boga o 10: ścieżka „ogień, potem ludzie” zyskuje +10 łaski Mokoszy, zaś „ludzie, potem ogień” +10 łaski Welesa. Obie ścieżki osiągają łącznie +20 łaski każdego boga. Druga ścieżka otrzymuje też istniejącą ochronę palenisk `bp_gromnica_guard_modifier`.
6. Oryginalna opcja zamknięcia drugiej sceny pozostaje dostępna; wykonanie obu czynów nie jest przymusowe.
7. Ścieżka lekceważenia Gromnicy nie otrzymuje darmowego dostępu do dwóch nagród. Jej dotychczasowy przebieg pozostaje bez zmian.
8. Oba nowe wybory oraz wszystkie opisy sceny `bp_gromnica.1003` zostały dodane do polskiej i angielskiej lokalizacji (po 7 kluczy).

## Istotne rozróżnienie

Nowe opcje **nie przyznają od razu pierwszej cechy Sądu I ani +1500 złota**. Pozytywny wynik Sądu Popiołu i Przysięgi będzie wymagał jeszcze uczciwego rozliczenia decyzji Welesa. Złoto +1500 będzie rozpatrywane tylko raz w roku podczas **drugiego** sądu, po Dziadach wiosennych.

## Kontrola statyczna, wykonana

- PASS: kod pierwszej sceny `bp_gromnica.1001` jest identyczny jak w stabilnym `main`.
- PASS: trzy unikalne identyfikatory wydarzeń `bp_gromnica.1001`, `.1002`, `.1003`; dwa nowe wybory prowadzą do `.1003`.
- PASS: dwie ścieżki, rzeczywiste koszty (-50 prestiżu / -35 złota), flagi obu czynów, osobne znaczniki kolejności.
- PASS: brak utraty pierwotnej opcji `bp_gromnica.1002.a`.
- PASS: poprawnie zbilansowane nawiasy klamrowe wydarzenia.
- PASS: wszystkie pierwotne klucze PL/EN zachowane, dodano identyczne 7 nowych kluczy na język bez duplikatów; zachowano BOM lokalizacji.
- **UWAGA:** to kontrola strukturalna, nie pełna walidacja silnika CK3. Zgodność silnika, czytelność opcji i UI wymagają testu w grze.

## Scenariusze do sprawdzenia w CK3

| Przebieg | Oczekiwany rezultat | Status |
| --- | --- | --- |
| Ogień w `1001`, potem pomoc osadom w `1002` | Koszt 35 złota i 50 prestiżu; scena `1003`; oba znaczniki czynów oraz `both_done` | NIE TESTOWANO W GRZE |
| Osady w `1001`, potem ogień w `1002` | Koszt 50 prestiżu i 35 złota; scena `1003`; oba znaczniki | NIE TESTOWANO W GRZE |
| Ogień albo osady, potem pierwotna opcja `1002.a` | Dotychczasowe zakończenie; bez flagi `both_done` | NIE TESTOWANO W GRZE |
| Zbyt mało złota na drugie działanie | Opcja opłacenia ognia niedostępna, brak przypadkowego bonusu | NIE TESTOWANO W GRZE |
| Zlekceważenie Gromnicy w `1001.c` | Bez dodatkowej ścieżki ratunku i nagrody za oba czyny | NIE TESTOWANO W GRZE |
| Wczytanie zapisu po wykonaniu obu czynów | Obie decyzje nadal zapisane, scena nie zapętla się | NIE TESTOWANO W GRZE |
| Weles po Gromnicy | Odczyt obydwu wcześniejszych flag nie zakłóca dotychczasowej fabuły Welesa | NIE TESTOWANO W GRZE |

Przy regresji przetestować starą wersję 0.1.9 na osobnej kopii zapisu. Nie mieszać niezależnie przetestowanych zapisów. Nie oznaczać całego 0.2.0 jako gotowego wydania na podstawie tej jednej poprawki.
