# Projekt mechaniki 0.2.0 ALPHA: Cztery Sądy Bogów

**Data koncepcji:** 26.10.2026  
**Status:** PODZIAŁ SĄDÓW USTALONY PRZEZ AUTORA (26.10.2026). Szczegóły nagród i cech pozostają propozycją. Bez zmian w działającym modzie 0.1.9.  
**Baza:** `v0.1.9-alpha` (kompletne źródła na GitHubie; próby w CK3 zaplanowane na wieczór).

## Główna idea

Cztery sądy pojawiają się **po 2., 6., 9. i 12. święcie**. Podział odzwierciedla znaczenie obrzędów, nie równe kwartały ani równe grupy po trzy. Każdy sąd jest narracyjnym następstwem rzeczywistych decyzji postaci, również odmowy lub zaniedbania obrzędów. **Sąd II ma rangę rozliczenia minionego roku i rytualnego zamknięcia starego cyklu.**

### Cztery rozdziały: zatwierdzony układ 2 + 4 + 3 + 3

| Po święcie | Podlegające ocenie święta | Roboczy tytuł sądu | Okno obrzędów / moment sądu |
| --- | --- | --- | --- |
| **2** | **1. Gromnica; 2. Siedem Nocy Welesa** | **I. Sąd Popiołu i Przysięgi** | Po 15 lutego, proponowany start od 16 lutego |
| **6** | **3. Wiosenny Nowy Rok; 4. Jare Gody; 5. Gaik / Turzyca; 6. Dziady wiosenne** | **II. Sąd Korzeni i Przodków: Zamknięcie starego roku** | Po 8 maja, proponowany start od 9 maja |
| **9** | **7. Stado; 8. Noc Kupały; 9. Święto Peruna** | **III. Sąd Ognia i Gromu** | Po 27 lipca, proponowany start od 28 lipca |
| **12** | **10. Święto Plonów; 11. Dziady jesienne; 12. Szczodre Gody** | **IV. Sąd Plonów, Cieni i Światła** | Po 6 stycznia następnego roku, proponowany start od 7 stycznia |

Daty otwarcia sądów to **propozycje implementacyjne wynikające z obecnych okien świąt 0.1.9**, nie nowe daty tradycji historycznej. Święto 12 przekracza granicę grudnia i stycznia i jest jednym obrzędem; nie wolno odpalać sądu IV ponownie na Nowy Rok.


Wydarzenia są niezależne od decyzji o rozpoczęciu obrzędu: odmowa, pominięcie lub zaniedbanie również powinny zostać odnotowane. Każdy sąd wywoływać automatycznie po domknięciu ostatniego święta przypisanego do danego sądu, poprzez **istniejący strażnik kalendarza**, bez drugiego codziennego on_action. Ochrona przed ponownym wywołaniem w tym samym okresie i po sukcesji.

## Wyjątkowa rola drugiego sądu: bilans minionego roku

Według przyjętej koncepcji świata moda przejście ze starego roku ku nowemu dokonuje się wraz z obrzędami wiosennymi. **Wiosenny Nowy Rok i Jare Gody rozpoczynają odnowę, ale dopiero Gaik / Turzyca i Dziady wiosenne pozwalają domknąć pamięć o minionym cyklu.** Sąd II jest więc wielkim *rytualnym zamknięciem i osądem minionego roku*, nawet jeśli w kalendarzu CK3 wypada po wcześniejszej wiosennej celebracji nowego roku.

To **świadoma interpretacja fabularna dla moda**. Nie twierdzić, że wszyscy historyczni Słowianie mieli jednolity kalendarz lub że ich rok cywilny kończył się 8 maja. Użytkownik definiuje wewnętrzną logikę obrzędową i opowieść.

Mechanika sądu II:
1. Rozpatruje wszystkie **cztery** święta rozdziału wiosennego oraz **wynik sądu I**, a nie tylko cztery osobne flagi obecności.
2. Uwzględnia otwarte zobowiązania ze **starego cyklu**, w szczególności prawdziwy stan dynastycznego długu Welesa, dotrzymane lub złamane przysięgi i wybory gracza. Może wspomnieć decyzje z dawnych świąt tylko wtedy, gdy zostały rzetelnie zapisane w danych.
3. Zamyka poprzedni rozdział symbolicznie, nie kasując długu Welesa ani nie resetując automatycznie nagród, traitów, strażnika kalendarza lub stanu innych świąt.
4. Jego konsekwencja fabularna powinna być wyraźnie **ważniejsza od zwykłego sądu sezonowego**. Wciąż przyznaje najwyżej jedną przewidzianą nagrodę za swój etap, nie powiela wypłaty z sądu I.
5. Aby nie pomylić wydarzeń stycznia z cyklem lutowo-majowym, zapis sądów musi mieć jednoznaczny identyfikator **cyklu obrzędowego**, niezależny od samego kalendarzowego przełomu roku. Przy późnej instalacji moda nie dopowiadać niezaobserwowanych decyzji.

Pozostałe sądy rozliczają swoje grupy świąt, a IV **nie jest drugim konkurencyjnym „sądem całego roku”**. Może zamykać cykl dwunastu obrzędów i przygotowywać następny, lecz ostateczne rytualne rozliczenie minionego roku jest motywem II.

## Pamięć konkretnych decyzji

Nie opierać oceny na tym, czy gracz tylko zobaczył wydarzenie ani na jednym globalnym, wiecznie narastającym współczynniku.

1. Każde święto musi przekazać do dziennika rozdziału informację o rzeczywistym wyniku wyborów postaci: `odbyty obrzęd`, `wybór / ścieżka`, `warunki próby`, `odmowa`, `brak działania`.
2. Dla czterech rozdziałów zarezerwować oddzielne znaczniki na władcy, tak aby jego czyny nie mieszały się automatycznie z wyborami poprzednika; **dług Welesa nadal pozostaje dynastyczny**.
3. Pozwolić co najmniej na trzy interpretacje postępowania: odpowiedzialność za lud, próba siły/odwagi, umowa z bogami za określoną cenę. Każda nie musi mieć identycznego zakończenia, ale nie sprowadzać wszystkich moralnie trudnych decyzji do „błąd”.
4. Ocena zależy od **2, 4, 3 albo 3 rzeczywistych świąt odpowiedniego rozdziału**, a zakończenie i opis mają przywołać konkretne zdarzenia (np. ochronę gaju, krew obiecaną Welesowi, dobroć wobec rannych Peruna).
5. Komplet danych każdego rozdziału, a dla sądu II także pamięć o pierwszym sądzie i zobowiązaniach minionego cyklu, trzeba zapisywać trwale do chwili rozliczenia. Dotychczasowe flagi świąt często wygasają po 90–120 dniach; nie wolno używać ich jako jedynego zapisu całego roku.
6. Blokada jednokrotnego naliczenia za święto i za sąd, również w debug. Unikać naliczania nagrody przez wielokrotne otwarcie testowych okien.

## Nagrody i cechy postaci

**Wola autora: nagroda finansowa ma być znacząca, najlepiej +1500 złota.**

### Proponowany model

- Każdy z czterech sądów może przyznać **+1500 złota** za uznany przez mechanikę, znaczący przebieg przypisanych do niego świąt (odpowiednio 2 / 4 / 3 / 3, a dla II także bilans minionego roku).
- Cztery sądy dają zatem do **+6000 złota na jedną postać**, jeśli zostaną wszystkie cztery nagrody zdobyte. To mocny, celowo hojny bonus, nie zwykły bilans świąt.
- **Nie wypłacać ponownie tej samej nagrody co rok tej samej postaci**. Może wracać fabularny sąd, ale jednorazową wypłatę danego etapu należy chronić stałym znacznikiem na postaci. Następny władca wypracowuje własne zasługi.
- Słaby lub niepełny przebieg świąt ma inne zakończenie, bez automatycznego +1500. Konkretne progi i alternatywne nagrody do zatwierdzenia z autorem.
- Obecny niespłacony dynastyczny dług Welesa **nie znika** po przyznaniu złota; wpływa zwłaszcza na najwyższy sąd.
- Nie zamieniać nagrody na stały odnawialny dochód bez wyraźnej zgody autora.

### Widoczna cecha (trait), nie tymczasowy modyfikator

Nowa mechanika powinna pokazywać wyróżnienie w **panelu cech postaci CK3**, z autorską ikoną DDS. Robocza propozycja: **jedna cecha rozwijająca się przez cztery stopnie**, a nie cztery oddzielne, bez końca kumulujące się cechy.

| Stopień | Proponowana nazwa | Motyw ikony | Robocze premie |
| --- | --- | --- | --- |
| I | **Znak Pierwszego Ognia** | żar i znak przysięgi | +1 zarządzania, +1 wiedzy |
| II | **Strażnik Korzeni** | święty dąb, splecione korzenie | +2 zarządzania, +2 wiedzy |
| III | **Naznaczony Gromem** | grom nad kręgiem słonecznym | +2 zarządzania, +2 wiedzy, +2 wojskowości |
| IV | **Wybraniec Dwunastu** | rozświetlony krąg dwunastu znaków | +4 zarządzania, +3 wiedzy, +3 wojskowości, +10% miesięcznego dochodu |

Każdy stopień zastępuje poprzedni, bez sumowania statystyk z czterech poziomów. Zdolności i nazwy są **robocze**, a dostęp do kolejnego stopnia powinien wynikać z faktycznie zdobytych wyróżnień, nie z samego upływu dat. Po nieudanym sądzie postać zachowuje dotychczasowy stopień i może próbować w kolejnym obiegu, zamiast automatycznie tracić cechę.

W implementacji: `common/traits/bp_covenant_traits.txt`, lokalizacje PL/EN i osobne ikony pod `gfx/interface/icons/traits/`. Postaci otrzymują cechę przez `add_trait` oraz tracą wcześniejszy stopień przez `remove_trait`. Nie nadawać cech dziedzicznie. Sprawdzić zgodność składni i wyświetlania z CK3 `1.20.*` w teście gry.

## Potrzebne pliki i logika nowej wersji

- `events/bp_judgement_events.txt`: cztery główne historie, odmienne warianty tekstu, wynik sądu i finał.
- `common/scripted_effects/bp_judgement_effects.txt`: zapis wyniku, przydział złota i awans cechy.
- `common/scripted_triggers/bp_judgement_triggers.txt`: warunki sądu, odmowa i blokady antyduplikacyjne.
- `common/traits/bp_covenant_traits.txt`: cztery stopnie widocznej cechy.
- `gfx/interface/icons/traits/bp_covenant_1..4.dds`: autorskie ikony.
- Uzupełnienie istniejących 12 świąt o odnotowanie **wybranych skutków**, bez zmiany obecnych nagród i narracji.
- Integracja z istniejącym `bp_announcement.1299`, bez równoległego watchera.
- Dopisanie informacji do Księgi Bogów i czterech scen testowych debug.
- Lokalizacja PL/EN, changelog, manifest wydania i osobny plan testów `0.2.0`.

## Krytyczne warunki testowe

- Cztery punkty kalendarza wywołują się tylko raz w odpowiednim okresie, kolejno po 2., 6., 9. i 12. święcie; w szczególności sąd po Szczodrych Godach **po 6 stycznia**, nie podwaja święta na przełomie roku.
- Sąd II po Dziadach wiosennych uwzględnia zapisany wynik Sądu I i stan poprzedniego roku, ale nie wypłaca nagrody I drugi raz, nie kasuje długu Welesa i nie resetuje całego kalendarza.
- Sprawdzić przełomy roku, rozpoczęcie kampanii w styczniu/lutym/maju oraz sukcesję między sądami; nie odtwarzać brakującej historii z domysłów.
- Postać, która odmówiła wszystkich świąt, nie dostaje automatycznej cechy i +1500 złota.
- Wydarzenie odzwierciedla konkretne ścieżki, nie jedynie obecność na świętach. Kontrola grup 2 / 4 / 3 / 3, bez pozostałości starego podziału po trzy.
- Maksymalnie jedna nagroda +1500 za każdy etap na postać; powtarzanie debug, zapisu, sukcesja i kolejny rok nie mnożą wypłat wbrew regułom.
- Cecha wyświetla się w panelu, ma poprawną ikonę, nazwę, opis, premii zgodne z projektem; przy awansie wcześniejsza cecha znika.
- Dług Welesa oraz istniejące efekty świąt nadal działają.
- Test kompatybilności na nowym i kontynuowanym zapisie; jeśli gracz włącza 0.2.0 w środku cyklu, brakujących wyborów **nie rekonstruować z domysłów**.
- Co najmniej: kontrola statyczna referencji, walidacja ikon, próba w silniku CK3, `error.log`.

## Ustalenia wymagające decyzji autora

1. Czy każdy udany sąd ma dawać +1500 złota (łącznie do 6000 na władcę), czy +1500 tylko finał roczny? **Domyślnie projektuj po +1500 za każdy sąd.**
2. Czy jedna rozwijająca się cecha jest właściwa, czy autor woli cztery niezależne cechy? **Domyślnie jedna czterostopniowa cecha.**
3. Jak kwalifikować „udany” przebieg grup 2 / 4 / 3 / 3 i bilans minionego roku w sądzie II: progi ilościowe czy narracyjny bilans różnych ścieżek? **Domyślnie ocena decyzji, nie samo uczestnictwo, z więcej niż jednym możliwym wariantem powodzenia.**

**Podział 2 / 4 / 3 / 3 oraz rola drugiego sądu są decyzją autora.** Szczegóły nagród, stopni cechy i kwalifikowania sukcesu pozostają robocze. Nie zmieniać tagu 0.1.9 ani deklarować testu w grze przed rzeczywistą sesją.
