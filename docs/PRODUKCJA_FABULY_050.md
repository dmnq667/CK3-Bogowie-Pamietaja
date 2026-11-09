# Gniew i Łaska Bogów — produkcja fabuły 0.5.0

Status: rozpoczęta produkcja. Gałąź rozwojowa izolowana od 0.4.6.

## Cel
Dwanaście powracających świąt, po 10 odrębnych scen fabularnych każde: 120 scen. Nie są to kosmetyczne przeredagowania tego samego wydarzenia. Każda scena ma własny konflikt, wybory i zapamiętywane następstwa.

## Dystrybucja na każde święto
- 4 sceny dostępne ogólnie;
- 3 sceny będące kontynuacją wcześniej dokonanych wyborów;
- 2 sceny zależne od realnego stanu postaci, rodziny lub państwa;
- 1 scena dla najwyższej rangi boskiego znamienia.

## Kontrakt implementacyjny
1. Nie zastępować działającego harmonogramu świąt nowymi, równoległymi on_action.
2. Zachować zatrzymywanie gry na widocznym wydarzeniu i istniejące ilustracje.
3. Wybór sceny następuje tylko raz na święto w danym roku; dopiero później wykonują się właściwe skutki wyboru.
4. Warianty warunkowe muszą mieć prawdziwe warunki (istniejąca postać, wojna, stres, dług wobec Welesa itd.) oraz bezpieczny wariant rezerwowy.
5. Zapisać identyfikator rozegranej sceny i czas jej rozegrania. Unikać powtórzenia sceny w następnym cyklu; nie tworzyć sytuacji bez dostępnego wydarzenia.
6. Czyn dokonany w jednej scenie może zostać użyty przez inne święto i podczas sądu. Nie wolno „pamiętać” czynów, których gracz nie popełnił.
7. Nagrody i kary muszą być widoczne i odpowiadać dokonanej decyzji, w tym stresowi i charakterowi władcy.
8. Odniesienia do dworzan i krewnych mogą dotyczyć wyłącznie istniejących i właściwie sprawdzonych postaci.
9. Wydarzenia wyjątkowe po IV stopniu nie mogą blokować dostępu do zwykłego kalendarza świąt.
10. Tekst ma zachować wysoki, mroczny, literacki rejestr; bez sztucznie rozwlekłych scen.
11. Zachować save compatibility tam, gdzie to możliwe; nie usuwać starych identyfikatorów eventów, zmiennych ani lokalizacji potrzebnych zapisom.
12. Przed wydaniem: kontrola nazw zdarzeń, identyfikatorów lokalizacji, kodowania UTF-8 BOM w plikach YML, nawiasów, istniejących zasobów graficznych oraz konfliktów z obecnymi watcherami.

## Dwunastka
1. Gromnica
2. Siedem nocy Welesa
3. Wiosenny Nowy Rok
4. Jare Gody
5. Gaik / Turzyca
6. Dziady wiosenne
7. Stado
8. Noc Kupały
9. Święto Peruna
10. Dożynki
11. Dziady jesienne
12. Szczodre Gody

## Rozliczenie sądów
Projekt fabularny musi respektować uzgodniony czteroletni rozwój znamion, ale aktualną implementację sądów należy najpierw przejrzeć — w gałęzi 0.4.6 pierwszy sąd jest uruchamiany po tygodniu Welesa i nie jest to jeszcze komplet czterech dorocznych sądów. Nie opisywać tego jako już wdrożonego.

## Etapy techniczne wewnątrz jednej wersji wydania
A. Audyt uruchamiania świąt i efektów.
B. Silnik wyboru wariantów + pamięć.
C. 120 autorskich scen i polska lokalizacja.
D. Integracja następstw oraz sądów.
E. Statyczna walidacja i paczka DEV.
F. Test w CK3 — konieczny, by potwierdzić działanie silnika gry.

Zasada wydania: jedna kompletna wersja 0.5.0 DEV do testów, bez obowiązku zatwierdzania osobno Gaiku, ale bez nazywania wersji „sprawdzoną w CK3”, dopóki nie odbędzie się test gry.
