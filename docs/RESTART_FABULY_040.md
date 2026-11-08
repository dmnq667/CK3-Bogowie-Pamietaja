# Gniew i Łaska Bogów — całkowita przebudowa fabuły 0.4.0

**Decyzja produkcyjna:** 8 listopada 2026. Podstawa: uwagi użytkownika z testów 0.3.0 oraz przegląd plików `Bogowie_Pamietaja/events/`. **Dokument projektowy, nie wdrożenie skryptów.**

## 0. Bezwarunkowe ustalenia

1. **WSZYSTKIE dotychczasowe historie świąt i powtarzalnych sądów wymagają napisania od nowa.** Nie wystarczy retusz językowy.
2. **Zostają**: 28 grafik świąt z nowej serii, trzy zatwierdzone grafiki boskich objawień (Weles A01, Perun A02, Mokosz A03 lustrzana), kalendarz 12 świąt i idea gniewu/łaski trzech bogów.
3. **Maksymalnie dwa widoczne okna z jednego święta, łącznie z zapowiedzią**. Docelowo **JEDNO** okno na święto, bez natychmiastowych kaskad `trigger_event`. Wyjątkowe drugie okno może pojawić się tylko wtedy, gdy gracz rozstrzyga rzeczywistą sytuację wymagającą decyzji. Potwierdzenia, opisy wyników i „przyjmuję dar” wykonują się automatycznie, bez kolejnego okna.
4. Nie powtarzać schematu „daj 50 złota, daj 80 prestiżu, odmów” w każdym święcie. Udział może przynosić mały automatyczny bonus, natomiast decyzje mają dotyczyć **osób, wojen, majątku, lojalności, stresu, rodu i życia**.
5. **Główna fabuła to osobne historie bogów**, uruchamiane przez rzeczywiste działanie/stan postaci, nie przez obowiązkowe kliknięcie we wszystkich obrzędach. Długie opowieści rozdzielać miesiącami, a nie w kilkusekundowych sekwencjach okien.
6. Teksty: **wysoki rejestr polszczyzny, naturalne zdania, konkretna sytuacja, jasny sprawca, jawna stawka i prawdziwe następstwo**. Żadnych metafor zastępujących informację, enigmatycznych wstępów, pierścieni i „bram Welesa” bez znaczenia fabularnego.
7. **Silne korzyści i silne straty**, warunkowo: śmierć, utrata ważnej osoby, ciężkie rany, wieloletnia klątwa, rozpad lojalności, rozwój ziem, znaczna redukcja stresu, wojenne premie. Ryzyko śmierci **zawsze wyraźnie opisane przed wyborem**.
8. Zachować grę na obecnym zapisie: skrypty przygotować na **oddzielnej gałęzi 0.4.0**, nie zmieniać bieżącej testowanej `0.3.0`. Kolejno obsłużyć wydarzenia z dawnych zapisów, flagi i niezakończone zobowiązania. Zanim zostanie wydana paczka, sprawdzić w silniku CK3.

## 1. Potwierdzona przyczyna nudnej rozgrywki: nie tylko tekst, lecz architektura

W obecnej `0.3.0` istnieje **70** definicji wydarzeń w 12 głównych plikach świąt, **7** w pliku pierwszego sądu i osobno **28** definicji w pliku obwieszczeń. Nie każda jest widoczna; część istnieje dla migracji starszych zapisów. Bezpośrednie łańcuchy kliknięć mają w najgorszym wariancie (bez liczenia zapowiedzi i odroczonych konsekwencji) przykładowo:

| Święto | Obecna długa ścieżka w kodzie | Najwyżej w 0.4 |
| --- | --- | --- |
| Gromnica | `1001` (+ wariant `1002`) | 1–2 |
| Siedem Nocy Welesa | `2001 → 2003 → 2006`, inne ścieżki z więźniem | 1–2; dług poza świętem |
| Wiosenny Nowy Rok | `3001 → 3002` | 1–2 |
| Jare Gody | `4001 → 4002` | 1–2 |
| Gaik / Turzyca | `5001 → 5002` | 1–2 |
| Dziady wiosenne | `6001 → 6002 → 2013` przy długu | 1–2; dług poza świętem |
| Stado | `7001 → 7002` | 1–2 |
| Noc Kupały | `8001 → 8002 → 8003 → 8004` | 1–2 |
| Święto Peruna | `9101 → 9102 → 9103 → 9104 → 9105` | 1–2; Perun poza świętem |
| Dożynki | `9201 → 9202 → 9203 → 9204 → 9205` | 1–2 |
| Dziady jesienne | `9301 → 9302 → 9303 → 9304 → 9305`; inne odgałęzienia prowadzą aż do `9308 → bp_weles.2013` | 1–2 |
| Szczodre Gody | `9401 → 9402 → 9403 → 9404 → 9405`, późniejsze echa | 1–2 |

**Przyczyna UX:** okno obwieszczenia potrafi otworzyć obrzęd; obrzęd uruchamia następny obrzęd; po wyborach następuje informacyjne podsumowanie lub nagroda do odebrania osobnym kliknięciem. **Usunąć mechanizm kaskady**, nie tylko skrócić opis.

## 2. Docelowe święta — 12 różnych sytuacji, jeden mocny wybór zamiast pięciu ceremonii

W poniższych konceptach podajemy *prawdziwe stawki do zaimplementowania*, a nie zatwierdzone jeszcze wartości balansu. Zawsze dopasować wariant opisu do obecnych cech, wojny, dostępnych postaci i pamięci decyzji.

| Święto | Jedno konkretne wydarzenie | Wybór, który coś zmienia | Możliwa konsekwencja po czasie |
| --- | --- | --- | --- |
| **Gromnica** | Po zimowej burzy zamarzają dwie osady; zapasy opału wystarczą tylko na jeden transport | Ochronić osady kosztem zapasów i obronności albo zabezpieczyć własny gród | Wzrost/popularność i mniejszy stres współczującego vs silniejszy garnizon, gniew ludzi; Mokosz pamięta decyzję |
| **Siedem Nocy Welesa** | Więzień zna miejsce skarbu i proponuje informację za wolność; Weles żąda, by dotrzymać obietnicy | Uwolnić rzeczywistego więźnia i dotrzymać słowa, zatrzymać go i zabrać wiedzę lub podpisać krwawy układ | Realny skarb albo oszustwo; klątwa i późniejsze żądanie Welesa dotyczą **tej konkretnej obietnicy** |
| **Wiosenny Nowy Rok** | Wojsko domaga się ziarna przeznaczonego na siew | Nakarmić wojsko, aby szybciej wróciło do gotowości, albo ocalić przyszłe plony | Siła oddziałów kontra przyszły dochód i niezadowolenie chłopów; Mokosz pamięta |
| **Jare Gody** | Dwa rody chcą rozwiązać gwałtowny spór pod ochroną święta | Doprowadzić do kosztownego pojednania albo poprzeć jedną stronę | Relacje z realnymi możnymi, przyszła przychylność/niechęć, utrata prestiżu lub nowy sojusz |
| **Gaik / Turzyca** | Zarządca chce wyrąbać święty gaj na umocnienia przed zagrożeniem | Dodatkowe umocnienia vs zachowanie gaju i uspokojenie poddanych | Premie obrony vs trwały uraz lokalnej ludności i gniew Mokoszy |
| **Dziady wiosenne** | Odnaleziono świadectwo dawnej, konkretnej krzywdy rodu; odnaleziono **żyjących** pokrzywdzonych | Oddać ziemię/należność, przyznać się albo wybrać milczenie | Zmiana stosunków z rodami, straty finansowe, możliwy przyszły konflikt; nie „tajemnicze imię bez nazwiska” |
| **Stado** | Podczas uczty wojowie dwóch zależnych panów sięgają po broń | Ułaskawić, rozbroić lub poprzeć własnego stronnika | Przyszła lojalność wasali, utrata drużynników, opinii lub nowi rywale; możliwe pojednanie |
| **Noc Kupały** | Osoba związana z dworem znika w wezbranej rzece; ratunek staje się niebezpieczny | Podjąć osobiste ryzyko i ją ratować, wysłać wojów lub nie narażać innych | Uratowane życie, realna rana lub śmierć uczestnika; wzrost/utrata stresu zależnie od cech |
| **Święto Peruna** | Wojowie domagają się, by władca dotrzymał przysięgi złożonej przed bitwą | Wyruszyć osobiście, oddać dowództwo lub złamać przysięgę | Premia do działań wojennych i prestiżu albo tchórzostwo zapamiętane przez Peruna i wojsko |
| **Dożynki** | Skarbiec potrzebuje daniny, ale wieś po grabieży nie ma z czego płacić | Darować daninę, częściowo ją odroczyć lub ściągnąć siłą | Rzeczywisty dochód, kontrola w hrabstwie, popularność, rozwój, bunt albo gniew Mokoszy |
| **Dziady jesienne** | W czasie obrzędu przychodzi **żywy** krewny człowieka, którego dotknęła ostatnia decyzja władcy | Otworzyć dochodzenie i ukarać sprawcę, wypłacić odszkodowanie lub uciszyć skargę | Reakcje realnej rodziny/wasali, ujawnienie własnego czynu, wzrost tyranii lub oczyszczenie imienia; **koniec przy tym oknie**, bez „Sądu bez króla” i „Wiedzy pod popiołem” |
| **Szczodre Gody** | O schronienie prosi rodzina niedawnego wroga, przybyła z miejsca objętego wojną | Przyjąć i chronić, wydać wrogowi, wykorzystać jako zakładników | Trwała nienawiść i ryzyko odwetu albo wdzięczność i porozumienie; nie kolejna seria wpłat i rytuałów |

**Warunek techniczny:** jeżeli nie ma odpowiedniego prawdziwego jeńca, członka rodu, wasala lub aktywnej wojny, scena wybiera *wiarygodny wariant zastępczy*, nie fikcyjną osobę. Nie wolno twierdzić, że gracz zabił lub obiecał coś, czego system nie odnotował.

## 3. Główne historie bogów — poza kalendarzem

### Weles: „Cena ocalonej głowy”
- Wejście: silnie zestresowany władca lub ktoś, kto już ma u Welesa dług; propozycja natychmiastowego zdjęcia wielkiej ilości stresu w zamian za **ściśle określone zobowiązanie**.
- Zapis: kto przyjął, jakie świadczenie obiecał, jaki rzeczywisty człowiek może być zapłatą, termin wyroku; stan dynastii po sukcesji.
- Po wyznaczonym czasie bóg **osobiście** staje przed władcą (zatwierdzona ilustracja A01) i domaga się dotrzymania słowa.
- Wybór: oddać wskazanego więźnia lub wybraną osobę zgodną z warunkami, poświęcić własny majątek/pozycję dla ratunku, sprzeciwić się.
- **Prawdziwa śmierć w grze**: jeśli złożona ofiara dotyczy istniejącej postaci; jeśli gracz sam zaryzykuje życie — jawny procent, realne `death` przy porażce. Rodzina zabitego pamięta sprawcę.
- Odmowa nie może kończyć się pięknym, lecz pustym zdaniem o „głębi korzeni”. Musi mieć zapisaną, egzekwowaną cenę.

### Perun: „Przysięga przed bitwą”
- Wejście: faktyczna wojna, zachowanie władcy lub zapamiętane porzucenie wojów; charakter odważny/tchórzliwy kształtuje ton i dostępne wybory.
- Krótka scena wymagająca decyzji — wystawić się na śmiertelne niebezpieczeństwo w zamian za silny wojenny dar albo odmówić i ponieść konkretną karę w wojsku.
- Nie losować śmierci bez wcześniejszego komunikatu o ryzyku. W scenie objawienia pojawia się zatwierdzony Perun A02.
- Po miesiącach może nastąpić *wynik*: wdzięczność wojów, bunt, utrata lojalności, następstwo dotrzymanej przysięgi.

### Mokosz: „Głód pod twoim panowaniem”
- Wejście: utrata plonów, realna krzywda poddanych, nieudzielenie pomocy, lub wybitna troska o ludzi.
- Ukazuje się **osobiście** przy spichlerzu (zatwierdzona grafika A03). Nie ocenia wyłącznie charakteru postaci, ale **wcześniej zapisane działania**.
- Dobre czyny mogą przynieść wieloletni rozwój i ulgę od stresu; chciwość — nieurodzaj, bunt, choroby/zagrożenia zależnie od mechanik zweryfikowanych w CK3.
- Błogosławieństwo i kara powinny być **odczuwalne w danych prowincjach**, nie jedynie w pobożności.

**Częstotliwość:** fabuła boska musi być rzadsza i ważniejsza niż święta. Przed implementacją ustalić kontrolę częstotliwości: najwyżej jedna duża boska interwencja na kwartał na postać, chyba że gracz świadomie wywoła osobistą katastrofę.

## 4. Jak rozpoznać „jakim władcą jest gracz”

System **nie odczytuje magicznie całej historii dowolnego gracza**. Ma do dyspozycji udostępnione przez CK3 stany, cechy, statystyki, aktywne wojny, relacje oraz nasze zapisane flagi/zmienne. Zapisujemy co najmniej:

- żywy/martwy, wojna/pokój, cechy `brave`, `craven`, `compassionate`, `callous` i inne zweryfikowane w plikach gry;
- poziom stresu, prestiż, złoto, tyrania/postrach tam, gdzie warunki i efekty są legalne;
- czy faktycznie ochroniono wieś, wypędzono wygnańca, wydano wyrok, oszczędzono lub poświęcono realnego więźnia;
- czy przysięga została zawarta, spełniona lub złamana; nie opierać późniejszej historii na dawno wygasłej 30-dniowej fladze;
- komu wyrządzono krzywdę: jeśli gra i event pozwalają zachować prawdziwy scope lub identyfikator postaci, a jeśli nie — konsekwentnie użyć wariantu bez wskazywania konkretnego nazwiska;
- pamięć dynastii do rozliczenia działań przodków, odrębnie od bieżącego charakteru władcy.

**Warunek przyjęcia:** opis `brave` nie może różnić się od `craven` tylko przymiotnikiem — inny dostęp do czynu i inny stres, ryzyko, relacje lub nagroda.

## 5. Jeden rozwijany znak i cztery sądy — nowa funkcja

- Zachować pierwotną ideę **jednej rozwijającej się cechy** i czterech rozliczeń roku.
- **Nie generować czterech dodatkowych wieloetapowych „sądów” z fantastycznymi bramami.** W Księdze Bogów pokazać bilans czynów, status przysiąg i przychylność.
- Jeden krótki, osobny wyrok tylko wówczas, gdy zaszły ważne wydarzenia; ocena niedokończonych świąt i mniejsze skutki mogą być obliczane w tle.
- Nagroda 1500 złota, wcześniej zatwierdzona dla **Sądu Korzeni i Przodków**, pozostaje **warunkowa, maksymalnie raz na rok obrzędowy** po dowiedzionym spełnieniu wymogów. Nie rozdawać jej bez powodu.

## 6. Kryteria akceptacji przed wydaniem 0.4.0

1. Dla wszystkich 12 świąt: **maksymalnie dwa widoczne okna licząc zapowiedź, wywołania natychmiastowe i potwierdzenia**; cel to jedno.
2. Żadne `bp_harvest.9204`, `bp_autumn.9304` ani `bp_szczodre.9404` nie może zostać automatycznym czwartym oknem dawnego łańcucha.
3. Każde wydarzenie ma jednozdaniową, sprawdzalną stawkę; etykiety opcji mówią o koszcie i ryzyku **przed** wyborem.
4. Minimum trzy naprawdę różne rozgrywki testowe: odważny/wojenny, tchórzliwy/oportunistyczny i opiekuńczy; inne sceny i realne inne wyniki.
5. Pozytywne i negatywne konsekwencje mają konkretne modyfikatory, zapisy pamięci i realne następstwa po czasie.
6. Wszystkie nowe i stare wywołania wydarzeń mają odwołania do istniejących lokalizacji PL/EN oraz nowego zestawu DDS; żadna stara grafika nie wraca.
7. Test po sukcesji: dług Welesa i odpowiedzialność rodu nadal są czytelne i poprawnie działają.
8. Test na kopii gry: brak niekończącej się kaskady, brak czerwonych błędów w `error.log`, brak błędnych ikon.
9. **0.3.0 nadal pozostaje do testów porównawczych**. Nie nadpisywać jej wersją 0.4 przed testem i świadomą decyzją o wydaniu.

## 7. Kolejność rzeczywistego wdrożenia

- **Faza 1:** rozłączyć okna zapowiedzi od kaskadowych ciągów; wszystkie święta jako krótkie obrzędy, max 2 okna, zachować kalendarz, premie i istniejące grafiki. Wsparcie starych sejwów.
- **Faza 2:** napisać od zera **12 różnych scen** z konkretnymi ludzkimi konfliktami i systemem zapamiętywania decyzji. Zastąpić abstrakcyjne teksty całego cyklu.
- **Faza 3:** przepisane **3 główne kampanie boskie**, autentyczne i mocne konsekwencje, reakcje na charakter i dawne działania, grafiki A01/A02/A03. Wymagane testy silnika CK3.
- **Faza 4:** uprościć cztery kwartalne wyroki i Księgę Bogów; zachować jedną rozwijaną cechę.
- **Faza 5:** całościowy test kilkunastoletniej rozgrywki, sprawdzenie stresu, balansu i kompatybilności zapisu; dopiero potem nowa paczka.

**Projekt 0.4.0 nie jest jeszcze nową grywalną wersją.** Gałąź służy odrębnej produkcji, aby nie naruszyć przygotowanego testu 0.3.0.
