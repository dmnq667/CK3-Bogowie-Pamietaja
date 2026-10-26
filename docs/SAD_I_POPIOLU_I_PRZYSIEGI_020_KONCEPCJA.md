# Sąd I. Popiół i Przysięga

**Status:** KONCEPCJA ROBOCZA DO AKCEPTACJI AUTORA, bez zmian w źródłach 0.1.9.  
**Wersja docelowa:** 0.2.0.  
**Moment:** po Siedmiu Nocach Welesa (9–15 II), proponowany początek od 16 lutego.  
**Zasada finansowa:** ten sąd NIE wypłaca złota. Warunkowe 1500 złota raz na rok obrzędowy może przyznać tylko Sąd II po Dziadach wiosennych.

## Dramaturgia

Sąd ma przypomnieć, co władca zrobił przy Gromnicy (ochrona ognia, pomoc osadom lub zlekceważenie ostrzeżenia) i Siedmiu Nocach Welesa (uczciwy dar, ślub milczenia, świadoma ofiara, wybór więźnia i ewentualne ocalenie go, naprawienie krzywdy, odmowa, ucieczka albo kłamstwo). Nie stosować prostego testu dobry/zły. Podstawą oceny ma być wzięcie odpowiedzialności, cena czynu i prawdomówność.

### Wydarzenie otwierające: To, czego nie strawił ogień

> Trzeciej nocy po odejściu Welesa straże znajdują w wygasłym palenisku garść mokrej ziemi. Nie ma śladów włamania, popiół pozostaje zimny, lecz pośrodku leży moneta, której nie widziano w żadnym skarbcu.
>
> Na jednej stronie wyryto znak płomienia. Na drugiej imię człowieka, którego władca nigdy nie spotkał.
>
> Wezwany żerca długo przygląda się znalezisku.
>
> „Ogień pamięta, komu dałeś schronienie. Ziemia pamięta, czyje imię kazałeś jej przyjąć. A Weles zna słowa, których wolałbyś nie wypowiedzieć”.
>
> Tej nocy sen nie nadchodzi. Za drzwiami słychać kroki, choć wartownicy przysięgają, że korytarz jest pusty.

Dalsze opisy mają przywoływać autentyczne znaki ze źródłowych wydarzeń: czarny śnieg i sadzę z Gromnicy, ziemię z uratowanej osady, pył z otwartych składów, monety znalezione pod dębem, wybranego więźnia lub krew ofiary i krzywdę przodków. Władca nie może przez nową opcję dialogową unieważnić wcześniejszych działań.

## Proponowane warianty wyniku

| Wariant | Wybory w poprzednich świętach | Proponowany skutek |
| --- | --- | --- |
| **Światło dla żywych** (nowa nazwa, do zatwierdzenia) | Władca **strzegł ognia i uratował ludzi**, a następnie uczciwie zmierzył się z żądaniami Welesa | Możliwość otrzymania pierwszego stopnia cechy i **+5 dyplomacji na rok** |
| **Słowo dane ziemi** (nazwa zaakceptowana) | Władca przyjął trudną, nawet krwawą ofiarę, ale nie wyparł się odpowiedzialności | Możliwość otrzymania pierwszego stopnia cechy, **+5 intrygi i +10 postrachu na rok**; dług Welesa nadal obowiązuje |
| **Granica ofiary** (nowa nazwa, do zatwierdzenia) | Władca ochronił swoich ludzi, lecz świadomie odmówił ofiary, którą uznał za niedopuszczalną | Możliwość otrzymania pierwszego stopnia cechy i **+5 wiedzy na rok** |
| **Noc niełaski** (nowa nazwa, do zatwierdzenia) | Władca lekceważył ostrzeżenia, uciekł przed zobowiązaniami albo okłamał Welesa | **Brak cechy**, niepokojące zakończenie i **zapis przewinienia do Sądu II**; nie powielać nadmiernie już istniejącej klątwy Welesa |
| **Niedopełniona cena** | Niezakończony wybór więźnia lub inne rzeczywiście nierozstrzygnięte zobowiązanie | Osobna scena o zawieszonej przysiędze. Bez przyznawania sukcesu ani automatycznego orzekania winy |

### Nazwy rozstrzygnięć, propozycje do zatwierdzenia

Autor zaakceptował skutki i ich siłę, ale poprosił o zmianę trzech nazw. Ostatecznego wyboru nazw jeszcze nie potwierdził.

| Funkcja rozstrzygnięcia | Nazwa rekomendowana | Dodatkowe propozycje |
| --- | --- | --- |
| Ochrona ognia i ratunek ludzi | **Światło dla żywych** | Ogień dochowany; Straż ostatniego płomienia |
| Świadoma odpowiedzialność za trudną ofiarę | **Słowo dane ziemi** (bez zmian) | Nie dotyczy |
| Świadoma odmowa niedopuszczalnej ofiary | **Granica ofiary** | Dar, którego nie oddano; Nie wszystko wolno poświęcić |
| Zaniedbanie, ucieczka albo kłamstwo wobec Welesa | **Noc niełaski** | Znak niełaski; Gdy bogowie milczą |

### Niezbędne rozstrzygnięcie projektowe: „strzegł ognia **i** uratował ludzi”

Sformułowanie autora celowo zawiera oba działania, ale **w 0.1.9 opcje Gromnicy wykluczają się**: w `bp_gromnica.1001.a` władca opłaca ochronę ognia (flaga `bp_gromnica_fire`), a w `bp_gromnica.1001.b` wysyła pomoc do osad (flaga `bp_gromnica_village`). Nie może w tym samym przebiegu wybrać obu.

Nie wolno deklarować, że warunek łączny już działa. Przed kodowaniem 0.2.0 ustalić z autorem, czy dodać **osobną możliwość późniejszego ratowania ludzi przy zachowaniu świętego ognia**, czy świadomie dopuszczać w „Świetle dla żywych” jeden z tych czynów wraz z uczciwym rozliczeniem Welesa. Na razie zachować pełne brzmienie autora i oznaczyć zależność jako wymagającą decyzji.

Warunki są **propozycją scenariuszową**, niezatwierdzonym balansem. Zakończenia powinny wymagać świadomej decyzji w sądzie i opierać się na prawdziwych wyborach z poprzednich świąt.

## Trait i związek z następnym sądem

- Roboczo jedna widoczna, trwała cecha pierwszego stopnia: **Znak Pierwszego Ognia**, np. +1 zarządzania i +1 wiedzy. Dodatkowa roczna premia zależy od ścieżki.
- Cechy nie przyznawać automatycznie za samo uczestnictwo ani za porzucenie wszystkich obrzędów.
- Nie karać od razu za sam fakt nowo otwartego długu Welesa! Wielka łaska w wydarzeniu Welesa otwiera dynastyczny dług, a jego rozliczenie następuje później. To jeszcze nie jest złamanie słowa.
- Kłamstwo wobec przodków i świadome odrzucenie wcześniejszych wyborów może zaciążyć na Sądzie II.
- Zapisać wynik Sądu I jako pamięć ocenianą po Dziadach wiosennych. Sukces w Sądzie I nie gwarantuje +1500 złota w Sądzie II.
- Gdy sąd nie daje cechy, nie blokować jej definitywnie; postać może na nią zasłużyć w następnych latach.

## Mapa istniejących mechanik i ograniczenia

- Gromnica, wydarzenie bp_gromnica.1001: opcja A ustawia bp_gromnica_fire, B ustawia bp_gromnica_village, C daje 20 złota i obniża łaskę Welesa, ale nie zapisuje osobnej flagi.
- Weles bp_weles.2001–2008: bp_weles_fled, bp_weles_oath_of_silence, bp_weles_offering, bp_weles_blood, bp_weles_merciful, bp_weles_truth, bp_weles_lied i inne znaczniki pozwalają rozróżnić ścieżki.
- Weles bp_weles.2002.d (odmowa ofiary) oraz bp_weles.2003.c (prośba o czas) nie mają własnych znaczników wyboru. Implementacja 0.2.0 powinna je dodać i utrwalać wynik.
- Pierwszy sąd przypada po 15 lutego, ale ścieżka więźnia może nadal oczekiwać na rozstrzygnięcie przez około 20 dni. Nie traktować jej bezwarunkowo jako winy.
- Nowy sąd powinien korzystać z istniejącego strażnika kalendarza; nie dodawać drugiego codziennego on_action.
- Raz na cykl obrzędowy, również po ponownym wczytaniu gry lub sukcesji. W debug nie wolno zwielokrotniać cech i innych nagród.
- Wynik i istotne wybory archiwizować do Sądu II. Obecne flagi Gromnicy i Welesa często wygasają po 90 dniach; nie można uzależnić majowego sądu wyłącznie od ich bieżącej obecności.
- Testować: ogień + uczciwy dar; ratunek osad + łaska więźnia; ofiara z więźnia; świeżo zaciągnięty dług; stary dług dynastyczny; oszustwo; odmowa z zasad; ucieczka; brak udziału; nierozstrzygnięty więzień; powtarzanie debug i zmiana władcy.

**Do uzgodnienia:** czy wszystkie pozytywne ścieżki nadają tę samą rozwijającą się cechę, a różni je tylko czasowy bonus i skutki fabularne. Na razie taki wariant rekomendowany, ale niezatwierdzony.
