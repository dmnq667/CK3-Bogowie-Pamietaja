# Projekt mechaniki 0.2.0 ALPHA: Cztery Sądy Bogów

**Data koncepcji:** 26.10.2026  
**Status:** PROPOZYCJA DO UZGODNIENIA Z AUTOREM. Bez zmian w działającym modzie 0.1.9.  
**Baza:** `v0.1.9-alpha` (kompletne źródła na GitHubie; próby w CK3 zaplanowane na wieczór).

## Główna idea

Po każdej **trójce** świąt gracz otrzymuje dodatkowe, narracyjnie rozbudowane wydarzenie sądu bogów. Nie jest to kolejny obrzęd, lecz **konsekwencja dotychczasowych wyborów postaci**.

W wypowiedzi autora wystąpiła sprzeczność: „po trzech pierwszych” i później „po pierwszym”. Przyjęto logiczny porządek **po 3., 6., 9. i 12. święcie**. Potwierdzić przy dalszym projektowaniu; nie zakładać, że chodzi o literalne kwartały kalendarzowe.

### Cztery rozdziały

| Po święcie | Podlegające ocenie święta | Roboczy tytuł sądu | Domknięcie okna obrzędu |
| --- | --- | --- | --- |
| 3 | Gromnica, Siedem Nocy Welesa, Wiosenny Nowy Rok | **Sąd Popiołu i Przysięgi** | po 14 marca |
| 6 | Jare Gody, Gaik / Turzyca, Dziady wiosenne | **Sąd Korzeni i Przodków** | po 8 maja |
| 9 | Stado, Noc Kupały, Święto Peruna | **Sąd Ognia i Gromu** | po 27 lipca |
| 12 | Święto Plonów, Dziady jesienne, Szczodre Gody | **Sąd Dwunastu Świąt** | po 6 stycznia następnego roku |

Wydarzenia są niezależne od decyzji o rozpoczęciu obrzędu: odmowa, pominięcie lub zaniedbanie również powinny zostać odnotowane. Każdy sąd wywoływać automatycznie po domknięciu okresu trzeciego święta, poprzez **istniejący strażnik kalendarza**, bez drugiego codziennego on_action. Ochrona przed ponownym wywołaniem w tym samym okresie i po sukcesji.

## Pamięć konkretnych decyzji

Nie opierać oceny na tym, czy gracz tylko zobaczył wydarzenie ani na jednym globalnym, wiecznie narastającym współczynniku.

1. Każde święto musi przekazać do dziennika rozdziału informację o rzeczywistym wyniku wyborów postaci: `odbyty obrzęd`, `wybór / ścieżka`, `warunki próby`, `odmowa`, `brak działania`.
2. Dla czterech rozdziałów zarezerwować oddzielne znaczniki na władcy, tak aby jego czyny nie mieszały się automatycznie z wyborami poprzednika; **dług Welesa nadal pozostaje dynastyczny**.
3. Pozwolić co najmniej na trzy interpretacje postępowania: odpowiedzialność za lud, próba siły/odwagi, umowa z bogami za określoną cenę. Każda nie musi mieć identycznego zakończenia, ale nie sprowadzać wszystkich moralnie trudnych decyzji do „błąd”.
4. Ocena zależy od **trzech rzeczywistych świąt danego rozdziału**, a zakończenie i opis mają przywołać konkretne zdarzenia (np. ochronę gaju, krew obiecaną Welesowi, dobroć wobec rannych Peruna).
5. Komplet danych danej trójki trzeba zapisywać trwale do chwili sądu. Dotychczasowe flagi świąt często wygasają po 90–120 dniach; nie wolno używać ich jako jedynego zapisu całego roku.
6. Blokada jednokrotnego naliczenia za święto i za sąd, również w debug. Unikać naliczania nagrody przez wielokrotne otwarcie testowych okien.

## Nagrody i cechy postaci

**Wola autora: nagroda finansowa ma być znacząca, najlepiej +1500 złota.**

### Proponowany model

- Każdy z czterech sądów może przyznać **+1500 złota** za uznany przez mechanikę, znaczący przebieg trzech poprzednich świąt.
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

- Cztery punkty kalendarza wywołują się tylko raz w odpowiednim okresie; w szczególności sąd po Szczodrych Godach **po 6 stycznia**, nie podwaja święta na przełomie roku.
- Postać, która odmówiła wszystkich świąt, nie dostaje automatycznej cechy i +1500 złota.
- Wydarzenie odzwierciedla konkretne ścieżki, nie jedynie obecność na trzech świętach.
- Maksymalnie jedna nagroda +1500 za każdy etap na postać; powtarzanie debug, zapisu, sukcesja i kolejny rok nie mnożą wypłat wbrew regułom.
- Cecha wyświetla się w panelu, ma poprawną ikonę, nazwę, opis, premii zgodne z projektem; przy awansie wcześniejsza cecha znika.
- Dług Welesa oraz istniejące efekty świąt nadal działają.
- Test kompatybilności na nowym i kontynuowanym zapisie; jeśli gracz włącza 0.2.0 w środku cyklu, brakujących wyborów **nie rekonstruować z domysłów**.
- Co najmniej: kontrola statyczna referencji, walidacja ikon, próba w silniku CK3, `error.log`.

## Ustalenia wymagające decyzji autora

1. Czy każdy udany sąd ma dawać +1500 złota (łącznie do 6000 na władcę), czy +1500 tylko finał roczny? **Domyślnie projektuj po +1500 za każdy sąd.**
2. Czy jedna rozwijająca się cecha jest właściwa, czy autor woli cztery niezależne cechy? **Domyślnie jedna czterostopniowa cecha.**
3. Jak kwalifikować „udany” przebieg trzech świąt: przynajmniej 2 wyniki znaczące / 3, czy narracyjny bilans różnych ścieżek? **Domyślnie ocena decyzji, nie samo uczestnictwo, z więcej niż jednym możliwym wariantem powodzenia.**

**Nie implementować bez konsultacji, nie zmieniać tagu 0.1.9 i nie deklarować testu w grze przed rzeczywistą sesją.**
