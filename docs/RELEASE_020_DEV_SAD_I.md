# Bogowie Pamiętają 0.2.0 DEV: Sąd Popiołu i Przysięgi

**Stan produkcji:** KOD ZAPISANY NA GAŁĘZI ROBOCZEJ, SPRAWDZENIE STATYCZNE PASS; TEST W CK3 OCZEKUJE.  
**Gałąź:** [feature/0.2.0-gromnica-dual-duty](../tree/feature/0.2.0-gromnica-dual-duty).  
**Baza stabilna:** `v0.1.9-alpha` na `main`, bez zmian.  
**Zakres:** zakończona implementacja techniczna tylko **Sądu I**, nie wszystkich czterech sądów.

## Potwierdzone decyzje autora

- Po Gromnicy i Siedmiu Nocach Welesa odbywa się **Sąd Popiołu i Przysięgi**.
- Nazwy rozstrzygnięć: **Światło dla żywych**, **Słowo dane ziemi**, **Granica ofiary**, **Gdy bogowie milczą**; dodatkowo techniczne zakończenie **Niedopełniona cena** dla rzeczywiście nierozstrzygniętych spraw.
- Nagrody roczne Sądu I: **+5 dyplomacji**, **+5 intrygi i +10 naturalnego postrachu**, **+5 wiedzy**. Każdy bonus trwa jeden rok i przysługuje wyłącznie za przyjęty pozytywny wyrok.
- Jedna wspólna rozwijana linia cechy na cztery sądy, bez kumulowania oddzielnych znaków.
- **Sąd I nie wypłaca złota.** Warunkowa premia +1500 złota raz na rok obrzędowy jest zarezerwowana wyłącznie dla Sądu II po Dziadach wiosennych.

## Wprowadzone zmiany

1. **Gromnica**. Po pierwszej decyzji można dodatkowo ratować ludzi lub opłacić straże, ponosząc drugi rzeczywisty koszt. Nowa scena `bp_gromnica.1003`, marker `bp_gromnica_both_done_v020`. Zaniedbanie otrzymuje odrębny marker.
2. **Weles**. Zapisano istotne rozgałęzienia tego roku, w tym odmowę ofiary, prośbę o czas, kłamstwo, ratunek więźnia, krwawą ofiarę, szczerość i świadomie przyjęty dług. Wcześniejsze konsekwencje ekonomiczne i dynastyczny dług Welesa pozostają nienaruszone.
3. **Kalendarz**. Pierwszy sąd jest wywoływany między 16 a 18 lutego przez istniejący `bp_announcement.1299`. Nie utworzono drugiego codziennego strażnika. Właściwy sąd ma blokadę dynastyczną na 345 dni i jednokrotne zakończenie.
4. **Fabuła**. Siedem wydarzeń: otwarcie `bp_judgement.1001`, rozliczenie czynów `.1002` i pięć wyników `.1011`–`.1015`. Wstęp nawiązuje do rzeczywistego wyboru Gromnicy, dalsza scena do rzeczywistego wyboru Welesa.
5. **Pierwsza cecha**. `bp_gods_mark_1_v020`, widoczny i trwały **Znak Pierwszego Ognia**, +1 zarządzania i +1 wiedzy. Przyznawany tylko za przyjęte pozytywne zakończenie, bez dziedziczenia i bez powtarzania. Następne sądy mają podnosić stopień tej samej linii cechy, zastępując dotychczasowy znak.
6. **Grafika cechy**. Własny `DDS BC3/DXT5` 64×64 pod `gfx/interface/icons/traits/bp_gods_mark_1_v020.dds` oraz źródłowy projekt SVG w `source_artwork/icons`. Sceny korzystają z już zatwierdzonych teł Gromnicy i Welesa, aby nie podmieniać oryginalnej stylistyki użytkownika.
7. **Bonusy tymczasowe**. `bp_first_court_light_modifier_v020` daje +5 dyplomacji na rok, `bp_first_court_oath_modifier_v020` daje +5 intrygi i **+10 naturalnego postrachu** na rok, `bp_first_court_boundary_modifier_v020` daje +5 wiedzy na rok. To postrach naturalny (parametr `dread_baseline_add`), nie nieodwracalna jednorazowa zmiana poziomu postrachu.
8. **Księga Bogów**. W rozdziale Welesa dodano wyłącznie odczytywaną kartę Sądu I `bp_book.0012`. Odróżnia aktualny wyrok postaci od historycznego, ostatniego wyroku rodu. Dane historyczne są trwałe, nie generują premii.
9. **Lokalizacja**. Komplet polski i angielski, z zachowaniem BOM oryginalnych plików i parzystości kluczy.
10. **Debug**. Dostęp do sądu z dotychczasowego menu testowego (`bp_test.9006`), na kopii zapisu. Wpis debug nie służy do nieskończonego generowania cech.

## Reguły rozstrzygnięcia

- **Gdy bogowie milczą** ma pierwszeństwo przy kłamstwie wobec Welesa, ucieczce lub zlekceważeniu zimowych ostrzeżeń.
- **Słowo dane ziemi** ma pierwszeństwo przy krwawej ofierze z człowieka, nawet gdy wykonano oba czyny Gromnicy. Ma także inne ścieżki świadomie przyjętej ceny.
- **Światło dla żywych** wymaga obu realnie wykonanych czynów Gromnicy oraz prawdy lub łaski wobec więźnia w Siedmiu Nocach Welesa.
- **Granica ofiary** wymaga ratowania mieszkańców i świadomego odmówienia niegodziwej ceny.
- **Niedopełniona cena** ma zastosowanie do spraw rozpoczętych, lecz nierozstrzygniętych; nie oznacza automatycznie kłamstwa.
- Dług Welesa powstały z nowego paktu nie jest automatycznie złamaną przysięgą. Pozostaje do rozliczenia w osobnej, istniejącej mechanice i wpływa na przyszły Sąd II.
- Pierwszy sąd **nie rekonstruuje dawnych wyborów**, których mod nie obserwował w czasie aktywacji 0.2.0.

## Weryfikacja

| Sprawdzenie | Status |
| --- | --- |
| Obecność plików, nowe wydarzenia, unikalność ID, komplet referencji | PASS, kontrola statyczna |
| Polski i angielski, zgodność kluczy, brak duplikatów, zachowany UTF-8 BOM | PASS, kontrola statyczna |
| Definicja cechy oraz DDS z nagłówkiem BC3/DXT5 64×64 | PASS, kontrola strukturalna |
| Różne rozstrzygnięcia na podstawie istniejących wyborów, blokady, roczne premie | Kod przygotowany, **czeka na test w CK3** |
| Wyświetlenie ikony, wysokość bonusów i zachowanie po wczytaniu zapisu | **NIE TESTOWANO W CK3** |
| Zgodność ze zmodyfikowanym zestawem innych modów | **NIE TESTOWANO** |

Skrypt walidacyjny: `tools/validate_first_court_020.py`. Workflow budujący paczkę rozwojową: `.github/workflows/validate-first-court-020.yml`. Wynik GitHub Actions trzeba odczytać na stronie zakładki **Actions**; sam zapis workflow nie jest jeszcze dowodem ukończonego przebiegu CI.

## Redakcja tempa rozgrywki, po pierwszym teście użytkownika

W pierwszym rzeczywistym teście gry autor potwierdził wywoływanie się wydarzeń, ale zgłosił **zbyt wiele kolejnych okien, za dużo fabuły do czytania i znak zapytania zamiast ikony cechy**. W gałęzi 0.2.0 wprowadzono kolejną poprawkę:

- **Gromnica:** dwa okna zamiast trzech. Trzecia scena `bp_gromnica.1003` pozostała jako ukryty, zgodny z dawnymi zapisami znacznik; oba czyny nadal wymagają osobnych kosztów i ustawiają flagę `bp_gromnica_both_done_v020`.
- **Siedem Nocy Welesa:** otwarcie i wybór ofiary połączono w jednym wydarzeniu; pomniejsze błogosławieństwo i klątwa wykonywane bez kolejnych okien potwierdzeń; przypomnienie o długu jest ukryte, a sceny wyłącznie potwierdzające spłatę długu nie są automatycznie otwierane. Scena wyboru więźnia i prawdziwe wybory moralne pozostają.
- **Sąd I:** jedna scena `bp_judgement.1001` oblicza wynik i daje rzeczywisty wybór przyjęcia lub odrzucenia znamienia, zachowując wszystkie dotychczasowe efekty. Zdarzenia `.1002` i `.1011`–`.1015` pozostają dla zgodności ze starym zapisem w środku łańcucha.
- **Zapowiedzi:** 12 automatycznych popupów świąt zostało wyłączonych. Kalendarz i ręczne decyzje obrzędowe działają nadal; bezczynne wydarzenia zapowiedzi nie są uruchamiane na nowych kampaniach.
- **Redakcja:** 19 najważniejszych opisów Gromnicy i Welesa skrócono o **54% po polsku** i **36% po angielsku**. Zachowano atmosferę obrzędową, długi Welesa, realne ceny i kluczowe wybory.
- **Ikona:** plik cechy zastąpiono DDS `A8R8G8B8`, **120 × 120 px**, z mipmapami. Dawny `DXT5 64 × 64` wyświetlał znak zapytania. **Nowy plik jest strukturalnie prawidłowy, ale nadal wymaga ponownego sprawdzenia w grze.**
- **Wydanie testowe:** GitHub Actions uruchamia walidator i przygotowuje ZIP do **nadpisania istniejącej instalacji na H:**, bez tworzenia drugiego moda.

Wszystkie ustalenia dotyczące **+1500 złota dopiero podczas Sądu II** pozostają bez zmian.

## Plan testów w silniku CK3

1. **Najpierw przetestować niezmienioną 0.1.9**, na oddzielnej kopii gry. Nie pomylić tego z gałęzią 0.2.0.
2. Osobna kopia kampanii w trybie debug, z aktywnym wyłącznie `0.2.0-dev`. Sprawdzić rozbudowaną Gromnicę w obydwu kolejnościach.
3. Rozpocząć Siedem Nocy Welesa i przygotować po jednym zapisie przed każdą odmienną decyzją.
4. Doprowadzić kalendarz do **16 lutego**. Sąd powinien przyjść automatycznie i wykorzystać realne wybory.
5. Spróbować otrzymać wszystkie pięć wyników i odrzucić proponowaną cechę w dowolnej pozytywnej ścieżce.
6. Sprawdzić w panelu postaci ikonę **Znaku Pierwszego Ognia** i faktyczne liczby: +1 zarządzania, +1 wiedzy, a przez rok odpowiedni bonus +5 lub +10 naturalnego postrachu.
7. Otworzyć Księgę Bogów, przejść do Welesa i do karty pierwszego sądu. Kontrola aktualnego wyniku, kolejnego roku oraz pamięci dawnego wyroku rodu.
8. Zapisać i wczytać grę, przetestować zmianę władcy, powtórzenie debug oraz następną zimę. Nie może nastąpić podwójna wypłata ani ponowne przyznanie tego samego bonusu w bieżącym cyklu.
9. Przesłać w razie problemów świeży `Documents\Paradox Interactive\Crusader Kings III\logs\error.log` oraz zrzut.
10. Dopiero po teście w grze połączyć poprawki z gałęzią główną i zaplanować następny sąd.

**Nie oznaczać jako finalne wydanie ani nie zmieniać tagu 0.1.9 przed sesją CK3.**
