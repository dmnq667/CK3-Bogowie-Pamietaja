# Gniew i Łaska Bogów: start prac nad wersją 0.3.0 DEV

**Status:** pierwsza implementacja zapisana; wymaga testów w CK3.  
**Baza:** `feature/0.2.0-gromnica-dual-duty`. Nie zmieniono `main` ani tagu `v0.1.9-alpha`.

## Zatwierdzony kierunek

- Dwanaście świąt zostaje, razem z dotychczasowymi ilustracjami użytkownika i kalendarzem.
- Święto ma być zwięzłym obrzędem, który nagradza uczestnictwo. Fabuła rozwija się przede wszystkim w osobnych, niekoniecznie corocznych interwencjach bogów.
- Tekst: staranna polszczyzna wysokiego rejestru, słowiańskie obrazowanie, ale jasne przyczyny, żądania, stawka i konsekwencje. Bez metafor zaciemniających sens.
- Rozgałęzienia uwzględniają cechy, wybory, zobowiązania i stres. Kara może obejmować śmierć władcy. To nie ma być losowy zgon bez ostrzeżenia.
- Gromnica, Weles i Sąd I stanowią pierwszy cykl do pełnych testów. Zachować nagrody, flagi i dotychczasowe cztery sądy; 1500 złota wyłącznie warunkowo po Sądzie II.

## Zmiany już zakodowane

- W `events/bp_weles_events.txt` dodano `bp_weles.2020` uruchamiane w ciągu 7–14 dni po drugiej odmowie spłaty długu w zdarzeniu `bp_weles.2012`.
- Trzy odpowiedzi: spłata 400 złota i uznanie winy rodu; pięcioletnia kara, stres i utrata prestiżu; świadome wyzwanie Welesa z **35% ryzyka śmierci** i 65% ryzyka dotkliwej kary (wartości prototypowe).
- Opis wydarzenia reaguje na `brave` i `craven`; trzecia odpowiedź uwzględnia te cechy także w skutkach stresu i prestiżu.
- Wybór śmiertelnego ryzyka należy do gracza. Nie wymuszono takiego ryzyka za samo uczestnictwo w święcie.
- Dodano komplet siedmiu kluczy lokalizacji PL i EN, bez nowych ilustracji. Wydarzenie korzysta z już istniejącego tła Welesa.
- Zachowano obecny system długu dynastycznego. Decyzja o dobrowolnym zniesieniu długu korzysta z istniejącego efektu `bp_weles_settle_debt_018_effect`.

## Do sprawdzenia i wdrożenia dalej

1. Test w silniku CK3: trigger, skalowanie dat, `random_list`, `death`, ewentualne reakcje po sukcesji, lokalizacja i grafika.
2. Sprawdzenie `error.log`; walidacja wersji gry z aktualną strukturą skryptów.
3. Zweryfikować, czy przyczyna śmierci jest dobrze opisana w historii postaci. Obecnie użyto istniejącego `death_execution` jako technicznego prototypu, nie własnej przyczyny boskiego zgonu.
4. Oddzielić nagrody świąteczne od interwencji w Gromnicy i Welesie, bez masowej produkcji kolejnych okien.
5. Wprowadzić szerszą pamięć wydarzeń oraz mechanikę boskiej przychylności i gniewu, opartą na rzeczywistych działaniach postaci.
6. Przeprowadzić redakcję pozostałych tekstów zgodnie z przyjętym standardem.
7. Naprawić i przetestować ikonę cechy w grze; kontrola strukturalna DDS nie wystarcza.
8. Przygotować paczkę aktualizacyjną dopiero po weryfikacji wymaganych plików.

**Nie nazywać tej gałęzi gotową wersją do gry bez sprawdzenia jej w CK3.**

## Druga partia zmian: rytuały, redakcja i pamięć dynastii

- Gromnica i Siedem Nocy Welesa przy pierwszym otwarciu obrzędu przyznają od razu umiarkowaną nagrodę: odpowiednio **50 / 75 pobożności i -10 stresu**. Koszty i następne wybory pozostały niezależne.
- Przeredagowano **21 kluczy polskiej lokalizacji**: wstępne sceny wszystkich 12 świąt, kluczowe sceny Gromnicy i Welesa oraz etykiety wyborów przy ofierze. Nacisk na jawne przyczyny, ceny i skutki.
- Dodano trwałe zmienne dynastyczne (ich poprzednie 90-dniowe flagi pozostają do obsługi istniejących sądów):
  - `bp_gromnica_protected_fire_ever_v030` — obrona świętego ognia;
  - `bp_gromnica_aided_villagers_ever_v030` — pomoc mieszkańcom;
  - `bp_gromnica_neglected_ever_v030` — odmowa pomocy;
  - `bp_weles_prisoner_sacrificed_ever_v030` — wykonana ofiara z więźnia.
- Nowe wydarzenie Welesa `2020` może odwołać się do przeszłej ofiary z więźnia. Scena ma odrębną lokalizację PL i EN.
- Kontrola statyczna: 1 definicja wydarzenia 2020, 1 wywołanie przez dalszą odmowę długu, pełne klucze nowych opisów PL/EN, bilans nawiasów poprawny.
- **Pozostała lokalizacja (setki kluczy) wymaga dalszej redakcji**. Nie uznawać całości za zakończoną.
- **Nie testowano silnika CK3** i nie przygotowano jeszcze instalacyjnej paczki `0.3.0`. Ryzyko niespójności w grze pozostaje.

## Trzecia partia: Perun, Mokosz i plan ilustracji

- Święto Peruna `bp_perun.9101` i Wiosenny Nowy Rok `bp_spring.3001` dają uczestnikowi od razu małe premie (75/50 pobożności, -10 stresu).
- Po świadomej odmowie obrzędu Peruna `bp_perun.9101.c` zaplanowane jest odrębne `bp_perun.9110` po 14–35 dniach, z reakcją na `brave` lub `craven`. Próba może zakończyć się dobrowolnym, świadomie wybranym ryzykiem śmierci (25% w prototypie); inne możliwości obejmują zadośćuczynienie albo długotrwałą karę.
- Po świadomym zatrzymaniu zasobów podczas Wiosennego Nowego Roku `bp_spring.3001.c` zaplanowane jest `bp_spring.3010` po 45–75 dniach. Mokosz rozpoznaje `compassionate` / `callous` i rozstrzyga o pomocy przy siewie lub wieloletniej szkodzie dla plonów.
- Oba wydarzenia korzystają z **istniejących, zatwierdzonych ilustracji** i mają komplet kluczy PL oraz EN.
- Stałe zmienne zapisują pojednanie z Perunem, odmowę obrzędu Peruna, odmowę pomocy w wiosennym siewie oraz naprawienie tej szkody.
- Szczegóły ewentualnych nowych grafik i wymagania produkcyjne zapisano w `docs/OPRAWA_BOGOW_030.md`.
- Kontrola statyczna: po jednej definicji i po jednym wywołaniu nowych interwencji 9110 i 3010; klucze lokalizacji PL i EN pełne; nawiasy zrównoważone.
- **Nie przeprowadzono testu CK3**, więc zgodność konkretnej wersji silnika i wygląd eventów wymagają sprawdzenia przed paczką instalacyjną.
