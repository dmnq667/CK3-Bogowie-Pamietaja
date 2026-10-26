# BOGOWIE PAMIĘTAJĄ: WERSJA 0.1.9 ALPHA, DWANAŚCIE ŚWIĄT

**Data:** 26.10.2026  
**Punkt wyjścia:** `Bogowie_Pamietaja_v0.1.8_ALPHA_DLUG_WELESA.zip`.  
**Status:** gotowa do testów w silniku, walidacja statyczna PASS. **Nie testowano jeszcze nowej wersji w uruchomionym CK3.**

## Co dodano

| Święto | Okres w CK3 | Zdarzenia | Grafiki |
| --- | --- | --- | --- |
| **9. Święto Peruna: Pod gromem** | 20–27 lipca | `bp_perun.9101`–`.9108` | 01 główna, 02 przysięga i próby, 03 boski znak i niełaska |
| **10. Święto Plonów: Co daje ziemia** | 28 sierpnia – 5 września | `bp_harvest.9201`–`.9208` | 01 główna, 02 podział plonów, 03 próba naprawy i skutki |
| **11. Dziady jesienne: Ci, którzy wracają** | 25–31 października | `bp_autumn.9301`–`.9308` | 01 główna, 02 spotkanie przodków, 03 sąd i rozliczenie |
| **12. Szczodre Gody: Światło powraca** | 21 grudnia – 6 stycznia | `bp_szczodre.9401`–`.9408` | 01 główna, 02 uczta i zobowiązanie, 03 zmarli i konsekwencje |

Do każdej historii dodano trzy próby prowadzące do mocnego błogosławieństwa tylko po spełnieniu warunków. Próby mają koszt i wpływ na przebieg historii. Gracz może odmówić obrzędu, ale święto nadejdzie automatycznie niezależnie od niego.

### Perun
- Test odwagi działa w trakcie wojny i w pokoju; podjęcie własnego ryzyka, koszt przysięgi i pomoc rannemu.
- Wielka łaska: **+20 przewagi podczas osobistego dowodzenia, +50% obrażeń armii i +100% skuteczności rycerzy** przez 12 miesięcy. W pokoju może być zachowana na maksymalnie 2 lata i później aktywowana osobną decyzją w trakcie wojny.
- Błogosławieństwo jest mechanicznie silne, lecz ograniczone czasowo; **nie jest związane skryptowo z identyfikatorem jednej wojny**. Nie twierdzić inaczej.

### Święto Plonów
- Wariant po wcześniejszym zranieniu świętego gaju oraz wariant wynikający z pamięci o Gaiku.
- Trzy próby: obrzęd, rzeczywisty podział zapasów, troska o przyszły siew.
- Wielka łaska na stolicę: +100% wzrostu rozwoju oraz +50% podatków przez 3 lata. Alternatywą są skromne wsparcie albo kara za chciwość.
- W następnej wersji warto sprawdzić limit łączenia łaski Plonów z modyfikatorem Mokoszy z Jarych Godów. W 0.1.9 **brak mechanicznego zakazu kumulacji**; zakres ograniczono do jednej stolicy.

### Dziady jesienne
- Nie są kopią Dziadów wiosennych. Jesień jest czasem odpowiedzialności za czyny rodu.
- Odczytywany jest **istniejący dynastyczny dług Welesa z 0.1.8**. Gdy dług pozostaje otwarty, wielka łaska jest niedostępna, a osobne wydarzenie pozwala podjąć próbę spłaty za pomocą wcześniej istniejącego `bp_weles.2013`.
- Dwie alternatywne wielkie łaski: +6 do wojskowości i +60% skuteczności rycerzy lub +6 do zarządzania i +40% miesięcznego dochodu na 2 lata. Nadpisują wcześniejsze modyfikatory Wiedzy Przodków, aby nie powielać podobnych premii.

### Szczodre Gody
- **Jeden okres od 21 grudnia do 6 stycznia**, bez resetu w dniu 1 stycznia. Odprawienie, odmowa i zapowiedź korzystają z dynastycznej blokady na 335 dni. W styczniu nie da się ponownie odprawić święta rozpoczętego w grudniu. Okres uruchomiony dopiero po wgraniu aktualizacji w styczniu może działać bez grudniowej zapowiedzi.
- Rozliczenie roku, pamięć o zmarłych, otwarcie stołu dla podróżnych, dotrzymanie obietnicy, warunkowy wątek długu Welesa.
- Dwie formy wielkiej łaski: osobista odnowa państwa (+6 do zarządzania i +35% dochodu przez rok) albo odnowa stolicy (+70% tempa rozwoju i +25% podatków przez dwa lata).
- Nierozliczony dług Welesa ogranicza wielką łaskę i nie znika z Nowym Rokiem.

## Interfejs i stare święta

- Rozszerzono istniejący, działający `bp_announcement.1299` do 12 okien. **Nie uruchomiono drugiego strażnika**.
- Dodano 4 dostępne w okresie decyzje rozpoczęcia, jedną opcję aktywacji wojennego błogosławieństwa Peruna, 4 niezależne automatyczne zapowiedzi oraz 4 podglądy testowe.
- Księga Bogów pokazuje teraz wszystkie 12 dat; Kronika Świąt ma trzecią kartę z nowymi świętami, widoczną z wcześniejszej karty kroniki.
- Sceny pierwszych ośmiu świąt, kalendarz ich zapowiedzi, Weles i jego dług dynastyczny nie były zmieniane. Dotychczasowych grafik nie edytowano.

## Materiały wizualne

- Dotychczasowe **20 JPG i 20 DDS** zachowano identycznie bajt po bajcie.
- Dodano 12 nowych autorskich JPG użytkownika oraz 12 tekstur DDS, 1592×848 px, BC1/DXT1.
- Perun: **główna grafika 01(2)** z ostatniej przesyłki; tło 02(2) do próby i 03(2) do znaku, bez korzystania z wcześniejszych wersji Peruna oraz bez generowania nowych grafik.
- Dożynki, Dziady jesienne i Szczodre Gody: dostarczone przez użytkownika obrazy 01–03.
- Nowe sceny zarejestrowano w `common/event_backgrounds/bp_slavic_holiday_backgrounds.txt` i przypisano przez `override_background`, pozostawiając portrety postaci CK3.
- Oryginalne JPG dołączono w `source_artwork/`, nie trzeba ich osobno wgrywać do gry.

## Wynik walidacji

Wyniki szczegółowe: `docs/VALIDATION_019.json`:
- **131** ID wydarzeń, wszystkie unikalne; 32 nowe wydarzenia głównych rozdziałów, 4 nowe zapowiedzi, 4 podglądy testowe, 4 karty statusu w kronice, 2 nowe ekrany debug i karta kroniki.
- **669** unikalnych kluczy PL i **669** EN, kompletność i parzystość.
- Zweryfikowane 254 wywołania eventów i 119 odwołań do scen, bez niezdefiniowanych odniesień.
- 32 tekstury DDS można odczytać; 12 nowych obrazów jest weryfikowanych względem oryginałów.
- Test modelu kalendarza: **32 872 dni**, w tym lata przestępne, plus **2520** asercji blokady Szczodrych Godów na przełomie lat.
- Porównanie z paczką 0.1.8: 56 plików bez zmian (w tym 20 JPG i 20 DDS). Zmieniono tylko 11 oczekiwanych plików mechaniki, lokalizacji i manifestu; dodano nowe skrypty.
- Installer wymaga 32 DDS, sprawdza format/rozmiar i wykonuje kopię poprzedniej instalacji na H:.

## Nieweryfikowane w grze

**Nie odpalono CK3 w tym środowisku.** Trzeba sprawdzić w rzeczywistym silniku: wywołania sezonów, wpływ i skalowanie nowych modyfikatorów, wejście do wojny po zachowaniu łaski Peruna, przełom grudnia i stycznia, wygląd nowych teł pod portretami, użyteczność Księgi Bogów oraz log błędów. W przypadku crasha wrócić do backupu i dostarczyć `error.log`.

Ten ZIP nie zmienia osobnego moda *The Weight of Words*.
